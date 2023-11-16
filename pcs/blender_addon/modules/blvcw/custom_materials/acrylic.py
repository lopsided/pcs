import bpy

class Material():
    def __init__(self):
        pass
    
    def load():

        # MATERIAL
        iridescent_acrylic_edge_emission = bpy.data.materials.new(name='Iridescent Acrylic Edge Emission')
        iridescent_acrylic_edge_emission.use_nodes = True
        node_tree0 = iridescent_acrylic_edge_emission.node_tree

        for node in node_tree0.nodes:
            node_tree0.nodes.remove(node)
        # NODES
        material_output_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
        if hasattr(material_output_0, 'color'):
            material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(material_output_0, 'hide'):
            material_output_0.hide = False
        if hasattr(material_output_0, 'is_active_output'):
            material_output_0.is_active_output = True
        if hasattr(material_output_0, 'location'):
            material_output_0.location = (420.0, 400.0)
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
                input_.hide = True
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
                input_.hide = True
            if hasattr(input_, 'hide_value'):
                input_.hide_value = True
            if hasattr(input_, 'name'):
                input_.name = 'Thickness'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False

        node_tree1 = bpy.data.node_groups.get('Iridescent Acrylic Edge Emission')
        if not node_tree1:
            node_tree1 = bpy.data.node_groups.new('Iridescent Acrylic Edge Emission', 'ShaderNodeTree')
            for node in node_tree1.nodes:
                node_tree1.nodes.remove(node)
            # INPUTS
            input = node_tree1.inputs.new('NodeSocketFloatFactor', 'Acrylic Factor')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.08333331346511841
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = 'Acrylic Factor'
            input = node_tree1.inputs.new('NodeSocketColor', 'Iridescent Color 1')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (0.8227859139442444, 0.0, 0.5936002731323242, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Iridescent Color 1'
            input = node_tree1.inputs.new('NodeSocketColor', 'Iridescent Color 2')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (0.18765491247177124, 0.7835378646850586, 0.0, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Iridescent Color 2'
            input = node_tree1.inputs.new('NodeSocketColor', 'Iridescent Color 3')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (0.004024718888103962, 0.10224173218011856, 0.7605247497558594, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Iridescent Color 3'
            input = node_tree1.inputs.new('NodeSocketColor', 'Edge Emission Color')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (0.0, 0.2521688640117645, 1.0, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Edge Emission Color'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', 'Frensel / Facing')
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
                input.name = 'Frensel / Facing'
            input = node_tree1.inputs.new('NodeSocketFloat', 'Emission Strength')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.5
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 10000.0
            if hasattr(input, 'min_value'):
                input.min_value = -10000.0
            if hasattr(input, 'name'):
                input.name = 'Emission Strength'
            input = node_tree1.inputs.new('NodeSocketFloat', 'Edge Emision Size')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 1.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 3.4028234663852886e+38
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = 'Edge Emision Size'
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
            author_1 = node_tree1.nodes.new('NodeFrame')
            if hasattr(author_1, 'color'):
                author_1.color = (0.015208303928375244, 0.12743757665157318, 0.18447497487068176)
            if hasattr(author_1, 'hide'):
                author_1.hide = False
            if hasattr(author_1, 'label'):
                author_1.label = 'By: Dr. Hacker "BE HACK 2000"'
            if hasattr(author_1, 'label_size'):
                author_1.label_size = 16
            if hasattr(author_1, 'location'):
                author_1.location = (620.0, 240.0)
            if hasattr(author_1, 'mute'):
                author_1.mute = False
            if hasattr(author_1, 'name'):
                author_1.name = 'Author'
            if hasattr(author_1, 'shrink'):
                author_1.shrink = True
            if hasattr(author_1, 'use_custom_color'):
                author_1.use_custom_color = True
            if hasattr(author_1, 'width'):
                author_1.width = 290.4296875

            layer_weight_003_1 = node_tree1.nodes.new('ShaderNodeLayerWeight')
            if hasattr(layer_weight_003_1, 'color'):
                layer_weight_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(layer_weight_003_1, 'hide'):
                layer_weight_003_1.hide = False
            if hasattr(layer_weight_003_1, 'location'):
                layer_weight_003_1.location = (-380.0, 268.0)
            if hasattr(layer_weight_003_1, 'mute'):
                layer_weight_003_1.mute = False
            if hasattr(layer_weight_003_1, 'name'):
                layer_weight_003_1.name = 'Layer Weight.003'
            if hasattr(layer_weight_003_1, 'use_custom_color'):
                layer_weight_003_1.use_custom_color = False
            if hasattr(layer_weight_003_1, 'width'):
                layer_weight_003_1.width = 140.0
            input_ = next((input_ for input_ in layer_weight_003_1.inputs if input_.identifier=='Blend'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.20000001788139343
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Blend'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in layer_weight_003_1.inputs if input_.identifier=='Normal'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.0, 0.0, 0.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = True
                if hasattr(input_, 'name'):
                    input_.name = 'Normal'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            output = next((output for output in layer_weight_003_1.outputs if output.identifier=='Fresnel'), None)
            if output:
                if hasattr(output, 'default_value'):
                    output.default_value = 0.0
                if hasattr(output, 'display_shape'):
                    output.display_shape = 'CIRCLE'
                if hasattr(output, 'enabled'):
                    output.enabled = True
                if hasattr(output, 'hide'):
                    output.hide = True
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Fresnel'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in layer_weight_003_1.outputs if output.identifier=='Facing'), None)
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
                    output.name = 'Facing'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            layer_weight_1 = node_tree1.nodes.new('ShaderNodeLayerWeight')
            if hasattr(layer_weight_1, 'color'):
                layer_weight_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(layer_weight_1, 'hide'):
                layer_weight_1.hide = False
            if hasattr(layer_weight_1, 'location'):
                layer_weight_1.location = (-380.0, 340.0)
            if hasattr(layer_weight_1, 'mute'):
                layer_weight_1.mute = False
            if hasattr(layer_weight_1, 'name'):
                layer_weight_1.name = 'Layer Weight'
            if hasattr(layer_weight_1, 'use_custom_color'):
                layer_weight_1.use_custom_color = False
            if hasattr(layer_weight_1, 'width'):
                layer_weight_1.width = 140.0
            input_ = next((input_ for input_ in layer_weight_1.inputs if input_.identifier=='Blend'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.20000001788139343
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Blend'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in layer_weight_1.inputs if input_.identifier=='Normal'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.0, 0.0, 0.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = True
                if hasattr(input_, 'name'):
                    input_.name = 'Normal'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            output = next((output for output in layer_weight_1.outputs if output.identifier=='Fresnel'), None)
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
                    output.name = 'Fresnel'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in layer_weight_1.outputs if output.identifier=='Facing'), None)
            if output:
                if hasattr(output, 'default_value'):
                    output.default_value = 0.0
                if hasattr(output, 'display_shape'):
                    output.display_shape = 'CIRCLE'
                if hasattr(output, 'enabled'):
                    output.enabled = True
                if hasattr(output, 'hide'):
                    output.hide = True
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Facing'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            math_1 = node_tree1.nodes.new('ShaderNodeMath')
            if hasattr(math_1, 'color'):
                math_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(math_1, 'hide'):
                math_1.hide = False
            if hasattr(math_1, 'location'):
                math_1.location = (-200.0, -160.0)
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
                    input_.default_value = 25.0
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
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
                    input_.hide = True
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

            mix_1 = node_tree1.nodes.new('ShaderNodeMix')
            if hasattr(mix_1, 'blend_type'):
                mix_1.blend_type = 'MIX'
            if hasattr(mix_1, 'clamp_factor'):
                mix_1.clamp_factor = True
            if hasattr(mix_1, 'clamp_result'):
                mix_1.clamp_result = False
            if hasattr(mix_1, 'color'):
                mix_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_1, 'data_type'):
                mix_1.data_type = 'RGBA'
            if hasattr(mix_1, 'factor_mode'):
                mix_1.factor_mode = 'UNIFORM'
            if hasattr(mix_1, 'hide'):
                mix_1.hide = False
            if hasattr(mix_1, 'location'):
                mix_1.location = (-200.0, 26.0)
            if hasattr(mix_1, 'mute'):
                mix_1.mute = False
            if hasattr(mix_1, 'name'):
                mix_1.name = 'Mix'
            if hasattr(mix_1, 'use_custom_color'):
                mix_1.use_custom_color = False
            if hasattr(mix_1, 'width'):
                mix_1.width = 140.0
            input_ = next((input_ for input_ in mix_1.inputs if input_.identifier=='Factor_Float'), None)
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
                    input_.name = 'Factor'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in mix_1.inputs if input_.identifier=='Factor_Vector'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.5, 0.5, 0.5)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = False
                if hasattr(input_, 'hide'):
                    input_.hide = False
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Factor'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in mix_1.inputs if input_.identifier=='A_Float'), None)
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
                    input_.name = 'A'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in mix_1.inputs if input_.identifier=='B_Float'), None)
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
                    input_.name = 'B'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in mix_1.inputs if input_.identifier=='A_Vector'), None)
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
                    input_.name = 'A'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in mix_1.inputs if input_.identifier=='B_Vector'), None)
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
                    input_.name = 'B'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in mix_1.inputs if input_.identifier=='A_Color'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = False
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'A'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in mix_1.inputs if input_.identifier=='B_Color'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = False
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'B'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            output = next((output for output in mix_1.outputs if output.identifier=='Result_Float'), None)
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
                    output.name = 'Result'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in mix_1.outputs if output.identifier=='Result_Vector'), None)
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
                    output.name = 'Result'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in mix_1.outputs if output.identifier=='Result_Color'), None)
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
                    output.name = 'Result'
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
                glossy_bsdf_1.location = (-205.0, 270.0)
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
                    input_.default_value = (0.8227859139442444, 0.0, 0.5936002731323242, 1.0)
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
                    input_.default_value = 0.0010000000474974513
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
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
                    input_.hide = True
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
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Weight'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False

            glossy_bsdf_001_1 = node_tree1.nodes.new('ShaderNodeBsdfGlossy')
            if hasattr(glossy_bsdf_001_1, 'color'):
                glossy_bsdf_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(glossy_bsdf_001_1, 'distribution'):
                glossy_bsdf_001_1.distribution = 'GGX'
            if hasattr(glossy_bsdf_001_1, 'hide'):
                glossy_bsdf_001_1.hide = False
            if hasattr(glossy_bsdf_001_1, 'location'):
                glossy_bsdf_001_1.location = (-205.0, 148.0)
            if hasattr(glossy_bsdf_001_1, 'mute'):
                glossy_bsdf_001_1.mute = False
            if hasattr(glossy_bsdf_001_1, 'name'):
                glossy_bsdf_001_1.name = 'Glossy BSDF.001'
            if hasattr(glossy_bsdf_001_1, 'use_custom_color'):
                glossy_bsdf_001_1.use_custom_color = False
            if hasattr(glossy_bsdf_001_1, 'width'):
                glossy_bsdf_001_1.width = 150.0
            input_ = next((input_ for input_ in glossy_bsdf_001_1.inputs if input_.identifier=='Color'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.18765491247177124, 0.7835378646850586, 0.0, 1.0)
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
            input_ = next((input_ for input_ in glossy_bsdf_001_1.inputs if input_.identifier=='Roughness'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.0010000000474974513
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Roughness'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in glossy_bsdf_001_1.inputs if input_.identifier=='Normal'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.0, 0.0, 0.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = True
                if hasattr(input_, 'name'):
                    input_.name = 'Normal'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in glossy_bsdf_001_1.inputs if input_.identifier=='Weight'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.0
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = False
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Weight'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False

            layer_weight_002_1 = node_tree1.nodes.new('ShaderNodeLayerWeight')
            if hasattr(layer_weight_002_1, 'color'):
                layer_weight_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(layer_weight_002_1, 'hide'):
                layer_weight_002_1.hide = False
            if hasattr(layer_weight_002_1, 'location'):
                layer_weight_002_1.location = (-200.0, 340.0)
            if hasattr(layer_weight_002_1, 'mute'):
                layer_weight_002_1.mute = False
            if hasattr(layer_weight_002_1, 'name'):
                layer_weight_002_1.name = 'Layer Weight.002'
            if hasattr(layer_weight_002_1, 'use_custom_color'):
                layer_weight_002_1.use_custom_color = False
            if hasattr(layer_weight_002_1, 'width'):
                layer_weight_002_1.width = 140.0
            input_ = next((input_ for input_ in layer_weight_002_1.inputs if input_.identifier=='Blend'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.9200000762939453
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Blend'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in layer_weight_002_1.inputs if input_.identifier=='Normal'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.0, 0.0, 0.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = True
                if hasattr(input_, 'name'):
                    input_.name = 'Normal'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            output = next((output for output in layer_weight_002_1.outputs if output.identifier=='Fresnel'), None)
            if output:
                if hasattr(output, 'default_value'):
                    output.default_value = 0.0
                if hasattr(output, 'display_shape'):
                    output.display_shape = 'CIRCLE'
                if hasattr(output, 'enabled'):
                    output.enabled = True
                if hasattr(output, 'hide'):
                    output.hide = True
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Fresnel'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in layer_weight_002_1.outputs if output.identifier=='Facing'), None)
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
                    output.name = 'Facing'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            emission_1 = node_tree1.nodes.new('ShaderNodeEmission')
            if hasattr(emission_1, 'color'):
                emission_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(emission_1, 'hide'):
                emission_1.hide = False
            if hasattr(emission_1, 'location'):
                emission_1.location = (-20.0, -130.0)
            if hasattr(emission_1, 'mute'):
                emission_1.mute = False
            if hasattr(emission_1, 'name'):
                emission_1.name = 'Emission'
            if hasattr(emission_1, 'use_custom_color'):
                emission_1.use_custom_color = False
            if hasattr(emission_1, 'width'):
                emission_1.width = 140.0
            input_ = next((input_ for input_ in emission_1.inputs if input_.identifier=='Color'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.0, 0.2521688640117645, 1.0, 1.0)
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
            input_ = next((input_ for input_ in emission_1.inputs if input_.identifier=='Strength'), None)
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
                    input_.name = 'Strength'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in emission_1.inputs if input_.identifier=='Weight'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.0
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = False
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Weight'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False

            mix_shader_001_1 = node_tree1.nodes.new('ShaderNodeMixShader')
            if hasattr(mix_shader_001_1, 'color'):
                mix_shader_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_shader_001_1, 'hide'):
                mix_shader_001_1.hide = False
            if hasattr(mix_shader_001_1, 'location'):
                mix_shader_001_1.location = (-20.0, 270.0)
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

            glossy_bsdf_002_1 = node_tree1.nodes.new('ShaderNodeBsdfGlossy')
            if hasattr(glossy_bsdf_002_1, 'color'):
                glossy_bsdf_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(glossy_bsdf_002_1, 'distribution'):
                glossy_bsdf_002_1.distribution = 'GGX'
            if hasattr(glossy_bsdf_002_1, 'hide'):
                glossy_bsdf_002_1.hide = False
            if hasattr(glossy_bsdf_002_1, 'location'):
                glossy_bsdf_002_1.location = (-25.0, 136.0)
            if hasattr(glossy_bsdf_002_1, 'mute'):
                glossy_bsdf_002_1.mute = False
            if hasattr(glossy_bsdf_002_1, 'name'):
                glossy_bsdf_002_1.name = 'Glossy BSDF.002'
            if hasattr(glossy_bsdf_002_1, 'use_custom_color'):
                glossy_bsdf_002_1.use_custom_color = False
            if hasattr(glossy_bsdf_002_1, 'width'):
                glossy_bsdf_002_1.width = 150.0
            input_ = next((input_ for input_ in glossy_bsdf_002_1.inputs if input_.identifier=='Color'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.004024718888103962, 0.10224173218011856, 0.7605247497558594, 1.0)
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
            input_ = next((input_ for input_ in glossy_bsdf_002_1.inputs if input_.identifier=='Roughness'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.0010000000474974513
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Roughness'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in glossy_bsdf_002_1.inputs if input_.identifier=='Normal'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.0, 0.0, 0.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = True
                if hasattr(input_, 'name'):
                    input_.name = 'Normal'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in glossy_bsdf_002_1.inputs if input_.identifier=='Weight'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.0
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = False
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Weight'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False

            layer_weight_001_1 = node_tree1.nodes.new('ShaderNodeLayerWeight')
            if hasattr(layer_weight_001_1, 'color'):
                layer_weight_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(layer_weight_001_1, 'hide'):
                layer_weight_001_1.hide = False
            if hasattr(layer_weight_001_1, 'location'):
                layer_weight_001_1.location = (-20.0, 340.0)
            if hasattr(layer_weight_001_1, 'mute'):
                layer_weight_001_1.mute = False
            if hasattr(layer_weight_001_1, 'name'):
                layer_weight_001_1.name = 'Layer Weight.001'
            if hasattr(layer_weight_001_1, 'use_custom_color'):
                layer_weight_001_1.use_custom_color = False
            if hasattr(layer_weight_001_1, 'width'):
                layer_weight_001_1.width = 140.0
            input_ = next((input_ for input_ in layer_weight_001_1.inputs if input_.identifier=='Blend'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.49999991059303284
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Blend'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in layer_weight_001_1.inputs if input_.identifier=='Normal'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = (0.0, 0.0, 0.0)
                if hasattr(input_, 'display_shape'):
                    input_.display_shape = 'CIRCLE'
                if hasattr(input_, 'enabled'):
                    input_.enabled = True
                if hasattr(input_, 'hide'):
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = True
                if hasattr(input_, 'name'):
                    input_.name = 'Normal'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            output = next((output for output in layer_weight_001_1.outputs if output.identifier=='Fresnel'), None)
            if output:
                if hasattr(output, 'default_value'):
                    output.default_value = 0.0
                if hasattr(output, 'display_shape'):
                    output.display_shape = 'CIRCLE'
                if hasattr(output, 'enabled'):
                    output.enabled = True
                if hasattr(output, 'hide'):
                    output.hide = True
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Fresnel'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False
            output = next((output for output in layer_weight_001_1.outputs if output.identifier=='Facing'), None)
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
                    output.name = 'Facing'
                if hasattr(output, 'show_expanded'):
                    output.show_expanded = False

            mix_shader_1 = node_tree1.nodes.new('ShaderNodeMixShader')
            if hasattr(mix_shader_1, 'color'):
                mix_shader_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_shader_1, 'hide'):
                mix_shader_1.hide = False
            if hasattr(mix_shader_1, 'location'):
                mix_shader_1.location = (160.0, 206.0)
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

            mix_shader_002_1 = node_tree1.nodes.new('ShaderNodeMixShader')
            if hasattr(mix_shader_002_1, 'color'):
                mix_shader_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_shader_002_1, 'hide'):
                mix_shader_002_1.hide = False
            if hasattr(mix_shader_002_1, 'location'):
                mix_shader_002_1.location = (160.0, 340.0)
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

            node_tree2 = bpy.data.node_groups.get('Color Ramp.002')
            if not node_tree2:
                node_tree2 = bpy.data.node_groups.new('Color Ramp.002', 'ShaderNodeTree')
                for node in node_tree2.nodes:
                    node_tree2.nodes.remove(node)
                # INPUTS
                input = node_tree2.inputs.new('NodeSocketFloatFactor', 'Input Factor')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.5
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 1.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0
                if hasattr(input, 'name'):
                    input.name = 'Input Factor'
                input = node_tree2.inputs.new('NodeSocketFloat', 'Factor Multiplier')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 1.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 3.4028234663852886e+38
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0
                if hasattr(input, 'name'):
                    input.name = 'Factor Multiplier'
                input = node_tree2.inputs.new('NodeSocketColor', 'Color1')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = (0.0, 0.013257999904453754, 0.15981000661849976, 1.0)
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'name'):
                    input.name = 'Color1'
                input = node_tree2.inputs.new('NodeSocketColor', 'Color2')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = (0.0, 1.0, 0.969556987285614, 1.0)
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'name'):
                    input.name = 'Color2'
                # OUTPUTS
                output = node_tree2.outputs.new('NodeSocketColor', 'Color')
                if hasattr(output, 'attribute_domain'):
                    output.attribute_domain = 'POINT'
                if hasattr(output, 'default_value'):
                    output.default_value = (0.0, 0.0, 0.0, 0.0)
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Color'
                # NODES
                node_group_description_2 = node_tree2.nodes.new('NodeFrame')
                if hasattr(node_group_description_2, 'color'):
                    node_group_description_2.color = (0.9258300065994263, 0.3908109962940216, 0.07050599902868271)
                if hasattr(node_group_description_2, 'hide'):
                    node_group_description_2.hide = False
                if hasattr(node_group_description_2, 'label'):
                    node_group_description_2.label = 'COLOR RAMP NODE GROUP'
                if hasattr(node_group_description_2, 'label_size'):
                    node_group_description_2.label_size = 15
                if hasattr(node_group_description_2, 'location'):
                    node_group_description_2.location = (-800.0, 159.99996948242188)
                if hasattr(node_group_description_2, 'mute'):
                    node_group_description_2.mute = False
                if hasattr(node_group_description_2, 'name'):
                    node_group_description_2.name = 'Node Group Description'
                if hasattr(node_group_description_2, 'shrink'):
                    node_group_description_2.shrink = True
                if hasattr(node_group_description_2, 'text'):
                    node_group_description_2.text = bpy.data.texts.get('Color Ramp Node.002')
                if hasattr(node_group_description_2, 'use_custom_color'):
                    node_group_description_2.use_custom_color = True
                if hasattr(node_group_description_2, 'width'):
                    node_group_description_2.width = 337.6953125

                author_001_2 = node_tree2.nodes.new('NodeFrame')
                if hasattr(author_001_2, 'color'):
                    author_001_2.color = (0.015208303928375244, 0.12743757665157318, 0.18447497487068176)
                if hasattr(author_001_2, 'hide'):
                    author_001_2.hide = False
                if hasattr(author_001_2, 'label'):
                    author_001_2.label = 'By: Dr. Hacker "BE HACK 2000"'
                if hasattr(author_001_2, 'label_size'):
                    author_001_2.label_size = 20
                if hasattr(author_001_2, 'location'):
                    author_001_2.location = (-80.0, -180.0)
                if hasattr(author_001_2, 'mute'):
                    author_001_2.mute = False
                if hasattr(author_001_2, 'name'):
                    author_001_2.name = 'Author.001'
                if hasattr(author_001_2, 'shrink'):
                    author_001_2.shrink = True
                if hasattr(author_001_2, 'use_custom_color'):
                    author_001_2.use_custom_color = True
                if hasattr(author_001_2, 'width'):
                    author_001_2.width = 319.072509765625

                reroute_001_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_001_2, 'color'):
                    reroute_001_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_001_2, 'hide'):
                    reroute_001_2.hide = False
                if hasattr(reroute_001_2, 'location'):
                    reroute_001_2.location = (-203.5904541015625, -35.567657470703125)
                if hasattr(reroute_001_2, 'mute'):
                    reroute_001_2.mute = False
                if hasattr(reroute_001_2, 'name'):
                    reroute_001_2.name = 'Reroute.001'
                if hasattr(reroute_001_2, 'use_custom_color'):
                    reroute_001_2.use_custom_color = False
                if hasattr(reroute_001_2, 'width'):
                    reroute_001_2.width = 16.0

                reroute_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_2, 'color'):
                    reroute_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_2, 'hide'):
                    reroute_2.hide = False
                if hasattr(reroute_2, 'location'):
                    reroute_2.location = (-203.56576538085938, -111.79473876953125)
                if hasattr(reroute_2, 'mute'):
                    reroute_2.mute = False
                if hasattr(reroute_2, 'name'):
                    reroute_2.name = 'Reroute'
                if hasattr(reroute_2, 'use_custom_color'):
                    reroute_2.use_custom_color = False
                if hasattr(reroute_2, 'width'):
                    reroute_2.width = 16.0

                math_2 = node_tree2.nodes.new('ShaderNodeMath')
                if hasattr(math_2, 'color'):
                    math_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(math_2, 'hide'):
                    math_2.hide = False
                if hasattr(math_2, 'location'):
                    math_2.location = (-660.0, 0.0)
                if hasattr(math_2, 'mute'):
                    math_2.mute = False
                if hasattr(math_2, 'name'):
                    math_2.name = 'Math'
                if hasattr(math_2, 'operation'):
                    math_2.operation = 'MULTIPLY'
                if hasattr(math_2, 'use_clamp'):
                    math_2.use_clamp = False
                if hasattr(math_2, 'use_custom_color'):
                    math_2.use_custom_color = False
                if hasattr(math_2, 'width'):
                    math_2.width = 140.0
                input_ = next((input_ for input_ in math_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in math_2.inputs if input_.identifier=='Value_001'), None)
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
                        input_.name = 'Value'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in math_2.inputs if input_.identifier=='Value_002'), None)
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
                output = next((output for output in math_2.outputs if output.identifier=='Value'), None)
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

                reroute_012_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_012_2, 'color'):
                    reroute_012_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_012_2, 'hide'):
                    reroute_012_2.hide = False
                if hasattr(reroute_012_2, 'location'):
                    reroute_012_2.location = (-499.365966796875, -34.67010498046875)
                if hasattr(reroute_012_2, 'mute'):
                    reroute_012_2.mute = False
                if hasattr(reroute_012_2, 'name'):
                    reroute_012_2.name = 'Reroute.012'
                if hasattr(reroute_012_2, 'use_custom_color'):
                    reroute_012_2.use_custom_color = False
                if hasattr(reroute_012_2, 'width'):
                    reroute_012_2.width = 16.0

                reroute_002_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_002_2, 'color'):
                    reroute_002_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_002_2, 'hide'):
                    reroute_002_2.hide = False
                if hasattr(reroute_002_2, 'location'):
                    reroute_002_2.location = (-199.4525146484375, -157.26007080078125)
                if hasattr(reroute_002_2, 'mute'):
                    reroute_002_2.mute = False
                if hasattr(reroute_002_2, 'name'):
                    reroute_002_2.name = 'Reroute.002'
                if hasattr(reroute_002_2, 'use_custom_color'):
                    reroute_002_2.use_custom_color = False
                if hasattr(reroute_002_2, 'width'):
                    reroute_002_2.width = 16.0

                mix_2 = node_tree2.nodes.new('ShaderNodeMix')
                if hasattr(mix_2, 'blend_type'):
                    mix_2.blend_type = 'MIX'
                if hasattr(mix_2, 'clamp_factor'):
                    mix_2.clamp_factor = True
                if hasattr(mix_2, 'clamp_result'):
                    mix_2.clamp_result = False
                if hasattr(mix_2, 'color'):
                    mix_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(mix_2, 'data_type'):
                    mix_2.data_type = 'RGBA'
                if hasattr(mix_2, 'factor_mode'):
                    mix_2.factor_mode = 'UNIFORM'
                if hasattr(mix_2, 'hide'):
                    mix_2.hide = False
                if hasattr(mix_2, 'location'):
                    mix_2.location = (-173.0228271484375, -0.8092041015625)
                if hasattr(mix_2, 'mute'):
                    mix_2.mute = False
                if hasattr(mix_2, 'name'):
                    mix_2.name = 'Mix'
                if hasattr(mix_2, 'use_custom_color'):
                    mix_2.use_custom_color = False
                if hasattr(mix_2, 'width'):
                    mix_2.width = 140.0
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='Factor_Float'), None)
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
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='Factor_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.5, 0.5, 0.5)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = False
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='A_Float'), None)
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
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='B_Float'), None)
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
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='A_Vector'), None)
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
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='B_Vector'), None)
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
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='A_Color'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.013257999904453754, 0.15981000661849976, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = False
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='B_Color'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 1.0, 0.969556987285614, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = False
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in mix_2.outputs if output.identifier=='Result_Float'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in mix_2.outputs if output.identifier=='Result_Vector'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in mix_2.outputs if output.identifier=='Result_Color'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                reroute_003_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_003_2, 'color'):
                    reroute_003_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_003_2, 'hide'):
                    reroute_003_2.hide = False
                if hasattr(reroute_003_2, 'location'):
                    reroute_003_2.location = (-219.19992065429688, -134.0416717529297)
                if hasattr(reroute_003_2, 'mute'):
                    reroute_003_2.mute = False
                if hasattr(reroute_003_2, 'name'):
                    reroute_003_2.name = 'Reroute.003'
                if hasattr(reroute_003_2, 'use_custom_color'):
                    reroute_003_2.use_custom_color = False
                if hasattr(reroute_003_2, 'width'):
                    reroute_003_2.width = 16.0

                reroute_010_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_010_2, 'color'):
                    reroute_010_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_010_2, 'hide'):
                    reroute_010_2.hide = False
                if hasattr(reroute_010_2, 'location'):
                    reroute_010_2.location = (-720.0, -80.0)
                if hasattr(reroute_010_2, 'mute'):
                    reroute_010_2.mute = False
                if hasattr(reroute_010_2, 'name'):
                    reroute_010_2.name = 'Reroute.010'
                if hasattr(reroute_010_2, 'use_custom_color'):
                    reroute_010_2.use_custom_color = False
                if hasattr(reroute_010_2, 'width'):
                    reroute_010_2.width = 16.0

                reroute_011_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_011_2, 'color'):
                    reroute_011_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_011_2, 'hide'):
                    reroute_011_2.hide = False
                if hasattr(reroute_011_2, 'location'):
                    reroute_011_2.location = (-740.0, -100.0)
                if hasattr(reroute_011_2, 'mute'):
                    reroute_011_2.mute = False
                if hasattr(reroute_011_2, 'name'):
                    reroute_011_2.name = 'Reroute.011'
                if hasattr(reroute_011_2, 'use_custom_color'):
                    reroute_011_2.use_custom_color = False
                if hasattr(reroute_011_2, 'width'):
                    reroute_011_2.width = 16.0

                reroute_007_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_007_2, 'color'):
                    reroute_007_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_007_2, 'hide'):
                    reroute_007_2.hide = False
                if hasattr(reroute_007_2, 'location'):
                    reroute_007_2.location = (-681.0607299804688, -114.50245666503906)
                if hasattr(reroute_007_2, 'mute'):
                    reroute_007_2.mute = False
                if hasattr(reroute_007_2, 'name'):
                    reroute_007_2.name = 'Reroute.007'
                if hasattr(reroute_007_2, 'use_custom_color'):
                    reroute_007_2.use_custom_color = False
                if hasattr(reroute_007_2, 'width'):
                    reroute_007_2.width = 16.0

                reroute_006_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_006_2, 'color'):
                    reroute_006_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_006_2, 'hide'):
                    reroute_006_2.hide = False
                if hasattr(reroute_006_2, 'location'):
                    reroute_006_2.location = (-699.8770751953125, -136.7299041748047)
                if hasattr(reroute_006_2, 'mute'):
                    reroute_006_2.mute = False
                if hasattr(reroute_006_2, 'name'):
                    reroute_006_2.name = 'Reroute.006'
                if hasattr(reroute_006_2, 'use_custom_color'):
                    reroute_006_2.use_custom_color = False
                if hasattr(reroute_006_2, 'width'):
                    reroute_006_2.width = 16.0

                reroute_014_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_014_2, 'color'):
                    reroute_014_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_014_2, 'hide'):
                    reroute_014_2.hide = False
                if hasattr(reroute_014_2, 'location'):
                    reroute_014_2.location = (-680.1669311523438, -35.075286865234375)
                if hasattr(reroute_014_2, 'mute'):
                    reroute_014_2.mute = False
                if hasattr(reroute_014_2, 'name'):
                    reroute_014_2.name = 'Reroute.014'
                if hasattr(reroute_014_2, 'use_custom_color'):
                    reroute_014_2.use_custom_color = False
                if hasattr(reroute_014_2, 'width'):
                    reroute_014_2.width = 16.0

                reroute_005_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_005_2, 'color'):
                    reroute_005_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_005_2, 'hide'):
                    reroute_005_2.hide = False
                if hasattr(reroute_005_2, 'location'):
                    reroute_005_2.location = (-200.00006103515625, -260.0)
                if hasattr(reroute_005_2, 'mute'):
                    reroute_005_2.mute = False
                if hasattr(reroute_005_2, 'name'):
                    reroute_005_2.name = 'Reroute.005'
                if hasattr(reroute_005_2, 'use_custom_color'):
                    reroute_005_2.use_custom_color = False
                if hasattr(reroute_005_2, 'width'):
                    reroute_005_2.width = 16.0

                reroute_004_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_004_2, 'color'):
                    reroute_004_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_004_2, 'hide'):
                    reroute_004_2.hide = False
                if hasattr(reroute_004_2, 'location'):
                    reroute_004_2.location = (-220.00006103515625, -240.0)
                if hasattr(reroute_004_2, 'mute'):
                    reroute_004_2.mute = False
                if hasattr(reroute_004_2, 'name'):
                    reroute_004_2.name = 'Reroute.004'
                if hasattr(reroute_004_2, 'use_custom_color'):
                    reroute_004_2.use_custom_color = False
                if hasattr(reroute_004_2, 'width'):
                    reroute_004_2.width = 16.0

                reroute_008_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_008_2, 'color'):
                    reroute_008_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_008_2, 'hide'):
                    reroute_008_2.hide = False
                if hasattr(reroute_008_2, 'location'):
                    reroute_008_2.location = (-740.0, -260.0)
                if hasattr(reroute_008_2, 'mute'):
                    reroute_008_2.mute = False
                if hasattr(reroute_008_2, 'name'):
                    reroute_008_2.name = 'Reroute.008'
                if hasattr(reroute_008_2, 'use_custom_color'):
                    reroute_008_2.use_custom_color = False
                if hasattr(reroute_008_2, 'width'):
                    reroute_008_2.width = 16.0

                reroute_015_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_015_2, 'color'):
                    reroute_015_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_015_2, 'hide'):
                    reroute_015_2.hide = False
                if hasattr(reroute_015_2, 'location'):
                    reroute_015_2.location = (-700.2451171875, -56.91032409667969)
                if hasattr(reroute_015_2, 'mute'):
                    reroute_015_2.mute = False
                if hasattr(reroute_015_2, 'name'):
                    reroute_015_2.name = 'Reroute.015'
                if hasattr(reroute_015_2, 'use_custom_color'):
                    reroute_015_2.use_custom_color = False
                if hasattr(reroute_015_2, 'width'):
                    reroute_015_2.width = 16.0

                reroute_009_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_009_2, 'color'):
                    reroute_009_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_009_2, 'hide'):
                    reroute_009_2.hide = False
                if hasattr(reroute_009_2, 'location'):
                    reroute_009_2.location = (-720.0, -240.0)
                if hasattr(reroute_009_2, 'mute'):
                    reroute_009_2.mute = False
                if hasattr(reroute_009_2, 'name'):
                    reroute_009_2.name = 'Reroute.009'
                if hasattr(reroute_009_2, 'use_custom_color'):
                    reroute_009_2.use_custom_color = False
                if hasattr(reroute_009_2, 'width'):
                    reroute_009_2.width = 16.0

                group_input_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_2, 'color'):
                    group_input_2.color = (0.6151790022850037, 0.6093840003013611, 0.45541998744010925)
                if hasattr(group_input_2, 'hide'):
                    group_input_2.hide = False
                if hasattr(group_input_2, 'location'):
                    group_input_2.location = (-900.0, 0.0)
                if hasattr(group_input_2, 'mute'):
                    group_input_2.mute = False
                if hasattr(group_input_2, 'name'):
                    group_input_2.name = 'Group Input'
                if hasattr(group_input_2, 'use_custom_color'):
                    group_input_2.use_custom_color = True
                if hasattr(group_input_2, 'width'):
                    group_input_2.width = 140.0
                if hasattr(group_input_2.outputs[0], 'default_value'):
                    group_input_2.outputs[0].default_value = 0.5
                if hasattr(group_input_2.outputs[0], 'display_shape'):
                    group_input_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[0], 'enabled'):
                    group_input_2.outputs[0].enabled = True
                if hasattr(group_input_2.outputs[0], 'hide'):
                    group_input_2.outputs[0].hide = False
                if hasattr(group_input_2.outputs[0], 'hide_value'):
                    group_input_2.outputs[0].hide_value = False
                if hasattr(group_input_2.outputs[0], 'name'):
                    group_input_2.outputs[0].name = 'Input Factor'
                if hasattr(group_input_2.outputs[0], 'show_expanded'):
                    group_input_2.outputs[0].show_expanded = False
                if hasattr(group_input_2.outputs[1], 'default_value'):
                    group_input_2.outputs[1].default_value = 0.0
                if hasattr(group_input_2.outputs[1], 'display_shape'):
                    group_input_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[1], 'enabled'):
                    group_input_2.outputs[1].enabled = True
                if hasattr(group_input_2.outputs[1], 'hide'):
                    group_input_2.outputs[1].hide = False
                if hasattr(group_input_2.outputs[1], 'hide_value'):
                    group_input_2.outputs[1].hide_value = False
                if hasattr(group_input_2.outputs[1], 'name'):
                    group_input_2.outputs[1].name = 'Factor Multiplier'
                if hasattr(group_input_2.outputs[1], 'show_expanded'):
                    group_input_2.outputs[1].show_expanded = False
                if hasattr(group_input_2.outputs[2], 'default_value'):
                    group_input_2.outputs[2].default_value = (0.0, 0.013257999904453754, 0.15981000661849976, 1.0)
                if hasattr(group_input_2.outputs[2], 'display_shape'):
                    group_input_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[2], 'enabled'):
                    group_input_2.outputs[2].enabled = True
                if hasattr(group_input_2.outputs[2], 'hide'):
                    group_input_2.outputs[2].hide = False
                if hasattr(group_input_2.outputs[2], 'hide_value'):
                    group_input_2.outputs[2].hide_value = False
                if hasattr(group_input_2.outputs[2], 'name'):
                    group_input_2.outputs[2].name = 'Color1'
                if hasattr(group_input_2.outputs[2], 'show_expanded'):
                    group_input_2.outputs[2].show_expanded = False
                if hasattr(group_input_2.outputs[3], 'default_value'):
                    group_input_2.outputs[3].default_value = (0.0, 1.0, 0.969556987285614, 1.0)
                if hasattr(group_input_2.outputs[3], 'display_shape'):
                    group_input_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[3], 'enabled'):
                    group_input_2.outputs[3].enabled = True
                if hasattr(group_input_2.outputs[3], 'hide'):
                    group_input_2.outputs[3].hide = False
                if hasattr(group_input_2.outputs[3], 'hide_value'):
                    group_input_2.outputs[3].hide_value = False
                if hasattr(group_input_2.outputs[3], 'name'):
                    group_input_2.outputs[3].name = 'Color2'
                if hasattr(group_input_2.outputs[3], 'show_expanded'):
                    group_input_2.outputs[3].show_expanded = False

                group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
                if hasattr(group_output_2, 'color'):
                    group_output_2.color = (0.6151790022850037, 0.6093840003013611, 0.45541998744010925)
                if hasattr(group_output_2, 'hide'):
                    group_output_2.hide = False
                if hasattr(group_output_2, 'is_active_output'):
                    group_output_2.is_active_output = True
                if hasattr(group_output_2, 'location'):
                    group_output_2.location = (-0.69171142578125, -2.0771484375)
                if hasattr(group_output_2, 'mute'):
                    group_output_2.mute = False
                if hasattr(group_output_2, 'name'):
                    group_output_2.name = 'Group Output'
                if hasattr(group_output_2, 'use_custom_color'):
                    group_output_2.use_custom_color = True
                if hasattr(group_output_2, 'width'):
                    group_output_2.width = 140.0
                if hasattr(group_output_2.inputs[0], 'default_value'):
                    group_output_2.inputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
                if hasattr(group_output_2.inputs[0], 'display_shape'):
                    group_output_2.inputs[0].display_shape = 'CIRCLE'
                if hasattr(group_output_2.inputs[0], 'enabled'):
                    group_output_2.inputs[0].enabled = True
                if hasattr(group_output_2.inputs[0], 'hide'):
                    group_output_2.inputs[0].hide = False
                if hasattr(group_output_2.inputs[0], 'hide_value'):
                    group_output_2.inputs[0].hide_value = False
                if hasattr(group_output_2.inputs[0], 'name'):
                    group_output_2.inputs[0].name = 'Color'
                if hasattr(group_output_2.inputs[0], 'show_expanded'):
                    group_output_2.inputs[0].show_expanded = False

                reroute_013_2 = node_tree2.nodes.new('NodeReroute')
                if hasattr(reroute_013_2, 'color'):
                    reroute_013_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(reroute_013_2, 'hide'):
                    reroute_013_2.hide = False
                if hasattr(reroute_013_2, 'location'):
                    reroute_013_2.location = (-498.9912414550781, -195.82192993164062)
                if hasattr(reroute_013_2, 'mute'):
                    reroute_013_2.mute = False
                if hasattr(reroute_013_2, 'name'):
                    reroute_013_2.name = 'Reroute.013'
                if hasattr(reroute_013_2, 'use_custom_color'):
                    reroute_013_2.use_custom_color = False
                if hasattr(reroute_013_2, 'width'):
                    reroute_013_2.width = 16.0

                colorramp_2 = node_tree2.nodes.new('ShaderNodeValToRGB')
                if hasattr(colorramp_2, 'color'):
                    colorramp_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(colorramp_2, 'color_ramp'):
                    if hasattr(colorramp_2.color_ramp, 'color_mode'):
                        colorramp_2.color_ramp.color_mode = 'RGB'
                    if hasattr(colorramp_2.color_ramp, 'elements'):
                        if 0 >= len(colorramp_2.color_ramp.elements):
                            colorramp_2.color_ramp.elements.new(0.5855249166488647)
                        if hasattr(colorramp_2.color_ramp.elements[0], 'alpha'):
                            colorramp_2.color_ramp.elements[0].alpha = 1.0
                        if hasattr(colorramp_2.color_ramp.elements[0], 'color'):
                            colorramp_2.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
                        if hasattr(colorramp_2.color_ramp.elements[0], 'position'):
                            colorramp_2.color_ramp.elements[0].position = 0.5855249166488647
                        if 1 >= len(colorramp_2.color_ramp.elements):
                            colorramp_2.color_ramp.elements.new(1.0)
                        if hasattr(colorramp_2.color_ramp.elements[1], 'alpha'):
                            colorramp_2.color_ramp.elements[1].alpha = 1.0
                        if hasattr(colorramp_2.color_ramp.elements[1], 'color'):
                            colorramp_2.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
                        if hasattr(colorramp_2.color_ramp.elements[1], 'position'):
                            colorramp_2.color_ramp.elements[1].position = 1.0
                    if hasattr(colorramp_2.color_ramp, 'hue_interpolation'):
                        colorramp_2.color_ramp.hue_interpolation = 'NEAR'
                    if hasattr(colorramp_2.color_ramp, 'interpolation'):
                        colorramp_2.color_ramp.interpolation = 'B_SPLINE'
                if hasattr(colorramp_2, 'hide'):
                    colorramp_2.hide = False
                if hasattr(colorramp_2, 'location'):
                    colorramp_2.location = (-480.0, 0.0)
                if hasattr(colorramp_2, 'mute'):
                    colorramp_2.mute = False
                if hasattr(colorramp_2, 'name'):
                    colorramp_2.name = 'ColorRamp'
                if hasattr(colorramp_2, 'use_custom_color'):
                    colorramp_2.use_custom_color = False
                if hasattr(colorramp_2, 'width'):
                    colorramp_2.width = 234.1341552734375
                input_ = next((input_ for input_ in colorramp_2.inputs if input_.identifier=='Fac'), None)
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
                output = next((output for output in colorramp_2.outputs if output.identifier=='Color'), None)
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
                output = next((output for output in colorramp_2.outputs if output.identifier=='Alpha'), None)
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

                # LINKS
                node_tree2.links.new(reroute_2.outputs[0], mix_2.inputs[0])
                node_tree2.links.new(mix_2.outputs[2], group_output_2.inputs[0])
                node_tree2.links.new(reroute_003_2.outputs[0], mix_2.inputs[6])
                node_tree2.links.new(reroute_002_2.outputs[0], mix_2.inputs[7])
                node_tree2.links.new(reroute_007_2.outputs[0], math_2.inputs[0])
                node_tree2.links.new(reroute_006_2.outputs[0], math_2.inputs[1])
                node_tree2.links.new(reroute_001_2.outputs[0], reroute_2.inputs[0])
                node_tree2.links.new(reroute_005_2.outputs[0], reroute_002_2.inputs[0])
                node_tree2.links.new(reroute_004_2.outputs[0], reroute_003_2.inputs[0])
                node_tree2.links.new(reroute_009_2.outputs[0], reroute_004_2.inputs[0])
                node_tree2.links.new(reroute_008_2.outputs[0], reroute_005_2.inputs[0])
                node_tree2.links.new(reroute_015_2.outputs[0], reroute_006_2.inputs[0])
                node_tree2.links.new(reroute_014_2.outputs[0], reroute_007_2.inputs[0])
                node_tree2.links.new(reroute_011_2.outputs[0], reroute_008_2.inputs[0])
                node_tree2.links.new(reroute_010_2.outputs[0], reroute_009_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[2], reroute_010_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[3], reroute_011_2.inputs[0])
                node_tree2.links.new(math_2.outputs[0], reroute_012_2.inputs[0])
                node_tree2.links.new(reroute_012_2.outputs[0], reroute_013_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[0], reroute_014_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[1], reroute_015_2.inputs[0])
                node_tree2.links.new(colorramp_2.outputs[0], reroute_001_2.inputs[0])
                node_tree2.links.new(reroute_013_2.outputs[0], colorramp_2.inputs[0])

            color_ramp_group_1 = node_tree1.nodes.new('ShaderNodeGroup')
            if hasattr(color_ramp_group_1, 'node_tree'):
                color_ramp_group_1.node_tree = bpy.data.node_groups.get('Color Ramp.002')
            if hasattr(color_ramp_group_1, 'color'):
                color_ramp_group_1.color = (0.9258301854133606, 0.39081063866615295, 0.07050637900829315)
            if hasattr(color_ramp_group_1, 'hide'):
                color_ramp_group_1.hide = False
            if hasattr(color_ramp_group_1, 'label'):
                color_ramp_group_1.label = 'Color Ramp'
            if hasattr(color_ramp_group_1, 'location'):
                color_ramp_group_1.location = (-25.484039306640625, 14.0)
            if hasattr(color_ramp_group_1, 'mute'):
                color_ramp_group_1.mute = False
            if hasattr(color_ramp_group_1, 'name'):
                color_ramp_group_1.name = 'Color Ramp Group'
            if hasattr(color_ramp_group_1, 'use_custom_color'):
                color_ramp_group_1.use_custom_color = True
            if hasattr(color_ramp_group_1, 'width'):
                color_ramp_group_1.width = 150.96807861328125
            if hasattr(color_ramp_group_1.inputs[0], 'default_value'):
                color_ramp_group_1.inputs[0].default_value = 0.5
            if hasattr(color_ramp_group_1.inputs[0], 'display_shape'):
                color_ramp_group_1.inputs[0].display_shape = 'CIRCLE'
            if hasattr(color_ramp_group_1.inputs[0], 'enabled'):
                color_ramp_group_1.inputs[0].enabled = True
            if hasattr(color_ramp_group_1.inputs[0], 'hide'):
                color_ramp_group_1.inputs[0].hide = False
            if hasattr(color_ramp_group_1.inputs[0], 'hide_value'):
                color_ramp_group_1.inputs[0].hide_value = False
            if hasattr(color_ramp_group_1.inputs[0], 'name'):
                color_ramp_group_1.inputs[0].name = 'Input Factor'
            if hasattr(color_ramp_group_1.inputs[0], 'show_expanded'):
                color_ramp_group_1.inputs[0].show_expanded = False
            if hasattr(color_ramp_group_1.inputs[1], 'default_value'):
                color_ramp_group_1.inputs[1].default_value = 1.0
            if hasattr(color_ramp_group_1.inputs[1], 'display_shape'):
                color_ramp_group_1.inputs[1].display_shape = 'CIRCLE'
            if hasattr(color_ramp_group_1.inputs[1], 'enabled'):
                color_ramp_group_1.inputs[1].enabled = True
            if hasattr(color_ramp_group_1.inputs[1], 'hide'):
                color_ramp_group_1.inputs[1].hide = False
            if hasattr(color_ramp_group_1.inputs[1], 'hide_value'):
                color_ramp_group_1.inputs[1].hide_value = False
            if hasattr(color_ramp_group_1.inputs[1], 'name'):
                color_ramp_group_1.inputs[1].name = 'Factor Multiplier'
            if hasattr(color_ramp_group_1.inputs[1], 'show_expanded'):
                color_ramp_group_1.inputs[1].show_expanded = False
            if hasattr(color_ramp_group_1.inputs[2], 'default_value'):
                color_ramp_group_1.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
            if hasattr(color_ramp_group_1.inputs[2], 'display_shape'):
                color_ramp_group_1.inputs[2].display_shape = 'CIRCLE'
            if hasattr(color_ramp_group_1.inputs[2], 'enabled'):
                color_ramp_group_1.inputs[2].enabled = True
            if hasattr(color_ramp_group_1.inputs[2], 'hide'):
                color_ramp_group_1.inputs[2].hide = True
            if hasattr(color_ramp_group_1.inputs[2], 'hide_value'):
                color_ramp_group_1.inputs[2].hide_value = False
            if hasattr(color_ramp_group_1.inputs[2], 'name'):
                color_ramp_group_1.inputs[2].name = 'Color1'
            if hasattr(color_ramp_group_1.inputs[2], 'show_expanded'):
                color_ramp_group_1.inputs[2].show_expanded = False
            if hasattr(color_ramp_group_1.inputs[3], 'default_value'):
                color_ramp_group_1.inputs[3].default_value = (0.9999987483024597, 0.999998927116394, 1.0, 1.0)
            if hasattr(color_ramp_group_1.inputs[3], 'display_shape'):
                color_ramp_group_1.inputs[3].display_shape = 'CIRCLE'
            if hasattr(color_ramp_group_1.inputs[3], 'enabled'):
                color_ramp_group_1.inputs[3].enabled = True
            if hasattr(color_ramp_group_1.inputs[3], 'hide'):
                color_ramp_group_1.inputs[3].hide = True
            if hasattr(color_ramp_group_1.inputs[3], 'hide_value'):
                color_ramp_group_1.inputs[3].hide_value = False
            if hasattr(color_ramp_group_1.inputs[3], 'name'):
                color_ramp_group_1.inputs[3].name = 'Color2'
            if hasattr(color_ramp_group_1.inputs[3], 'show_expanded'):
                color_ramp_group_1.inputs[3].show_expanded = False
            if hasattr(color_ramp_group_1.outputs[0], 'default_value'):
                color_ramp_group_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            if hasattr(color_ramp_group_1.outputs[0], 'display_shape'):
                color_ramp_group_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(color_ramp_group_1.outputs[0], 'enabled'):
                color_ramp_group_1.outputs[0].enabled = True
            if hasattr(color_ramp_group_1.outputs[0], 'hide'):
                color_ramp_group_1.outputs[0].hide = False
            if hasattr(color_ramp_group_1.outputs[0], 'hide_value'):
                color_ramp_group_1.outputs[0].hide_value = False
            if hasattr(color_ramp_group_1.outputs[0], 'name'):
                color_ramp_group_1.outputs[0].name = 'Color'
            if hasattr(color_ramp_group_1.outputs[0], 'show_expanded'):
                color_ramp_group_1.outputs[0].show_expanded = False

            add_shader_1 = node_tree1.nodes.new('ShaderNodeAddShader')
            if hasattr(add_shader_1, 'color'):
                add_shader_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(add_shader_1, 'hide'):
                add_shader_1.hide = False
            if hasattr(add_shader_1, 'location'):
                add_shader_1.location = (340.0, 340.0)
            if hasattr(add_shader_1, 'mute'):
                add_shader_1.mute = False
            if hasattr(add_shader_1, 'name'):
                add_shader_1.name = 'Add Shader'
            if hasattr(add_shader_1, 'use_custom_color'):
                add_shader_1.use_custom_color = False
            if hasattr(add_shader_1, 'width'):
                add_shader_1.width = 140.0

            mix_shader_003_1 = node_tree1.nodes.new('ShaderNodeMixShader')
            if hasattr(mix_shader_003_1, 'color'):
                mix_shader_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_shader_003_1, 'hide'):
                mix_shader_003_1.hide = False
            if hasattr(mix_shader_003_1, 'location'):
                mix_shader_003_1.location = (520.0, 340.0)
            if hasattr(mix_shader_003_1, 'mute'):
                mix_shader_003_1.mute = False
            if hasattr(mix_shader_003_1, 'name'):
                mix_shader_003_1.name = 'Mix Shader.003'
            if hasattr(mix_shader_003_1, 'use_custom_color'):
                mix_shader_003_1.use_custom_color = False
            if hasattr(mix_shader_003_1, 'width'):
                mix_shader_003_1.width = 140.0
            input_ = next((input_ for input_ in mix_shader_003_1.inputs if input_.identifier=='Fac'), None)
            if input_:
                if hasattr(input_, 'default_value'):
                    input_.default_value = 0.08333331346511841
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

            group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
            if hasattr(group_output_1, 'color'):
                group_output_1.color = (0.6151790022850037, 0.6093840003013611, 0.45541998744010925)
            if hasattr(group_output_1, 'hide'):
                group_output_1.hide = False
            if hasattr(group_output_1, 'is_active_output'):
                group_output_1.is_active_output = True
            if hasattr(group_output_1, 'location'):
                group_output_1.location = (700.0, 340.0)
            if hasattr(group_output_1, 'mute'):
                group_output_1.mute = False
            if hasattr(group_output_1, 'name'):
                group_output_1.name = 'Group Output'
            if hasattr(group_output_1, 'use_custom_color'):
                group_output_1.use_custom_color = True
            if hasattr(group_output_1, 'width'):
                group_output_1.width = 140.0

            node_tree2 = bpy.data.node_groups.get('Acrylic Converter')
            if not node_tree2:
                node_tree2 = bpy.data.node_groups.new('Acrylic Converter', 'ShaderNodeTree')
                for node in node_tree2.nodes:
                    node_tree2.nodes.remove(node)
                # OUTPUTS
                output = node_tree2.outputs.new('NodeSocketShader', 'Shader')
                if hasattr(output, 'attribute_domain'):
                    output.attribute_domain = 'POINT'
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Shader'
                output = node_tree2.outputs.new('NodeSocketShader', 'Volume')
                if hasattr(output, 'attribute_domain'):
                    output.attribute_domain = 'POINT'
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Volume'
                # NODES
                glossy_bsdf_003_2 = node_tree2.nodes.new('ShaderNodeBsdfGlossy')
                if hasattr(glossy_bsdf_003_2, 'color'):
                    glossy_bsdf_003_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(glossy_bsdf_003_2, 'distribution'):
                    glossy_bsdf_003_2.distribution = 'GGX'
                if hasattr(glossy_bsdf_003_2, 'hide'):
                    glossy_bsdf_003_2.hide = False
                if hasattr(glossy_bsdf_003_2, 'location'):
                    glossy_bsdf_003_2.location = (-345.0, 53.0)
                if hasattr(glossy_bsdf_003_2, 'mute'):
                    glossy_bsdf_003_2.mute = False
                if hasattr(glossy_bsdf_003_2, 'name'):
                    glossy_bsdf_003_2.name = 'Glossy BSDF.003'
                if hasattr(glossy_bsdf_003_2, 'use_custom_color'):
                    glossy_bsdf_003_2.use_custom_color = False
                if hasattr(glossy_bsdf_003_2, 'width'):
                    glossy_bsdf_003_2.width = 150.0
                input_ = next((input_ for input_ in glossy_bsdf_003_2.inputs if input_.identifier=='Color'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glossy_bsdf_003_2.inputs if input_.identifier=='Roughness'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.05000000074505806
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Roughness'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glossy_bsdf_003_2.inputs if input_.identifier=='Normal'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = True
                    if hasattr(input_, 'name'):
                        input_.name = 'Normal'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glossy_bsdf_003_2.inputs if input_.identifier=='Weight'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Weight'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False

                transparent_bsdf_2 = node_tree2.nodes.new('ShaderNodeBsdfTransparent')
                if hasattr(transparent_bsdf_2, 'color'):
                    transparent_bsdf_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(transparent_bsdf_2, 'hide'):
                    transparent_bsdf_2.hide = False
                if hasattr(transparent_bsdf_2, 'location'):
                    transparent_bsdf_2.location = (-340.0, -147.0)
                if hasattr(transparent_bsdf_2, 'mute'):
                    transparent_bsdf_2.mute = False
                if hasattr(transparent_bsdf_2, 'name'):
                    transparent_bsdf_2.name = 'Transparent BSDF'
                if hasattr(transparent_bsdf_2, 'use_custom_color'):
                    transparent_bsdf_2.use_custom_color = False
                if hasattr(transparent_bsdf_2, 'width'):
                    transparent_bsdf_2.width = 140.0
                input_ = next((input_ for input_ in transparent_bsdf_2.inputs if input_.identifier=='Color'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.6920710802078247, 0.6920710802078247, 0.6920710802078247, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in transparent_bsdf_2.inputs if input_.identifier=='Weight'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Weight'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False

                glass_bsdf_2 = node_tree2.nodes.new('ShaderNodeBsdfGlass')
                if hasattr(glass_bsdf_2, 'color'):
                    glass_bsdf_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(glass_bsdf_2, 'distribution'):
                    glass_bsdf_2.distribution = 'SHARP'
                if hasattr(glass_bsdf_2, 'hide'):
                    glass_bsdf_2.hide = False
                if hasattr(glass_bsdf_2, 'location'):
                    glass_bsdf_2.location = (-345.0, -47.0)
                if hasattr(glass_bsdf_2, 'mute'):
                    glass_bsdf_2.mute = False
                if hasattr(glass_bsdf_2, 'name'):
                    glass_bsdf_2.name = 'Glass BSDF'
                if hasattr(glass_bsdf_2, 'use_custom_color'):
                    glass_bsdf_2.use_custom_color = False
                if hasattr(glass_bsdf_2, 'width'):
                    glass_bsdf_2.width = 150.0
                input_ = next((input_ for input_ in glass_bsdf_2.inputs if input_.identifier=='Color'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glass_bsdf_2.inputs if input_.identifier=='Roughness'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.01414213515818119
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Roughness'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glass_bsdf_2.inputs if input_.identifier=='IOR'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.4900000095367432
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'IOR'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glass_bsdf_2.inputs if input_.identifier=='Normal'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = True
                    if hasattr(input_, 'name'):
                        input_.name = 'Normal'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glass_bsdf_2.inputs if input_.identifier=='Weight'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Weight'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False

                light_path_2 = node_tree2.nodes.new('ShaderNodeLightPath')
                if hasattr(light_path_2, 'color'):
                    light_path_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(light_path_2, 'hide'):
                    light_path_2.hide = False
                if hasattr(light_path_2, 'location'):
                    light_path_2.location = (-340.0, 120.0)
                if hasattr(light_path_2, 'mute'):
                    light_path_2.mute = False
                if hasattr(light_path_2, 'name'):
                    light_path_2.name = 'Light Path'
                if hasattr(light_path_2, 'use_custom_color'):
                    light_path_2.use_custom_color = False
                if hasattr(light_path_2, 'width'):
                    light_path_2.width = 140.0
                output = next((output for output in light_path_2.outputs if output.identifier=='Is Camera Ray'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Is Camera Ray'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Is Shadow Ray'), None)
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
                output = next((output for output in light_path_2.outputs if output.identifier=='Is Diffuse Ray'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Is Diffuse Ray'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Is Glossy Ray'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Is Glossy Ray'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Is Singular Ray'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Is Singular Ray'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Is Reflection Ray'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Is Reflection Ray'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Is Transmission Ray'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Is Transmission Ray'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Ray Length'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Ray Length'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Ray Depth'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Ray Depth'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Diffuse Depth'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Diffuse Depth'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Glossy Depth'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Glossy Depth'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Transparent Depth'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Transparent Depth'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in light_path_2.outputs if output.identifier=='Transmission Depth'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Transmission Depth'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                mix_shader_004_2 = node_tree2.nodes.new('ShaderNodeMixShader')
                if hasattr(mix_shader_004_2, 'color'):
                    mix_shader_004_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(mix_shader_004_2, 'hide'):
                    mix_shader_004_2.hide = False
                if hasattr(mix_shader_004_2, 'location'):
                    mix_shader_004_2.location = (-180.0, 120.0)
                if hasattr(mix_shader_004_2, 'mute'):
                    mix_shader_004_2.mute = False
                if hasattr(mix_shader_004_2, 'name'):
                    mix_shader_004_2.name = 'Mix Shader.004'
                if hasattr(mix_shader_004_2, 'use_custom_color'):
                    mix_shader_004_2.use_custom_color = False
                if hasattr(mix_shader_004_2, 'width'):
                    mix_shader_004_2.width = 140.0
                input_ = next((input_ for input_ in mix_shader_004_2.inputs if input_.identifier=='Fac'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.949999988079071
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Fac'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False

                mix_shader_003_2 = node_tree2.nodes.new('ShaderNodeMixShader')
                if hasattr(mix_shader_003_2, 'color'):
                    mix_shader_003_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(mix_shader_003_2, 'hide'):
                    mix_shader_003_2.hide = False
                if hasattr(mix_shader_003_2, 'location'):
                    mix_shader_003_2.location = (-20.0, 120.0)
                if hasattr(mix_shader_003_2, 'mute'):
                    mix_shader_003_2.mute = False
                if hasattr(mix_shader_003_2, 'name'):
                    mix_shader_003_2.name = 'Mix Shader.003'
                if hasattr(mix_shader_003_2, 'use_custom_color'):
                    mix_shader_003_2.use_custom_color = False
                if hasattr(mix_shader_003_2, 'width'):
                    mix_shader_003_2.width = 140.0
                input_ = next((input_ for input_ in mix_shader_003_2.inputs if input_.identifier=='Fac'), None)
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
                        input_.name = 'Fac'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False

                volume_absorption_2 = node_tree2.nodes.new('ShaderNodeVolumeAbsorption')
                if hasattr(volume_absorption_2, 'color'):
                    volume_absorption_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(volume_absorption_2, 'hide'):
                    volume_absorption_2.hide = False
                if hasattr(volume_absorption_2, 'location'):
                    volume_absorption_2.location = (-20.0, -20.0)
                if hasattr(volume_absorption_2, 'mute'):
                    volume_absorption_2.mute = False
                if hasattr(volume_absorption_2, 'name'):
                    volume_absorption_2.name = 'Volume Absorption'
                if hasattr(volume_absorption_2, 'use_custom_color'):
                    volume_absorption_2.use_custom_color = False
                if hasattr(volume_absorption_2, 'width'):
                    volume_absorption_2.width = 140.0
                input_ = next((input_ for input_ in volume_absorption_2.inputs if input_.identifier=='Color'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.7874122262001038, 0.7874122262001038, 0.7874122262001038, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in volume_absorption_2.inputs if input_.identifier=='Density'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.10000000149011612
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Density'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in volume_absorption_2.inputs if input_.identifier=='Weight'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Weight'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False

                group_input_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_2, 'color'):
                    group_input_2.color = (0.6151790022850037, 0.6093840003013611, 0.45541998744010925)
                if hasattr(group_input_2, 'hide'):
                    group_input_2.hide = False
                if hasattr(group_input_2, 'location'):
                    group_input_2.location = (-500.0, 120.0)
                if hasattr(group_input_2, 'mute'):
                    group_input_2.mute = False
                if hasattr(group_input_2, 'name'):
                    group_input_2.name = 'Group Input'
                if hasattr(group_input_2, 'use_custom_color'):
                    group_input_2.use_custom_color = True
                if hasattr(group_input_2, 'width'):
                    group_input_2.width = 140.0

                group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
                if hasattr(group_output_2, 'color'):
                    group_output_2.color = (0.6151790022850037, 0.6093840003013611, 0.45541998744010925)
                if hasattr(group_output_2, 'hide'):
                    group_output_2.hide = False
                if hasattr(group_output_2, 'is_active_output'):
                    group_output_2.is_active_output = True
                if hasattr(group_output_2, 'location'):
                    group_output_2.location = (160.0, 120.0)
                if hasattr(group_output_2, 'mute'):
                    group_output_2.mute = False
                if hasattr(group_output_2, 'name'):
                    group_output_2.name = 'Group Output'
                if hasattr(group_output_2, 'use_custom_color'):
                    group_output_2.use_custom_color = True
                if hasattr(group_output_2, 'width'):
                    group_output_2.width = 140.0

                # LINKS
                node_tree2.links.new(transparent_bsdf_2.outputs[0], mix_shader_003_2.inputs[2])
                node_tree2.links.new(light_path_2.outputs[1], mix_shader_003_2.inputs[0])
                node_tree2.links.new(glass_bsdf_2.outputs[0], mix_shader_004_2.inputs[2])
                node_tree2.links.new(glossy_bsdf_003_2.outputs[0], mix_shader_004_2.inputs[1])
                node_tree2.links.new(mix_shader_004_2.outputs[0], mix_shader_003_2.inputs[1])
                node_tree2.links.new(mix_shader_003_2.outputs[0], group_output_2.inputs[0])
                node_tree2.links.new(volume_absorption_2.outputs[0], group_output_2.inputs[1])

            acrylic_converter_1 = node_tree1.nodes.new('ShaderNodeGroup')
            if hasattr(acrylic_converter_1, 'node_tree'):
                acrylic_converter_1.node_tree = bpy.data.node_groups.get('Acrylic Converter')
            if hasattr(acrylic_converter_1, 'color'):
                acrylic_converter_1.color = (0.3519147038459778, 0.477032333612442, 0.5925787687301636)
            if hasattr(acrylic_converter_1, 'hide'):
                acrylic_converter_1.hide = False
            if hasattr(acrylic_converter_1, 'label'):
                acrylic_converter_1.label = 'Acrylic Converter'
            if hasattr(acrylic_converter_1, 'location'):
                acrylic_converter_1.location = (340.0, 220.0)
            if hasattr(acrylic_converter_1, 'mute'):
                acrylic_converter_1.mute = False
            if hasattr(acrylic_converter_1, 'name'):
                acrylic_converter_1.name = 'Acrylic Converter'
            if hasattr(acrylic_converter_1, 'use_custom_color'):
                acrylic_converter_1.use_custom_color = True
            if hasattr(acrylic_converter_1, 'width'):
                acrylic_converter_1.width = 140.0

            group_input_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_1, 'color'):
                group_input_1.color = (0.6151790022850037, 0.6093840003013611, 0.45541998744010925)
            if hasattr(group_input_1, 'hide'):
                group_input_1.hide = False
            if hasattr(group_input_1, 'location'):
                group_input_1.location = (-380.0, 198.0)
            if hasattr(group_input_1, 'mute'):
                group_input_1.mute = False
            if hasattr(group_input_1, 'name'):
                group_input_1.name = 'Group Input'
            if hasattr(group_input_1, 'use_custom_color'):
                group_input_1.use_custom_color = True
            if hasattr(group_input_1, 'width'):
                group_input_1.width = 140.0
            if hasattr(group_input_1.outputs[0], 'default_value'):
                group_input_1.outputs[0].default_value = 0.08333331346511841
            if hasattr(group_input_1.outputs[0], 'display_shape'):
                group_input_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[0], 'enabled'):
                group_input_1.outputs[0].enabled = True
            if hasattr(group_input_1.outputs[0], 'hide'):
                group_input_1.outputs[0].hide = True
            if hasattr(group_input_1.outputs[0], 'hide_value'):
                group_input_1.outputs[0].hide_value = False
            if hasattr(group_input_1.outputs[0], 'name'):
                group_input_1.outputs[0].name = 'Acrylic Factor'
            if hasattr(group_input_1.outputs[0], 'show_expanded'):
                group_input_1.outputs[0].show_expanded = False
            if hasattr(group_input_1.outputs[1], 'default_value'):
                group_input_1.outputs[1].default_value = (0.8227859139442444, 0.0, 0.5936002731323242, 1.0)
            if hasattr(group_input_1.outputs[1], 'display_shape'):
                group_input_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[1], 'enabled'):
                group_input_1.outputs[1].enabled = True
            if hasattr(group_input_1.outputs[1], 'hide'):
                group_input_1.outputs[1].hide = False
            if hasattr(group_input_1.outputs[1], 'hide_value'):
                group_input_1.outputs[1].hide_value = False
            if hasattr(group_input_1.outputs[1], 'name'):
                group_input_1.outputs[1].name = 'Iridescent Color 1'
            if hasattr(group_input_1.outputs[1], 'show_expanded'):
                group_input_1.outputs[1].show_expanded = False
            if hasattr(group_input_1.outputs[2], 'default_value'):
                group_input_1.outputs[2].default_value = (0.18765491247177124, 0.7835378646850586, 0.0, 1.0)
            if hasattr(group_input_1.outputs[2], 'display_shape'):
                group_input_1.outputs[2].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[2], 'enabled'):
                group_input_1.outputs[2].enabled = True
            if hasattr(group_input_1.outputs[2], 'hide'):
                group_input_1.outputs[2].hide = False
            if hasattr(group_input_1.outputs[2], 'hide_value'):
                group_input_1.outputs[2].hide_value = False
            if hasattr(group_input_1.outputs[2], 'name'):
                group_input_1.outputs[2].name = 'Iridescent Color 2'
            if hasattr(group_input_1.outputs[2], 'show_expanded'):
                group_input_1.outputs[2].show_expanded = False
            if hasattr(group_input_1.outputs[3], 'default_value'):
                group_input_1.outputs[3].default_value = (0.004024718888103962, 0.10224173218011856, 0.7605247497558594, 1.0)
            if hasattr(group_input_1.outputs[3], 'display_shape'):
                group_input_1.outputs[3].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[3], 'enabled'):
                group_input_1.outputs[3].enabled = True
            if hasattr(group_input_1.outputs[3], 'hide'):
                group_input_1.outputs[3].hide = False
            if hasattr(group_input_1.outputs[3], 'hide_value'):
                group_input_1.outputs[3].hide_value = False
            if hasattr(group_input_1.outputs[3], 'name'):
                group_input_1.outputs[3].name = 'Iridescent Color 3'
            if hasattr(group_input_1.outputs[3], 'show_expanded'):
                group_input_1.outputs[3].show_expanded = False
            if hasattr(group_input_1.outputs[4], 'default_value'):
                group_input_1.outputs[4].default_value = (0.0, 0.2521688640117645, 1.0, 1.0)
            if hasattr(group_input_1.outputs[4], 'display_shape'):
                group_input_1.outputs[4].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[4], 'enabled'):
                group_input_1.outputs[4].enabled = True
            if hasattr(group_input_1.outputs[4], 'hide'):
                group_input_1.outputs[4].hide = False
            if hasattr(group_input_1.outputs[4], 'hide_value'):
                group_input_1.outputs[4].hide_value = False
            if hasattr(group_input_1.outputs[4], 'name'):
                group_input_1.outputs[4].name = 'Edge Emission Color'
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
                group_input_1.outputs[5].name = 'Frensel / Facing'
            if hasattr(group_input_1.outputs[5], 'show_expanded'):
                group_input_1.outputs[5].show_expanded = False
            if hasattr(group_input_1.outputs[6], 'default_value'):
                group_input_1.outputs[6].default_value = 0.5
            if hasattr(group_input_1.outputs[6], 'display_shape'):
                group_input_1.outputs[6].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[6], 'enabled'):
                group_input_1.outputs[6].enabled = True
            if hasattr(group_input_1.outputs[6], 'hide'):
                group_input_1.outputs[6].hide = False
            if hasattr(group_input_1.outputs[6], 'hide_value'):
                group_input_1.outputs[6].hide_value = False
            if hasattr(group_input_1.outputs[6], 'name'):
                group_input_1.outputs[6].name = 'Emission Strength'
            if hasattr(group_input_1.outputs[6], 'show_expanded'):
                group_input_1.outputs[6].show_expanded = False
            if hasattr(group_input_1.outputs[7], 'default_value'):
                group_input_1.outputs[7].default_value = 1.0
            if hasattr(group_input_1.outputs[7], 'display_shape'):
                group_input_1.outputs[7].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[7], 'enabled'):
                group_input_1.outputs[7].enabled = True
            if hasattr(group_input_1.outputs[7], 'hide'):
                group_input_1.outputs[7].hide = False
            if hasattr(group_input_1.outputs[7], 'hide_value'):
                group_input_1.outputs[7].hide_value = False
            if hasattr(group_input_1.outputs[7], 'name'):
                group_input_1.outputs[7].name = 'Edge Emision Size'
            if hasattr(group_input_1.outputs[7], 'show_expanded'):
                group_input_1.outputs[7].show_expanded = False

            group_input_001_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_001_1, 'color'):
                group_input_001_1.color = (0.6151790022850037, 0.6093840003013611, 0.45541998744010925)
            if hasattr(group_input_001_1, 'hide'):
                group_input_001_1.hide = False
            if hasattr(group_input_001_1, 'location'):
                group_input_001_1.location = (340.0, 100.0)
            if hasattr(group_input_001_1, 'mute'):
                group_input_001_1.mute = False
            if hasattr(group_input_001_1, 'name'):
                group_input_001_1.name = 'Group Input.001'
            if hasattr(group_input_001_1, 'use_custom_color'):
                group_input_001_1.use_custom_color = True
            if hasattr(group_input_001_1, 'width'):
                group_input_001_1.width = 140.0
            if hasattr(group_input_001_1.outputs[0], 'default_value'):
                group_input_001_1.outputs[0].default_value = 0.08333331346511841
            if hasattr(group_input_001_1.outputs[0], 'display_shape'):
                group_input_001_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[0], 'enabled'):
                group_input_001_1.outputs[0].enabled = True
            if hasattr(group_input_001_1.outputs[0], 'hide'):
                group_input_001_1.outputs[0].hide = False
            if hasattr(group_input_001_1.outputs[0], 'hide_value'):
                group_input_001_1.outputs[0].hide_value = False
            if hasattr(group_input_001_1.outputs[0], 'name'):
                group_input_001_1.outputs[0].name = 'Acrylic Factor'
            if hasattr(group_input_001_1.outputs[0], 'show_expanded'):
                group_input_001_1.outputs[0].show_expanded = False
            if hasattr(group_input_001_1.outputs[1], 'default_value'):
                group_input_001_1.outputs[1].default_value = (0.8227859139442444, 0.0, 0.5936002731323242, 1.0)
            if hasattr(group_input_001_1.outputs[1], 'display_shape'):
                group_input_001_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[1], 'enabled'):
                group_input_001_1.outputs[1].enabled = True
            if hasattr(group_input_001_1.outputs[1], 'hide'):
                group_input_001_1.outputs[1].hide = True
            if hasattr(group_input_001_1.outputs[1], 'hide_value'):
                group_input_001_1.outputs[1].hide_value = False
            if hasattr(group_input_001_1.outputs[1], 'name'):
                group_input_001_1.outputs[1].name = 'Iridescent Color 1'
            if hasattr(group_input_001_1.outputs[1], 'show_expanded'):
                group_input_001_1.outputs[1].show_expanded = False
            if hasattr(group_input_001_1.outputs[2], 'default_value'):
                group_input_001_1.outputs[2].default_value = (0.18765491247177124, 0.7835378646850586, 0.0, 1.0)
            if hasattr(group_input_001_1.outputs[2], 'display_shape'):
                group_input_001_1.outputs[2].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[2], 'enabled'):
                group_input_001_1.outputs[2].enabled = True
            if hasattr(group_input_001_1.outputs[2], 'hide'):
                group_input_001_1.outputs[2].hide = True
            if hasattr(group_input_001_1.outputs[2], 'hide_value'):
                group_input_001_1.outputs[2].hide_value = False
            if hasattr(group_input_001_1.outputs[2], 'name'):
                group_input_001_1.outputs[2].name = 'Iridescent Color 2'
            if hasattr(group_input_001_1.outputs[2], 'show_expanded'):
                group_input_001_1.outputs[2].show_expanded = False
            if hasattr(group_input_001_1.outputs[3], 'default_value'):
                group_input_001_1.outputs[3].default_value = (0.004024718888103962, 0.10224173218011856, 0.7605247497558594, 1.0)
            if hasattr(group_input_001_1.outputs[3], 'display_shape'):
                group_input_001_1.outputs[3].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[3], 'enabled'):
                group_input_001_1.outputs[3].enabled = True
            if hasattr(group_input_001_1.outputs[3], 'hide'):
                group_input_001_1.outputs[3].hide = True
            if hasattr(group_input_001_1.outputs[3], 'hide_value'):
                group_input_001_1.outputs[3].hide_value = False
            if hasattr(group_input_001_1.outputs[3], 'name'):
                group_input_001_1.outputs[3].name = 'Iridescent Color 3'
            if hasattr(group_input_001_1.outputs[3], 'show_expanded'):
                group_input_001_1.outputs[3].show_expanded = False
            if hasattr(group_input_001_1.outputs[4], 'default_value'):
                group_input_001_1.outputs[4].default_value = (0.0, 0.2521688640117645, 1.0, 1.0)
            if hasattr(group_input_001_1.outputs[4], 'display_shape'):
                group_input_001_1.outputs[4].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[4], 'enabled'):
                group_input_001_1.outputs[4].enabled = True
            if hasattr(group_input_001_1.outputs[4], 'hide'):
                group_input_001_1.outputs[4].hide = True
            if hasattr(group_input_001_1.outputs[4], 'hide_value'):
                group_input_001_1.outputs[4].hide_value = False
            if hasattr(group_input_001_1.outputs[4], 'name'):
                group_input_001_1.outputs[4].name = 'Edge Emission Color'
            if hasattr(group_input_001_1.outputs[4], 'show_expanded'):
                group_input_001_1.outputs[4].show_expanded = False
            if hasattr(group_input_001_1.outputs[5], 'default_value'):
                group_input_001_1.outputs[5].default_value = 0.0
            if hasattr(group_input_001_1.outputs[5], 'display_shape'):
                group_input_001_1.outputs[5].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[5], 'enabled'):
                group_input_001_1.outputs[5].enabled = True
            if hasattr(group_input_001_1.outputs[5], 'hide'):
                group_input_001_1.outputs[5].hide = True
            if hasattr(group_input_001_1.outputs[5], 'hide_value'):
                group_input_001_1.outputs[5].hide_value = False
            if hasattr(group_input_001_1.outputs[5], 'name'):
                group_input_001_1.outputs[5].name = 'Frensel / Facing'
            if hasattr(group_input_001_1.outputs[5], 'show_expanded'):
                group_input_001_1.outputs[5].show_expanded = False
            if hasattr(group_input_001_1.outputs[6], 'default_value'):
                group_input_001_1.outputs[6].default_value = 0.5
            if hasattr(group_input_001_1.outputs[6], 'display_shape'):
                group_input_001_1.outputs[6].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[6], 'enabled'):
                group_input_001_1.outputs[6].enabled = True
            if hasattr(group_input_001_1.outputs[6], 'hide'):
                group_input_001_1.outputs[6].hide = True
            if hasattr(group_input_001_1.outputs[6], 'hide_value'):
                group_input_001_1.outputs[6].hide_value = False
            if hasattr(group_input_001_1.outputs[6], 'name'):
                group_input_001_1.outputs[6].name = 'Emission Strength'
            if hasattr(group_input_001_1.outputs[6], 'show_expanded'):
                group_input_001_1.outputs[6].show_expanded = False
            if hasattr(group_input_001_1.outputs[7], 'default_value'):
                group_input_001_1.outputs[7].default_value = 1.0
            if hasattr(group_input_001_1.outputs[7], 'display_shape'):
                group_input_001_1.outputs[7].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[7], 'enabled'):
                group_input_001_1.outputs[7].enabled = True
            if hasattr(group_input_001_1.outputs[7], 'hide'):
                group_input_001_1.outputs[7].hide = True
            if hasattr(group_input_001_1.outputs[7], 'hide_value'):
                group_input_001_1.outputs[7].hide_value = False
            if hasattr(group_input_001_1.outputs[7], 'name'):
                group_input_001_1.outputs[7].name = 'Edge Emision Size'
            if hasattr(group_input_001_1.outputs[7], 'show_expanded'):
                group_input_001_1.outputs[7].show_expanded = False

            # LINKS
            node_tree1.links.new(emission_1.outputs[0], mix_shader_1.inputs[2])
            node_tree1.links.new(color_ramp_group_1.outputs[0], mix_shader_1.inputs[0])
            node_tree1.links.new(mix_shader_1.outputs[0], add_shader_1.inputs[1])
            node_tree1.links.new(glossy_bsdf_1.outputs[0], mix_shader_001_1.inputs[1])
            node_tree1.links.new(glossy_bsdf_001_1.outputs[0], mix_shader_001_1.inputs[2])
            node_tree1.links.new(glossy_bsdf_002_1.outputs[0], mix_shader_002_1.inputs[2])
            node_tree1.links.new(mix_shader_001_1.outputs[0], mix_shader_002_1.inputs[1])
            node_tree1.links.new(layer_weight_002_1.outputs[1], mix_shader_001_1.inputs[0])
            node_tree1.links.new(layer_weight_001_1.outputs[1], mix_shader_002_1.inputs[0])
            node_tree1.links.new(mix_shader_002_1.outputs[0], add_shader_1.inputs[0])
            node_tree1.links.new(layer_weight_1.outputs[0], mix_1.inputs[6])
            node_tree1.links.new(layer_weight_003_1.outputs[1], mix_1.inputs[7])
            node_tree1.links.new(group_input_1.outputs[1], glossy_bsdf_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[2], glossy_bsdf_001_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[3], glossy_bsdf_002_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[5], mix_1.inputs[0])
            node_tree1.links.new(math_1.outputs[0], emission_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[4], emission_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[6], math_1.inputs[0])
            node_tree1.links.new(mix_1.outputs[2], color_ramp_group_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[7], color_ramp_group_1.inputs[1])
            node_tree1.links.new(add_shader_1.outputs[0], mix_shader_003_1.inputs[1])
            node_tree1.links.new(acrylic_converter_1.outputs[0], mix_shader_003_1.inputs[2])
            node_tree1.links.new(mix_shader_003_1.outputs[0], group_output_1.inputs[0])
            node_tree1.links.new(acrylic_converter_1.outputs[1], group_output_1.inputs[1])
            node_tree1.links.new(group_input_001_1.outputs[0], mix_shader_003_1.inputs[0])

        iridescent_acrylic_edge_emission_0 = node_tree0.nodes.new('ShaderNodeGroup')
        if hasattr(iridescent_acrylic_edge_emission_0, 'node_tree'):
            iridescent_acrylic_edge_emission_0.node_tree = bpy.data.node_groups.get('Iridescent Acrylic Edge Emission')
        if hasattr(iridescent_acrylic_edge_emission_0, 'color'):
            iridescent_acrylic_edge_emission_0.color = (0.01520800031721592, 0.1274379938840866, 0.18447500467300415)
        if hasattr(iridescent_acrylic_edge_emission_0, 'hide'):
            iridescent_acrylic_edge_emission_0.hide = False
        if hasattr(iridescent_acrylic_edge_emission_0, 'label'):
            iridescent_acrylic_edge_emission_0.label = 'Iridescent Acrylic Edge Emission'
        if hasattr(iridescent_acrylic_edge_emission_0, 'location'):
            iridescent_acrylic_edge_emission_0.location = (192.02359008789062, 400.0)
        if hasattr(iridescent_acrylic_edge_emission_0, 'mute'):
            iridescent_acrylic_edge_emission_0.mute = False
        if hasattr(iridescent_acrylic_edge_emission_0, 'name'):
            iridescent_acrylic_edge_emission_0.name = 'Iridescent Acrylic Edge Emission'
        if hasattr(iridescent_acrylic_edge_emission_0, 'use_custom_color'):
            iridescent_acrylic_edge_emission_0.use_custom_color = True
        if hasattr(iridescent_acrylic_edge_emission_0, 'width'):
            iridescent_acrylic_edge_emission_0.width = 187.97640991210938
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[0], 'default_value'):
            iridescent_acrylic_edge_emission_0.inputs[0].default_value = 0.10000000149011612
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[0], 'display_shape'):
            iridescent_acrylic_edge_emission_0.inputs[0].display_shape = 'CIRCLE'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[0], 'enabled'):
            iridescent_acrylic_edge_emission_0.inputs[0].enabled = True
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[0], 'hide'):
            iridescent_acrylic_edge_emission_0.inputs[0].hide = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[0], 'hide_value'):
            iridescent_acrylic_edge_emission_0.inputs[0].hide_value = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[0], 'name'):
            iridescent_acrylic_edge_emission_0.inputs[0].name = 'Acrylic Factor'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[0], 'show_expanded'):
            iridescent_acrylic_edge_emission_0.inputs[0].show_expanded = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[1], 'default_value'):
            iridescent_acrylic_edge_emission_0.inputs[1].default_value = (0.8227859139442444, 0.0, 0.5936002731323242, 1.0)
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[1], 'display_shape'):
            iridescent_acrylic_edge_emission_0.inputs[1].display_shape = 'CIRCLE'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[1], 'enabled'):
            iridescent_acrylic_edge_emission_0.inputs[1].enabled = True
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[1], 'hide'):
            iridescent_acrylic_edge_emission_0.inputs[1].hide = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[1], 'hide_value'):
            iridescent_acrylic_edge_emission_0.inputs[1].hide_value = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[1], 'name'):
            iridescent_acrylic_edge_emission_0.inputs[1].name = 'Iridescent Color 1'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[1], 'show_expanded'):
            iridescent_acrylic_edge_emission_0.inputs[1].show_expanded = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[2], 'default_value'):
            iridescent_acrylic_edge_emission_0.inputs[2].default_value = (0.18765491247177124, 0.7835378646850586, 0.0, 1.0)
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[2], 'display_shape'):
            iridescent_acrylic_edge_emission_0.inputs[2].display_shape = 'CIRCLE'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[2], 'enabled'):
            iridescent_acrylic_edge_emission_0.inputs[2].enabled = True
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[2], 'hide'):
            iridescent_acrylic_edge_emission_0.inputs[2].hide = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[2], 'hide_value'):
            iridescent_acrylic_edge_emission_0.inputs[2].hide_value = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[2], 'name'):
            iridescent_acrylic_edge_emission_0.inputs[2].name = 'Iridescent Color 2'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[2], 'show_expanded'):
            iridescent_acrylic_edge_emission_0.inputs[2].show_expanded = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[3], 'default_value'):
            iridescent_acrylic_edge_emission_0.inputs[3].default_value = (0.004024718888103962, 0.10224173218011856, 0.7605247497558594, 1.0)
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[3], 'display_shape'):
            iridescent_acrylic_edge_emission_0.inputs[3].display_shape = 'CIRCLE'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[3], 'enabled'):
            iridescent_acrylic_edge_emission_0.inputs[3].enabled = True
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[3], 'hide'):
            iridescent_acrylic_edge_emission_0.inputs[3].hide = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[3], 'hide_value'):
            iridescent_acrylic_edge_emission_0.inputs[3].hide_value = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[3], 'name'):
            iridescent_acrylic_edge_emission_0.inputs[3].name = 'Iridescent Color 3'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[3], 'show_expanded'):
            iridescent_acrylic_edge_emission_0.inputs[3].show_expanded = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[4], 'default_value'):
            iridescent_acrylic_edge_emission_0.inputs[4].default_value = (0.3371630609035492, 0.0, 1.0, 1.0)
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[4], 'display_shape'):
            iridescent_acrylic_edge_emission_0.inputs[4].display_shape = 'CIRCLE'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[4], 'enabled'):
            iridescent_acrylic_edge_emission_0.inputs[4].enabled = True
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[4], 'hide'):
            iridescent_acrylic_edge_emission_0.inputs[4].hide = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[4], 'hide_value'):
            iridescent_acrylic_edge_emission_0.inputs[4].hide_value = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[4], 'name'):
            iridescent_acrylic_edge_emission_0.inputs[4].name = 'Edge Emission Color'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[4], 'show_expanded'):
            iridescent_acrylic_edge_emission_0.inputs[4].show_expanded = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[5], 'default_value'):
            iridescent_acrylic_edge_emission_0.inputs[5].default_value = 0.0
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[5], 'display_shape'):
            iridescent_acrylic_edge_emission_0.inputs[5].display_shape = 'CIRCLE'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[5], 'enabled'):
            iridescent_acrylic_edge_emission_0.inputs[5].enabled = True
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[5], 'hide'):
            iridescent_acrylic_edge_emission_0.inputs[5].hide = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[5], 'hide_value'):
            iridescent_acrylic_edge_emission_0.inputs[5].hide_value = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[5], 'name'):
            iridescent_acrylic_edge_emission_0.inputs[5].name = 'Frensel / Facing'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[5], 'show_expanded'):
            iridescent_acrylic_edge_emission_0.inputs[5].show_expanded = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[6], 'default_value'):
            iridescent_acrylic_edge_emission_0.inputs[6].default_value = 0.5
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[6], 'display_shape'):
            iridescent_acrylic_edge_emission_0.inputs[6].display_shape = 'CIRCLE'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[6], 'enabled'):
            iridescent_acrylic_edge_emission_0.inputs[6].enabled = True
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[6], 'hide'):
            iridescent_acrylic_edge_emission_0.inputs[6].hide = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[6], 'hide_value'):
            iridescent_acrylic_edge_emission_0.inputs[6].hide_value = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[6], 'name'):
            iridescent_acrylic_edge_emission_0.inputs[6].name = 'Emission Strength'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[6], 'show_expanded'):
            iridescent_acrylic_edge_emission_0.inputs[6].show_expanded = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[7], 'default_value'):
            iridescent_acrylic_edge_emission_0.inputs[7].default_value = 1.0
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[7], 'display_shape'):
            iridescent_acrylic_edge_emission_0.inputs[7].display_shape = 'CIRCLE'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[7], 'enabled'):
            iridescent_acrylic_edge_emission_0.inputs[7].enabled = True
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[7], 'hide'):
            iridescent_acrylic_edge_emission_0.inputs[7].hide = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[7], 'hide_value'):
            iridescent_acrylic_edge_emission_0.inputs[7].hide_value = False
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[7], 'name'):
            iridescent_acrylic_edge_emission_0.inputs[7].name = 'Edge Emision Size'
        if hasattr(iridescent_acrylic_edge_emission_0.inputs[7], 'show_expanded'):
            iridescent_acrylic_edge_emission_0.inputs[7].show_expanded = False

        # LINKS
        node_tree0.links.new(iridescent_acrylic_edge_emission_0.outputs[0], material_output_0.inputs[0])
        node_tree0.links.new(iridescent_acrylic_edge_emission_0.outputs[1], material_output_0.inputs[1])

        # TO ACTIVE
        # selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
        # for obj in selected_objects:
        #     obj.active_material = iridescent_acrylic_edge_emission
        return iridescent_acrylic_edge_emission