import bpy

class Material():
    def __init__(self):
        pass
    
    def load():
        # MATERIAL
        crystal_shader = bpy.data.materials.new(name='Crystal shader')
        crystal_shader.use_nodes = True
        node_tree0 = crystal_shader.node_tree

        for node in node_tree0.nodes:
            node_tree0.nodes.remove(node)
        # NODES
        texture_coordinate_0 = node_tree0.nodes.new('ShaderNodeTexCoord')
        if hasattr(texture_coordinate_0, 'color'):
            texture_coordinate_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(texture_coordinate_0, 'from_instancer'):
            texture_coordinate_0.from_instancer = False
        if hasattr(texture_coordinate_0, 'hide'):
            texture_coordinate_0.hide = False
        if hasattr(texture_coordinate_0, 'location'):
            texture_coordinate_0.location = (-1014.7542724609375, 77.5830078125)
        if hasattr(texture_coordinate_0, 'mute'):
            texture_coordinate_0.mute = False
        if hasattr(texture_coordinate_0, 'name'):
            texture_coordinate_0.name = 'Texture Coordinate'
        if hasattr(texture_coordinate_0, 'use_custom_color'):
            texture_coordinate_0.use_custom_color = False
        if hasattr(texture_coordinate_0, 'width'):
            texture_coordinate_0.width = 140.0
        output = next((output for output in texture_coordinate_0.outputs if output.identifier=='Generated'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Generated'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in texture_coordinate_0.outputs if output.identifier=='Normal'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Normal'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in texture_coordinate_0.outputs if output.identifier=='UV'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'UV'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in texture_coordinate_0.outputs if output.identifier=='Object'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Object'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in texture_coordinate_0.outputs if output.identifier=='Camera'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Camera'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in texture_coordinate_0.outputs if output.identifier=='Window'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Window'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in texture_coordinate_0.outputs if output.identifier=='Reflection'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Reflection'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        noise_texture_0 = node_tree0.nodes.new('ShaderNodeTexNoise')
        if hasattr(noise_texture_0, 'color'):
            noise_texture_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(noise_texture_0, 'hide'):
            noise_texture_0.hide = False
        if hasattr(noise_texture_0, 'location'):
            noise_texture_0.location = (-718.169921875, 168.140869140625)
        if hasattr(noise_texture_0, 'mute'):
            noise_texture_0.mute = False
        if hasattr(noise_texture_0, 'name'):
            noise_texture_0.name = 'Noise Texture'
        if hasattr(noise_texture_0, 'noise_dimensions'):
            noise_texture_0.noise_dimensions = '3D'
        if hasattr(noise_texture_0, 'use_custom_color'):
            noise_texture_0.use_custom_color = False
        if hasattr(noise_texture_0, 'width'):
            noise_texture_0.width = 140.0
        input_ = next((input_ for input_ in noise_texture_0.inputs if input_.identifier=='Vector'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Vector'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_0.inputs if input_.identifier=='W'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = False
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'W'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_0.inputs if input_.identifier=='Scale'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.7000000476837158
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Scale'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_0.inputs if input_.identifier=='Detail'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 15.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Detail'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Roughness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_0.inputs if input_.identifier=='Distortion'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Distortion'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in noise_texture_0.outputs if output.identifier=='Fac'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Fac'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in noise_texture_0.outputs if output.identifier=='Color'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Color'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        material_output_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
        if hasattr(material_output_0, 'color'):
            material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(material_output_0, 'hide'):
            material_output_0.hide = False
        if hasattr(material_output_0, 'is_active_output'):
            material_output_0.is_active_output = True
        if hasattr(material_output_0, 'location'):
            material_output_0.location = (919.92333984375, 403.7735595703125)
        if hasattr(material_output_0, 'mute'):
            material_output_0.mute = False
        if hasattr(material_output_0, 'name'):
            material_output_0.name = 'Material Output'
        if hasattr(material_output_0, 'target'):
            material_output_0.target = 'ALL'
        if hasattr(material_output_0, 'use_custom_color'):
            material_output_0.use_custom_color = False
        if hasattr(material_output_0, 'width'):
            material_output_0.width = 140.0
        input_ = next((input_ for input_ in material_output_0.inputs if input_.identifier=='Displacement'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Displacement'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in material_output_0.inputs if input_.identifier=='Thickness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = False
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Thickness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False

        bump_001_0 = node_tree0.nodes.new('ShaderNodeBump')
        if hasattr(bump_001_0, 'color'):
            bump_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(bump_001_0, 'hide'):
            bump_001_0.hide = False
        if hasattr(bump_001_0, 'invert'):
            bump_001_0.invert = False
        if hasattr(bump_001_0, 'location'):
            bump_001_0.location = (159.8421630859375, -15.581268310546875)
        if hasattr(bump_001_0, 'mute'):
            bump_001_0.mute = False
        if hasattr(bump_001_0, 'name'):
            bump_001_0.name = 'Bump.001'
        if hasattr(bump_001_0, 'use_custom_color'):
            bump_001_0.use_custom_color = False
        if hasattr(bump_001_0, 'width'):
            bump_001_0.width = 140.0
        input_ = next((input_ for input_ in bump_001_0.inputs if input_.identifier=='Strength'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.05999999865889549
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Strength'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in bump_001_0.inputs if input_.identifier=='Distance'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Distance'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in bump_001_0.inputs if input_.identifier=='Height'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Height'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in bump_001_0.inputs if input_.identifier=='Normal'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Normal'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in bump_001_0.outputs if output.identifier=='Normal'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Normal'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        bump_0 = node_tree0.nodes.new('ShaderNodeBump')
        if hasattr(bump_0, 'color'):
            bump_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(bump_0, 'hide'):
            bump_0.hide = False
        if hasattr(bump_0, 'invert'):
            bump_0.invert = False
        if hasattr(bump_0, 'location'):
            bump_0.location = (-54.32879638671875, -85.99708557128906)
        if hasattr(bump_0, 'mute'):
            bump_0.mute = False
        if hasattr(bump_0, 'name'):
            bump_0.name = 'Bump'
        if hasattr(bump_0, 'use_custom_color'):
            bump_0.use_custom_color = False
        if hasattr(bump_0, 'width'):
            bump_0.width = 140.0
        input_ = next((input_ for input_ in bump_0.inputs if input_.identifier=='Strength'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.10000000149011612
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Strength'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in bump_0.inputs if input_.identifier=='Distance'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Distance'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in bump_0.inputs if input_.identifier=='Height'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Height'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in bump_0.inputs if input_.identifier=='Normal'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Normal'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in bump_0.outputs if output.identifier=='Normal'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Normal'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        displacement_0 = node_tree0.nodes.new('ShaderNodeDisplacement')
        if hasattr(displacement_0, 'color'):
            displacement_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(displacement_0, 'hide'):
            displacement_0.hide = False
        if hasattr(displacement_0, 'location'):
            displacement_0.location = (431.888916015625, -614.963623046875)
        if hasattr(displacement_0, 'mute'):
            displacement_0.mute = False
        if hasattr(displacement_0, 'name'):
            displacement_0.name = 'Displacement'
        if hasattr(displacement_0, 'space'):
            displacement_0.space = 'OBJECT'
        if hasattr(displacement_0, 'use_custom_color'):
            displacement_0.use_custom_color = False
        if hasattr(displacement_0, 'width'):
            displacement_0.width = 140.0
        input_ = next((input_ for input_ in displacement_0.inputs if input_.identifier=='Height'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Height'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in displacement_0.inputs if input_.identifier=='Midlevel'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Midlevel'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in displacement_0.inputs if input_.identifier=='Scale'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.10000000149011612
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Scale'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in displacement_0.inputs if input_.identifier=='Normal'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Normal'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in displacement_0.outputs if output.identifier=='Displacement'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Displacement'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        colorramp_001_0 = node_tree0.nodes.new('ShaderNodeValToRGB')
        if hasattr(colorramp_001_0, 'color'):
            colorramp_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(colorramp_001_0, 'color_ramp'):
            if hasattr(colorramp_001_0.color_ramp, 'color_mode'):
                colorramp_001_0.color_ramp.color_mode = 'RGB'
            if hasattr(colorramp_001_0.color_ramp, 'elements'):
                if 0 >= len(colorramp_001_0.color_ramp.elements):
                    colorramp_001_0.color_ramp.elements.new(0.30909115076065063)
                if hasattr(colorramp_001_0.color_ramp.elements[0], 'alpha'):
                    colorramp_001_0.color_ramp.elements[0].alpha = 1.0
                if hasattr(colorramp_001_0.color_ramp.elements[0], 'color'):
                    colorramp_001_0.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
                if hasattr(colorramp_001_0.color_ramp.elements[0], 'position'):
                    colorramp_001_0.color_ramp.elements[0].position = 0.30909115076065063
                if 1 >= len(colorramp_001_0.color_ramp.elements):
                    colorramp_001_0.color_ramp.elements.new(0.4954550266265869)
                if hasattr(colorramp_001_0.color_ramp.elements[1], 'alpha'):
                    colorramp_001_0.color_ramp.elements[1].alpha = 1.0
                if hasattr(colorramp_001_0.color_ramp.elements[1], 'color'):
                    colorramp_001_0.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
                if hasattr(colorramp_001_0.color_ramp.elements[1], 'position'):
                    colorramp_001_0.color_ramp.elements[1].position = 0.4954550266265869
            if hasattr(colorramp_001_0.color_ramp, 'hue_interpolation'):
                colorramp_001_0.color_ramp.hue_interpolation = 'NEAR'
            if hasattr(colorramp_001_0.color_ramp, 'interpolation'):
                colorramp_001_0.color_ramp.interpolation = 'LINEAR'
        if hasattr(colorramp_001_0, 'hide'):
            colorramp_001_0.hide = False
        if hasattr(colorramp_001_0, 'location'):
            colorramp_001_0.location = (-449.09002685546875, -65.03225708007812)
        if hasattr(colorramp_001_0, 'mute'):
            colorramp_001_0.mute = False
        if hasattr(colorramp_001_0, 'name'):
            colorramp_001_0.name = 'ColorRamp.001'
        if hasattr(colorramp_001_0, 'use_custom_color'):
            colorramp_001_0.use_custom_color = False
        if hasattr(colorramp_001_0, 'width'):
            colorramp_001_0.width = 240.0
        input_ = next((input_ for input_ in colorramp_001_0.inputs if input_.identifier=='Fac'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Fac'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in colorramp_001_0.outputs if output.identifier=='Color'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Color'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in colorramp_001_0.outputs if output.identifier=='Alpha'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Alpha'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        colorramp_0 = node_tree0.nodes.new('ShaderNodeValToRGB')
        if hasattr(colorramp_0, 'color'):
            colorramp_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(colorramp_0, 'color_ramp'):
            if hasattr(colorramp_0.color_ramp, 'color_mode'):
                colorramp_0.color_ramp.color_mode = 'RGB'
            if hasattr(colorramp_0.color_ramp, 'elements'):
                if 0 >= len(colorramp_0.color_ramp.elements):
                    colorramp_0.color_ramp.elements.new(0.29999998211860657)
                if hasattr(colorramp_0.color_ramp.elements[0], 'alpha'):
                    colorramp_0.color_ramp.elements[0].alpha = 1.0
                if hasattr(colorramp_0.color_ramp.elements[0], 'color'):
                    colorramp_0.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
                if hasattr(colorramp_0.color_ramp.elements[0], 'position'):
                    colorramp_0.color_ramp.elements[0].position = 0.29999998211860657
                if 1 >= len(colorramp_0.color_ramp.elements):
                    colorramp_0.color_ramp.elements.new(1.0)
                if hasattr(colorramp_0.color_ramp.elements[1], 'alpha'):
                    colorramp_0.color_ramp.elements[1].alpha = 1.0
                if hasattr(colorramp_0.color_ramp.elements[1], 'color'):
                    colorramp_0.color_ramp.elements[1].color = (0.41326433420181274, 0.41326433420181274, 0.41326433420181274, 1.0)
                if hasattr(colorramp_0.color_ramp.elements[1], 'position'):
                    colorramp_0.color_ramp.elements[1].position = 1.0
            if hasattr(colorramp_0.color_ramp, 'hue_interpolation'):
                colorramp_0.color_ramp.hue_interpolation = 'NEAR'
            if hasattr(colorramp_0.color_ramp, 'interpolation'):
                colorramp_0.color_ramp.interpolation = 'LINEAR'
        if hasattr(colorramp_0, 'hide'):
            colorramp_0.hide = False
        if hasattr(colorramp_0, 'location'):
            colorramp_0.location = (-451.82769775390625, 211.45333862304688)
        if hasattr(colorramp_0, 'mute'):
            colorramp_0.mute = False
        if hasattr(colorramp_0, 'name'):
            colorramp_0.name = 'ColorRamp'
        if hasattr(colorramp_0, 'use_custom_color'):
            colorramp_0.use_custom_color = False
        if hasattr(colorramp_0, 'width'):
            colorramp_0.width = 240.0
        input_ = next((input_ for input_ in colorramp_0.inputs if input_.identifier=='Fac'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Fac'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in colorramp_0.outputs if output.identifier=='Color'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Color'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in colorramp_0.outputs if output.identifier=='Alpha'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Alpha'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        principled_bsdf_0 = node_tree0.nodes.new('ShaderNodeBsdfPrincipled')
        if hasattr(principled_bsdf_0, 'color'):
            principled_bsdf_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(principled_bsdf_0, 'distribution'):
            principled_bsdf_0.distribution = 'GGX'
        if hasattr(principled_bsdf_0, 'hide'):
            principled_bsdf_0.hide = False
        if hasattr(principled_bsdf_0, 'location'):
            principled_bsdf_0.location = (378.39892578125, 403.7735595703125)
        if hasattr(principled_bsdf_0, 'mute'):
            principled_bsdf_0.mute = False
        if hasattr(principled_bsdf_0, 'name'):
            principled_bsdf_0.name = 'Principled BSDF'
        if hasattr(principled_bsdf_0, 'subsurface_method'):
            principled_bsdf_0.subsurface_method = 'RANDOM_WALK'
        if hasattr(principled_bsdf_0, 'use_custom_color'):
            principled_bsdf_0.use_custom_color = False
        if hasattr(principled_bsdf_0, 'width'):
            principled_bsdf_0.width = 240.0
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Base Color'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (1.0, 0.5230486989021301, 0.7215041518211365, 1.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Base Color'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Subsurface'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Subsurface'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Subsurface Radius'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Subsurface Radius'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Subsurface Color'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Subsurface Color'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Subsurface IOR'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.399999976158142
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Subsurface IOR'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Subsurface Anisotropy'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Subsurface Anisotropy'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Metallic'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Metallic'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Specular'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Specular'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Specular Tint'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Specular Tint'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Roughness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Anisotropic'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Anisotropic'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Anisotropic Rotation'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Anisotropic Rotation'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Sheen'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Sheen'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Sheen Tint'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Sheen Tint'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Clearcoat'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Clearcoat'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Clearcoat Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.029999999329447746
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Clearcoat Roughness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='IOR'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.4500000476837158
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'IOR'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Transmission'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.9454545378684998
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Transmission'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Transmission Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Transmission Roughness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Emission'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0, 1.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Emission'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Emission Strength'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 4.399999618530273
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Emission Strength'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Alpha'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Alpha'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Normal'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Normal'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Clearcoat Normal'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Clearcoat Normal'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Tangent'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Tangent'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in principled_bsdf_0.inputs if input_.identifier=='Weight'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = False
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Weight'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False

        noise_texture_001_0 = node_tree0.nodes.new('ShaderNodeTexNoise')
        if hasattr(noise_texture_001_0, 'color'):
            noise_texture_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(noise_texture_001_0, 'hide'):
            noise_texture_001_0.hide = False
        if hasattr(noise_texture_001_0, 'location'):
            noise_texture_001_0.location = (-735.7659301757812, -63.824554443359375)
        if hasattr(noise_texture_001_0, 'mute'):
            noise_texture_001_0.mute = False
        if hasattr(noise_texture_001_0, 'name'):
            noise_texture_001_0.name = 'Noise Texture.001'
        if hasattr(noise_texture_001_0, 'noise_dimensions'):
            noise_texture_001_0.noise_dimensions = '3D'
        if hasattr(noise_texture_001_0, 'use_custom_color'):
            noise_texture_001_0.use_custom_color = False
        if hasattr(noise_texture_001_0, 'width'):
            noise_texture_001_0.width = 140.0
        input_ = next((input_ for input_ in noise_texture_001_0.inputs if input_.identifier=='Vector'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Vector'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_001_0.inputs if input_.identifier=='W'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = False
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'W'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_001_0.inputs if input_.identifier=='Scale'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 7.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Scale'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_001_0.inputs if input_.identifier=='Detail'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 15.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Detail'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_001_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.10000000149011612
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Roughness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in noise_texture_001_0.inputs if input_.identifier=='Distortion'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Distortion'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in noise_texture_001_0.outputs if output.identifier=='Fac'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Fac'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in noise_texture_001_0.outputs if output.identifier=='Color'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Color'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        voronoi_texture_0 = node_tree0.nodes.new('ShaderNodeTexVoronoi')
        if hasattr(voronoi_texture_0, 'color'):
            voronoi_texture_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(voronoi_texture_0, 'distance'):
            voronoi_texture_0.distance = 'EUCLIDEAN'
        if hasattr(voronoi_texture_0, 'feature'):
            voronoi_texture_0.feature = 'F1'
        if hasattr(voronoi_texture_0, 'hide'):
            voronoi_texture_0.hide = False
        if hasattr(voronoi_texture_0, 'location'):
            voronoi_texture_0.location = (167.567626953125, -597.9808349609375)
        if hasattr(voronoi_texture_0, 'mute'):
            voronoi_texture_0.mute = False
        if hasattr(voronoi_texture_0, 'name'):
            voronoi_texture_0.name = 'Voronoi Texture'
        if hasattr(voronoi_texture_0, 'use_custom_color'):
            voronoi_texture_0.use_custom_color = False
        if hasattr(voronoi_texture_0, 'voronoi_dimensions'):
            voronoi_texture_0.voronoi_dimensions = '3D'
        if hasattr(voronoi_texture_0, 'width'):
            voronoi_texture_0.width = 140.0
        input_ = next((input_ for input_ in voronoi_texture_0.inputs if input_.identifier=='Vector'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 0.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Vector'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in voronoi_texture_0.inputs if input_.identifier=='W'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = False
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'W'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in voronoi_texture_0.inputs if input_.identifier=='Scale'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 3.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Scale'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in voronoi_texture_0.inputs if input_.identifier=='Smoothness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = False
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Smoothness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in voronoi_texture_0.inputs if input_.identifier=='Exponent'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.5
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = False
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Exponent'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in voronoi_texture_0.inputs if input_.identifier=='Randomness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 1.0
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Randomness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in voronoi_texture_0.outputs if output.identifier=='Distance'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Distance'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in voronoi_texture_0.outputs if output.identifier=='Color'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Color'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in voronoi_texture_0.outputs if output.identifier=='Position'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = (0.0, 0.0, 0.0)
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = True
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Position'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in voronoi_texture_0.outputs if output.identifier=='W'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = False
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'W'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in voronoi_texture_0.outputs if output.identifier=='Radius'), None)
        if output:
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'display_shape'):
                output.display_shape = 'CIRCLE'
            if hasattr(output, 'enabled'):
                output.enabled = False
            if hasattr(output, 'hide'):
                output.hide = False
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Radius'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        # LINKS
        node_tree0.links.new(texture_coordinate_0.outputs[3], noise_texture_0.inputs[0])
        node_tree0.links.new(texture_coordinate_0.outputs[3], noise_texture_001_0.inputs[0])
        node_tree0.links.new(colorramp_0.outputs[0], principled_bsdf_0.inputs[9])
        node_tree0.links.new(bump_0.outputs[0], bump_001_0.inputs[3])
        node_tree0.links.new(bump_001_0.outputs[0], principled_bsdf_0.inputs[22])
        node_tree0.links.new(noise_texture_0.outputs[0], bump_0.inputs[2])
        node_tree0.links.new(noise_texture_001_0.outputs[0], colorramp_0.inputs[0])
        node_tree0.links.new(noise_texture_001_0.outputs[0], colorramp_001_0.inputs[0])
        node_tree0.links.new(colorramp_001_0.outputs[0], bump_001_0.inputs[2])
        node_tree0.links.new(displacement_0.outputs[0], material_output_0.inputs[2])
        node_tree0.links.new(texture_coordinate_0.outputs[3], voronoi_texture_0.inputs[0])
        node_tree0.links.new(principled_bsdf_0.outputs[0], material_output_0.inputs[0])
        node_tree0.links.new(voronoi_texture_0.outputs[0], displacement_0.inputs[0])

        return crystal_shader
        # # TO ACTIVE
        # selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
        # for obj in selected_objects:
        #     obj.active_material = crystal_shader
