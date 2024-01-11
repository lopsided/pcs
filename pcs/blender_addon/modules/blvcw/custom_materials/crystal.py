import bpy

class Material():
    def __init__(self):
        pass
    
    def load():
        # MATERIAL
        crystal = bpy.data.materials.new(name='Crystal')
        crystal.use_nodes = True
        node_tree0 = crystal.node_tree

        for node in node_tree0.nodes:
            node_tree0.nodes.remove(node)
        # NODES
        glass_bsdf_001_0 = node_tree0.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_001_0, 'color'):
            glass_bsdf_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(glass_bsdf_001_0, 'distribution'):
            glass_bsdf_001_0.distribution = 'GGX'
        if hasattr(glass_bsdf_001_0, 'hide'):
            glass_bsdf_001_0.hide = False
        if hasattr(glass_bsdf_001_0, 'location'):
            glass_bsdf_001_0.location = (293.2331848144531, 286.7701416015625)
        if hasattr(glass_bsdf_001_0, 'mute'):
            glass_bsdf_001_0.mute = False
        if hasattr(glass_bsdf_001_0, 'name'):
            glass_bsdf_001_0.name = 'Glass BSDF.001'
        if hasattr(glass_bsdf_001_0, 'use_custom_color'):
            glass_bsdf_001_0.use_custom_color = False
        if hasattr(glass_bsdf_001_0, 'width'):
            glass_bsdf_001_0.width = 150.0
        input_ = next((input_ for input_ in glass_bsdf_001_0.inputs if input_.identifier=='Color'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (1.0, 0.0, 0.0, 1.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Color'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in glass_bsdf_001_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0010000000474974513
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
        input_ = next((input_ for input_ in glass_bsdf_001_0.inputs if input_.identifier=='IOR'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 2.0
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
        input_ = next((input_ for input_ in glass_bsdf_001_0.inputs if input_.identifier=='Normal'), None)
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
        input_ = next((input_ for input_ in glass_bsdf_001_0.inputs if input_.identifier=='Weight'), None)
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

        glass_bsdf_002_0 = node_tree0.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_002_0, 'color'):
            glass_bsdf_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(glass_bsdf_002_0, 'distribution'):
            glass_bsdf_002_0.distribution = 'GGX'
        if hasattr(glass_bsdf_002_0, 'hide'):
            glass_bsdf_002_0.hide = False
        if hasattr(glass_bsdf_002_0, 'location'):
            glass_bsdf_002_0.location = (288.1683044433594, 77.394287109375)
        if hasattr(glass_bsdf_002_0, 'mute'):
            glass_bsdf_002_0.mute = False
        if hasattr(glass_bsdf_002_0, 'name'):
            glass_bsdf_002_0.name = 'Glass BSDF.002'
        if hasattr(glass_bsdf_002_0, 'use_custom_color'):
            glass_bsdf_002_0.use_custom_color = False
        if hasattr(glass_bsdf_002_0, 'width'):
            glass_bsdf_002_0.width = 150.0
        input_ = next((input_ for input_ in glass_bsdf_002_0.inputs if input_.identifier=='Color'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 1.0, 0.0, 1.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Color'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in glass_bsdf_002_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0010000000474974513
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
        input_ = next((input_ for input_ in glass_bsdf_002_0.inputs if input_.identifier=='IOR'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 2.0
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
        input_ = next((input_ for input_ in glass_bsdf_002_0.inputs if input_.identifier=='Normal'), None)
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
        input_ = next((input_ for input_ in glass_bsdf_002_0.inputs if input_.identifier=='Weight'), None)
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

        add_shader_001_0 = node_tree0.nodes.new('ShaderNodeAddShader')
        if hasattr(add_shader_001_0, 'color'):
            add_shader_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(add_shader_001_0, 'hide'):
            add_shader_001_0.hide = False
        if hasattr(add_shader_001_0, 'location'):
            add_shader_001_0.location = (772.5579223632812, 426.9981689453125)
        if hasattr(add_shader_001_0, 'mute'):
            add_shader_001_0.mute = False
        if hasattr(add_shader_001_0, 'name'):
            add_shader_001_0.name = 'Add Shader.001'
        if hasattr(add_shader_001_0, 'use_custom_color'):
            add_shader_001_0.use_custom_color = False
        if hasattr(add_shader_001_0, 'width'):
            add_shader_001_0.width = 140.0

        glass_bsdf_003_0 = node_tree0.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_003_0, 'color'):
            glass_bsdf_003_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(glass_bsdf_003_0, 'distribution'):
            glass_bsdf_003_0.distribution = 'GGX'
        if hasattr(glass_bsdf_003_0, 'hide'):
            glass_bsdf_003_0.hide = False
        if hasattr(glass_bsdf_003_0, 'location'):
            glass_bsdf_003_0.location = (288.1683044433594, -125.22750854492188)
        if hasattr(glass_bsdf_003_0, 'mute'):
            glass_bsdf_003_0.mute = False
        if hasattr(glass_bsdf_003_0, 'name'):
            glass_bsdf_003_0.name = 'Glass BSDF.003'
        if hasattr(glass_bsdf_003_0, 'use_custom_color'):
            glass_bsdf_003_0.use_custom_color = False
        if hasattr(glass_bsdf_003_0, 'width'):
            glass_bsdf_003_0.width = 150.0
        input_ = next((input_ for input_ in glass_bsdf_003_0.inputs if input_.identifier=='Color'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.0, 0.0, 1.0, 1.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Color'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in glass_bsdf_003_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0010000000474974513
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
        input_ = next((input_ for input_ in glass_bsdf_003_0.inputs if input_.identifier=='IOR'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 2.0
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
        input_ = next((input_ for input_ in glass_bsdf_003_0.inputs if input_.identifier=='Normal'), None)
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
        input_ = next((input_ for input_ in glass_bsdf_003_0.inputs if input_.identifier=='Weight'), None)
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

        add_shader_0 = node_tree0.nodes.new('ShaderNodeAddShader')
        if hasattr(add_shader_0, 'color'):
            add_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(add_shader_0, 'hide'):
            add_shader_0.hide = False
        if hasattr(add_shader_0, 'location'):
            add_shader_0.location = (527.7542114257812, 388.1622009277344)
        if hasattr(add_shader_0, 'mute'):
            add_shader_0.mute = False
        if hasattr(add_shader_0, 'name'):
            add_shader_0.name = 'Add Shader'
        if hasattr(add_shader_0, 'use_custom_color'):
            add_shader_0.use_custom_color = False
        if hasattr(add_shader_0, 'width'):
            add_shader_0.width = 140.0

        material_output_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
        if hasattr(material_output_0, 'color'):
            material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(material_output_0, 'hide'):
            material_output_0.hide = False
        if hasattr(material_output_0, 'is_active_output'):
            material_output_0.is_active_output = True
        if hasattr(material_output_0, 'location'):
            material_output_0.location = (1204.6102294921875, 451.0459899902344)
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

        glass_bsdf_0 = node_tree0.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_0, 'color'):
            glass_bsdf_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(glass_bsdf_0, 'distribution'):
            glass_bsdf_0.distribution = 'GGX'
        if hasattr(glass_bsdf_0, 'hide'):
            glass_bsdf_0.hide = False
        if hasattr(glass_bsdf_0, 'location'):
            glass_bsdf_0.location = (292.8089904785156, 501.2115478515625)
        if hasattr(glass_bsdf_0, 'mute'):
            glass_bsdf_0.mute = False
        if hasattr(glass_bsdf_0, 'name'):
            glass_bsdf_0.name = 'Glass BSDF'
        if hasattr(glass_bsdf_0, 'use_custom_color'):
            glass_bsdf_0.use_custom_color = False
        if hasattr(glass_bsdf_0, 'width'):
            glass_bsdf_0.width = 150.0
        input_ = next((input_ for input_ in glass_bsdf_0.inputs if input_.identifier=='Color'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(input_, 'display_shape'):
                input_.display_shape = 'CIRCLE'
            if hasattr(input_, 'enabled'):
                input_.enabled = True
            if hasattr(input_, 'hide'):
                input_.hide = False
            if hasattr(input_, 'hide_value'):
                input_.hide_value = False
            if hasattr(input_, 'name'):
                input_.name = 'Color'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in glass_bsdf_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.0010000000474974513
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
        input_ = next((input_ for input_ in glass_bsdf_0.inputs if input_.identifier=='IOR'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 2.0
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
        input_ = next((input_ for input_ in glass_bsdf_0.inputs if input_.identifier=='Normal'), None)
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
        input_ = next((input_ for input_ in glass_bsdf_0.inputs if input_.identifier=='Weight'), None)
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

        mix_shader_0 = node_tree0.nodes.new('ShaderNodeMixShader')
        if hasattr(mix_shader_0, 'color'):
            mix_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(mix_shader_0, 'hide'):
            mix_shader_0.hide = False
        if hasattr(mix_shader_0, 'location'):
            mix_shader_0.location = (967.2089233398438, 580.2929077148438)
        if hasattr(mix_shader_0, 'mute'):
            mix_shader_0.mute = False
        if hasattr(mix_shader_0, 'name'):
            mix_shader_0.name = 'Mix Shader'
        if hasattr(mix_shader_0, 'use_custom_color'):
            mix_shader_0.use_custom_color = False
        if hasattr(mix_shader_0, 'width'):
            mix_shader_0.width = 140.0
        input_ = next((input_ for input_ in mix_shader_0.inputs if input_.identifier=='Fac'), None)
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

        light_path_0 = node_tree0.nodes.new('ShaderNodeLightPath')
        if hasattr(light_path_0, 'color'):
            light_path_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(light_path_0, 'hide'):
            light_path_0.hide = False
        if hasattr(light_path_0, 'location'):
            light_path_0.location = (93.11836242675781, 637.15380859375)
        if hasattr(light_path_0, 'mute'):
            light_path_0.mute = False
        if hasattr(light_path_0, 'name'):
            light_path_0.name = 'Light Path'
        if hasattr(light_path_0, 'use_custom_color'):
            light_path_0.use_custom_color = False
        if hasattr(light_path_0, 'width'):
            light_path_0.width = 140.0
        output = next((output for output in light_path_0.outputs if output.identifier=='Is Camera Ray'), None)
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
                output.name = 'Is Camera Ray'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Is Shadow Ray'), None)
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
                output.name = 'Is Shadow Ray'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Is Diffuse Ray'), None)
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
                output.name = 'Is Diffuse Ray'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Is Glossy Ray'), None)
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
                output.name = 'Is Glossy Ray'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Is Singular Ray'), None)
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
                output.name = 'Is Singular Ray'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Is Reflection Ray'), None)
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
                output.name = 'Is Reflection Ray'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Is Transmission Ray'), None)
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
                output.name = 'Is Transmission Ray'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Ray Length'), None)
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
                output.name = 'Ray Length'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Ray Depth'), None)
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
                output.name = 'Ray Depth'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Diffuse Depth'), None)
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
                output.name = 'Diffuse Depth'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Glossy Depth'), None)
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
                output.name = 'Glossy Depth'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Transparent Depth'), None)
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
                output.name = 'Transparent Depth'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False
        output = next((output for output in light_path_0.outputs if output.identifier=='Transmission Depth'), None)
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
                output.name = 'Transmission Depth'
            if hasattr(output, 'show_expanded'):
                output.show_expanded = False

        node_tree1 = bpy.data.node_groups.get('IOR')
        if not node_tree1:
            node_tree1 = bpy.data.node_groups.new('IOR', 'ShaderNodeTree')
            for node in node_tree1.nodes:
                node_tree1.nodes.remove(node)
            # OUTPUTS
            output = node_tree1.outputs.new('NodeSocketFloat', 'Value')
            if hasattr(output, 'attribute_domain'):
                output.attribute_domain = 'POINT'
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'max_value'):
                output.max_value = 3.4028234663852886e+38
            if hasattr(output, 'min_value'):
                output.min_value = -3.4028234663852886e+38
            if hasattr(output, 'name'):
                output.name = 'Value'
            output = node_tree1.outputs.new('NodeSocketFloat', 'Value')
            if hasattr(output, 'attribute_domain'):
                output.attribute_domain = 'POINT'
            if hasattr(output, 'default_value'):
                output.default_value = 2.0
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'max_value'):
                output.max_value = 3.4028234663852886e+38
            if hasattr(output, 'min_value'):
                output.min_value = -3.4028234663852886e+38
            if hasattr(output, 'name'):
                output.name = 'Value'
            output = node_tree1.outputs.new('NodeSocketFloat', 'Value')
            if hasattr(output, 'attribute_domain'):
                output.attribute_domain = 'POINT'
            if hasattr(output, 'default_value'):
                output.default_value = 0.0
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'max_value'):
                output.max_value = 3.4028234663852886e+38
            if hasattr(output, 'min_value'):
                output.min_value = -3.4028234663852886e+38
            if hasattr(output, 'name'):
                output.name = 'Value'
            # NODES
            value_001_1 = node_tree1.nodes.new('ShaderNodeValue')
            if hasattr(value_001_1, 'color'):
                value_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(value_001_1, 'hide'):
                value_001_1.hide = False
            if hasattr(value_001_1, 'label'):
                value_001_1.label = 'DISPERSION'
            if hasattr(value_001_1, 'location'):
                value_001_1.location = (-149.7191619873047, 6.723371982574463)
            if hasattr(value_001_1, 'mute'):
                value_001_1.mute = False
            if hasattr(value_001_1, 'name'):
                value_001_1.name = 'Value.001'
            if hasattr(value_001_1, 'use_custom_color'):
                value_001_1.use_custom_color = False
            if hasattr(value_001_1, 'width'):
                value_001_1.width = 140.0
            output = next((output for output in value_001_1.outputs if output.identifier=='Value'), None)
            if output:
                if hasattr(output, 'default_value'):
                    output.default_value = 0.4399999976158142
                if hasattr(output, 'display_shape'):
                    output.display_shape = 'CIRCLE'
                if hasattr(output, 'enabled'):
                    output.enabled = True
                if hasattr(output, 'hide'):
                    output.hide = False
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Value'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            value_1 = node_tree1.nodes.new('ShaderNodeValue')
            if hasattr(value_1, 'color'):
                value_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(value_1, 'hide'):
                value_1.hide = False
            if hasattr(value_1, 'label'):
                value_1.label = 'IOR'
            if hasattr(value_1, 'location'):
                value_1.location = (-146.17860412597656, -96.40196228027344)
            if hasattr(value_1, 'mute'):
                value_1.mute = False
            if hasattr(value_1, 'name'):
                value_1.name = 'Value'
            if hasattr(value_1, 'use_custom_color'):
                value_1.use_custom_color = False
            if hasattr(value_1, 'width'):
                value_1.width = 140.0
            output = next((output for output in value_1.outputs if output.identifier=='Value'), None)
            if output:
                if hasattr(output, 'default_value'):
                    output.default_value = 2.0
                if hasattr(output, 'display_shape'):
                    output.display_shape = 'CIRCLE'
                if hasattr(output, 'enabled'):
                    output.enabled = True
                if hasattr(output, 'hide'):
                    output.hide = False
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Value'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            math_001_1 = node_tree1.nodes.new('ShaderNodeMath')
            if hasattr(math_001_1, 'color'):
                math_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(math_001_1, 'hide'):
                math_001_1.hide = False
            if hasattr(math_001_1, 'location'):
                math_001_1.location = (152.19119262695312, 127.27082061767578)
            if hasattr(math_001_1, 'mute'):
                math_001_1.mute = False
            if hasattr(math_001_1, 'name'):
                math_001_1.name = 'Math.001'
            if hasattr(math_001_1, 'operation'):
                math_001_1.operation = 'SUBTRACT'
            if hasattr(math_001_1, 'use_clamp'):
                math_001_1.use_clamp = False
            if hasattr(math_001_1, 'use_custom_color'):
                math_001_1.use_custom_color = False
            if hasattr(math_001_1, 'width'):
                math_001_1.width = 140.0
            input_ = next((input_ for input_ in math_001_1.inputs if input_.identifier=='Value'), None)
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
                    input_.name = 'Value'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in math_001_1.inputs if input_.identifier=='Value_001'), None)
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
                    input_.name = 'Value'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in math_001_1.inputs if input_.identifier=='Value_002'), None)
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
                    input_.name = 'Value'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            output = next((output for output in math_001_1.outputs if output.identifier=='Value'), None)
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
                    output.name = 'Value'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            group_input_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_1, 'color'):
                group_input_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(group_input_1, 'hide'):
                group_input_1.hide = False
            if hasattr(group_input_1, 'location'):
                group_input_1.location = (-349.71917724609375, -8.653131484985352)
            if hasattr(group_input_1, 'mute'):
                group_input_1.mute = False
            if hasattr(group_input_1, 'name'):
                group_input_1.name = 'Group Input'
            if hasattr(group_input_1, 'use_custom_color'):
                group_input_1.use_custom_color = False
            if hasattr(group_input_1, 'width'):
                group_input_1.width = 140.0

            group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
            if hasattr(group_output_1, 'color'):
                group_output_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(group_output_1, 'hide'):
                group_output_1.hide = False
            if hasattr(group_output_1, 'is_active_output'):
                group_output_1.is_active_output = True
            if hasattr(group_output_1, 'location'):
                group_output_1.location = (342.1911926269531, -8.653131484985352)
            if hasattr(group_output_1, 'mute'):
                group_output_1.mute = False
            if hasattr(group_output_1, 'name'):
                group_output_1.name = 'Group Output'
            if hasattr(group_output_1, 'use_custom_color'):
                group_output_1.use_custom_color = False
            if hasattr(group_output_1, 'width'):
                group_output_1.width = 140.0
            if hasattr(group_output_1.inputs[0], 'default_value'):
                group_output_1.inputs[0].default_value = 0.0
            if hasattr(group_output_1.inputs[0], 'display_shape'):
                group_output_1.inputs[0].display_shape = 'CIRCLE'
            if hasattr(group_output_1.inputs[0], 'enabled'):
                group_output_1.inputs[0].enabled = True
            if hasattr(group_output_1.inputs[0], 'hide'):
                group_output_1.inputs[0].hide = False
            if hasattr(group_output_1.inputs[0], 'hide_value'):
                group_output_1.inputs[0].hide_value = False
            if hasattr(group_output_1.inputs[0], 'name'):
                group_output_1.inputs[0].name = 'Value'
            if hasattr(group_output_1.inputs[0], 'show_expanded'):
                group_output_1.inputs[0].show_expanded = False
            if hasattr(group_output_1.inputs[1], 'default_value'):
                group_output_1.inputs[1].default_value = 2.0
            if hasattr(group_output_1.inputs[1], 'display_shape'):
                group_output_1.inputs[1].display_shape = 'CIRCLE'
            if hasattr(group_output_1.inputs[1], 'enabled'):
                group_output_1.inputs[1].enabled = True
            if hasattr(group_output_1.inputs[1], 'hide'):
                group_output_1.inputs[1].hide = False
            if hasattr(group_output_1.inputs[1], 'hide_value'):
                group_output_1.inputs[1].hide_value = False
            if hasattr(group_output_1.inputs[1], 'name'):
                group_output_1.inputs[1].name = 'Value'
            if hasattr(group_output_1.inputs[1], 'show_expanded'):
                group_output_1.inputs[1].show_expanded = False
            if hasattr(group_output_1.inputs[2], 'default_value'):
                group_output_1.inputs[2].default_value = 0.0
            if hasattr(group_output_1.inputs[2], 'display_shape'):
                group_output_1.inputs[2].display_shape = 'CIRCLE'
            if hasattr(group_output_1.inputs[2], 'enabled'):
                group_output_1.inputs[2].enabled = True
            if hasattr(group_output_1.inputs[2], 'hide'):
                group_output_1.inputs[2].hide = False
            if hasattr(group_output_1.inputs[2], 'hide_value'):
                group_output_1.inputs[2].hide_value = False
            if hasattr(group_output_1.inputs[2], 'name'):
                group_output_1.inputs[2].name = 'Value'
            if hasattr(group_output_1.inputs[2], 'show_expanded'):
                group_output_1.inputs[2].show_expanded = False

            math_1 = node_tree1.nodes.new('ShaderNodeMath')
            if hasattr(math_1, 'color'):
                math_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(math_1, 'hide'):
                math_1.hide = False
            if hasattr(math_1, 'location'):
                math_1.location = (142.9673614501953, -144.57708740234375)
            if hasattr(math_1, 'mute'):
                math_1.mute = False
            if hasattr(math_1, 'name'):
                math_1.name = 'Math'
            if hasattr(math_1, 'operation'):
                math_1.operation = 'ADD'
            if hasattr(math_1, 'use_clamp'):
                math_1.use_clamp = False
            if hasattr(math_1, 'use_custom_color'):
                math_1.use_custom_color = False
            if hasattr(math_1, 'width'):
                math_1.width = 140.0
            input_ = next((input_ for input_ in math_1.inputs if input_.identifier=='Value'), None)
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
                    input_.name = 'Value'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in math_1.inputs if input_.identifier=='Value_001'), None)
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
                    input_.name = 'Value'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in math_1.inputs if input_.identifier=='Value_002'), None)
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
                    input_.name = 'Value'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            output = next((output for output in math_1.outputs if output.identifier=='Value'), None)
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
                    output.name = 'Value'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            # LINKS
            node_tree1.links.new(math_1.outputs[0], group_output_1.inputs[0])
            node_tree1.links.new(value_1.outputs[0], group_output_1.inputs[1])
            node_tree1.links.new(math_001_1.outputs[0], group_output_1.inputs[2])
            node_tree1.links.new(value_1.outputs[0], math_1.inputs[0])
            node_tree1.links.new(value_1.outputs[0], math_001_1.inputs[0])
            node_tree1.links.new(value_001_1.outputs[0], math_001_1.inputs[1])
            node_tree1.links.new(value_001_1.outputs[0], math_1.inputs[1])

        group_0 = node_tree0.nodes.new('ShaderNodeGroup')
        if hasattr(group_0, 'node_tree'):
            group_0.node_tree = bpy.data.node_groups.get('IOR')
        if hasattr(group_0, 'color'):
            group_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(group_0, 'hide'):
            group_0.hide = False
        if hasattr(group_0, 'label'):
            group_0.label = 'IOR'
        if hasattr(group_0, 'location'):
            group_0.location = (1.57269287109375, 24.823808670043945)
        if hasattr(group_0, 'mute'):
            group_0.mute = False
        if hasattr(group_0, 'name'):
            group_0.name = 'Group'
        if hasattr(group_0, 'use_custom_color'):
            group_0.use_custom_color = False
        if hasattr(group_0, 'width'):
            group_0.width = 140.0
        if hasattr(group_0.outputs[0], 'default_value'):
            group_0.outputs[0].default_value = 0.0
        if hasattr(group_0.outputs[0], 'display_shape'):
            group_0.outputs[0].display_shape = 'CIRCLE'
        if hasattr(group_0.outputs[0], 'enabled'):
            group_0.outputs[0].enabled = True
        if hasattr(group_0.outputs[0], 'hide'):
            group_0.outputs[0].hide = False
        if hasattr(group_0.outputs[0], 'hide_value'):
            group_0.outputs[0].hide_value = False
        if hasattr(group_0.outputs[0], 'name'):
            group_0.outputs[0].name = 'Value'
        if hasattr(group_0.outputs[0], 'show_expanded'):
            group_0.outputs[0].show_expanded = False
        if hasattr(group_0.outputs[1], 'default_value'):
            group_0.outputs[1].default_value = 2.0
        if hasattr(group_0.outputs[1], 'display_shape'):
            group_0.outputs[1].display_shape = 'CIRCLE'
        if hasattr(group_0.outputs[1], 'enabled'):
            group_0.outputs[1].enabled = True
        if hasattr(group_0.outputs[1], 'hide'):
            group_0.outputs[1].hide = False
        if hasattr(group_0.outputs[1], 'hide_value'):
            group_0.outputs[1].hide_value = False
        if hasattr(group_0.outputs[1], 'name'):
            group_0.outputs[1].name = 'Value'
        if hasattr(group_0.outputs[1], 'show_expanded'):
            group_0.outputs[1].show_expanded = False
        if hasattr(group_0.outputs[2], 'default_value'):
            group_0.outputs[2].default_value = 0.0
        if hasattr(group_0.outputs[2], 'display_shape'):
            group_0.outputs[2].display_shape = 'CIRCLE'
        if hasattr(group_0.outputs[2], 'enabled'):
            group_0.outputs[2].enabled = True
        if hasattr(group_0.outputs[2], 'hide'):
            group_0.outputs[2].hide = False
        if hasattr(group_0.outputs[2], 'hide_value'):
            group_0.outputs[2].hide_value = False
        if hasattr(group_0.outputs[2], 'name'):
            group_0.outputs[2].name = 'Value'
        if hasattr(group_0.outputs[2], 'show_expanded'):
            group_0.outputs[2].show_expanded = False

        # LINKS
        node_tree0.links.new(group_0.outputs[0], glass_bsdf_003_0.inputs[2])
        node_tree0.links.new(group_0.outputs[1], glass_bsdf_002_0.inputs[2])
        node_tree0.links.new(group_0.outputs[1], glass_bsdf_001_0.inputs[2])
        node_tree0.links.new(group_0.outputs[2], glass_bsdf_0.inputs[2])
        node_tree0.links.new(glass_bsdf_001_0.outputs[0], add_shader_0.inputs[0])
        node_tree0.links.new(glass_bsdf_002_0.outputs[0], add_shader_0.inputs[1])
        node_tree0.links.new(add_shader_0.outputs[0], add_shader_001_0.inputs[0])
        node_tree0.links.new(glass_bsdf_003_0.outputs[0], add_shader_001_0.inputs[1])
        node_tree0.links.new(mix_shader_0.outputs[0], material_output_0.inputs[0])
        node_tree0.links.new(add_shader_001_0.outputs[0], mix_shader_0.inputs[2])
        node_tree0.links.new(glass_bsdf_0.outputs[0], mix_shader_0.inputs[1])
        node_tree0.links.new(light_path_0.outputs[0], mix_shader_0.inputs[0])

        # TO ACTIVE
        selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
        for obj in selected_objects:
            obj.active_material = crystal


        return crystal
