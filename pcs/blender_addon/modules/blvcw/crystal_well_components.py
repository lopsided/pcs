import math
import os
import bpy
import json
import random

import numpy as np
from types import SimpleNamespace
from blvcw.crystal_well_material import CrystalMaterialGlass, PlaneMaterial, CustomMaterial
import mathutils


class CrystalWellLoader:
    """
    VCW component to import default crystal collections or objects.
    """
    def __init__(self, crystal_object="CUSTOM", remesh_mode="NONE", remesh_octree_depth=4):
        self.crystal_object = crystal_object
        self.remesh_mode = remesh_mode
        self.remesh_octree_depth = remesh_octree_depth
        self.imported_crystals = []
        self.collection_name = "ImportedCrystals"
        self.number_crystal_variants = 1
        self.crystal_variants = []
        self.n_loaded_crystals = 0
        self.current_idx = 0

    def import_obj(self, import_path="", clear_material=True):
        if self.crystal_object in ["CUSTOM", "CUSTOM_SEQ"]:
            if not os.path.exists(import_path):
                raise ImportError("The file to import does not exist")

            # Delete previous imported collections:
            for collection in bpy.data.collections:
                if self.collection_name in collection.name:
                    for old_imported_object in collection.objects:
                        collection.objects.unlink(old_imported_object)
                    bpy.data.collections.remove(collection)

            collection = bpy.data.collections.new(self.collection_name)
            collection.hide_viewport = True
            collection.hide_render = True
            bpy.context.scene.collection.children.link(collection)

            bpy.ops.import_scene.obj(filepath=import_path)
            for selected_object in bpy.context.selected_objects:
                collection.objects.link(selected_object)
                bpy.data.collections["Collection"].objects.unlink(selected_object)  # Remove from base collection
                if clear_material:
                    selected_object.data.materials.clear()
                self.imported_crystals.append(selected_object)

    def clear_import(self):
        collection = bpy.data.collections[self.collection_name]
        bpy.data.collections.remove(collection)
        self.number_crystal_variants = 1
        self.imported_crystals = []
        self.crystal_variants = []

    def set_number_crystal_variants_per_render(self, number_crystal_variants):
        self.number_crystal_variants = number_crystal_variants

    def setup(self):
        if self.crystal_object == "CUSTOM":
            self.crystal_variants = random.sample(self.imported_crystals, self.number_crystal_variants)
        elif self.crystal_object == "CUSTOM_SEQ":
            self.crystal_variants = self.imported_crystals

    def load_crystal(self):
        """
        Used to load a crystal from the preloaded collection.
        If a CUSTOM object file is used, the crystal mesh is drawn from self.crystal_variants, which can be
        set in the UI from 0 - #loaded meshes
        If a CUSTOM_SEQ object file is used, all the meshes in the collection are used in order.
        """
        if self.crystal_object == "CUBE":
            bpy.ops.mesh.primitive_cube_add(size=0.5,
                                            enter_editmode=False,
                                            align="WORLD")
            crystal_cube = bpy.context.active_object
            return crystal_cube
        elif self.crystal_object in ["CUSTOM", "CUSTOM_SEQ"]:
            if self.crystal_object == "CUSTOM":
                crystal = random.choice(self.crystal_variants)
            else:
                crystal = self.crystal_variants[self.current_idx]
                self.current_idx = (self.current_idx + 1) % len(self.crystal_variants)
            new_crystal = crystal.copy()
            new_crystal.data = crystal.data.copy()
            new_crystal.data.name = f"vcw_crystal_mesh_{self.n_loaded_crystals}"
            new_crystal.name = f"vcw_crystal_{self.n_loaded_crystals}"

            # Remesh using bpy
            if self.remesh_mode != "NONE":
                modifier = new_crystal.modifiers.new(name="Remesh", type="REMESH")
                modifier.mode = self.remesh_mode
                modifier.octree_depth = self.remesh_octree_depth

            self.n_loaded_crystals += 1
            bpy.context.collection.objects.link(new_crystal)
            return new_crystal

    def get_number_of_variants(self):
        return len(self.imported_crystals)


class CrystalWellLight:
    """
    VCW Component that creates a top-down light (settings mostly taken from the UI)
    and a bottom light (settings build-in).
    Energy and color values are in both cases hard-coded because only a small range of values turned out to
    generate good images.
    """
    def __init__(self, light_type="AREA", light_angle_min=0, light_angle_max=0,
                 light_location=None, light_rotation=None, light_energy=None,
                 plane_length=15.0, use_bottom_light=True,
                 camera_distance=15.0, cw_depth=-10.0, transmission_mode=False):
        self.light_type = light_type
        self.light_angle_min = light_angle_min
        self.light_angle_max = light_angle_max
        self.light_location = light_location
        self.light_rotation = light_rotation
        self.light_energy = light_energy
        self.plane_length = plane_length
        self.use_bottom_light = use_bottom_light
        self.cw_depth = cw_depth
        self.light_radius_total = abs(camera_distance) + abs(cw_depth)
        self.transmission_mode = transmission_mode

    def setup(self):
        if self.transmission_mode:
            # transmisson mode only has bottom light
            print("Using transmission mode for lighting")
            if self.light_energy is not None:
                energy = self.light_energy
            else:
                energy = 100000 + 5000.0 * (random.random() - 0.5)
            bpy.ops.object.light_add(type="AREA",
                                     radius=100,
                                     location=(0, 0, self.cw_depth + self.cw_depth / 4),
                                     rotation=(math.pi, 0.0, 0.0))

            bpy.context.object.name = "vcw_" + "AREA" + "_light_bottom"
            bpy.context.object.data.energy = energy
            bpy.context.object.data.color = mathutils.Color((0.700, 0.711, 0.534))

            params = {
                "energy": energy
            }

        else:
            light_angle = np.deg2rad(np.random.uniform(self.light_angle_min, self.light_angle_max))

            if self.light_location is not None:
                assert len(self.light_location) == 3, "light_location must be a tuple of length 3"
                assert self.light_rotation is not None, "light_rotation must be set if light_location is set"
                assert len(self.light_rotation) == 3, "light_rotation must be a tuple of length 3"
                light_x, light_y, light_z = self.light_location
                rotation = self.light_rotation
            else:
                random_factor_x, random_factor_y = (np.random.choice([-1, 1]), np.random.choice([-1, 1]))
                light_x = self.light_radius_total * math.sin(light_angle) * random_factor_x
                light_y = self.light_radius_total * math.sin(light_angle) * random_factor_y
                light_z = self.light_radius_total * math.cos(light_angle) - abs(self.cw_depth)
                rotation = (-1 * random_factor_y * light_angle,
                            random_factor_x * light_angle,
                            0.0)

            # TOP-DOWN LIGHT:
            location = (light_x, light_y, light_z)

            if self.light_energy is not None:
                energy = self.light_energy
            elif self.light_type == "SUN":
                energy = 1
            else:
                energy = 10000.0 + np.random.normal(0.0, 1000.0)
            if self.light_type != "NONE":
                bpy.ops.object.light_add(type=self.light_type,
                                         radius=15,
                                         location=location,
                                         rotation=rotation)
                bpy.context.object.name = "vcw_" + self.light_type + "_light"
                bpy.context.object.data.energy = energy
                bpy.context.object.data.color = (1.0, 1.0, 1.0)

            # BOTTOM LIGHT:
            if self.use_bottom_light:
                energy_bottom = 10000.0 + 500.0 * (random.random() - 0.5)
                bpy.ops.object.light_add(type="AREA",
                                        radius=60,
                                        location=(0, 0, self.cw_depth + 1),
                                        rotation=(math.pi, 0.0, 0.0), )

                bpy.context.object.name = "vcw_" + "AREA" + "_light_bottom"
                bpy.context.object.data.energy = energy_bottom
                bpy.context.object.data.color = (1.0, 1.0, 1.0)

            params = {
                "angle": light_angle,
                "location": (light_x, light_y, light_z),
                "rotation": rotation,
                "energy": energy
            }
            if self.use_bottom_light:
                params["energy_bottom"] = energy_bottom

        return params


class CrystalWellCamera:
    """
    VCW camera component placed above the plane.
    It is positioned at the same position for every image, which mimics the real-world situation.
    """
    def __init__(self, field_of_view=1.5708 / 2, camera_distance=15.0, cw_depth=-10., transmission_mode=True):
        self.field_of_view = field_of_view
        self.camera_distance = camera_distance
        self.cw_depth = cw_depth
        self.transmission_mode = transmission_mode

    def setup(self):
        bpy.ops.object.camera_add(location=(0.0, 0.0, self.camera_distance), rotation=(0.0, 0.0, 0.0))
        bpy.context.object.name = "vcw_camera"
        if self.transmission_mode:
            bpy.context.object.data.lens_unit = "MILLIMETERS"
            bpy.context.object.data.lens = 75
            bpy.context.object.data.clip_start = 1e-06
            bpy.context.object.data.clip_end = 1000
        else:
            bpy.context.object.data.lens_unit = "FOV"
            bpy.context.object.data.dof.use_dof = True
            bpy.context.object.data.dof.focus_distance = self.camera_distance - (
                    self.cw_depth / 2.0)  # center at focus point (half of cw depth)
            bpy.context.object.data.dof.aperture_fstop = 0.1  # smaller -> more blur
            bpy.context.object.data.dof.focus_distance = self.camera_distance - (self.cw_depth / 2.0)
            bpy.context.object.data.angle = self.field_of_view
        bpy.context.scene.camera = bpy.context.object


class CrystalWellBuilder:
    """
    VCW component that adds the bottom plane and calls the chosen VCW distributor.
    Thus it adds the crystals with chosen material to the vcw.
    """
    def __init__(self, plane_length, cw_depth, distributor,
                 material_name, material_min_ior, material_max_ior,
                 material_min_roughness, material_max_roughness,
                 material_min_brightness, material_max_brightness,
                 custom_material='GLASS', transmission_mode=False):
        self.cw_depth = cw_depth  # == Plane position

        self.plane_length = plane_length
        self.plane_material = PlaneMaterial(material_name="vcw_plane_material")

        self.crystal_material = None
        if material_name == "NONE":
            self.crystal_material = SimpleNamespace(apply=lambda blender_object: blender_object.data.materials.clear(),
                                                    shuffle_properties=lambda *args: None)
        elif material_name == "GLASS":
            self.crystal_material = CrystalMaterialGlass(material_name=material_name,
                                                         min_ior=material_min_ior,
                                                         max_ior=material_max_ior,
                                                         min_brightness=material_min_brightness,
                                                         max_brightness=material_max_brightness,
                                                         min_roughness=material_min_roughness,
                                                         max_roughness=material_max_roughness)
        else:
            self.crystal_material = CustomMaterial(material_name=material_name,
                                                   min_ior=material_min_ior,
                                                   max_ior=material_max_ior,
                                                   min_brightness=material_min_brightness,
                                                   max_brightness=material_max_brightness,
                                                   custom_material=custom_material)

        self.crystal_distributor = distributor
        self.transmission_mode = transmission_mode

    def setup(self):
        plane = self._setup_plane()
        if self.transmission_mode:
            # second plane for glass  # todo: check what this is doing
            self.glass_material = CustomMaterial(material_name="CUSTOM",
                                                 custom_material="crystal")
            self.glass_material.apply(blender_object=plane)
        return self._setup_crystals()  # Returns annotations for Coco Dataset

    def _setup_plane(self):
        bpy.ops.mesh.primitive_plane_add(size=self.plane_length,
                                         enter_editmode=False,
                                         location=(0, 0, self.cw_depth))
        plane = bpy.context.object
        plane.name = "vcw_plane"
        return plane

    def _setup_crystals(self):
        brightnesses = []
        iors = []
        roughnesses = []
        number_crystals = 0
        for crystal in self.crystal_distributor.get_crystals():
            self.crystal_material.shuffle_properties()
            self.crystal_material.apply(blender_object=crystal)
            if self.crystal_material.material_name != "CrystalMaterialCUSTOM":
                brightnesses.append(self.crystal_material.properties["ShaderNodeBsdfGlass"]["0"][0])
                iors.append(self.crystal_material.properties["ShaderNodeBsdfGlass"]["2"])
                roughnesses.append(self.crystal_material.properties["ShaderNodeBsdfGlass"]["1"])
            number_crystals += 1

        params = {
            "annotations": self.crystal_distributor.get_annotations(),
            "locations": self.crystal_distributor.get_locations(),
            "scales": self.crystal_distributor.get_scales(),
            "rotations": self.crystal_distributor.get_rotations()
        }
        if len(brightnesses) > 0:
            params["brightnesses"] = brightnesses
            params["iors"] = iors
            params["roughnesses"] = roughnesses

        return params
    
    def _set_background(self):
        world = bpy.data.worlds['World']
        world.use_nodes = True
        bg = world.node_tree.nodes['Background']
        bg.inputs[0].default_value[:3] = (0.700, 0.711, 0.534)
        bg.inputs[1].default_value = 1.0

class CrystalWellRenderer:
    """
    VCW component that handles the actual rendering of images. Values for the renderer are hard-coded.
    """
    def __init__(self, number_frames, number_threads, res_x, res_y, output_path, device="CPU", generate_blender=False):
        self.number_frames = number_frames
        self.number_threads = number_threads
        self.res_x = res_x
        self.res_y = res_y
        self.output_path = output_path
        assert device in ["CPU", "GPU"]
        self.device = device
        self.generate_blender = generate_blender

    def setup(self):
        scene = bpy.context.scene

        scene.render.engine = "CYCLES"
        scene.render.threads_mode = "FIXED"
        scene.cycles.device = self.device
        scene.cycles.samples = 512
        scene.cycles.use_denoising = True
        scene.cycles.max_bounces = 32
        scene.cycles.diffuse_bounces = 32
        scene.cycles.glossy_bounces = 32
        scene.cycles.transparent_max_bounces = 32
        scene.cycles.transmission_bounces = 32
        scene.render.threads = self.number_threads
        scene.frame_set(self.number_frames)
        scene.render.image_settings.file_format = "PNG"

        scene.render.resolution_x = self.res_x
        scene.render.resolution_y = self.res_y

        if self.device == 'GPU':
            cycles_prefs = bpy.context.preferences.addons["cycles"].preferences
            cycles_prefs.compute_device_type = "CUDA"
            cycles_prefs.get_devices()
            for d in cycles_prefs.devices:
                d["use"] = 1  # Using all devices, include GPU and CPU

    def render_image(self, image_index):
        bpy.context.view_layer.update()

        image_index_str = str(image_index).zfill(10)
        bpy.context.scene.render.filepath = os.path.join(self.output_path,
                                                         f"{image_index_str}.png")

        print("Rendering image", image_index_str)
        bpy.ops.render.render(write_still=True)
        
        if self.generate_blender:
            filepath = os.path.join(self.output_path, f"{image_index_str}.blend")
            bpy.ops.wm.save_as_mainfile(filepath=filepath)
        
        return image_index_str + ".png"


class CrystalWellWriter:
    """
    VCW component used to write the segmentation files (image_number.png.json) that
    includes the polygons of each crystal.
    """
    def __init__(self, output_path):
        self.output_path = output_path

    def write_json(self, image_name, polygons, locations, scales, rotations,
                   brightnesses=None, iors=None, roughnesses=None, light_params=None):
        data = {
            "segmentation": polygons,
            "crystals": {
                "locations": locations,
                "scales": scales,
                "rotations": rotations
            },
            "materials": {
                "brightnesses": brightnesses,
                "iors": iors,
                "roughnesses": roughnesses
            },
            "light": light_params
        }
        json_file_path = os.path.join(self.output_path, image_name + ".json")
        with open(json_file_path, "w") as file:
            json.dump(data, file, indent=None)


class CrystalWellSettings:
    """
    VCW component to store every custom setting from the UI. Provided to CrystalWellSimulator that reads the values
    from the settings_dict.
    """
    def __init__(self,
                 number_threads=16, device="CPU", n_frames=1,
                 res_x=1024, res_y=1024,
                 field_of_view=1.5708 / 2, camera_distance=15.0, cw_depth=-15.0, output_path="",
                 number_crystals=10, number_crystals_std_dev=0,
                 distributor="DEFAULT", center_crystals=True, optimize_rotation=True,
                 crystal_location=None, crystal_scale=None, crystal_rotation=None,
                 total_crystal_area_min=0.05, total_crystal_area_max=0.5,
                 crystal_area_min=3**2, crystal_area_max=128**2,
                 crystal_edge_min=3, crystal_edge_max=384,
                 crystal_aspect_ratio_max=8/0.7, smooth_shading_distributor=True,
                 scaling_crystals_average=(1.0, 1.0, 1.0), scaling_crystals_std_dev=0.0,
                 rotation_crystals_average=(0.0, 0.0, 0.0), rotation_crystals_std_dev=0.0,
                 crystal_object="", crystal_import_path="", number_variants=1,
                 crystal_material_name="GLASS", crystal_material_min_ior=1.1, crystal_material_max_ior=1.6,
                 crystal_material_min_brightness=0.75, crystal_material_max_brightness=0.9,
                 crystal_material_min_roughness=0.0, crystal_material_max_roughness=0.4,
                 light_type="AREA", light_angle_min=0, light_angle_max=0, use_bottom_light=True,
                 light_location=None, light_rotation=None, light_energy=None,
                 remesh_mode="NONE", remesh_octree_depth=4,
                 number_images=1,
                 custom_material_name = '',
                 transmission_mode = True,
                 ):
        self.settings_dict = {
            "number_threads": number_threads,
            "device": device,
            "n_frames": n_frames,
            "res_x": res_x,
            "res_y": res_y,
            "field_of_view": field_of_view,
            "camera_distance": camera_distance,
            "cw_depth": cw_depth,
            "number_crystals": number_crystals,
            "number_crystals_std_dev": number_crystals_std_dev,
            "distributor": distributor,
            "center_crystals": center_crystals,
            "optimize_rotation": optimize_rotation,
            "crystal_location": crystal_location,
            "crystal_scale": crystal_scale,
            "crystal_rotation": crystal_rotation,
            "total_crystal_area_min": total_crystal_area_min,
            "total_crystal_area_max": total_crystal_area_max,
            "crystal_area_min": crystal_area_min,
            "crystal_area_max": crystal_area_max,
            "crystal_edge_min": crystal_edge_min,
            "crystal_edge_max": crystal_edge_max,
            "crystal_aspect_ratio_max": crystal_aspect_ratio_max,
            "smooth_shading_distributor": smooth_shading_distributor,
            "scaling_crystals_average": scaling_crystals_average,
            "scaling_crystals_std_dev": scaling_crystals_std_dev,
            "rotation_crystals_average": rotation_crystals_average,
            "rotation_crystals_std_dev": rotation_crystals_std_dev,
            "crystal_material_name": crystal_material_name,
            "crystal_material_min_ior": crystal_material_min_ior,
            "crystal_material_max_ior": crystal_material_max_ior,
            "crystal_material_min_brightness": crystal_material_min_brightness,
            "crystal_material_max_brightness": crystal_material_max_brightness,
            "crystal_material_min_roughness": crystal_material_min_roughness,
            "crystal_material_max_roughness": crystal_material_max_roughness,
            "light_type": light_type,
            "light_angle_min": light_angle_min,
            "light_angle_max": light_angle_max,
            "light_location": light_location,
            "light_rotation": light_rotation,
            "light_energy": light_energy,
            "use_bottom_light": use_bottom_light,
            "crystal_object": crystal_object,
            "crystal_import_path": crystal_import_path,
            "number_variants": number_variants,
            "output_path": output_path,
            "remesh_mode": remesh_mode,
            "remesh_octree_depth": remesh_octree_depth,
            "number_images": number_images,
            "transmission_mode": transmission_mode,
            "custom_material_name": custom_material_name
        }

    def print_settings(self):
        print("*** VCW SETTINGS ***")
        print(json.dumps(self.settings_dict, indent=4))

    def write_json(self):
        """
        Used to save the settings_dict as a json file.
        """
        json_file_path = os.path.join(self.settings_dict["output_path"], "vcw_settings" + ".json")
        with open(json_file_path, "w") as file:
            json.dump(self.settings_dict, file, indent=4)

    def from_json(self, json_file_path):
        """
        Used for headless execution.
        """
        with open(json_file_path, "r") as file:
            self.settings_dict = json.load(file)
