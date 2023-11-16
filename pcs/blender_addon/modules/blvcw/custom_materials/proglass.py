import bpy

class Material():
    def __init__(self):
        pass
    
    def load():
        import bpy

        # MATERIAL
        glass_shader_01 = bpy.data.materials.new(name='Glass Shader #01')
        glass_shader_01.use_nodes = True
        node_tree0 = glass_shader_01.node_tree

        for node in node_tree0.nodes:
            node_tree0.nodes.remove(node)
        # NODES
        node_tree1 = bpy.data.node_groups.get('Pro Glass 01')
        if not node_tree1:
            node_tree1 = bpy.data.node_groups.new('Pro Glass 01', 'ShaderNodeTree')
            for node in node_tree1.nodes:
                node_tree1.nodes.remove(node)
            # INPUTS
            input = node_tree1.inputs.new('NodeSocketColor', 'Glass & Volume Color')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (0.5380358099937439, 0.5030292868614197, 0.4672035574913025, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Glass & Volume Color'
            input = node_tree1.inputs.new('NodeSocketColor', 'Glossy Color')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Glossy Color'
            input = node_tree1.inputs.new('NodeSocketColor', 'Transparent ShadowColor')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (0.36344847083091736, 0.36344847083091736, 0.36344847083091736, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Transparent ShadowColor'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', 'Glass Roughness')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = 'Glass Roughness'
            input = node_tree1.inputs.new('NodeSocketFloat', 'IOR')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 1.5
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1000.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = 'IOR'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', 'Glossy Roughness')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = 'Glossy Roughness'
            input = node_tree1.inputs.new('NodeSocketFloat', 'Volume Density')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 1.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1000.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = 'Volume Density'
            # OUTPUTS
            output = node_tree1.outputs.new('NodeSocketShader', 'Shader')
            if hasattr(output, 'attribute_domain'):
                output.attribute_domain = 'POINT'
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Shader'
            output = node_tree1.outputs.new('NodeSocketShader', 'Volume')
            if hasattr(output, 'attribute_domain'):
                output.attribute_domain = 'POINT'
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Volume'
            # NODES
            glass_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfGlass')
            if hasattr(glass_bsdf_1, 'color'):
                glass_bsdf_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(glass_bsdf_1, 'distribution'):
                glass_bsdf_1.distribution = 'BECKMANN'
            if hasattr(glass_bsdf_1, 'hide'):
                glass_bsdf_1.hide = False
            if hasattr(glass_bsdf_1, 'location'):
                glass_bsdf_1.location = (17.961669921875, -24.273284912109375)
            if hasattr(glass_bsdf_1, 'mute'):
                glass_bsdf_1.mute = False
            if hasattr(glass_bsdf_1, 'name'):
                glass_bsdf_1.name = 'Glass BSDF'
            if hasattr(glass_bsdf_1, 'use_custom_color'):
                glass_bsdf_1.use_custom_color = False
            if hasattr(glass_bsdf_1, 'width'):
                glass_bsdf_1.width = 150.0
            input_ = next((input_ for input_ in glass_bsdf_1.inputs if input_.identifier=='Color'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.5380358099937439, 0.5030292868614197, 0.4672035574913025, 1.0)
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
            input_ = next((input_ for input_ in glass_bsdf_1.inputs if input_.identifier=='Roughness'), None)
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
                    input_.name = 'Roughness'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in glass_bsdf_1.inputs if input_.identifier=='IOR'), None)
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
            input_ = next((input_ for input_ in glass_bsdf_1.inputs if input_.identifier=='Normal'), None)
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
            input_ = next((input_ for input_ in glass_bsdf_1.inputs if input_.identifier=='Weight'), None)
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

            mix_shader_1 = node_tree1.nodes.new('ShaderNodeMixShader')
            if hasattr(mix_shader_1, 'color'):
                mix_shader_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_shader_1, 'hide'):
                mix_shader_1.hide = False
            if hasattr(mix_shader_1, 'location'):
                mix_shader_1.location = (461.15576171875, -43.679443359375)
            if hasattr(mix_shader_1, 'mute'):
                mix_shader_1.mute = False
            if hasattr(mix_shader_1, 'name'):
                mix_shader_1.name = 'Mix Shader'
            if hasattr(mix_shader_1, 'use_custom_color'):
                mix_shader_1.use_custom_color = False
            if hasattr(mix_shader_1, 'width'):
                mix_shader_1.width = 140.0
            input_ = next((input_ for input_ in mix_shader_1.inputs if input_.identifier=='Fac'), None)
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

            geometry_001_1 = node_tree1.nodes.new('ShaderNodeNewGeometry')
            if hasattr(geometry_001_1, 'color'):
                geometry_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(geometry_001_1, 'hide'):
                geometry_001_1.hide = False
            if hasattr(geometry_001_1, 'location'):
                geometry_001_1.location = (-787.9130859375, -322.8700866699219)
            if hasattr(geometry_001_1, 'mute'):
                geometry_001_1.mute = False
            if hasattr(geometry_001_1, 'name'):
                geometry_001_1.name = 'Geometry.001'
            if hasattr(geometry_001_1, 'use_custom_color'):
                geometry_001_1.use_custom_color = False
            if hasattr(geometry_001_1, 'width'):
                geometry_001_1.width = 140.0
            output = next((output for output in geometry_001_1.outputs if output.identifier=='Position'), None)
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
            output = next((output for output in geometry_001_1.outputs if output.identifier=='Normal'), None)
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
            output = next((output for output in geometry_001_1.outputs if output.identifier=='Tangent'), None)
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
                    output.name = 'Tangent'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_001_1.outputs if output.identifier=='True Normal'), None)
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
                    output.name = 'True Normal'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_001_1.outputs if output.identifier=='Incoming'), None)
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
                    output.name = 'Incoming'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_001_1.outputs if output.identifier=='Parametric'), None)
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
                    output.name = 'Parametric'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_001_1.outputs if output.identifier=='Backfacing'), None)
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
                    output.name = 'Backfacing'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_001_1.outputs if output.identifier=='Pointiness'), None)
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
                    output.name = 'Pointiness'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_001_1.outputs if output.identifier=='Random Per Island'), None)
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
                    output.name = 'Random Per Island'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            vector_math_1 = node_tree1.nodes.new('ShaderNodeVectorMath')
            if hasattr(vector_math_1, 'color'):
                vector_math_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(vector_math_1, 'hide'):
                vector_math_1.hide = False
            if hasattr(vector_math_1, 'location'):
                vector_math_1.location = (-585.81689453125, -232.3011474609375)
            if hasattr(vector_math_1, 'mute'):
                vector_math_1.mute = False
            if hasattr(vector_math_1, 'name'):
                vector_math_1.name = 'Vector Math'
            if hasattr(vector_math_1, 'operation'):
                vector_math_1.operation = 'DOT_PRODUCT'
            if hasattr(vector_math_1, 'use_custom_color'):
                vector_math_1.use_custom_color = False
            if hasattr(vector_math_1, 'width'):
                vector_math_1.width = 140.0
            input_ = next((input_ for input_ in vector_math_1.inputs if input_.identifier=='Vector'), None)
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
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Vector'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in vector_math_1.inputs if input_.identifier=='Vector_001'), None)
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
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Vector'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in vector_math_1.inputs if input_.identifier=='Vector_002'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.0, 0.0, 0.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = False
                if hasattr(input_, 'hide'):
                    input_.hide = False
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Vector'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in vector_math_1.inputs if input_.identifier=='Scale'), None)
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
                    input_.name = 'Scale'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            output = next((output for output in vector_math_1.outputs if output.identifier=='Vector'), None)
            if output:
                if hasattr(output, 'default_value'):
                    output.default_value = (0.0, 0.0, 0.0)
                if hasattr(output, 'display_shape'):
                    output.display_shape = 'CIRCLE'
                if hasattr(output, 'enabled'):
                    output.enabled = False
                if hasattr(output, 'hide'):
                    output.hide = False
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Vector'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in vector_math_1.outputs if output.identifier=='Value'), None)
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

            geometry_1 = node_tree1.nodes.new('ShaderNodeNewGeometry')
            if hasattr(geometry_1, 'color'):
                geometry_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(geometry_1, 'hide'):
                geometry_1.hide = False
            if hasattr(geometry_1, 'location'):
                geometry_1.location = (-781.2869873046875, -55.58123779296875)
            if hasattr(geometry_1, 'mute'):
                geometry_1.mute = False
            if hasattr(geometry_1, 'name'):
                geometry_1.name = 'Geometry'
            if hasattr(geometry_1, 'use_custom_color'):
                geometry_1.use_custom_color = False
            if hasattr(geometry_1, 'width'):
                geometry_1.width = 140.0
            output = next((output for output in geometry_1.outputs if output.identifier=='Position'), None)
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
            output = next((output for output in geometry_1.outputs if output.identifier=='Normal'), None)
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
            output = next((output for output in geometry_1.outputs if output.identifier=='Tangent'), None)
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
                    output.name = 'Tangent'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_1.outputs if output.identifier=='True Normal'), None)
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
                    output.name = 'True Normal'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_1.outputs if output.identifier=='Incoming'), None)
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
                    output.name = 'Incoming'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_1.outputs if output.identifier=='Parametric'), None)
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
                    output.name = 'Parametric'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_1.outputs if output.identifier=='Backfacing'), None)
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
                    output.name = 'Backfacing'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_1.outputs if output.identifier=='Pointiness'), None)
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
                    output.name = 'Pointiness'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in geometry_1.outputs if output.identifier=='Random Per Island'), None)
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
                    output.name = 'Random Per Island'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            colorramp_1 = node_tree1.nodes.new('ShaderNodeValToRGB')
            if hasattr(colorramp_1, 'color'):
                colorramp_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(colorramp_1, 'color_ramp'):
                if hasattr(colorramp_1.color_ramp, 'color_mode'):
                    colorramp_1.color_ramp.color_mode = 'RGB'
                if hasattr(colorramp_1.color_ramp, 'elements'):
                    if 0 >= len(colorramp_1.color_ramp.elements):
                        colorramp_1.color_ramp.elements.new(0.4954543709754944)
                    if hasattr(colorramp_1.color_ramp.elements[0], 'alpha'):
                        colorramp_1.color_ramp.elements[0].alpha = 1.0
                    if hasattr(colorramp_1.color_ramp.elements[0], 'color'):
                        colorramp_1.color_ramp.elements[0].color = (1.0, 1.0, 1.0, 1.0)
                    if hasattr(colorramp_1.color_ramp.elements[0], 'position'):
                        colorramp_1.color_ramp.elements[0].position = 0.4954543709754944
                    if 1 >= len(colorramp_1.color_ramp.elements):
                        colorramp_1.color_ramp.elements.new(0.5818184614181519)
                    if hasattr(colorramp_1.color_ramp.elements[1], 'alpha'):
                        colorramp_1.color_ramp.elements[1].alpha = 1.0
                    if hasattr(colorramp_1.color_ramp.elements[1], 'color'):
                        colorramp_1.color_ramp.elements[1].color = (0.0024097254499793053, 0.0024097254499793053, 0.0024097254499793053, 1.0)
                    if hasattr(colorramp_1.color_ramp.elements[1], 'position'):
                        colorramp_1.color_ramp.elements[1].position = 0.5818184614181519
                    if 2 >= len(colorramp_1.color_ramp.elements):
                        colorramp_1.color_ramp.elements.new(0.6681815385818481)
                    if hasattr(colorramp_1.color_ramp.elements[2], 'alpha'):
                        colorramp_1.color_ramp.elements[2].alpha = 1.0
                    if hasattr(colorramp_1.color_ramp.elements[2], 'color'):
                        colorramp_1.color_ramp.elements[2].color = (1.0, 1.0, 1.0, 1.0)
                    if hasattr(colorramp_1.color_ramp.elements[2], 'position'):
                        colorramp_1.color_ramp.elements[2].position = 0.6681815385818481
                    if 3 >= len(colorramp_1.color_ramp.elements):
                        colorramp_1.color_ramp.elements.new(0.7727270126342773)
                    if hasattr(colorramp_1.color_ramp.elements[3], 'alpha'):
                        colorramp_1.color_ramp.elements[3].alpha = 1.0
                    if hasattr(colorramp_1.color_ramp.elements[3], 'color'):
                        colorramp_1.color_ramp.elements[3].color = (0.23237457871437073, 0.23237457871437073, 0.23237457871437073, 1.0)
                    if hasattr(colorramp_1.color_ramp.elements[3], 'position'):
                        colorramp_1.color_ramp.elements[3].position = 0.7727270126342773
                if hasattr(colorramp_1.color_ramp, 'hue_interpolation'):
                    colorramp_1.color_ramp.hue_interpolation = 'NEAR'
                if hasattr(colorramp_1.color_ramp, 'interpolation'):
                    colorramp_1.color_ramp.interpolation = 'LINEAR'
            if hasattr(colorramp_1, 'hide'):
                colorramp_1.hide = False
            if hasattr(colorramp_1, 'location'):
                colorramp_1.location = (-373.78167724609375, -187.01663208007812)
            if hasattr(colorramp_1, 'mute'):
                colorramp_1.mute = False
            if hasattr(colorramp_1, 'name'):
                colorramp_1.name = 'ColorRamp'
            if hasattr(colorramp_1, 'use_custom_color'):
                colorramp_1.use_custom_color = False
            if hasattr(colorramp_1, 'width'):
                colorramp_1.width = 240.0
            input_ = next((input_ for input_ in colorramp_1.inputs if input_.identifier=='Fac'), None)
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
            output = next((output for output in colorramp_1.outputs if output.identifier=='Color'), None)
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
            output = next((output for output in colorramp_1.outputs if output.identifier=='Alpha'), None)
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

            math_1 = node_tree1.nodes.new('ShaderNodeMath')
            if hasattr(math_1, 'color'):
                math_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(math_1, 'hide'):
                math_1.hide = False
            if hasattr(math_1, 'location'):
                math_1.location = (-54.0869140625, -219.00228881835938)
            if hasattr(math_1, 'mute'):
                math_1.mute = False
            if hasattr(math_1, 'name'):
                math_1.name = 'Math'
            if hasattr(math_1, 'operation'):
                math_1.operation = 'MULTIPLY'
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

            glossy_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfGlossy')
            if hasattr(glossy_bsdf_1, 'color'):
                glossy_bsdf_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(glossy_bsdf_1, 'distribution'):
                glossy_bsdf_1.distribution = 'GGX'
            if hasattr(glossy_bsdf_1, 'hide'):
                glossy_bsdf_1.hide = False
            if hasattr(glossy_bsdf_1, 'location'):
                glossy_bsdf_1.location = (449.4283447265625, -226.29867553710938)
            if hasattr(glossy_bsdf_1, 'mute'):
                glossy_bsdf_1.mute = False
            if hasattr(glossy_bsdf_1, 'name'):
                glossy_bsdf_1.name = 'Glossy BSDF'
            if hasattr(glossy_bsdf_1, 'use_custom_color'):
                glossy_bsdf_1.use_custom_color = False
            if hasattr(glossy_bsdf_1, 'width'):
                glossy_bsdf_1.width = 150.0
            input_ = next((input_ for input_ in glossy_bsdf_1.inputs if input_.identifier=='Color'), None)
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
            input_ = next((input_ for input_ in glossy_bsdf_1.inputs if input_.identifier=='Roughness'), None)
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
                    input_.name = 'Roughness'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in glossy_bsdf_1.inputs if input_.identifier=='Normal'), None)
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
            input_ = next((input_ for input_ in glossy_bsdf_1.inputs if input_.identifier=='Weight'), None)
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

            fresnel_1 = node_tree1.nodes.new('ShaderNodeFresnel')
            if hasattr(fresnel_1, 'color'):
                fresnel_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(fresnel_1, 'hide'):
                fresnel_1.hide = False
            if hasattr(fresnel_1, 'location'):
                fresnel_1.location = (45.208465576171875, 131.21499633789062)
            if hasattr(fresnel_1, 'mute'):
                fresnel_1.mute = False
            if hasattr(fresnel_1, 'name'):
                fresnel_1.name = 'Fresnel'
            if hasattr(fresnel_1, 'use_custom_color'):
                fresnel_1.use_custom_color = False
            if hasattr(fresnel_1, 'width'):
                fresnel_1.width = 140.0
            input_ = next((input_ for input_ in fresnel_1.inputs if input_.identifier=='IOR'), None)
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
            input_ = next((input_ for input_ in fresnel_1.inputs if input_.identifier=='Normal'), None)
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
            output = next((output for output in fresnel_1.outputs if output.identifier=='Fac'), None)
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

            group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
            if hasattr(group_output_1, 'color'):
                group_output_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(group_output_1, 'hide'):
                group_output_1.hide = False
            if hasattr(group_output_1, 'is_active_output'):
                group_output_1.is_active_output = True
            if hasattr(group_output_1, 'location'):
                group_output_1.location = (1272.217041015625, 1.855438232421875)
            if hasattr(group_output_1, 'mute'):
                group_output_1.mute = False
            if hasattr(group_output_1, 'name'):
                group_output_1.name = 'Group Output'
            if hasattr(group_output_1, 'use_custom_color'):
                group_output_1.use_custom_color = False
            if hasattr(group_output_1, 'width'):
                group_output_1.width = 140.0

            mix_shader_001_1 = node_tree1.nodes.new('ShaderNodeMixShader')
            if hasattr(mix_shader_001_1, 'color'):
                mix_shader_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_shader_001_1, 'hide'):
                mix_shader_001_1.hide = False
            if hasattr(mix_shader_001_1, 'location'):
                mix_shader_001_1.location = (787.9130859375, -11.43780517578125)
            if hasattr(mix_shader_001_1, 'mute'):
                mix_shader_001_1.mute = False
            if hasattr(mix_shader_001_1, 'name'):
                mix_shader_001_1.name = 'Mix Shader.001'
            if hasattr(mix_shader_001_1, 'use_custom_color'):
                mix_shader_001_1.use_custom_color = False
            if hasattr(mix_shader_001_1, 'width'):
                mix_shader_001_1.width = 140.0
            input_ = next((input_ for input_ in mix_shader_001_1.inputs if input_.identifier=='Fac'), None)
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

            mix_shader_002_1 = node_tree1.nodes.new('ShaderNodeMixShader')
            if hasattr(mix_shader_002_1, 'color'):
                mix_shader_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_shader_002_1, 'hide'):
                mix_shader_002_1.hide = False
            if hasattr(mix_shader_002_1, 'location'):
                mix_shader_002_1.location = (1008.1781616210938, -0.30511474609375)
            if hasattr(mix_shader_002_1, 'mute'):
                mix_shader_002_1.mute = False
            if hasattr(mix_shader_002_1, 'name'):
                mix_shader_002_1.name = 'Mix Shader.002'
            if hasattr(mix_shader_002_1, 'use_custom_color'):
                mix_shader_002_1.use_custom_color = False
            if hasattr(mix_shader_002_1, 'width'):
                mix_shader_002_1.width = 140.0
            input_ = next((input_ for input_ in mix_shader_002_1.inputs if input_.identifier=='Fac'), None)
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

            light_path_1 = node_tree1.nodes.new('ShaderNodeLightPath')
            if hasattr(light_path_1, 'color'):
                light_path_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(light_path_1, 'hide'):
                light_path_1.hide = False
            if hasattr(light_path_1, 'location'):
                light_path_1.location = (449.1773681640625, 322.8701171875)
            if hasattr(light_path_1, 'mute'):
                light_path_1.mute = False
            if hasattr(light_path_1, 'name'):
                light_path_1.name = 'Light Path'
            if hasattr(light_path_1, 'use_custom_color'):
                light_path_1.use_custom_color = False
            if hasattr(light_path_1, 'width'):
                light_path_1.width = 140.0
            output = next((output for output in light_path_1.outputs if output.identifier=='Is Camera Ray'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Is Shadow Ray'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Is Diffuse Ray'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Is Glossy Ray'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Is Singular Ray'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Is Reflection Ray'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Is Transmission Ray'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Ray Length'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Ray Depth'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Diffuse Depth'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Glossy Depth'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Transparent Depth'), None)
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
            output = next((output for output in light_path_1.outputs if output.identifier=='Transmission Depth'), None)
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

            transparent_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfTransparent')
            if hasattr(transparent_bsdf_1, 'color'):
                transparent_bsdf_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(transparent_bsdf_1, 'hide'):
                transparent_bsdf_1.hide = False
            if hasattr(transparent_bsdf_1, 'location'):
                transparent_bsdf_1.location = (165.80612182617188, -243.53640747070312)
            if hasattr(transparent_bsdf_1, 'mute'):
                transparent_bsdf_1.mute = False
            if hasattr(transparent_bsdf_1, 'name'):
                transparent_bsdf_1.name = 'Transparent BSDF'
            if hasattr(transparent_bsdf_1, 'use_custom_color'):
                transparent_bsdf_1.use_custom_color = False
            if hasattr(transparent_bsdf_1, 'width'):
                transparent_bsdf_1.width = 140.0
            input_ = next((input_ for input_ in transparent_bsdf_1.inputs if input_.identifier=='Color'), None)
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
            input_ = next((input_ for input_ in transparent_bsdf_1.inputs if input_.identifier=='Weight'), None)
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

            transparent_bsdf_001_1 = node_tree1.nodes.new('ShaderNodeBsdfTransparent')
            if hasattr(transparent_bsdf_001_1, 'color'):
                transparent_bsdf_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(transparent_bsdf_001_1, 'hide'):
                transparent_bsdf_001_1.hide = False
            if hasattr(transparent_bsdf_001_1, 'location'):
                transparent_bsdf_001_1.location = (769.2218627929688, -245.391845703125)
            if hasattr(transparent_bsdf_001_1, 'mute'):
                transparent_bsdf_001_1.mute = False
            if hasattr(transparent_bsdf_001_1, 'name'):
                transparent_bsdf_001_1.name = 'Transparent BSDF.001'
            if hasattr(transparent_bsdf_001_1, 'use_custom_color'):
                transparent_bsdf_001_1.use_custom_color = False
            if hasattr(transparent_bsdf_001_1, 'width'):
                transparent_bsdf_001_1.width = 140.0
            input_ = next((input_ for input_ in transparent_bsdf_001_1.inputs if input_.identifier=='Color'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.36344847083091736, 0.36344847083091736, 0.36344847083091736, 1.0)
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
            input_ = next((input_ for input_ in transparent_bsdf_001_1.inputs if input_.identifier=='Weight'), None)
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

            volume_absorption_1 = node_tree1.nodes.new('ShaderNodeVolumeAbsorption')
            if hasattr(volume_absorption_1, 'color'):
                volume_absorption_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(volume_absorption_1, 'hide'):
                volume_absorption_1.hide = False
            if hasattr(volume_absorption_1, 'location'):
                volume_absorption_1.location = (1012.6009521484375, -222.6213836669922)
            if hasattr(volume_absorption_1, 'mute'):
                volume_absorption_1.mute = False
            if hasattr(volume_absorption_1, 'name'):
                volume_absorption_1.name = 'Volume Absorption'
            if hasattr(volume_absorption_1, 'use_custom_color'):
                volume_absorption_1.use_custom_color = False
            if hasattr(volume_absorption_1, 'width'):
                volume_absorption_1.width = 140.0
            input_ = next((input_ for input_ in volume_absorption_1.inputs if input_.identifier=='Color'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.5380359888076782, 0.5030289888381958, 0.4672040045261383, 1.0)
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
            input_ = next((input_ for input_ in volume_absorption_1.inputs if input_.identifier=='Density'), None)
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
                    input_.name = 'Density'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in volume_absorption_1.inputs if input_.identifier=='Weight'), None)
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

            group_input_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_1, 'color'):
                group_input_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(group_input_1, 'hide'):
                group_input_1.hide = False
            if hasattr(group_input_1, 'location'):
                group_input_1.location = (-1300.6181640625, 130.20584106445312)
            if hasattr(group_input_1, 'mute'):
                group_input_1.mute = False
            if hasattr(group_input_1, 'name'):
                group_input_1.name = 'Group Input'
            if hasattr(group_input_1, 'use_custom_color'):
                group_input_1.use_custom_color = False
            if hasattr(group_input_1, 'width'):
                group_input_1.width = 140.0
            if hasattr(group_input_1.outputs[0], 'default_value'):
                group_input_1.outputs[0].default_value = (0.5380358099937439, 0.5030292868614197, 0.4672035574913025, 1.0)
            if hasattr(group_input_1.outputs[0], 'display_shape'):
                group_input_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[0], 'enabled'):
                group_input_1.outputs[0].enabled = True
            if hasattr(group_input_1.outputs[0], 'hide'):
                group_input_1.outputs[0].hide = False
            if hasattr(group_input_1.outputs[0], 'hide_value'):
                group_input_1.outputs[0].hide_value = False
            if hasattr(group_input_1.outputs[0], 'name'):
                group_input_1.outputs[0].name = 'Glass & Volume Color'
            if hasattr(group_input_1.outputs[0], 'show_expanded'):
                group_input_1.outputs[0].show_expanded = False
            if hasattr(group_input_1.outputs[1], 'default_value'):
                group_input_1.outputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_1.outputs[1], 'display_shape'):
                group_input_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[1], 'enabled'):
                group_input_1.outputs[1].enabled = True
            if hasattr(group_input_1.outputs[1], 'hide'):
                group_input_1.outputs[1].hide = False
            if hasattr(group_input_1.outputs[1], 'hide_value'):
                group_input_1.outputs[1].hide_value = False
            if hasattr(group_input_1.outputs[1], 'name'):
                group_input_1.outputs[1].name = 'Glossy Color'
            if hasattr(group_input_1.outputs[1], 'show_expanded'):
                group_input_1.outputs[1].show_expanded = False
            if hasattr(group_input_1.outputs[2], 'default_value'):
                group_input_1.outputs[2].default_value = (0.36344847083091736, 0.36344847083091736, 0.36344847083091736, 1.0)
            if hasattr(group_input_1.outputs[2], 'display_shape'):
                group_input_1.outputs[2].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[2], 'enabled'):
                group_input_1.outputs[2].enabled = True
            if hasattr(group_input_1.outputs[2], 'hide'):
                group_input_1.outputs[2].hide = False
            if hasattr(group_input_1.outputs[2], 'hide_value'):
                group_input_1.outputs[2].hide_value = False
            if hasattr(group_input_1.outputs[2], 'name'):
                group_input_1.outputs[2].name = 'Transparent ShadowColor'
            if hasattr(group_input_1.outputs[2], 'show_expanded'):
                group_input_1.outputs[2].show_expanded = False
            if hasattr(group_input_1.outputs[3], 'default_value'):
                group_input_1.outputs[3].default_value = 0.0
            if hasattr(group_input_1.outputs[3], 'display_shape'):
                group_input_1.outputs[3].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[3], 'enabled'):
                group_input_1.outputs[3].enabled = True
            if hasattr(group_input_1.outputs[3], 'hide'):
                group_input_1.outputs[3].hide = False
            if hasattr(group_input_1.outputs[3], 'hide_value'):
                group_input_1.outputs[3].hide_value = False
            if hasattr(group_input_1.outputs[3], 'name'):
                group_input_1.outputs[3].name = 'Glass Roughness'
            if hasattr(group_input_1.outputs[3], 'show_expanded'):
                group_input_1.outputs[3].show_expanded = False
            if hasattr(group_input_1.outputs[4], 'default_value'):
                group_input_1.outputs[4].default_value = 1.5
            if hasattr(group_input_1.outputs[4], 'display_shape'):
                group_input_1.outputs[4].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[4], 'enabled'):
                group_input_1.outputs[4].enabled = True
            if hasattr(group_input_1.outputs[4], 'hide'):
                group_input_1.outputs[4].hide = False
            if hasattr(group_input_1.outputs[4], 'hide_value'):
                group_input_1.outputs[4].hide_value = False
            if hasattr(group_input_1.outputs[4], 'name'):
                group_input_1.outputs[4].name = 'IOR'
            if hasattr(group_input_1.outputs[4], 'show_expanded'):
                group_input_1.outputs[4].show_expanded = False
            if hasattr(group_input_1.outputs[5], 'default_value'):
                group_input_1.outputs[5].default_value = 0.0
            if hasattr(group_input_1.outputs[5], 'display_shape'):
                group_input_1.outputs[5].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[5], 'enabled'):
                group_input_1.outputs[5].enabled = True
            if hasattr(group_input_1.outputs[5], 'hide'):
                group_input_1.outputs[5].hide = False
            if hasattr(group_input_1.outputs[5], 'hide_value'):
                group_input_1.outputs[5].hide_value = False
            if hasattr(group_input_1.outputs[5], 'name'):
                group_input_1.outputs[5].name = 'Glossy Roughness'
            if hasattr(group_input_1.outputs[5], 'show_expanded'):
                group_input_1.outputs[5].show_expanded = False
            if hasattr(group_input_1.outputs[6], 'default_value'):
                group_input_1.outputs[6].default_value = 1.0
            if hasattr(group_input_1.outputs[6], 'display_shape'):
                group_input_1.outputs[6].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[6], 'enabled'):
                group_input_1.outputs[6].enabled = True
            if hasattr(group_input_1.outputs[6], 'hide'):
                group_input_1.outputs[6].hide = False
            if hasattr(group_input_1.outputs[6], 'hide_value'):
                group_input_1.outputs[6].hide_value = False
            if hasattr(group_input_1.outputs[6], 'name'):
                group_input_1.outputs[6].name = 'Volume Density'
            if hasattr(group_input_1.outputs[6], 'show_expanded'):
                group_input_1.outputs[6].show_expanded = False

            # LINKS
            node_tree1.links.new(mix_shader_001_1.outputs[0], mix_shader_002_1.inputs[1])
            node_tree1.links.new(glass_bsdf_1.outputs[0], mix_shader_1.inputs[1])
            node_tree1.links.new(mix_shader_1.outputs[0], mix_shader_001_1.inputs[1])
            node_tree1.links.new(transparent_bsdf_1.outputs[0], mix_shader_1.inputs[2])
            node_tree1.links.new(light_path_1.outputs[1], mix_shader_001_1.inputs[0])
            node_tree1.links.new(fresnel_1.outputs[0], mix_shader_1.inputs[0])
            node_tree1.links.new(glossy_bsdf_1.outputs[0], mix_shader_001_1.inputs[2])
            node_tree1.links.new(geometry_1.outputs[1], vector_math_1.inputs[0])
            node_tree1.links.new(geometry_001_1.outputs[4], vector_math_1.inputs[1])
            node_tree1.links.new(vector_math_1.outputs[1], colorramp_1.inputs[0])
            node_tree1.links.new(colorramp_1.outputs[0], math_1.inputs[0])
            node_tree1.links.new(math_1.outputs[0], transparent_bsdf_1.inputs[0])
            node_tree1.links.new(mix_shader_002_1.outputs[0], group_output_1.inputs[0])
            node_tree1.links.new(light_path_1.outputs[1], mix_shader_002_1.inputs[0])
            node_tree1.links.new(transparent_bsdf_001_1.outputs[0], mix_shader_002_1.inputs[2])
            node_tree1.links.new(volume_absorption_1.outputs[0], group_output_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[0], glass_bsdf_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[0], volume_absorption_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[1], glossy_bsdf_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[2], transparent_bsdf_001_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[3], glass_bsdf_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[4], fresnel_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[4], glass_bsdf_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[5], glossy_bsdf_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[6], volume_absorption_1.inputs[1])

        group_0 = node_tree0.nodes.new('ShaderNodeGroup')
        if hasattr(group_0, 'node_tree'):
            group_0.node_tree = bpy.data.node_groups.get('Pro Glass 01')
        if hasattr(group_0, 'color'):
            group_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(group_0, 'hide'):
            group_0.hide = False
        if hasattr(group_0, 'location'):
            group_0.location = (312.4166259765625, 291.62664794921875)
        if hasattr(group_0, 'mute'):
            group_0.mute = False
        if hasattr(group_0, 'name'):
            group_0.name = 'Group'
        if hasattr(group_0, 'use_custom_color'):
            group_0.use_custom_color = False
        if hasattr(group_0, 'width'):
            group_0.width = 198.88739013671875
        if hasattr(group_0.inputs[0], 'default_value'):
            group_0.inputs[0].default_value = (0.6049277782440186, 0.5655686259269714, 0.5252892971038818, 1.0)
        if hasattr(group_0.inputs[0], 'display_shape'):
            group_0.inputs[0].display_shape = 'CIRCLE'
        if hasattr(group_0.inputs[0], 'enabled'):
            group_0.inputs[0].enabled = True
        if hasattr(group_0.inputs[0], 'hide'):
            group_0.inputs[0].hide = False
        if hasattr(group_0.inputs[0], 'hide_value'):
            group_0.inputs[0].hide_value = False
        if hasattr(group_0.inputs[0], 'name'):
            group_0.inputs[0].name = 'Glass & Volume Color'
        if hasattr(group_0.inputs[0], 'show_expanded'):
            group_0.inputs[0].show_expanded = False
        if hasattr(group_0.inputs[1], 'default_value'):
            group_0.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
        if hasattr(group_0.inputs[1], 'display_shape'):
            group_0.inputs[1].display_shape = 'CIRCLE'
        if hasattr(group_0.inputs[1], 'enabled'):
            group_0.inputs[1].enabled = True
        if hasattr(group_0.inputs[1], 'hide'):
            group_0.inputs[1].hide = False
        if hasattr(group_0.inputs[1], 'hide_value'):
            group_0.inputs[1].hide_value = False
        if hasattr(group_0.inputs[1], 'name'):
            group_0.inputs[1].name = 'Glossy Color'
        if hasattr(group_0.inputs[1], 'show_expanded'):
            group_0.inputs[1].show_expanded = False
        if hasattr(group_0.inputs[2], 'default_value'):
            group_0.inputs[2].default_value = (0.36344847083091736, 0.36344847083091736, 0.36344847083091736, 1.0)
        if hasattr(group_0.inputs[2], 'display_shape'):
            group_0.inputs[2].display_shape = 'CIRCLE'
        if hasattr(group_0.inputs[2], 'enabled'):
            group_0.inputs[2].enabled = True
        if hasattr(group_0.inputs[2], 'hide'):
            group_0.inputs[2].hide = False
        if hasattr(group_0.inputs[2], 'hide_value'):
            group_0.inputs[2].hide_value = False
        if hasattr(group_0.inputs[2], 'name'):
            group_0.inputs[2].name = 'Transparent ShadowColor'
        if hasattr(group_0.inputs[2], 'show_expanded'):
            group_0.inputs[2].show_expanded = False
        if hasattr(group_0.inputs[3], 'default_value'):
            group_0.inputs[3].default_value = 0.0
        if hasattr(group_0.inputs[3], 'display_shape'):
            group_0.inputs[3].display_shape = 'CIRCLE'
        if hasattr(group_0.inputs[3], 'enabled'):
            group_0.inputs[3].enabled = True
        if hasattr(group_0.inputs[3], 'hide'):
            group_0.inputs[3].hide = False
        if hasattr(group_0.inputs[3], 'hide_value'):
            group_0.inputs[3].hide_value = False
        if hasattr(group_0.inputs[3], 'name'):
            group_0.inputs[3].name = 'Glass Roughness'
        if hasattr(group_0.inputs[3], 'show_expanded'):
            group_0.inputs[3].show_expanded = False
        if hasattr(group_0.inputs[4], 'default_value'):
            group_0.inputs[4].default_value = 1.5
        if hasattr(group_0.inputs[4], 'display_shape'):
            group_0.inputs[4].display_shape = 'CIRCLE'
        if hasattr(group_0.inputs[4], 'enabled'):
            group_0.inputs[4].enabled = True
        if hasattr(group_0.inputs[4], 'hide'):
            group_0.inputs[4].hide = False
        if hasattr(group_0.inputs[4], 'hide_value'):
            group_0.inputs[4].hide_value = False
        if hasattr(group_0.inputs[4], 'name'):
            group_0.inputs[4].name = 'IOR'
        if hasattr(group_0.inputs[4], 'show_expanded'):
            group_0.inputs[4].show_expanded = False
        if hasattr(group_0.inputs[5], 'default_value'):
            group_0.inputs[5].default_value = 0.0
        if hasattr(group_0.inputs[5], 'display_shape'):
            group_0.inputs[5].display_shape = 'CIRCLE'
        if hasattr(group_0.inputs[5], 'enabled'):
            group_0.inputs[5].enabled = True
        if hasattr(group_0.inputs[5], 'hide'):
            group_0.inputs[5].hide = False
        if hasattr(group_0.inputs[5], 'hide_value'):
            group_0.inputs[5].hide_value = False
        if hasattr(group_0.inputs[5], 'name'):
            group_0.inputs[5].name = 'Glossy Roughness'
        if hasattr(group_0.inputs[5], 'show_expanded'):
            group_0.inputs[5].show_expanded = False
        if hasattr(group_0.inputs[6], 'default_value'):
            group_0.inputs[6].default_value = 2.0
        if hasattr(group_0.inputs[6], 'display_shape'):
            group_0.inputs[6].display_shape = 'CIRCLE'
        if hasattr(group_0.inputs[6], 'enabled'):
            group_0.inputs[6].enabled = True
        if hasattr(group_0.inputs[6], 'hide'):
            group_0.inputs[6].hide = False
        if hasattr(group_0.inputs[6], 'hide_value'):
            group_0.inputs[6].hide_value = False
        if hasattr(group_0.inputs[6], 'name'):
            group_0.inputs[6].name = 'Volume Density'
        if hasattr(group_0.inputs[6], 'show_expanded'):
            group_0.inputs[6].show_expanded = False

        material_output_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
        if hasattr(material_output_0, 'color'):
            material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(material_output_0, 'hide'):
            material_output_0.hide = False
        if hasattr(material_output_0, 'is_active_output'):
            material_output_0.is_active_output = True
        if hasattr(material_output_0, 'location'):
            material_output_0.location = (570.4635009765625, 293.4527587890625)
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

        # LINKS
        node_tree0.links.new(group_0.outputs[0], material_output_0.inputs[0])
        node_tree0.links.new(group_0.outputs[1], material_output_0.inputs[1])

        return glass_shader_01
        # # TO ACTIVE
        # selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
        # for obj in selected_objects:
        #     obj.active_material = glass_shader_01
