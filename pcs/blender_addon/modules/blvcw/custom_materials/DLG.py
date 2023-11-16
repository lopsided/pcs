import bpy

class Material():
    def __init__(self):
        pass
    
    def load():
        import bpy

        # MATERIAL
        dispersion_light_glass = bpy.data.materials.new(name='Dispersion Light Glass')
        dispersion_light_glass.use_nodes = True
        node_tree0 = dispersion_light_glass.node_tree

        for node in node_tree0.nodes:
            node_tree0.nodes.remove(node)
        # NODES
        material_output_001_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
        if hasattr(material_output_001_0, 'color'):
            material_output_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(material_output_001_0, 'hide'):
            material_output_001_0.hide = False
        if hasattr(material_output_001_0, 'is_active_output'):
            material_output_001_0.is_active_output = True
        if hasattr(material_output_001_0, 'location'):
            material_output_001_0.location = (577.5897216796875, 765.9930419921875)
        if hasattr(material_output_001_0, 'mute'):
            material_output_001_0.mute = False
        if hasattr(material_output_001_0, 'name'):
            material_output_001_0.name = 'Material Output.001'
        if hasattr(material_output_001_0, 'target'):
            material_output_001_0.target = 'ALL'
        if hasattr(material_output_001_0, 'use_custom_color'):
            material_output_001_0.use_custom_color = False
        if hasattr(material_output_001_0, 'width'):
            material_output_001_0.width = 140.0
        input_ = next((input_ for input_ in material_output_001_0.inputs if input_.identifier=='Displacement'), None)
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
        input_ = next((input_ for input_ in material_output_001_0.inputs if input_.identifier=='Thickness'), None)
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

        mix_shader_0 = node_tree0.nodes.new('ShaderNodeMixShader')
        if hasattr(mix_shader_0, 'color'):
            mix_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(mix_shader_0, 'hide'):
            mix_shader_0.hide = False
        if hasattr(mix_shader_0, 'location'):
            mix_shader_0.location = (324.27960205078125, 794.6932373046875)
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

        add_shader_0 = node_tree0.nodes.new('ShaderNodeAddShader')
        if hasattr(add_shader_0, 'color'):
            add_shader_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(add_shader_0, 'hide'):
            add_shader_0.hide = False
        if hasattr(add_shader_0, 'location'):
            add_shader_0.location = (68.24461364746094, 715.4537353515625)
        if hasattr(add_shader_0, 'mute'):
            add_shader_0.mute = False
        if hasattr(add_shader_0, 'name'):
            add_shader_0.name = 'Add Shader'
        if hasattr(add_shader_0, 'use_custom_color'):
            add_shader_0.use_custom_color = False
        if hasattr(add_shader_0, 'width'):
            add_shader_0.width = 140.0

        glass_bsdf_001_0 = node_tree0.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_001_0, 'color'):
            glass_bsdf_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(glass_bsdf_001_0, 'distribution'):
            glass_bsdf_001_0.distribution = 'BECKMANN'
        if hasattr(glass_bsdf_001_0, 'hide'):
            glass_bsdf_001_0.hide = False
        if hasattr(glass_bsdf_001_0, 'location'):
            glass_bsdf_001_0.location = (-602.7418212890625, 387.7802429199219)
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
        input_ = next((input_ for input_ in glass_bsdf_001_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.20000000298023224
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
            glass_bsdf_002_0.distribution = 'BECKMANN'
        if hasattr(glass_bsdf_002_0, 'hide'):
            glass_bsdf_002_0.hide = False
        if hasattr(glass_bsdf_002_0, 'location'):
            glass_bsdf_002_0.location = (-251.00015258789062, 279.92767333984375)
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
        input_ = next((input_ for input_ in glass_bsdf_002_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.20000000298023224
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
                input_.default_value = 1.5
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
            add_shader_001_0.location = (-252.99310302734375, 683.7171630859375)
        if hasattr(add_shader_001_0, 'mute'):
            add_shader_001_0.mute = False
        if hasattr(add_shader_001_0, 'name'):
            add_shader_001_0.name = 'Add Shader.001'
        if hasattr(add_shader_001_0, 'use_custom_color'):
            add_shader_001_0.use_custom_color = False
        if hasattr(add_shader_001_0, 'width'):
            add_shader_001_0.width = 140.0

        glass_bsdf_0 = node_tree0.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_0, 'color'):
            glass_bsdf_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(glass_bsdf_0, 'distribution'):
            glass_bsdf_0.distribution = 'BECKMANN'
        if hasattr(glass_bsdf_0, 'hide'):
            glass_bsdf_0.hide = False
        if hasattr(glass_bsdf_0, 'location'):
            glass_bsdf_0.location = (-574.3212280273438, 597.280029296875)
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
        input_ = next((input_ for input_ in glass_bsdf_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.20000000298023224
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

        light_path_0 = node_tree0.nodes.new('ShaderNodeLightPath')
        if hasattr(light_path_0, 'color'):
            light_path_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(light_path_0, 'hide'):
            light_path_0.hide = False
        if hasattr(light_path_0, 'location'):
            light_path_0.location = (-237.04754638671875, 1112.1092529296875)
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

        # LINKS
        node_tree0.links.new(mix_shader_0.outputs[0], material_output_001_0.inputs[0])
        node_tree0.links.new(add_shader_0.outputs[0], mix_shader_0.inputs[1])
        node_tree0.links.new(add_shader_001_0.outputs[0], add_shader_0.inputs[0])
        node_tree0.links.new(glass_bsdf_0.outputs[0], add_shader_001_0.inputs[0])
        node_tree0.links.new(glass_bsdf_001_0.outputs[0], add_shader_001_0.inputs[1])
        node_tree0.links.new(glass_bsdf_002_0.outputs[0], add_shader_0.inputs[1])
        node_tree0.links.new(light_path_0.outputs[12], mix_shader_0.inputs[0])

        return dispersion_light_glass
        # TO ACTIVE
        # selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
        # for obj in selected_objects:
        #     obj.active_material = dispersion_light_glass
