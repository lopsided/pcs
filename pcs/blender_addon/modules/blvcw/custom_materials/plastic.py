import bpy

class Material():
    def __init__(self):
        pass
    
    def load():
        import bpy

        # MATERIAL
        blister_plastic_transparent_sheen_ = bpy.data.materials.new(name='Blister Plastic (Transparent Sheen)')
        blister_plastic_transparent_sheen_.use_nodes = True
        node_tree0 = blister_plastic_transparent_sheen_.node_tree

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
            material_output_0.location = (10.0, 0.0)
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

        node_tree1 = bpy.data.node_groups.get('Blister Plastic (Transparent Sheen)')
        if not node_tree1:
            node_tree1 = bpy.data.node_groups.new('Blister Plastic (Transparent Sheen)', 'ShaderNodeTree')
            for node in node_tree1.nodes:
                node_tree1.nodes.remove(node)
            # INPUTS
            input = node_tree1.inputs.new('NodeSocketColor', 'Base Color')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Base Color'
            input = node_tree1.inputs.new('NodeSocketColor', 'Transparent Color')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Transparent Color'
            input = node_tree1.inputs.new('NodeSocketColor', 'Reflection Color')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'name'):
                input.name = 'Reflection Color'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', 'Reflection Factor')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.25
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = 'Reflection Factor'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', 'COLOR VARIATION')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.0
            if hasattr(input, 'hide_value'):
                input.hide_value = True
            if hasattr(input, 'max_value'):
                input.max_value = 3.4028234663852886e+38
            if hasattr(input, 'min_value'):
                input.min_value = -3.4028234663852886e+38
            if hasattr(input, 'name'):
                input.name = 'COLOR VARIATION'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', '  Color Variation Scale')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 6.5
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 10.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.05000000074505806
            if hasattr(input, 'name'):
                input.name = '  Color Variation Scale'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', '  Color Variation Distortion')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.15000000596046448
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 3.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = '  Color Variation Distortion'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', '  Random Color Var')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.7749999761581421
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = '  Random Color Var'
            input = node_tree1.inputs.new('NodeSocketFloat', 'COLOR ADJUSTMENTS')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.0
            if hasattr(input, 'hide_value'):
                input.hide_value = True
            if hasattr(input, 'max_value'):
                input.max_value = 3.4028234663852886e+38
            if hasattr(input, 'min_value'):
                input.min_value = -3.4028234663852886e+38
            if hasattr(input, 'name'):
                input.name = 'COLOR ADJUSTMENTS'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', '  Unpaint')
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
                input.name = '  Unpaint'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', '  Color Inverter')
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
                input.name = '  Color Inverter'
            input = node_tree1.inputs.new('NodeSocketFloat', '  Contrast')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 100.0
            if hasattr(input, 'min_value'):
                input.min_value = -100.0
            if hasattr(input, 'name'):
                input.name = '  Contrast'
            input = node_tree1.inputs.new('NodeSocketFloatUnsigned', '  Gamma')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 1.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 10.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0010000000474974513
            if hasattr(input, 'name'):
                input.name = '  Gamma'
            input = node_tree1.inputs.new('NodeSocketFloat', '  Hue / Sat Value')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 1.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 2.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = '  Hue / Sat Value'
            input = node_tree1.inputs.new('NodeSocketFloat', '    Hue')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.49999991059303284
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = '    Hue'
            input = node_tree1.inputs.new('NodeSocketFloat', '    Saturation')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 1.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 2.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = '    Saturation'
            input = node_tree1.inputs.new('NodeSocketFloat', 'BRIGHTNESS')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.0
            if hasattr(input, 'hide_value'):
                input.hide_value = True
            if hasattr(input, 'max_value'):
                input.max_value = 3.4028234663852886e+38
            if hasattr(input, 'min_value'):
                input.min_value = -3.4028234663852886e+38
            if hasattr(input, 'name'):
                input.name = 'BRIGHTNESS'
            input = node_tree1.inputs.new('NodeSocketFloat', '  Glowing Level')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 1.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 3.4028234663852886e+38
            if hasattr(input, 'min_value'):
                input.min_value = -3.4028234663852886e+38
            if hasattr(input, 'name'):
                input.name = '  Glowing Level'
            input = node_tree1.inputs.new('NodeSocketFloat', '  Brightness')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.0
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 100.0
            if hasattr(input, 'min_value'):
                input.min_value = -100.0
            if hasattr(input, 'name'):
                input.name = '  Brightness'
            input = node_tree1.inputs.new('NodeSocketFloat', '  Dark / Bright Threshold')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 2.5
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 10000.0
            if hasattr(input, 'min_value'):
                input.min_value = -10000.0
            if hasattr(input, 'name'):
                input.name = '  Dark / Bright Threshold'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', '    Dark Spot Intensity')
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
                input.name = '    Dark Spot Intensity'
            input = node_tree1.inputs.new('NodeSocketFloatFactor', '    Bright Spot Intensity')
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
                input.name = '    Bright Spot Intensity'
            input = node_tree1.inputs.new('NodeSocketFloat', 'Blend')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.10000000149011612
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 1.0
            if hasattr(input, 'min_value'):
                input.min_value = 0.0
            if hasattr(input, 'name'):
                input.name = 'Blend'
            input = node_tree1.inputs.new('NodeSocketFloat', 'Roughness')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.47999998927116394
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 10000.0
            if hasattr(input, 'min_value'):
                input.min_value = -10000.0
            if hasattr(input, 'name'):
                input.name = 'Roughness'
            input = node_tree1.inputs.new('NodeSocketFloat', 'Falloff Strength')
            if hasattr(input, 'attribute_domain'):
                input.attribute_domain = 'POINT'
            if hasattr(input, 'default_value'):
                input.default_value = 0.125
            if hasattr(input, 'hide_value'):
                input.hide_value = False
            if hasattr(input, 'max_value'):
                input.max_value = 10000.0
            if hasattr(input, 'min_value'):
                input.min_value = -10000.0
            if hasattr(input, 'name'):
                input.name = 'Falloff Strength'
            # OUTPUTS
            output = node_tree1.outputs.new('NodeSocketShader', 'Shader')
            if hasattr(output, 'attribute_domain'):
                output.attribute_domain = 'POINT'
            if hasattr(output, 'hide_value'):
                output.hide_value = False
            if hasattr(output, 'name'):
                output.name = 'Shader'
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
                author_1.location = (-90.0, -147.0)
            if hasattr(author_1, 'mute'):
                author_1.mute = False
            if hasattr(author_1, 'name'):
                author_1.name = 'Author'
            if hasattr(author_1, 'shrink'):
                author_1.shrink = True
            if hasattr(author_1, 'use_custom_color'):
                author_1.use_custom_color = True
            if hasattr(author_1, 'width'):
                author_1.width = 290.4298095703125

            group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
            if hasattr(group_output_1, 'color'):
                group_output_1.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
            if hasattr(group_output_1, 'hide'):
                group_output_1.hide = False
            if hasattr(group_output_1, 'is_active_output'):
                group_output_1.is_active_output = True
            if hasattr(group_output_1, 'location'):
                group_output_1.location = (0.0, 0.0)
            if hasattr(group_output_1, 'mute'):
                group_output_1.mute = False
            if hasattr(group_output_1, 'name'):
                group_output_1.name = 'Group Output'
            if hasattr(group_output_1, 'use_custom_color'):
                group_output_1.use_custom_color = True
            if hasattr(group_output_1, 'width'):
                group_output_1.width = 140.0

            group_input_002_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_002_1, 'color'):
                group_input_002_1.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
            if hasattr(group_input_002_1, 'hide'):
                group_input_002_1.hide = False
            if hasattr(group_input_002_1, 'location'):
                group_input_002_1.location = (-1120.0, 0.0)
            if hasattr(group_input_002_1, 'mute'):
                group_input_002_1.mute = False
            if hasattr(group_input_002_1, 'name'):
                group_input_002_1.name = 'Group Input.002'
            if hasattr(group_input_002_1, 'use_custom_color'):
                group_input_002_1.use_custom_color = True
            if hasattr(group_input_002_1, 'width'):
                group_input_002_1.width = 140.0
            if hasattr(group_input_002_1.outputs[0], 'default_value'):
                group_input_002_1.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_002_1.outputs[0], 'display_shape'):
                group_input_002_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[0], 'enabled'):
                group_input_002_1.outputs[0].enabled = True
            if hasattr(group_input_002_1.outputs[0], 'hide'):
                group_input_002_1.outputs[0].hide = True
            if hasattr(group_input_002_1.outputs[0], 'hide_value'):
                group_input_002_1.outputs[0].hide_value = False
            if hasattr(group_input_002_1.outputs[0], 'name'):
                group_input_002_1.outputs[0].name = 'Base Color'
            if hasattr(group_input_002_1.outputs[0], 'show_expanded'):
                group_input_002_1.outputs[0].show_expanded = False
            if hasattr(group_input_002_1.outputs[1], 'default_value'):
                group_input_002_1.outputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_002_1.outputs[1], 'display_shape'):
                group_input_002_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[1], 'enabled'):
                group_input_002_1.outputs[1].enabled = True
            if hasattr(group_input_002_1.outputs[1], 'hide'):
                group_input_002_1.outputs[1].hide = True
            if hasattr(group_input_002_1.outputs[1], 'hide_value'):
                group_input_002_1.outputs[1].hide_value = False
            if hasattr(group_input_002_1.outputs[1], 'name'):
                group_input_002_1.outputs[1].name = 'Transparent Color'
            if hasattr(group_input_002_1.outputs[1], 'show_expanded'):
                group_input_002_1.outputs[1].show_expanded = False
            if hasattr(group_input_002_1.outputs[2], 'default_value'):
                group_input_002_1.outputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_002_1.outputs[2], 'display_shape'):
                group_input_002_1.outputs[2].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[2], 'enabled'):
                group_input_002_1.outputs[2].enabled = True
            if hasattr(group_input_002_1.outputs[2], 'hide'):
                group_input_002_1.outputs[2].hide = True
            if hasattr(group_input_002_1.outputs[2], 'hide_value'):
                group_input_002_1.outputs[2].hide_value = False
            if hasattr(group_input_002_1.outputs[2], 'name'):
                group_input_002_1.outputs[2].name = 'Reflection Color'
            if hasattr(group_input_002_1.outputs[2], 'show_expanded'):
                group_input_002_1.outputs[2].show_expanded = False
            if hasattr(group_input_002_1.outputs[3], 'default_value'):
                group_input_002_1.outputs[3].default_value = 0.25
            if hasattr(group_input_002_1.outputs[3], 'display_shape'):
                group_input_002_1.outputs[3].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[3], 'enabled'):
                group_input_002_1.outputs[3].enabled = True
            if hasattr(group_input_002_1.outputs[3], 'hide'):
                group_input_002_1.outputs[3].hide = True
            if hasattr(group_input_002_1.outputs[3], 'hide_value'):
                group_input_002_1.outputs[3].hide_value = False
            if hasattr(group_input_002_1.outputs[3], 'name'):
                group_input_002_1.outputs[3].name = 'Reflection Factor'
            if hasattr(group_input_002_1.outputs[3], 'show_expanded'):
                group_input_002_1.outputs[3].show_expanded = False
            if hasattr(group_input_002_1.outputs[4], 'default_value'):
                group_input_002_1.outputs[4].default_value = 0.0
            if hasattr(group_input_002_1.outputs[4], 'display_shape'):
                group_input_002_1.outputs[4].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[4], 'enabled'):
                group_input_002_1.outputs[4].enabled = True
            if hasattr(group_input_002_1.outputs[4], 'hide'):
                group_input_002_1.outputs[4].hide = True
            if hasattr(group_input_002_1.outputs[4], 'hide_value'):
                group_input_002_1.outputs[4].hide_value = True
            if hasattr(group_input_002_1.outputs[4], 'name'):
                group_input_002_1.outputs[4].name = 'COLOR VARIATION'
            if hasattr(group_input_002_1.outputs[4], 'show_expanded'):
                group_input_002_1.outputs[4].show_expanded = False
            if hasattr(group_input_002_1.outputs[5], 'default_value'):
                group_input_002_1.outputs[5].default_value = 6.5
            if hasattr(group_input_002_1.outputs[5], 'display_shape'):
                group_input_002_1.outputs[5].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[5], 'enabled'):
                group_input_002_1.outputs[5].enabled = True
            if hasattr(group_input_002_1.outputs[5], 'hide'):
                group_input_002_1.outputs[5].hide = True
            if hasattr(group_input_002_1.outputs[5], 'hide_value'):
                group_input_002_1.outputs[5].hide_value = False
            if hasattr(group_input_002_1.outputs[5], 'name'):
                group_input_002_1.outputs[5].name = '  Color Variation Scale'
            if hasattr(group_input_002_1.outputs[5], 'show_expanded'):
                group_input_002_1.outputs[5].show_expanded = False
            if hasattr(group_input_002_1.outputs[6], 'default_value'):
                group_input_002_1.outputs[6].default_value = 0.15000000596046448
            if hasattr(group_input_002_1.outputs[6], 'display_shape'):
                group_input_002_1.outputs[6].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[6], 'enabled'):
                group_input_002_1.outputs[6].enabled = True
            if hasattr(group_input_002_1.outputs[6], 'hide'):
                group_input_002_1.outputs[6].hide = True
            if hasattr(group_input_002_1.outputs[6], 'hide_value'):
                group_input_002_1.outputs[6].hide_value = False
            if hasattr(group_input_002_1.outputs[6], 'name'):
                group_input_002_1.outputs[6].name = '  Color Variation Distortion'
            if hasattr(group_input_002_1.outputs[6], 'show_expanded'):
                group_input_002_1.outputs[6].show_expanded = False
            if hasattr(group_input_002_1.outputs[7], 'default_value'):
                group_input_002_1.outputs[7].default_value = 0.7749999761581421
            if hasattr(group_input_002_1.outputs[7], 'display_shape'):
                group_input_002_1.outputs[7].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[7], 'enabled'):
                group_input_002_1.outputs[7].enabled = True
            if hasattr(group_input_002_1.outputs[7], 'hide'):
                group_input_002_1.outputs[7].hide = True
            if hasattr(group_input_002_1.outputs[7], 'hide_value'):
                group_input_002_1.outputs[7].hide_value = False
            if hasattr(group_input_002_1.outputs[7], 'name'):
                group_input_002_1.outputs[7].name = '  Random Color Var'
            if hasattr(group_input_002_1.outputs[7], 'show_expanded'):
                group_input_002_1.outputs[7].show_expanded = False
            if hasattr(group_input_002_1.outputs[8], 'default_value'):
                group_input_002_1.outputs[8].default_value = 0.0
            if hasattr(group_input_002_1.outputs[8], 'display_shape'):
                group_input_002_1.outputs[8].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[8], 'enabled'):
                group_input_002_1.outputs[8].enabled = True
            if hasattr(group_input_002_1.outputs[8], 'hide'):
                group_input_002_1.outputs[8].hide = True
            if hasattr(group_input_002_1.outputs[8], 'hide_value'):
                group_input_002_1.outputs[8].hide_value = True
            if hasattr(group_input_002_1.outputs[8], 'name'):
                group_input_002_1.outputs[8].name = 'COLOR ADJUSTMENTS'
            if hasattr(group_input_002_1.outputs[8], 'show_expanded'):
                group_input_002_1.outputs[8].show_expanded = False
            if hasattr(group_input_002_1.outputs[9], 'default_value'):
                group_input_002_1.outputs[9].default_value = 0.0
            if hasattr(group_input_002_1.outputs[9], 'display_shape'):
                group_input_002_1.outputs[9].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[9], 'enabled'):
                group_input_002_1.outputs[9].enabled = True
            if hasattr(group_input_002_1.outputs[9], 'hide'):
                group_input_002_1.outputs[9].hide = True
            if hasattr(group_input_002_1.outputs[9], 'hide_value'):
                group_input_002_1.outputs[9].hide_value = False
            if hasattr(group_input_002_1.outputs[9], 'name'):
                group_input_002_1.outputs[9].name = '  Unpaint'
            if hasattr(group_input_002_1.outputs[9], 'show_expanded'):
                group_input_002_1.outputs[9].show_expanded = False
            if hasattr(group_input_002_1.outputs[10], 'default_value'):
                group_input_002_1.outputs[10].default_value = 0.0
            if hasattr(group_input_002_1.outputs[10], 'display_shape'):
                group_input_002_1.outputs[10].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[10], 'enabled'):
                group_input_002_1.outputs[10].enabled = True
            if hasattr(group_input_002_1.outputs[10], 'hide'):
                group_input_002_1.outputs[10].hide = True
            if hasattr(group_input_002_1.outputs[10], 'hide_value'):
                group_input_002_1.outputs[10].hide_value = False
            if hasattr(group_input_002_1.outputs[10], 'name'):
                group_input_002_1.outputs[10].name = '  Color Inverter'
            if hasattr(group_input_002_1.outputs[10], 'show_expanded'):
                group_input_002_1.outputs[10].show_expanded = False
            if hasattr(group_input_002_1.outputs[11], 'default_value'):
                group_input_002_1.outputs[11].default_value = 0.0
            if hasattr(group_input_002_1.outputs[11], 'display_shape'):
                group_input_002_1.outputs[11].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[11], 'enabled'):
                group_input_002_1.outputs[11].enabled = True
            if hasattr(group_input_002_1.outputs[11], 'hide'):
                group_input_002_1.outputs[11].hide = True
            if hasattr(group_input_002_1.outputs[11], 'hide_value'):
                group_input_002_1.outputs[11].hide_value = False
            if hasattr(group_input_002_1.outputs[11], 'name'):
                group_input_002_1.outputs[11].name = '  Contrast'
            if hasattr(group_input_002_1.outputs[11], 'show_expanded'):
                group_input_002_1.outputs[11].show_expanded = False
            if hasattr(group_input_002_1.outputs[12], 'default_value'):
                group_input_002_1.outputs[12].default_value = 1.0
            if hasattr(group_input_002_1.outputs[12], 'display_shape'):
                group_input_002_1.outputs[12].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[12], 'enabled'):
                group_input_002_1.outputs[12].enabled = True
            if hasattr(group_input_002_1.outputs[12], 'hide'):
                group_input_002_1.outputs[12].hide = True
            if hasattr(group_input_002_1.outputs[12], 'hide_value'):
                group_input_002_1.outputs[12].hide_value = False
            if hasattr(group_input_002_1.outputs[12], 'name'):
                group_input_002_1.outputs[12].name = '  Gamma'
            if hasattr(group_input_002_1.outputs[12], 'show_expanded'):
                group_input_002_1.outputs[12].show_expanded = False
            if hasattr(group_input_002_1.outputs[13], 'default_value'):
                group_input_002_1.outputs[13].default_value = 1.0
            if hasattr(group_input_002_1.outputs[13], 'display_shape'):
                group_input_002_1.outputs[13].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[13], 'enabled'):
                group_input_002_1.outputs[13].enabled = True
            if hasattr(group_input_002_1.outputs[13], 'hide'):
                group_input_002_1.outputs[13].hide = True
            if hasattr(group_input_002_1.outputs[13], 'hide_value'):
                group_input_002_1.outputs[13].hide_value = False
            if hasattr(group_input_002_1.outputs[13], 'name'):
                group_input_002_1.outputs[13].name = '  Hue / Sat Value'
            if hasattr(group_input_002_1.outputs[13], 'show_expanded'):
                group_input_002_1.outputs[13].show_expanded = False
            if hasattr(group_input_002_1.outputs[14], 'default_value'):
                group_input_002_1.outputs[14].default_value = 0.49999991059303284
            if hasattr(group_input_002_1.outputs[14], 'display_shape'):
                group_input_002_1.outputs[14].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[14], 'enabled'):
                group_input_002_1.outputs[14].enabled = True
            if hasattr(group_input_002_1.outputs[14], 'hide'):
                group_input_002_1.outputs[14].hide = True
            if hasattr(group_input_002_1.outputs[14], 'hide_value'):
                group_input_002_1.outputs[14].hide_value = False
            if hasattr(group_input_002_1.outputs[14], 'name'):
                group_input_002_1.outputs[14].name = '    Hue'
            if hasattr(group_input_002_1.outputs[14], 'show_expanded'):
                group_input_002_1.outputs[14].show_expanded = False
            if hasattr(group_input_002_1.outputs[15], 'default_value'):
                group_input_002_1.outputs[15].default_value = 1.0
            if hasattr(group_input_002_1.outputs[15], 'display_shape'):
                group_input_002_1.outputs[15].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[15], 'enabled'):
                group_input_002_1.outputs[15].enabled = True
            if hasattr(group_input_002_1.outputs[15], 'hide'):
                group_input_002_1.outputs[15].hide = True
            if hasattr(group_input_002_1.outputs[15], 'hide_value'):
                group_input_002_1.outputs[15].hide_value = False
            if hasattr(group_input_002_1.outputs[15], 'name'):
                group_input_002_1.outputs[15].name = '    Saturation'
            if hasattr(group_input_002_1.outputs[15], 'show_expanded'):
                group_input_002_1.outputs[15].show_expanded = False
            if hasattr(group_input_002_1.outputs[16], 'default_value'):
                group_input_002_1.outputs[16].default_value = 0.0
            if hasattr(group_input_002_1.outputs[16], 'display_shape'):
                group_input_002_1.outputs[16].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[16], 'enabled'):
                group_input_002_1.outputs[16].enabled = True
            if hasattr(group_input_002_1.outputs[16], 'hide'):
                group_input_002_1.outputs[16].hide = True
            if hasattr(group_input_002_1.outputs[16], 'hide_value'):
                group_input_002_1.outputs[16].hide_value = True
            if hasattr(group_input_002_1.outputs[16], 'name'):
                group_input_002_1.outputs[16].name = 'BRIGHTNESS'
            if hasattr(group_input_002_1.outputs[16], 'show_expanded'):
                group_input_002_1.outputs[16].show_expanded = False
            if hasattr(group_input_002_1.outputs[17], 'default_value'):
                group_input_002_1.outputs[17].default_value = 1.0
            if hasattr(group_input_002_1.outputs[17], 'display_shape'):
                group_input_002_1.outputs[17].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[17], 'enabled'):
                group_input_002_1.outputs[17].enabled = True
            if hasattr(group_input_002_1.outputs[17], 'hide'):
                group_input_002_1.outputs[17].hide = True
            if hasattr(group_input_002_1.outputs[17], 'hide_value'):
                group_input_002_1.outputs[17].hide_value = False
            if hasattr(group_input_002_1.outputs[17], 'name'):
                group_input_002_1.outputs[17].name = '  Glowing Level'
            if hasattr(group_input_002_1.outputs[17], 'show_expanded'):
                group_input_002_1.outputs[17].show_expanded = False
            if hasattr(group_input_002_1.outputs[18], 'default_value'):
                group_input_002_1.outputs[18].default_value = 0.0
            if hasattr(group_input_002_1.outputs[18], 'display_shape'):
                group_input_002_1.outputs[18].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[18], 'enabled'):
                group_input_002_1.outputs[18].enabled = True
            if hasattr(group_input_002_1.outputs[18], 'hide'):
                group_input_002_1.outputs[18].hide = True
            if hasattr(group_input_002_1.outputs[18], 'hide_value'):
                group_input_002_1.outputs[18].hide_value = False
            if hasattr(group_input_002_1.outputs[18], 'name'):
                group_input_002_1.outputs[18].name = '  Brightness'
            if hasattr(group_input_002_1.outputs[18], 'show_expanded'):
                group_input_002_1.outputs[18].show_expanded = False
            if hasattr(group_input_002_1.outputs[19], 'default_value'):
                group_input_002_1.outputs[19].default_value = 2.5
            if hasattr(group_input_002_1.outputs[19], 'display_shape'):
                group_input_002_1.outputs[19].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[19], 'enabled'):
                group_input_002_1.outputs[19].enabled = True
            if hasattr(group_input_002_1.outputs[19], 'hide'):
                group_input_002_1.outputs[19].hide = True
            if hasattr(group_input_002_1.outputs[19], 'hide_value'):
                group_input_002_1.outputs[19].hide_value = False
            if hasattr(group_input_002_1.outputs[19], 'name'):
                group_input_002_1.outputs[19].name = '  Dark / Bright Threshold'
            if hasattr(group_input_002_1.outputs[19], 'show_expanded'):
                group_input_002_1.outputs[19].show_expanded = False
            if hasattr(group_input_002_1.outputs[20], 'default_value'):
                group_input_002_1.outputs[20].default_value = 0.0
            if hasattr(group_input_002_1.outputs[20], 'display_shape'):
                group_input_002_1.outputs[20].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[20], 'enabled'):
                group_input_002_1.outputs[20].enabled = True
            if hasattr(group_input_002_1.outputs[20], 'hide'):
                group_input_002_1.outputs[20].hide = True
            if hasattr(group_input_002_1.outputs[20], 'hide_value'):
                group_input_002_1.outputs[20].hide_value = False
            if hasattr(group_input_002_1.outputs[20], 'name'):
                group_input_002_1.outputs[20].name = '    Dark Spot Intensity'
            if hasattr(group_input_002_1.outputs[20], 'show_expanded'):
                group_input_002_1.outputs[20].show_expanded = False
            if hasattr(group_input_002_1.outputs[21], 'default_value'):
                group_input_002_1.outputs[21].default_value = 0.0
            if hasattr(group_input_002_1.outputs[21], 'display_shape'):
                group_input_002_1.outputs[21].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[21], 'enabled'):
                group_input_002_1.outputs[21].enabled = True
            if hasattr(group_input_002_1.outputs[21], 'hide'):
                group_input_002_1.outputs[21].hide = True
            if hasattr(group_input_002_1.outputs[21], 'hide_value'):
                group_input_002_1.outputs[21].hide_value = False
            if hasattr(group_input_002_1.outputs[21], 'name'):
                group_input_002_1.outputs[21].name = '    Bright Spot Intensity'
            if hasattr(group_input_002_1.outputs[21], 'show_expanded'):
                group_input_002_1.outputs[21].show_expanded = False
            if hasattr(group_input_002_1.outputs[22], 'default_value'):
                group_input_002_1.outputs[22].default_value = 0.10000000149011612
            if hasattr(group_input_002_1.outputs[22], 'display_shape'):
                group_input_002_1.outputs[22].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[22], 'enabled'):
                group_input_002_1.outputs[22].enabled = True
            if hasattr(group_input_002_1.outputs[22], 'hide'):
                group_input_002_1.outputs[22].hide = True
            if hasattr(group_input_002_1.outputs[22], 'hide_value'):
                group_input_002_1.outputs[22].hide_value = False
            if hasattr(group_input_002_1.outputs[22], 'name'):
                group_input_002_1.outputs[22].name = 'Blend'
            if hasattr(group_input_002_1.outputs[22], 'show_expanded'):
                group_input_002_1.outputs[22].show_expanded = False
            if hasattr(group_input_002_1.outputs[23], 'default_value'):
                group_input_002_1.outputs[23].default_value = 0.47999998927116394
            if hasattr(group_input_002_1.outputs[23], 'display_shape'):
                group_input_002_1.outputs[23].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[23], 'enabled'):
                group_input_002_1.outputs[23].enabled = True
            if hasattr(group_input_002_1.outputs[23], 'hide'):
                group_input_002_1.outputs[23].hide = False
            if hasattr(group_input_002_1.outputs[23], 'hide_value'):
                group_input_002_1.outputs[23].hide_value = False
            if hasattr(group_input_002_1.outputs[23], 'name'):
                group_input_002_1.outputs[23].name = 'Roughness'
            if hasattr(group_input_002_1.outputs[23], 'show_expanded'):
                group_input_002_1.outputs[23].show_expanded = False
            if hasattr(group_input_002_1.outputs[24], 'default_value'):
                group_input_002_1.outputs[24].default_value = 0.125
            if hasattr(group_input_002_1.outputs[24], 'display_shape'):
                group_input_002_1.outputs[24].display_shape = 'CIRCLE'
            if hasattr(group_input_002_1.outputs[24], 'enabled'):
                group_input_002_1.outputs[24].enabled = True
            if hasattr(group_input_002_1.outputs[24], 'hide'):
                group_input_002_1.outputs[24].hide = False
            if hasattr(group_input_002_1.outputs[24], 'hide_value'):
                group_input_002_1.outputs[24].hide_value = False
            if hasattr(group_input_002_1.outputs[24], 'name'):
                group_input_002_1.outputs[24].name = 'Falloff Strength'
            if hasattr(group_input_002_1.outputs[24], 'show_expanded'):
                group_input_002_1.outputs[24].show_expanded = False

            group_input_004_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_004_1, 'color'):
                group_input_004_1.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
            if hasattr(group_input_004_1, 'hide'):
                group_input_004_1.hide = False
            if hasattr(group_input_004_1, 'location'):
                group_input_004_1.location = (-320.0, -134.0)
            if hasattr(group_input_004_1, 'mute'):
                group_input_004_1.mute = False
            if hasattr(group_input_004_1, 'name'):
                group_input_004_1.name = 'Group Input.004'
            if hasattr(group_input_004_1, 'use_custom_color'):
                group_input_004_1.use_custom_color = True
            if hasattr(group_input_004_1, 'width'):
                group_input_004_1.width = 140.0
            if hasattr(group_input_004_1.outputs[0], 'default_value'):
                group_input_004_1.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_004_1.outputs[0], 'display_shape'):
                group_input_004_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[0], 'enabled'):
                group_input_004_1.outputs[0].enabled = True
            if hasattr(group_input_004_1.outputs[0], 'hide'):
                group_input_004_1.outputs[0].hide = True
            if hasattr(group_input_004_1.outputs[0], 'hide_value'):
                group_input_004_1.outputs[0].hide_value = False
            if hasattr(group_input_004_1.outputs[0], 'name'):
                group_input_004_1.outputs[0].name = 'Base Color'
            if hasattr(group_input_004_1.outputs[0], 'show_expanded'):
                group_input_004_1.outputs[0].show_expanded = False
            if hasattr(group_input_004_1.outputs[1], 'default_value'):
                group_input_004_1.outputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_004_1.outputs[1], 'display_shape'):
                group_input_004_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[1], 'enabled'):
                group_input_004_1.outputs[1].enabled = True
            if hasattr(group_input_004_1.outputs[1], 'hide'):
                group_input_004_1.outputs[1].hide = True
            if hasattr(group_input_004_1.outputs[1], 'hide_value'):
                group_input_004_1.outputs[1].hide_value = False
            if hasattr(group_input_004_1.outputs[1], 'name'):
                group_input_004_1.outputs[1].name = 'Transparent Color'
            if hasattr(group_input_004_1.outputs[1], 'show_expanded'):
                group_input_004_1.outputs[1].show_expanded = False
            if hasattr(group_input_004_1.outputs[2], 'default_value'):
                group_input_004_1.outputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_004_1.outputs[2], 'display_shape'):
                group_input_004_1.outputs[2].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[2], 'enabled'):
                group_input_004_1.outputs[2].enabled = True
            if hasattr(group_input_004_1.outputs[2], 'hide'):
                group_input_004_1.outputs[2].hide = False
            if hasattr(group_input_004_1.outputs[2], 'hide_value'):
                group_input_004_1.outputs[2].hide_value = False
            if hasattr(group_input_004_1.outputs[2], 'name'):
                group_input_004_1.outputs[2].name = 'Reflection Color'
            if hasattr(group_input_004_1.outputs[2], 'show_expanded'):
                group_input_004_1.outputs[2].show_expanded = False
            if hasattr(group_input_004_1.outputs[3], 'default_value'):
                group_input_004_1.outputs[3].default_value = 0.25
            if hasattr(group_input_004_1.outputs[3], 'display_shape'):
                group_input_004_1.outputs[3].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[3], 'enabled'):
                group_input_004_1.outputs[3].enabled = True
            if hasattr(group_input_004_1.outputs[3], 'hide'):
                group_input_004_1.outputs[3].hide = False
            if hasattr(group_input_004_1.outputs[3], 'hide_value'):
                group_input_004_1.outputs[3].hide_value = False
            if hasattr(group_input_004_1.outputs[3], 'name'):
                group_input_004_1.outputs[3].name = 'Reflection Factor'
            if hasattr(group_input_004_1.outputs[3], 'show_expanded'):
                group_input_004_1.outputs[3].show_expanded = False
            if hasattr(group_input_004_1.outputs[4], 'default_value'):
                group_input_004_1.outputs[4].default_value = 0.0
            if hasattr(group_input_004_1.outputs[4], 'display_shape'):
                group_input_004_1.outputs[4].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[4], 'enabled'):
                group_input_004_1.outputs[4].enabled = True
            if hasattr(group_input_004_1.outputs[4], 'hide'):
                group_input_004_1.outputs[4].hide = True
            if hasattr(group_input_004_1.outputs[4], 'hide_value'):
                group_input_004_1.outputs[4].hide_value = True
            if hasattr(group_input_004_1.outputs[4], 'name'):
                group_input_004_1.outputs[4].name = 'COLOR VARIATION'
            if hasattr(group_input_004_1.outputs[4], 'show_expanded'):
                group_input_004_1.outputs[4].show_expanded = False
            if hasattr(group_input_004_1.outputs[5], 'default_value'):
                group_input_004_1.outputs[5].default_value = 6.5
            if hasattr(group_input_004_1.outputs[5], 'display_shape'):
                group_input_004_1.outputs[5].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[5], 'enabled'):
                group_input_004_1.outputs[5].enabled = True
            if hasattr(group_input_004_1.outputs[5], 'hide'):
                group_input_004_1.outputs[5].hide = True
            if hasattr(group_input_004_1.outputs[5], 'hide_value'):
                group_input_004_1.outputs[5].hide_value = False
            if hasattr(group_input_004_1.outputs[5], 'name'):
                group_input_004_1.outputs[5].name = '  Color Variation Scale'
            if hasattr(group_input_004_1.outputs[5], 'show_expanded'):
                group_input_004_1.outputs[5].show_expanded = False
            if hasattr(group_input_004_1.outputs[6], 'default_value'):
                group_input_004_1.outputs[6].default_value = 0.15000000596046448
            if hasattr(group_input_004_1.outputs[6], 'display_shape'):
                group_input_004_1.outputs[6].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[6], 'enabled'):
                group_input_004_1.outputs[6].enabled = True
            if hasattr(group_input_004_1.outputs[6], 'hide'):
                group_input_004_1.outputs[6].hide = True
            if hasattr(group_input_004_1.outputs[6], 'hide_value'):
                group_input_004_1.outputs[6].hide_value = False
            if hasattr(group_input_004_1.outputs[6], 'name'):
                group_input_004_1.outputs[6].name = '  Color Variation Distortion'
            if hasattr(group_input_004_1.outputs[6], 'show_expanded'):
                group_input_004_1.outputs[6].show_expanded = False
            if hasattr(group_input_004_1.outputs[7], 'default_value'):
                group_input_004_1.outputs[7].default_value = 0.7749999761581421
            if hasattr(group_input_004_1.outputs[7], 'display_shape'):
                group_input_004_1.outputs[7].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[7], 'enabled'):
                group_input_004_1.outputs[7].enabled = True
            if hasattr(group_input_004_1.outputs[7], 'hide'):
                group_input_004_1.outputs[7].hide = True
            if hasattr(group_input_004_1.outputs[7], 'hide_value'):
                group_input_004_1.outputs[7].hide_value = False
            if hasattr(group_input_004_1.outputs[7], 'name'):
                group_input_004_1.outputs[7].name = '  Random Color Var'
            if hasattr(group_input_004_1.outputs[7], 'show_expanded'):
                group_input_004_1.outputs[7].show_expanded = False
            if hasattr(group_input_004_1.outputs[8], 'default_value'):
                group_input_004_1.outputs[8].default_value = 0.0
            if hasattr(group_input_004_1.outputs[8], 'display_shape'):
                group_input_004_1.outputs[8].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[8], 'enabled'):
                group_input_004_1.outputs[8].enabled = True
            if hasattr(group_input_004_1.outputs[8], 'hide'):
                group_input_004_1.outputs[8].hide = True
            if hasattr(group_input_004_1.outputs[8], 'hide_value'):
                group_input_004_1.outputs[8].hide_value = True
            if hasattr(group_input_004_1.outputs[8], 'name'):
                group_input_004_1.outputs[8].name = 'COLOR ADJUSTMENTS'
            if hasattr(group_input_004_1.outputs[8], 'show_expanded'):
                group_input_004_1.outputs[8].show_expanded = False
            if hasattr(group_input_004_1.outputs[9], 'default_value'):
                group_input_004_1.outputs[9].default_value = 0.0
            if hasattr(group_input_004_1.outputs[9], 'display_shape'):
                group_input_004_1.outputs[9].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[9], 'enabled'):
                group_input_004_1.outputs[9].enabled = True
            if hasattr(group_input_004_1.outputs[9], 'hide'):
                group_input_004_1.outputs[9].hide = True
            if hasattr(group_input_004_1.outputs[9], 'hide_value'):
                group_input_004_1.outputs[9].hide_value = False
            if hasattr(group_input_004_1.outputs[9], 'name'):
                group_input_004_1.outputs[9].name = '  Unpaint'
            if hasattr(group_input_004_1.outputs[9], 'show_expanded'):
                group_input_004_1.outputs[9].show_expanded = False
            if hasattr(group_input_004_1.outputs[10], 'default_value'):
                group_input_004_1.outputs[10].default_value = 0.0
            if hasattr(group_input_004_1.outputs[10], 'display_shape'):
                group_input_004_1.outputs[10].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[10], 'enabled'):
                group_input_004_1.outputs[10].enabled = True
            if hasattr(group_input_004_1.outputs[10], 'hide'):
                group_input_004_1.outputs[10].hide = True
            if hasattr(group_input_004_1.outputs[10], 'hide_value'):
                group_input_004_1.outputs[10].hide_value = False
            if hasattr(group_input_004_1.outputs[10], 'name'):
                group_input_004_1.outputs[10].name = '  Color Inverter'
            if hasattr(group_input_004_1.outputs[10], 'show_expanded'):
                group_input_004_1.outputs[10].show_expanded = False
            if hasattr(group_input_004_1.outputs[11], 'default_value'):
                group_input_004_1.outputs[11].default_value = 0.0
            if hasattr(group_input_004_1.outputs[11], 'display_shape'):
                group_input_004_1.outputs[11].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[11], 'enabled'):
                group_input_004_1.outputs[11].enabled = True
            if hasattr(group_input_004_1.outputs[11], 'hide'):
                group_input_004_1.outputs[11].hide = True
            if hasattr(group_input_004_1.outputs[11], 'hide_value'):
                group_input_004_1.outputs[11].hide_value = False
            if hasattr(group_input_004_1.outputs[11], 'name'):
                group_input_004_1.outputs[11].name = '  Contrast'
            if hasattr(group_input_004_1.outputs[11], 'show_expanded'):
                group_input_004_1.outputs[11].show_expanded = False
            if hasattr(group_input_004_1.outputs[12], 'default_value'):
                group_input_004_1.outputs[12].default_value = 1.0
            if hasattr(group_input_004_1.outputs[12], 'display_shape'):
                group_input_004_1.outputs[12].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[12], 'enabled'):
                group_input_004_1.outputs[12].enabled = True
            if hasattr(group_input_004_1.outputs[12], 'hide'):
                group_input_004_1.outputs[12].hide = True
            if hasattr(group_input_004_1.outputs[12], 'hide_value'):
                group_input_004_1.outputs[12].hide_value = False
            if hasattr(group_input_004_1.outputs[12], 'name'):
                group_input_004_1.outputs[12].name = '  Gamma'
            if hasattr(group_input_004_1.outputs[12], 'show_expanded'):
                group_input_004_1.outputs[12].show_expanded = False
            if hasattr(group_input_004_1.outputs[13], 'default_value'):
                group_input_004_1.outputs[13].default_value = 1.0
            if hasattr(group_input_004_1.outputs[13], 'display_shape'):
                group_input_004_1.outputs[13].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[13], 'enabled'):
                group_input_004_1.outputs[13].enabled = True
            if hasattr(group_input_004_1.outputs[13], 'hide'):
                group_input_004_1.outputs[13].hide = True
            if hasattr(group_input_004_1.outputs[13], 'hide_value'):
                group_input_004_1.outputs[13].hide_value = False
            if hasattr(group_input_004_1.outputs[13], 'name'):
                group_input_004_1.outputs[13].name = '  Hue / Sat Value'
            if hasattr(group_input_004_1.outputs[13], 'show_expanded'):
                group_input_004_1.outputs[13].show_expanded = False
            if hasattr(group_input_004_1.outputs[14], 'default_value'):
                group_input_004_1.outputs[14].default_value = 0.49999991059303284
            if hasattr(group_input_004_1.outputs[14], 'display_shape'):
                group_input_004_1.outputs[14].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[14], 'enabled'):
                group_input_004_1.outputs[14].enabled = True
            if hasattr(group_input_004_1.outputs[14], 'hide'):
                group_input_004_1.outputs[14].hide = True
            if hasattr(group_input_004_1.outputs[14], 'hide_value'):
                group_input_004_1.outputs[14].hide_value = False
            if hasattr(group_input_004_1.outputs[14], 'name'):
                group_input_004_1.outputs[14].name = '    Hue'
            if hasattr(group_input_004_1.outputs[14], 'show_expanded'):
                group_input_004_1.outputs[14].show_expanded = False
            if hasattr(group_input_004_1.outputs[15], 'default_value'):
                group_input_004_1.outputs[15].default_value = 1.0
            if hasattr(group_input_004_1.outputs[15], 'display_shape'):
                group_input_004_1.outputs[15].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[15], 'enabled'):
                group_input_004_1.outputs[15].enabled = True
            if hasattr(group_input_004_1.outputs[15], 'hide'):
                group_input_004_1.outputs[15].hide = True
            if hasattr(group_input_004_1.outputs[15], 'hide_value'):
                group_input_004_1.outputs[15].hide_value = False
            if hasattr(group_input_004_1.outputs[15], 'name'):
                group_input_004_1.outputs[15].name = '    Saturation'
            if hasattr(group_input_004_1.outputs[15], 'show_expanded'):
                group_input_004_1.outputs[15].show_expanded = False
            if hasattr(group_input_004_1.outputs[16], 'default_value'):
                group_input_004_1.outputs[16].default_value = 0.0
            if hasattr(group_input_004_1.outputs[16], 'display_shape'):
                group_input_004_1.outputs[16].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[16], 'enabled'):
                group_input_004_1.outputs[16].enabled = True
            if hasattr(group_input_004_1.outputs[16], 'hide'):
                group_input_004_1.outputs[16].hide = True
            if hasattr(group_input_004_1.outputs[16], 'hide_value'):
                group_input_004_1.outputs[16].hide_value = True
            if hasattr(group_input_004_1.outputs[16], 'name'):
                group_input_004_1.outputs[16].name = 'BRIGHTNESS'
            if hasattr(group_input_004_1.outputs[16], 'show_expanded'):
                group_input_004_1.outputs[16].show_expanded = False
            if hasattr(group_input_004_1.outputs[17], 'default_value'):
                group_input_004_1.outputs[17].default_value = 1.0
            if hasattr(group_input_004_1.outputs[17], 'display_shape'):
                group_input_004_1.outputs[17].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[17], 'enabled'):
                group_input_004_1.outputs[17].enabled = True
            if hasattr(group_input_004_1.outputs[17], 'hide'):
                group_input_004_1.outputs[17].hide = True
            if hasattr(group_input_004_1.outputs[17], 'hide_value'):
                group_input_004_1.outputs[17].hide_value = False
            if hasattr(group_input_004_1.outputs[17], 'name'):
                group_input_004_1.outputs[17].name = '  Glowing Level'
            if hasattr(group_input_004_1.outputs[17], 'show_expanded'):
                group_input_004_1.outputs[17].show_expanded = False
            if hasattr(group_input_004_1.outputs[18], 'default_value'):
                group_input_004_1.outputs[18].default_value = 0.0
            if hasattr(group_input_004_1.outputs[18], 'display_shape'):
                group_input_004_1.outputs[18].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[18], 'enabled'):
                group_input_004_1.outputs[18].enabled = True
            if hasattr(group_input_004_1.outputs[18], 'hide'):
                group_input_004_1.outputs[18].hide = True
            if hasattr(group_input_004_1.outputs[18], 'hide_value'):
                group_input_004_1.outputs[18].hide_value = False
            if hasattr(group_input_004_1.outputs[18], 'name'):
                group_input_004_1.outputs[18].name = '  Brightness'
            if hasattr(group_input_004_1.outputs[18], 'show_expanded'):
                group_input_004_1.outputs[18].show_expanded = False
            if hasattr(group_input_004_1.outputs[19], 'default_value'):
                group_input_004_1.outputs[19].default_value = 2.5
            if hasattr(group_input_004_1.outputs[19], 'display_shape'):
                group_input_004_1.outputs[19].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[19], 'enabled'):
                group_input_004_1.outputs[19].enabled = True
            if hasattr(group_input_004_1.outputs[19], 'hide'):
                group_input_004_1.outputs[19].hide = True
            if hasattr(group_input_004_1.outputs[19], 'hide_value'):
                group_input_004_1.outputs[19].hide_value = False
            if hasattr(group_input_004_1.outputs[19], 'name'):
                group_input_004_1.outputs[19].name = '  Dark / Bright Threshold'
            if hasattr(group_input_004_1.outputs[19], 'show_expanded'):
                group_input_004_1.outputs[19].show_expanded = False
            if hasattr(group_input_004_1.outputs[20], 'default_value'):
                group_input_004_1.outputs[20].default_value = 0.0
            if hasattr(group_input_004_1.outputs[20], 'display_shape'):
                group_input_004_1.outputs[20].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[20], 'enabled'):
                group_input_004_1.outputs[20].enabled = True
            if hasattr(group_input_004_1.outputs[20], 'hide'):
                group_input_004_1.outputs[20].hide = True
            if hasattr(group_input_004_1.outputs[20], 'hide_value'):
                group_input_004_1.outputs[20].hide_value = False
            if hasattr(group_input_004_1.outputs[20], 'name'):
                group_input_004_1.outputs[20].name = '    Dark Spot Intensity'
            if hasattr(group_input_004_1.outputs[20], 'show_expanded'):
                group_input_004_1.outputs[20].show_expanded = False
            if hasattr(group_input_004_1.outputs[21], 'default_value'):
                group_input_004_1.outputs[21].default_value = 0.0
            if hasattr(group_input_004_1.outputs[21], 'display_shape'):
                group_input_004_1.outputs[21].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[21], 'enabled'):
                group_input_004_1.outputs[21].enabled = True
            if hasattr(group_input_004_1.outputs[21], 'hide'):
                group_input_004_1.outputs[21].hide = True
            if hasattr(group_input_004_1.outputs[21], 'hide_value'):
                group_input_004_1.outputs[21].hide_value = False
            if hasattr(group_input_004_1.outputs[21], 'name'):
                group_input_004_1.outputs[21].name = '    Bright Spot Intensity'
            if hasattr(group_input_004_1.outputs[21], 'show_expanded'):
                group_input_004_1.outputs[21].show_expanded = False
            if hasattr(group_input_004_1.outputs[22], 'default_value'):
                group_input_004_1.outputs[22].default_value = 0.10000000149011612
            if hasattr(group_input_004_1.outputs[22], 'display_shape'):
                group_input_004_1.outputs[22].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[22], 'enabled'):
                group_input_004_1.outputs[22].enabled = True
            if hasattr(group_input_004_1.outputs[22], 'hide'):
                group_input_004_1.outputs[22].hide = True
            if hasattr(group_input_004_1.outputs[22], 'hide_value'):
                group_input_004_1.outputs[22].hide_value = False
            if hasattr(group_input_004_1.outputs[22], 'name'):
                group_input_004_1.outputs[22].name = 'Blend'
            if hasattr(group_input_004_1.outputs[22], 'show_expanded'):
                group_input_004_1.outputs[22].show_expanded = False
            if hasattr(group_input_004_1.outputs[23], 'default_value'):
                group_input_004_1.outputs[23].default_value = 0.47999998927116394
            if hasattr(group_input_004_1.outputs[23], 'display_shape'):
                group_input_004_1.outputs[23].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[23], 'enabled'):
                group_input_004_1.outputs[23].enabled = True
            if hasattr(group_input_004_1.outputs[23], 'hide'):
                group_input_004_1.outputs[23].hide = True
            if hasattr(group_input_004_1.outputs[23], 'hide_value'):
                group_input_004_1.outputs[23].hide_value = False
            if hasattr(group_input_004_1.outputs[23], 'name'):
                group_input_004_1.outputs[23].name = 'Roughness'
            if hasattr(group_input_004_1.outputs[23], 'show_expanded'):
                group_input_004_1.outputs[23].show_expanded = False
            if hasattr(group_input_004_1.outputs[24], 'default_value'):
                group_input_004_1.outputs[24].default_value = 0.125
            if hasattr(group_input_004_1.outputs[24], 'display_shape'):
                group_input_004_1.outputs[24].display_shape = 'CIRCLE'
            if hasattr(group_input_004_1.outputs[24], 'enabled'):
                group_input_004_1.outputs[24].enabled = True
            if hasattr(group_input_004_1.outputs[24], 'hide'):
                group_input_004_1.outputs[24].hide = True
            if hasattr(group_input_004_1.outputs[24], 'hide_value'):
                group_input_004_1.outputs[24].hide_value = False
            if hasattr(group_input_004_1.outputs[24], 'name'):
                group_input_004_1.outputs[24].name = 'Falloff Strength'
            if hasattr(group_input_004_1.outputs[24], 'show_expanded'):
                group_input_004_1.outputs[24].show_expanded = False

            mix_shader_1 = node_tree1.nodes.new('ShaderNodeMixShader')
            if hasattr(mix_shader_1, 'color'):
                mix_shader_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(mix_shader_1, 'hide'):
                mix_shader_1.hide = False
            if hasattr(mix_shader_1, 'location'):
                mix_shader_1.location = (-320.0, 0.0)
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

            diffuse_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfDiffuse')
            if hasattr(diffuse_bsdf_1, 'color'):
                diffuse_bsdf_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(diffuse_bsdf_1, 'hide'):
                diffuse_bsdf_1.hide = False
            if hasattr(diffuse_bsdf_1, 'location'):
                diffuse_bsdf_1.location = (-480.0, -206.0)
            if hasattr(diffuse_bsdf_1, 'mute'):
                diffuse_bsdf_1.mute = False
            if hasattr(diffuse_bsdf_1, 'name'):
                diffuse_bsdf_1.name = 'Diffuse BSDF'
            if hasattr(diffuse_bsdf_1, 'use_custom_color'):
                diffuse_bsdf_1.use_custom_color = False
            if hasattr(diffuse_bsdf_1, 'width'):
                diffuse_bsdf_1.width = 140.0
            input_ = next((input_ for input_ in diffuse_bsdf_1.inputs if input_.identifier=='Color'), None)
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
                    input_.name = 'Color'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in diffuse_bsdf_1.inputs if input_.identifier=='Roughness'), None)
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
            input_ = next((input_ for input_ in diffuse_bsdf_1.inputs if input_.identifier=='Normal'), None)
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
            input_ = next((input_ for input_ in diffuse_bsdf_1.inputs if input_.identifier=='Weight'), None)
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
                mix_shader_001_1.location = (-480.0, -94.0)
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
                    input_.default_value = 0.15000000596046448
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

            layer_weight_1 = node_tree1.nodes.new('ShaderNodeLayerWeight')
            if hasattr(layer_weight_1, 'color'):
                layer_weight_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(layer_weight_1, 'hide'):
                layer_weight_1.hide = False
            if hasattr(layer_weight_1, 'location'):
                layer_weight_1.location = (-480.0, 0.0)
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

            glossy_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfGlossy')
            if hasattr(glossy_bsdf_1, 'color'):
                glossy_bsdf_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(glossy_bsdf_1, 'distribution'):
                glossy_bsdf_1.distribution = 'GGX'
            if hasattr(glossy_bsdf_1, 'hide'):
                glossy_bsdf_1.hide = False
            if hasattr(glossy_bsdf_1, 'location'):
                glossy_bsdf_1.location = (-640.0, -92.0)
            if hasattr(glossy_bsdf_1, 'mute'):
                glossy_bsdf_1.mute = False
            if hasattr(glossy_bsdf_1, 'name'):
                glossy_bsdf_1.name = 'Glossy BSDF'
            if hasattr(glossy_bsdf_1, 'use_custom_color'):
                glossy_bsdf_1.use_custom_color = False
            if hasattr(glossy_bsdf_1, 'width'):
                glossy_bsdf_1.width = 140.0
            input_ = next((input_ for input_ in glossy_bsdf_1.inputs if input_.identifier=='Color'), None)
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
                    input_.name = 'Color'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False
            input_ = next((input_ for input_ in glossy_bsdf_1.inputs if input_.identifier=='Roughness'), None)
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

            math_1 = node_tree1.nodes.new('ShaderNodeMath')
            if hasattr(math_1, 'color'):
                math_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(math_1, 'hide'):
                math_1.hide = False
            if hasattr(math_1, 'location'):
                math_1.location = (-640.0, -206.0)
            if hasattr(math_1, 'mute'):
                math_1.mute = False
            if hasattr(math_1, 'name'):
                math_1.name = 'Math'
            if hasattr(math_1, 'operation'):
                math_1.operation = 'SUBTRACT'
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

            group_input_003_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_003_1, 'color'):
                group_input_003_1.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
            if hasattr(group_input_003_1, 'hide'):
                group_input_003_1.hide = False
            if hasattr(group_input_003_1, 'location'):
                group_input_003_1.location = (-640.0, -298.0)
            if hasattr(group_input_003_1, 'mute'):
                group_input_003_1.mute = False
            if hasattr(group_input_003_1, 'name'):
                group_input_003_1.name = 'Group Input.003'
            if hasattr(group_input_003_1, 'use_custom_color'):
                group_input_003_1.use_custom_color = True
            if hasattr(group_input_003_1, 'width'):
                group_input_003_1.width = 140.0
            if hasattr(group_input_003_1.outputs[0], 'default_value'):
                group_input_003_1.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_003_1.outputs[0], 'display_shape'):
                group_input_003_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[0], 'enabled'):
                group_input_003_1.outputs[0].enabled = True
            if hasattr(group_input_003_1.outputs[0], 'hide'):
                group_input_003_1.outputs[0].hide = True
            if hasattr(group_input_003_1.outputs[0], 'hide_value'):
                group_input_003_1.outputs[0].hide_value = False
            if hasattr(group_input_003_1.outputs[0], 'name'):
                group_input_003_1.outputs[0].name = 'Base Color'
            if hasattr(group_input_003_1.outputs[0], 'show_expanded'):
                group_input_003_1.outputs[0].show_expanded = False
            if hasattr(group_input_003_1.outputs[1], 'default_value'):
                group_input_003_1.outputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_003_1.outputs[1], 'display_shape'):
                group_input_003_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[1], 'enabled'):
                group_input_003_1.outputs[1].enabled = True
            if hasattr(group_input_003_1.outputs[1], 'hide'):
                group_input_003_1.outputs[1].hide = True
            if hasattr(group_input_003_1.outputs[1], 'hide_value'):
                group_input_003_1.outputs[1].hide_value = False
            if hasattr(group_input_003_1.outputs[1], 'name'):
                group_input_003_1.outputs[1].name = 'Transparent Color'
            if hasattr(group_input_003_1.outputs[1], 'show_expanded'):
                group_input_003_1.outputs[1].show_expanded = False
            if hasattr(group_input_003_1.outputs[2], 'default_value'):
                group_input_003_1.outputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_003_1.outputs[2], 'display_shape'):
                group_input_003_1.outputs[2].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[2], 'enabled'):
                group_input_003_1.outputs[2].enabled = True
            if hasattr(group_input_003_1.outputs[2], 'hide'):
                group_input_003_1.outputs[2].hide = True
            if hasattr(group_input_003_1.outputs[2], 'hide_value'):
                group_input_003_1.outputs[2].hide_value = False
            if hasattr(group_input_003_1.outputs[2], 'name'):
                group_input_003_1.outputs[2].name = 'Reflection Color'
            if hasattr(group_input_003_1.outputs[2], 'show_expanded'):
                group_input_003_1.outputs[2].show_expanded = False
            if hasattr(group_input_003_1.outputs[3], 'default_value'):
                group_input_003_1.outputs[3].default_value = 0.25
            if hasattr(group_input_003_1.outputs[3], 'display_shape'):
                group_input_003_1.outputs[3].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[3], 'enabled'):
                group_input_003_1.outputs[3].enabled = True
            if hasattr(group_input_003_1.outputs[3], 'hide'):
                group_input_003_1.outputs[3].hide = True
            if hasattr(group_input_003_1.outputs[3], 'hide_value'):
                group_input_003_1.outputs[3].hide_value = False
            if hasattr(group_input_003_1.outputs[3], 'name'):
                group_input_003_1.outputs[3].name = 'Reflection Factor'
            if hasattr(group_input_003_1.outputs[3], 'show_expanded'):
                group_input_003_1.outputs[3].show_expanded = False
            if hasattr(group_input_003_1.outputs[4], 'default_value'):
                group_input_003_1.outputs[4].default_value = 0.0
            if hasattr(group_input_003_1.outputs[4], 'display_shape'):
                group_input_003_1.outputs[4].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[4], 'enabled'):
                group_input_003_1.outputs[4].enabled = True
            if hasattr(group_input_003_1.outputs[4], 'hide'):
                group_input_003_1.outputs[4].hide = True
            if hasattr(group_input_003_1.outputs[4], 'hide_value'):
                group_input_003_1.outputs[4].hide_value = True
            if hasattr(group_input_003_1.outputs[4], 'name'):
                group_input_003_1.outputs[4].name = 'COLOR VARIATION'
            if hasattr(group_input_003_1.outputs[4], 'show_expanded'):
                group_input_003_1.outputs[4].show_expanded = False
            if hasattr(group_input_003_1.outputs[5], 'default_value'):
                group_input_003_1.outputs[5].default_value = 6.5
            if hasattr(group_input_003_1.outputs[5], 'display_shape'):
                group_input_003_1.outputs[5].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[5], 'enabled'):
                group_input_003_1.outputs[5].enabled = True
            if hasattr(group_input_003_1.outputs[5], 'hide'):
                group_input_003_1.outputs[5].hide = True
            if hasattr(group_input_003_1.outputs[5], 'hide_value'):
                group_input_003_1.outputs[5].hide_value = False
            if hasattr(group_input_003_1.outputs[5], 'name'):
                group_input_003_1.outputs[5].name = '  Color Variation Scale'
            if hasattr(group_input_003_1.outputs[5], 'show_expanded'):
                group_input_003_1.outputs[5].show_expanded = False
            if hasattr(group_input_003_1.outputs[6], 'default_value'):
                group_input_003_1.outputs[6].default_value = 0.15000000596046448
            if hasattr(group_input_003_1.outputs[6], 'display_shape'):
                group_input_003_1.outputs[6].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[6], 'enabled'):
                group_input_003_1.outputs[6].enabled = True
            if hasattr(group_input_003_1.outputs[6], 'hide'):
                group_input_003_1.outputs[6].hide = True
            if hasattr(group_input_003_1.outputs[6], 'hide_value'):
                group_input_003_1.outputs[6].hide_value = False
            if hasattr(group_input_003_1.outputs[6], 'name'):
                group_input_003_1.outputs[6].name = '  Color Variation Distortion'
            if hasattr(group_input_003_1.outputs[6], 'show_expanded'):
                group_input_003_1.outputs[6].show_expanded = False
            if hasattr(group_input_003_1.outputs[7], 'default_value'):
                group_input_003_1.outputs[7].default_value = 0.7749999761581421
            if hasattr(group_input_003_1.outputs[7], 'display_shape'):
                group_input_003_1.outputs[7].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[7], 'enabled'):
                group_input_003_1.outputs[7].enabled = True
            if hasattr(group_input_003_1.outputs[7], 'hide'):
                group_input_003_1.outputs[7].hide = True
            if hasattr(group_input_003_1.outputs[7], 'hide_value'):
                group_input_003_1.outputs[7].hide_value = False
            if hasattr(group_input_003_1.outputs[7], 'name'):
                group_input_003_1.outputs[7].name = '  Random Color Var'
            if hasattr(group_input_003_1.outputs[7], 'show_expanded'):
                group_input_003_1.outputs[7].show_expanded = False
            if hasattr(group_input_003_1.outputs[8], 'default_value'):
                group_input_003_1.outputs[8].default_value = 0.0
            if hasattr(group_input_003_1.outputs[8], 'display_shape'):
                group_input_003_1.outputs[8].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[8], 'enabled'):
                group_input_003_1.outputs[8].enabled = True
            if hasattr(group_input_003_1.outputs[8], 'hide'):
                group_input_003_1.outputs[8].hide = True
            if hasattr(group_input_003_1.outputs[8], 'hide_value'):
                group_input_003_1.outputs[8].hide_value = True
            if hasattr(group_input_003_1.outputs[8], 'name'):
                group_input_003_1.outputs[8].name = 'COLOR ADJUSTMENTS'
            if hasattr(group_input_003_1.outputs[8], 'show_expanded'):
                group_input_003_1.outputs[8].show_expanded = False
            if hasattr(group_input_003_1.outputs[9], 'default_value'):
                group_input_003_1.outputs[9].default_value = 0.0
            if hasattr(group_input_003_1.outputs[9], 'display_shape'):
                group_input_003_1.outputs[9].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[9], 'enabled'):
                group_input_003_1.outputs[9].enabled = True
            if hasattr(group_input_003_1.outputs[9], 'hide'):
                group_input_003_1.outputs[9].hide = True
            if hasattr(group_input_003_1.outputs[9], 'hide_value'):
                group_input_003_1.outputs[9].hide_value = False
            if hasattr(group_input_003_1.outputs[9], 'name'):
                group_input_003_1.outputs[9].name = '  Unpaint'
            if hasattr(group_input_003_1.outputs[9], 'show_expanded'):
                group_input_003_1.outputs[9].show_expanded = False
            if hasattr(group_input_003_1.outputs[10], 'default_value'):
                group_input_003_1.outputs[10].default_value = 0.0
            if hasattr(group_input_003_1.outputs[10], 'display_shape'):
                group_input_003_1.outputs[10].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[10], 'enabled'):
                group_input_003_1.outputs[10].enabled = True
            if hasattr(group_input_003_1.outputs[10], 'hide'):
                group_input_003_1.outputs[10].hide = True
            if hasattr(group_input_003_1.outputs[10], 'hide_value'):
                group_input_003_1.outputs[10].hide_value = False
            if hasattr(group_input_003_1.outputs[10], 'name'):
                group_input_003_1.outputs[10].name = '  Color Inverter'
            if hasattr(group_input_003_1.outputs[10], 'show_expanded'):
                group_input_003_1.outputs[10].show_expanded = False
            if hasattr(group_input_003_1.outputs[11], 'default_value'):
                group_input_003_1.outputs[11].default_value = 0.0
            if hasattr(group_input_003_1.outputs[11], 'display_shape'):
                group_input_003_1.outputs[11].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[11], 'enabled'):
                group_input_003_1.outputs[11].enabled = True
            if hasattr(group_input_003_1.outputs[11], 'hide'):
                group_input_003_1.outputs[11].hide = True
            if hasattr(group_input_003_1.outputs[11], 'hide_value'):
                group_input_003_1.outputs[11].hide_value = False
            if hasattr(group_input_003_1.outputs[11], 'name'):
                group_input_003_1.outputs[11].name = '  Contrast'
            if hasattr(group_input_003_1.outputs[11], 'show_expanded'):
                group_input_003_1.outputs[11].show_expanded = False
            if hasattr(group_input_003_1.outputs[12], 'default_value'):
                group_input_003_1.outputs[12].default_value = 1.0
            if hasattr(group_input_003_1.outputs[12], 'display_shape'):
                group_input_003_1.outputs[12].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[12], 'enabled'):
                group_input_003_1.outputs[12].enabled = True
            if hasattr(group_input_003_1.outputs[12], 'hide'):
                group_input_003_1.outputs[12].hide = True
            if hasattr(group_input_003_1.outputs[12], 'hide_value'):
                group_input_003_1.outputs[12].hide_value = False
            if hasattr(group_input_003_1.outputs[12], 'name'):
                group_input_003_1.outputs[12].name = '  Gamma'
            if hasattr(group_input_003_1.outputs[12], 'show_expanded'):
                group_input_003_1.outputs[12].show_expanded = False
            if hasattr(group_input_003_1.outputs[13], 'default_value'):
                group_input_003_1.outputs[13].default_value = 1.0
            if hasattr(group_input_003_1.outputs[13], 'display_shape'):
                group_input_003_1.outputs[13].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[13], 'enabled'):
                group_input_003_1.outputs[13].enabled = True
            if hasattr(group_input_003_1.outputs[13], 'hide'):
                group_input_003_1.outputs[13].hide = True
            if hasattr(group_input_003_1.outputs[13], 'hide_value'):
                group_input_003_1.outputs[13].hide_value = False
            if hasattr(group_input_003_1.outputs[13], 'name'):
                group_input_003_1.outputs[13].name = '  Hue / Sat Value'
            if hasattr(group_input_003_1.outputs[13], 'show_expanded'):
                group_input_003_1.outputs[13].show_expanded = False
            if hasattr(group_input_003_1.outputs[14], 'default_value'):
                group_input_003_1.outputs[14].default_value = 0.49999991059303284
            if hasattr(group_input_003_1.outputs[14], 'display_shape'):
                group_input_003_1.outputs[14].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[14], 'enabled'):
                group_input_003_1.outputs[14].enabled = True
            if hasattr(group_input_003_1.outputs[14], 'hide'):
                group_input_003_1.outputs[14].hide = True
            if hasattr(group_input_003_1.outputs[14], 'hide_value'):
                group_input_003_1.outputs[14].hide_value = False
            if hasattr(group_input_003_1.outputs[14], 'name'):
                group_input_003_1.outputs[14].name = '    Hue'
            if hasattr(group_input_003_1.outputs[14], 'show_expanded'):
                group_input_003_1.outputs[14].show_expanded = False
            if hasattr(group_input_003_1.outputs[15], 'default_value'):
                group_input_003_1.outputs[15].default_value = 1.0
            if hasattr(group_input_003_1.outputs[15], 'display_shape'):
                group_input_003_1.outputs[15].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[15], 'enabled'):
                group_input_003_1.outputs[15].enabled = True
            if hasattr(group_input_003_1.outputs[15], 'hide'):
                group_input_003_1.outputs[15].hide = True
            if hasattr(group_input_003_1.outputs[15], 'hide_value'):
                group_input_003_1.outputs[15].hide_value = False
            if hasattr(group_input_003_1.outputs[15], 'name'):
                group_input_003_1.outputs[15].name = '    Saturation'
            if hasattr(group_input_003_1.outputs[15], 'show_expanded'):
                group_input_003_1.outputs[15].show_expanded = False
            if hasattr(group_input_003_1.outputs[16], 'default_value'):
                group_input_003_1.outputs[16].default_value = 0.0
            if hasattr(group_input_003_1.outputs[16], 'display_shape'):
                group_input_003_1.outputs[16].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[16], 'enabled'):
                group_input_003_1.outputs[16].enabled = True
            if hasattr(group_input_003_1.outputs[16], 'hide'):
                group_input_003_1.outputs[16].hide = True
            if hasattr(group_input_003_1.outputs[16], 'hide_value'):
                group_input_003_1.outputs[16].hide_value = True
            if hasattr(group_input_003_1.outputs[16], 'name'):
                group_input_003_1.outputs[16].name = 'BRIGHTNESS'
            if hasattr(group_input_003_1.outputs[16], 'show_expanded'):
                group_input_003_1.outputs[16].show_expanded = False
            if hasattr(group_input_003_1.outputs[17], 'default_value'):
                group_input_003_1.outputs[17].default_value = 1.0
            if hasattr(group_input_003_1.outputs[17], 'display_shape'):
                group_input_003_1.outputs[17].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[17], 'enabled'):
                group_input_003_1.outputs[17].enabled = True
            if hasattr(group_input_003_1.outputs[17], 'hide'):
                group_input_003_1.outputs[17].hide = True
            if hasattr(group_input_003_1.outputs[17], 'hide_value'):
                group_input_003_1.outputs[17].hide_value = False
            if hasattr(group_input_003_1.outputs[17], 'name'):
                group_input_003_1.outputs[17].name = '  Glowing Level'
            if hasattr(group_input_003_1.outputs[17], 'show_expanded'):
                group_input_003_1.outputs[17].show_expanded = False
            if hasattr(group_input_003_1.outputs[18], 'default_value'):
                group_input_003_1.outputs[18].default_value = 0.0
            if hasattr(group_input_003_1.outputs[18], 'display_shape'):
                group_input_003_1.outputs[18].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[18], 'enabled'):
                group_input_003_1.outputs[18].enabled = True
            if hasattr(group_input_003_1.outputs[18], 'hide'):
                group_input_003_1.outputs[18].hide = True
            if hasattr(group_input_003_1.outputs[18], 'hide_value'):
                group_input_003_1.outputs[18].hide_value = False
            if hasattr(group_input_003_1.outputs[18], 'name'):
                group_input_003_1.outputs[18].name = '  Brightness'
            if hasattr(group_input_003_1.outputs[18], 'show_expanded'):
                group_input_003_1.outputs[18].show_expanded = False
            if hasattr(group_input_003_1.outputs[19], 'default_value'):
                group_input_003_1.outputs[19].default_value = 2.5
            if hasattr(group_input_003_1.outputs[19], 'display_shape'):
                group_input_003_1.outputs[19].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[19], 'enabled'):
                group_input_003_1.outputs[19].enabled = True
            if hasattr(group_input_003_1.outputs[19], 'hide'):
                group_input_003_1.outputs[19].hide = True
            if hasattr(group_input_003_1.outputs[19], 'hide_value'):
                group_input_003_1.outputs[19].hide_value = False
            if hasattr(group_input_003_1.outputs[19], 'name'):
                group_input_003_1.outputs[19].name = '  Dark / Bright Threshold'
            if hasattr(group_input_003_1.outputs[19], 'show_expanded'):
                group_input_003_1.outputs[19].show_expanded = False
            if hasattr(group_input_003_1.outputs[20], 'default_value'):
                group_input_003_1.outputs[20].default_value = 0.0
            if hasattr(group_input_003_1.outputs[20], 'display_shape'):
                group_input_003_1.outputs[20].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[20], 'enabled'):
                group_input_003_1.outputs[20].enabled = True
            if hasattr(group_input_003_1.outputs[20], 'hide'):
                group_input_003_1.outputs[20].hide = True
            if hasattr(group_input_003_1.outputs[20], 'hide_value'):
                group_input_003_1.outputs[20].hide_value = False
            if hasattr(group_input_003_1.outputs[20], 'name'):
                group_input_003_1.outputs[20].name = '    Dark Spot Intensity'
            if hasattr(group_input_003_1.outputs[20], 'show_expanded'):
                group_input_003_1.outputs[20].show_expanded = False
            if hasattr(group_input_003_1.outputs[21], 'default_value'):
                group_input_003_1.outputs[21].default_value = 0.0
            if hasattr(group_input_003_1.outputs[21], 'display_shape'):
                group_input_003_1.outputs[21].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[21], 'enabled'):
                group_input_003_1.outputs[21].enabled = True
            if hasattr(group_input_003_1.outputs[21], 'hide'):
                group_input_003_1.outputs[21].hide = True
            if hasattr(group_input_003_1.outputs[21], 'hide_value'):
                group_input_003_1.outputs[21].hide_value = False
            if hasattr(group_input_003_1.outputs[21], 'name'):
                group_input_003_1.outputs[21].name = '    Bright Spot Intensity'
            if hasattr(group_input_003_1.outputs[21], 'show_expanded'):
                group_input_003_1.outputs[21].show_expanded = False
            if hasattr(group_input_003_1.outputs[22], 'default_value'):
                group_input_003_1.outputs[22].default_value = 0.10000000149011612
            if hasattr(group_input_003_1.outputs[22], 'display_shape'):
                group_input_003_1.outputs[22].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[22], 'enabled'):
                group_input_003_1.outputs[22].enabled = True
            if hasattr(group_input_003_1.outputs[22], 'hide'):
                group_input_003_1.outputs[22].hide = False
            if hasattr(group_input_003_1.outputs[22], 'hide_value'):
                group_input_003_1.outputs[22].hide_value = False
            if hasattr(group_input_003_1.outputs[22], 'name'):
                group_input_003_1.outputs[22].name = 'Blend'
            if hasattr(group_input_003_1.outputs[22], 'show_expanded'):
                group_input_003_1.outputs[22].show_expanded = False
            if hasattr(group_input_003_1.outputs[23], 'default_value'):
                group_input_003_1.outputs[23].default_value = 0.47999998927116394
            if hasattr(group_input_003_1.outputs[23], 'display_shape'):
                group_input_003_1.outputs[23].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[23], 'enabled'):
                group_input_003_1.outputs[23].enabled = True
            if hasattr(group_input_003_1.outputs[23], 'hide'):
                group_input_003_1.outputs[23].hide = True
            if hasattr(group_input_003_1.outputs[23], 'hide_value'):
                group_input_003_1.outputs[23].hide_value = False
            if hasattr(group_input_003_1.outputs[23], 'name'):
                group_input_003_1.outputs[23].name = 'Roughness'
            if hasattr(group_input_003_1.outputs[23], 'show_expanded'):
                group_input_003_1.outputs[23].show_expanded = False
            if hasattr(group_input_003_1.outputs[24], 'default_value'):
                group_input_003_1.outputs[24].default_value = 0.125
            if hasattr(group_input_003_1.outputs[24], 'display_shape'):
                group_input_003_1.outputs[24].display_shape = 'CIRCLE'
            if hasattr(group_input_003_1.outputs[24], 'enabled'):
                group_input_003_1.outputs[24].enabled = True
            if hasattr(group_input_003_1.outputs[24], 'hide'):
                group_input_003_1.outputs[24].hide = True
            if hasattr(group_input_003_1.outputs[24], 'hide_value'):
                group_input_003_1.outputs[24].hide_value = False
            if hasattr(group_input_003_1.outputs[24], 'name'):
                group_input_003_1.outputs[24].name = 'Falloff Strength'
            if hasattr(group_input_003_1.outputs[24], 'show_expanded'):
                group_input_003_1.outputs[24].show_expanded = False

            transparent_bsdf_1 = node_tree1.nodes.new('ShaderNodeBsdfTransparent')
            if hasattr(transparent_bsdf_1, 'color'):
                transparent_bsdf_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(transparent_bsdf_1, 'hide'):
                transparent_bsdf_1.hide = False
            if hasattr(transparent_bsdf_1, 'location'):
                transparent_bsdf_1.location = (-640.0, 0.0)
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
                    input_.hide = True
                if hasattr(input_, 'hide_value'):
                    input_.hide_value = False
                if hasattr(input_, 'name'):
                    input_.name = 'Weight'
                if hasattr(input_, 'show_expanded'):
                    input_.show_expanded = False

            group_input_001_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_001_1, 'color'):
                group_input_001_1.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
            if hasattr(group_input_001_1, 'hide'):
                group_input_001_1.hide = False
            if hasattr(group_input_001_1, 'location'):
                group_input_001_1.location = (-800.0, -508.0)
            if hasattr(group_input_001_1, 'mute'):
                group_input_001_1.mute = False
            if hasattr(group_input_001_1, 'name'):
                group_input_001_1.name = 'Group Input.001'
            if hasattr(group_input_001_1, 'use_custom_color'):
                group_input_001_1.use_custom_color = True
            if hasattr(group_input_001_1, 'width'):
                group_input_001_1.width = 140.0
            if hasattr(group_input_001_1.outputs[0], 'default_value'):
                group_input_001_1.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_001_1.outputs[0], 'display_shape'):
                group_input_001_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[0], 'enabled'):
                group_input_001_1.outputs[0].enabled = True
            if hasattr(group_input_001_1.outputs[0], 'hide'):
                group_input_001_1.outputs[0].hide = True
            if hasattr(group_input_001_1.outputs[0], 'hide_value'):
                group_input_001_1.outputs[0].hide_value = False
            if hasattr(group_input_001_1.outputs[0], 'name'):
                group_input_001_1.outputs[0].name = 'Base Color'
            if hasattr(group_input_001_1.outputs[0], 'show_expanded'):
                group_input_001_1.outputs[0].show_expanded = False
            if hasattr(group_input_001_1.outputs[1], 'default_value'):
                group_input_001_1.outputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_001_1.outputs[1], 'display_shape'):
                group_input_001_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[1], 'enabled'):
                group_input_001_1.outputs[1].enabled = True
            if hasattr(group_input_001_1.outputs[1], 'hide'):
                group_input_001_1.outputs[1].hide = False
            if hasattr(group_input_001_1.outputs[1], 'hide_value'):
                group_input_001_1.outputs[1].hide_value = False
            if hasattr(group_input_001_1.outputs[1], 'name'):
                group_input_001_1.outputs[1].name = 'Transparent Color'
            if hasattr(group_input_001_1.outputs[1], 'show_expanded'):
                group_input_001_1.outputs[1].show_expanded = False
            if hasattr(group_input_001_1.outputs[2], 'default_value'):
                group_input_001_1.outputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_001_1.outputs[2], 'display_shape'):
                group_input_001_1.outputs[2].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[2], 'enabled'):
                group_input_001_1.outputs[2].enabled = True
            if hasattr(group_input_001_1.outputs[2], 'hide'):
                group_input_001_1.outputs[2].hide = True
            if hasattr(group_input_001_1.outputs[2], 'hide_value'):
                group_input_001_1.outputs[2].hide_value = False
            if hasattr(group_input_001_1.outputs[2], 'name'):
                group_input_001_1.outputs[2].name = 'Reflection Color'
            if hasattr(group_input_001_1.outputs[2], 'show_expanded'):
                group_input_001_1.outputs[2].show_expanded = False
            if hasattr(group_input_001_1.outputs[3], 'default_value'):
                group_input_001_1.outputs[3].default_value = 0.25
            if hasattr(group_input_001_1.outputs[3], 'display_shape'):
                group_input_001_1.outputs[3].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[3], 'enabled'):
                group_input_001_1.outputs[3].enabled = True
            if hasattr(group_input_001_1.outputs[3], 'hide'):
                group_input_001_1.outputs[3].hide = True
            if hasattr(group_input_001_1.outputs[3], 'hide_value'):
                group_input_001_1.outputs[3].hide_value = False
            if hasattr(group_input_001_1.outputs[3], 'name'):
                group_input_001_1.outputs[3].name = 'Reflection Factor'
            if hasattr(group_input_001_1.outputs[3], 'show_expanded'):
                group_input_001_1.outputs[3].show_expanded = False
            if hasattr(group_input_001_1.outputs[4], 'default_value'):
                group_input_001_1.outputs[4].default_value = 0.0
            if hasattr(group_input_001_1.outputs[4], 'display_shape'):
                group_input_001_1.outputs[4].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[4], 'enabled'):
                group_input_001_1.outputs[4].enabled = True
            if hasattr(group_input_001_1.outputs[4], 'hide'):
                group_input_001_1.outputs[4].hide = True
            if hasattr(group_input_001_1.outputs[4], 'hide_value'):
                group_input_001_1.outputs[4].hide_value = True
            if hasattr(group_input_001_1.outputs[4], 'name'):
                group_input_001_1.outputs[4].name = 'COLOR VARIATION'
            if hasattr(group_input_001_1.outputs[4], 'show_expanded'):
                group_input_001_1.outputs[4].show_expanded = False
            if hasattr(group_input_001_1.outputs[5], 'default_value'):
                group_input_001_1.outputs[5].default_value = 6.5
            if hasattr(group_input_001_1.outputs[5], 'display_shape'):
                group_input_001_1.outputs[5].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[5], 'enabled'):
                group_input_001_1.outputs[5].enabled = True
            if hasattr(group_input_001_1.outputs[5], 'hide'):
                group_input_001_1.outputs[5].hide = True
            if hasattr(group_input_001_1.outputs[5], 'hide_value'):
                group_input_001_1.outputs[5].hide_value = False
            if hasattr(group_input_001_1.outputs[5], 'name'):
                group_input_001_1.outputs[5].name = '  Color Variation Scale'
            if hasattr(group_input_001_1.outputs[5], 'show_expanded'):
                group_input_001_1.outputs[5].show_expanded = False
            if hasattr(group_input_001_1.outputs[6], 'default_value'):
                group_input_001_1.outputs[6].default_value = 0.15000000596046448
            if hasattr(group_input_001_1.outputs[6], 'display_shape'):
                group_input_001_1.outputs[6].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[6], 'enabled'):
                group_input_001_1.outputs[6].enabled = True
            if hasattr(group_input_001_1.outputs[6], 'hide'):
                group_input_001_1.outputs[6].hide = True
            if hasattr(group_input_001_1.outputs[6], 'hide_value'):
                group_input_001_1.outputs[6].hide_value = False
            if hasattr(group_input_001_1.outputs[6], 'name'):
                group_input_001_1.outputs[6].name = '  Color Variation Distortion'
            if hasattr(group_input_001_1.outputs[6], 'show_expanded'):
                group_input_001_1.outputs[6].show_expanded = False
            if hasattr(group_input_001_1.outputs[7], 'default_value'):
                group_input_001_1.outputs[7].default_value = 0.7749999761581421
            if hasattr(group_input_001_1.outputs[7], 'display_shape'):
                group_input_001_1.outputs[7].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[7], 'enabled'):
                group_input_001_1.outputs[7].enabled = True
            if hasattr(group_input_001_1.outputs[7], 'hide'):
                group_input_001_1.outputs[7].hide = True
            if hasattr(group_input_001_1.outputs[7], 'hide_value'):
                group_input_001_1.outputs[7].hide_value = False
            if hasattr(group_input_001_1.outputs[7], 'name'):
                group_input_001_1.outputs[7].name = '  Random Color Var'
            if hasattr(group_input_001_1.outputs[7], 'show_expanded'):
                group_input_001_1.outputs[7].show_expanded = False
            if hasattr(group_input_001_1.outputs[8], 'default_value'):
                group_input_001_1.outputs[8].default_value = 0.0
            if hasattr(group_input_001_1.outputs[8], 'display_shape'):
                group_input_001_1.outputs[8].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[8], 'enabled'):
                group_input_001_1.outputs[8].enabled = True
            if hasattr(group_input_001_1.outputs[8], 'hide'):
                group_input_001_1.outputs[8].hide = True
            if hasattr(group_input_001_1.outputs[8], 'hide_value'):
                group_input_001_1.outputs[8].hide_value = True
            if hasattr(group_input_001_1.outputs[8], 'name'):
                group_input_001_1.outputs[8].name = 'COLOR ADJUSTMENTS'
            if hasattr(group_input_001_1.outputs[8], 'show_expanded'):
                group_input_001_1.outputs[8].show_expanded = False
            if hasattr(group_input_001_1.outputs[9], 'default_value'):
                group_input_001_1.outputs[9].default_value = 0.0
            if hasattr(group_input_001_1.outputs[9], 'display_shape'):
                group_input_001_1.outputs[9].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[9], 'enabled'):
                group_input_001_1.outputs[9].enabled = True
            if hasattr(group_input_001_1.outputs[9], 'hide'):
                group_input_001_1.outputs[9].hide = True
            if hasattr(group_input_001_1.outputs[9], 'hide_value'):
                group_input_001_1.outputs[9].hide_value = False
            if hasattr(group_input_001_1.outputs[9], 'name'):
                group_input_001_1.outputs[9].name = '  Unpaint'
            if hasattr(group_input_001_1.outputs[9], 'show_expanded'):
                group_input_001_1.outputs[9].show_expanded = False
            if hasattr(group_input_001_1.outputs[10], 'default_value'):
                group_input_001_1.outputs[10].default_value = 0.0
            if hasattr(group_input_001_1.outputs[10], 'display_shape'):
                group_input_001_1.outputs[10].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[10], 'enabled'):
                group_input_001_1.outputs[10].enabled = True
            if hasattr(group_input_001_1.outputs[10], 'hide'):
                group_input_001_1.outputs[10].hide = True
            if hasattr(group_input_001_1.outputs[10], 'hide_value'):
                group_input_001_1.outputs[10].hide_value = False
            if hasattr(group_input_001_1.outputs[10], 'name'):
                group_input_001_1.outputs[10].name = '  Color Inverter'
            if hasattr(group_input_001_1.outputs[10], 'show_expanded'):
                group_input_001_1.outputs[10].show_expanded = False
            if hasattr(group_input_001_1.outputs[11], 'default_value'):
                group_input_001_1.outputs[11].default_value = 0.0
            if hasattr(group_input_001_1.outputs[11], 'display_shape'):
                group_input_001_1.outputs[11].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[11], 'enabled'):
                group_input_001_1.outputs[11].enabled = True
            if hasattr(group_input_001_1.outputs[11], 'hide'):
                group_input_001_1.outputs[11].hide = True
            if hasattr(group_input_001_1.outputs[11], 'hide_value'):
                group_input_001_1.outputs[11].hide_value = False
            if hasattr(group_input_001_1.outputs[11], 'name'):
                group_input_001_1.outputs[11].name = '  Contrast'
            if hasattr(group_input_001_1.outputs[11], 'show_expanded'):
                group_input_001_1.outputs[11].show_expanded = False
            if hasattr(group_input_001_1.outputs[12], 'default_value'):
                group_input_001_1.outputs[12].default_value = 1.0
            if hasattr(group_input_001_1.outputs[12], 'display_shape'):
                group_input_001_1.outputs[12].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[12], 'enabled'):
                group_input_001_1.outputs[12].enabled = True
            if hasattr(group_input_001_1.outputs[12], 'hide'):
                group_input_001_1.outputs[12].hide = True
            if hasattr(group_input_001_1.outputs[12], 'hide_value'):
                group_input_001_1.outputs[12].hide_value = False
            if hasattr(group_input_001_1.outputs[12], 'name'):
                group_input_001_1.outputs[12].name = '  Gamma'
            if hasattr(group_input_001_1.outputs[12], 'show_expanded'):
                group_input_001_1.outputs[12].show_expanded = False
            if hasattr(group_input_001_1.outputs[13], 'default_value'):
                group_input_001_1.outputs[13].default_value = 1.0
            if hasattr(group_input_001_1.outputs[13], 'display_shape'):
                group_input_001_1.outputs[13].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[13], 'enabled'):
                group_input_001_1.outputs[13].enabled = True
            if hasattr(group_input_001_1.outputs[13], 'hide'):
                group_input_001_1.outputs[13].hide = True
            if hasattr(group_input_001_1.outputs[13], 'hide_value'):
                group_input_001_1.outputs[13].hide_value = False
            if hasattr(group_input_001_1.outputs[13], 'name'):
                group_input_001_1.outputs[13].name = '  Hue / Sat Value'
            if hasattr(group_input_001_1.outputs[13], 'show_expanded'):
                group_input_001_1.outputs[13].show_expanded = False
            if hasattr(group_input_001_1.outputs[14], 'default_value'):
                group_input_001_1.outputs[14].default_value = 0.49999991059303284
            if hasattr(group_input_001_1.outputs[14], 'display_shape'):
                group_input_001_1.outputs[14].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[14], 'enabled'):
                group_input_001_1.outputs[14].enabled = True
            if hasattr(group_input_001_1.outputs[14], 'hide'):
                group_input_001_1.outputs[14].hide = True
            if hasattr(group_input_001_1.outputs[14], 'hide_value'):
                group_input_001_1.outputs[14].hide_value = False
            if hasattr(group_input_001_1.outputs[14], 'name'):
                group_input_001_1.outputs[14].name = '    Hue'
            if hasattr(group_input_001_1.outputs[14], 'show_expanded'):
                group_input_001_1.outputs[14].show_expanded = False
            if hasattr(group_input_001_1.outputs[15], 'default_value'):
                group_input_001_1.outputs[15].default_value = 1.0
            if hasattr(group_input_001_1.outputs[15], 'display_shape'):
                group_input_001_1.outputs[15].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[15], 'enabled'):
                group_input_001_1.outputs[15].enabled = True
            if hasattr(group_input_001_1.outputs[15], 'hide'):
                group_input_001_1.outputs[15].hide = True
            if hasattr(group_input_001_1.outputs[15], 'hide_value'):
                group_input_001_1.outputs[15].hide_value = False
            if hasattr(group_input_001_1.outputs[15], 'name'):
                group_input_001_1.outputs[15].name = '    Saturation'
            if hasattr(group_input_001_1.outputs[15], 'show_expanded'):
                group_input_001_1.outputs[15].show_expanded = False
            if hasattr(group_input_001_1.outputs[16], 'default_value'):
                group_input_001_1.outputs[16].default_value = 0.0
            if hasattr(group_input_001_1.outputs[16], 'display_shape'):
                group_input_001_1.outputs[16].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[16], 'enabled'):
                group_input_001_1.outputs[16].enabled = True
            if hasattr(group_input_001_1.outputs[16], 'hide'):
                group_input_001_1.outputs[16].hide = True
            if hasattr(group_input_001_1.outputs[16], 'hide_value'):
                group_input_001_1.outputs[16].hide_value = True
            if hasattr(group_input_001_1.outputs[16], 'name'):
                group_input_001_1.outputs[16].name = 'BRIGHTNESS'
            if hasattr(group_input_001_1.outputs[16], 'show_expanded'):
                group_input_001_1.outputs[16].show_expanded = False
            if hasattr(group_input_001_1.outputs[17], 'default_value'):
                group_input_001_1.outputs[17].default_value = 1.0
            if hasattr(group_input_001_1.outputs[17], 'display_shape'):
                group_input_001_1.outputs[17].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[17], 'enabled'):
                group_input_001_1.outputs[17].enabled = True
            if hasattr(group_input_001_1.outputs[17], 'hide'):
                group_input_001_1.outputs[17].hide = True
            if hasattr(group_input_001_1.outputs[17], 'hide_value'):
                group_input_001_1.outputs[17].hide_value = False
            if hasattr(group_input_001_1.outputs[17], 'name'):
                group_input_001_1.outputs[17].name = '  Glowing Level'
            if hasattr(group_input_001_1.outputs[17], 'show_expanded'):
                group_input_001_1.outputs[17].show_expanded = False
            if hasattr(group_input_001_1.outputs[18], 'default_value'):
                group_input_001_1.outputs[18].default_value = 0.0
            if hasattr(group_input_001_1.outputs[18], 'display_shape'):
                group_input_001_1.outputs[18].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[18], 'enabled'):
                group_input_001_1.outputs[18].enabled = True
            if hasattr(group_input_001_1.outputs[18], 'hide'):
                group_input_001_1.outputs[18].hide = True
            if hasattr(group_input_001_1.outputs[18], 'hide_value'):
                group_input_001_1.outputs[18].hide_value = False
            if hasattr(group_input_001_1.outputs[18], 'name'):
                group_input_001_1.outputs[18].name = '  Brightness'
            if hasattr(group_input_001_1.outputs[18], 'show_expanded'):
                group_input_001_1.outputs[18].show_expanded = False
            if hasattr(group_input_001_1.outputs[19], 'default_value'):
                group_input_001_1.outputs[19].default_value = 2.5
            if hasattr(group_input_001_1.outputs[19], 'display_shape'):
                group_input_001_1.outputs[19].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[19], 'enabled'):
                group_input_001_1.outputs[19].enabled = True
            if hasattr(group_input_001_1.outputs[19], 'hide'):
                group_input_001_1.outputs[19].hide = True
            if hasattr(group_input_001_1.outputs[19], 'hide_value'):
                group_input_001_1.outputs[19].hide_value = False
            if hasattr(group_input_001_1.outputs[19], 'name'):
                group_input_001_1.outputs[19].name = '  Dark / Bright Threshold'
            if hasattr(group_input_001_1.outputs[19], 'show_expanded'):
                group_input_001_1.outputs[19].show_expanded = False
            if hasattr(group_input_001_1.outputs[20], 'default_value'):
                group_input_001_1.outputs[20].default_value = 0.0
            if hasattr(group_input_001_1.outputs[20], 'display_shape'):
                group_input_001_1.outputs[20].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[20], 'enabled'):
                group_input_001_1.outputs[20].enabled = True
            if hasattr(group_input_001_1.outputs[20], 'hide'):
                group_input_001_1.outputs[20].hide = True
            if hasattr(group_input_001_1.outputs[20], 'hide_value'):
                group_input_001_1.outputs[20].hide_value = False
            if hasattr(group_input_001_1.outputs[20], 'name'):
                group_input_001_1.outputs[20].name = '    Dark Spot Intensity'
            if hasattr(group_input_001_1.outputs[20], 'show_expanded'):
                group_input_001_1.outputs[20].show_expanded = False
            if hasattr(group_input_001_1.outputs[21], 'default_value'):
                group_input_001_1.outputs[21].default_value = 0.0
            if hasattr(group_input_001_1.outputs[21], 'display_shape'):
                group_input_001_1.outputs[21].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[21], 'enabled'):
                group_input_001_1.outputs[21].enabled = True
            if hasattr(group_input_001_1.outputs[21], 'hide'):
                group_input_001_1.outputs[21].hide = True
            if hasattr(group_input_001_1.outputs[21], 'hide_value'):
                group_input_001_1.outputs[21].hide_value = False
            if hasattr(group_input_001_1.outputs[21], 'name'):
                group_input_001_1.outputs[21].name = '    Bright Spot Intensity'
            if hasattr(group_input_001_1.outputs[21], 'show_expanded'):
                group_input_001_1.outputs[21].show_expanded = False
            if hasattr(group_input_001_1.outputs[22], 'default_value'):
                group_input_001_1.outputs[22].default_value = 0.10000000149011612
            if hasattr(group_input_001_1.outputs[22], 'display_shape'):
                group_input_001_1.outputs[22].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[22], 'enabled'):
                group_input_001_1.outputs[22].enabled = True
            if hasattr(group_input_001_1.outputs[22], 'hide'):
                group_input_001_1.outputs[22].hide = True
            if hasattr(group_input_001_1.outputs[22], 'hide_value'):
                group_input_001_1.outputs[22].hide_value = False
            if hasattr(group_input_001_1.outputs[22], 'name'):
                group_input_001_1.outputs[22].name = 'Blend'
            if hasattr(group_input_001_1.outputs[22], 'show_expanded'):
                group_input_001_1.outputs[22].show_expanded = False
            if hasattr(group_input_001_1.outputs[23], 'default_value'):
                group_input_001_1.outputs[23].default_value = 0.47999998927116394
            if hasattr(group_input_001_1.outputs[23], 'display_shape'):
                group_input_001_1.outputs[23].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[23], 'enabled'):
                group_input_001_1.outputs[23].enabled = True
            if hasattr(group_input_001_1.outputs[23], 'hide'):
                group_input_001_1.outputs[23].hide = True
            if hasattr(group_input_001_1.outputs[23], 'hide_value'):
                group_input_001_1.outputs[23].hide_value = False
            if hasattr(group_input_001_1.outputs[23], 'name'):
                group_input_001_1.outputs[23].name = 'Roughness'
            if hasattr(group_input_001_1.outputs[23], 'show_expanded'):
                group_input_001_1.outputs[23].show_expanded = False
            if hasattr(group_input_001_1.outputs[24], 'default_value'):
                group_input_001_1.outputs[24].default_value = 0.125
            if hasattr(group_input_001_1.outputs[24], 'display_shape'):
                group_input_001_1.outputs[24].display_shape = 'CIRCLE'
            if hasattr(group_input_001_1.outputs[24], 'enabled'):
                group_input_001_1.outputs[24].enabled = True
            if hasattr(group_input_001_1.outputs[24], 'hide'):
                group_input_001_1.outputs[24].hide = True
            if hasattr(group_input_001_1.outputs[24], 'hide_value'):
                group_input_001_1.outputs[24].hide_value = False
            if hasattr(group_input_001_1.outputs[24], 'name'):
                group_input_001_1.outputs[24].name = 'Falloff Strength'
            if hasattr(group_input_001_1.outputs[24], 'show_expanded'):
                group_input_001_1.outputs[24].show_expanded = False

            node_tree2 = bpy.data.node_groups.get('Color Variation Ver. 3')
            if not node_tree2:
                node_tree2 = bpy.data.node_groups.new('Color Variation Ver. 3', 'ShaderNodeTree')
                for node in node_tree2.nodes:
                    node_tree2.nodes.remove(node)
                # INPUTS
                input = node_tree2.inputs.new('NodeSocketColor', 'Input Color')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'name'):
                    input.name = 'Input Color'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', 'COLOR VARIATION')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = True
                if hasattr(input, 'max_value'):
                    input.max_value = 3.4028234663852886e+38
                if hasattr(input, 'min_value'):
                    input.min_value = -3.4028234663852886e+38
                if hasattr(input, 'name'):
                    input.name = 'COLOR VARIATION'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', '  Color Variation Scale')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.5
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 10.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.05000000074505806
                if hasattr(input, 'name'):
                    input.name = '  Color Variation Scale'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', '  Color Variation Distortion')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 3.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0
                if hasattr(input, 'name'):
                    input.name = '  Color Variation Distortion'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', '  Random Color Var')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 1.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 1.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0
                if hasattr(input, 'name'):
                    input.name = '  Random Color Var'
                input = node_tree2.inputs.new('NodeSocketFloat', 'COLOR ADJUSTMENTS')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = True
                if hasattr(input, 'max_value'):
                    input.max_value = 3.4028234663852886e+38
                if hasattr(input, 'min_value'):
                    input.min_value = -3.4028234663852886e+38
                if hasattr(input, 'name'):
                    input.name = 'COLOR ADJUSTMENTS'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', '  Unpaint')
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
                    input.name = '  Unpaint'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', '  Color Inverter')
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
                    input.name = '  Color Inverter'
                input = node_tree2.inputs.new('NodeSocketFloat', '  Contrast')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 100.0
                if hasattr(input, 'min_value'):
                    input.min_value = -100.0
                if hasattr(input, 'name'):
                    input.name = '  Contrast'
                input = node_tree2.inputs.new('NodeSocketFloatUnsigned', '  Gamma')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 1.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 10.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0010000000474974513
                if hasattr(input, 'name'):
                    input.name = '  Gamma'
                input = node_tree2.inputs.new('NodeSocketFloat', '  Hue / Sat Value')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 2.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 2.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0
                if hasattr(input, 'name'):
                    input.name = '  Hue / Sat Value'
                input = node_tree2.inputs.new('NodeSocketFloat', '    Hue')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.49999991059303284
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 1.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0
                if hasattr(input, 'name'):
                    input.name = '    Hue'
                input = node_tree2.inputs.new('NodeSocketFloat', '    Saturation')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 1.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 2.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0
                if hasattr(input, 'name'):
                    input.name = '    Saturation'
                input = node_tree2.inputs.new('NodeSocketFloat', 'BRIGHTNESS')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = True
                if hasattr(input, 'max_value'):
                    input.max_value = 3.4028234663852886e+38
                if hasattr(input, 'min_value'):
                    input.min_value = -3.4028234663852886e+38
                if hasattr(input, 'name'):
                    input.name = 'BRIGHTNESS'
                input = node_tree2.inputs.new('NodeSocketFloat', '  Glowing Level')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 1.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 3.4028234663852886e+38
                if hasattr(input, 'min_value'):
                    input.min_value = -3.4028234663852886e+38
                if hasattr(input, 'name'):
                    input.name = '  Glowing Level'
                input = node_tree2.inputs.new('NodeSocketFloat', '  Brightness')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 100.0
                if hasattr(input, 'min_value'):
                    input.min_value = -100.0
                if hasattr(input, 'name'):
                    input.name = '  Brightness'
                input = node_tree2.inputs.new('NodeSocketFloat', '  Dark / Bright Threshold')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 10000.0
                if hasattr(input, 'min_value'):
                    input.min_value = -10000.0
                if hasattr(input, 'name'):
                    input.name = '  Dark / Bright Threshold'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', '    Dark Spot Intensity')
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
                    input.name = '    Dark Spot Intensity'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', '    Bright Spot Intensity')
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
                    input.name = '    Bright Spot Intensity'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', '  Roughness')
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
                    input.name = '  Roughness'
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
                    node_group_description_2.color = (0.11353799700737, 0.30544498562812805, 0.6079999804496765)
                if hasattr(node_group_description_2, 'hide'):
                    node_group_description_2.hide = False
                if hasattr(node_group_description_2, 'label'):
                    node_group_description_2.label = 'COLOR VARIATIOON NODE'
                if hasattr(node_group_description_2, 'label_size'):
                    node_group_description_2.label_size = 15
                if hasattr(node_group_description_2, 'location'):
                    node_group_description_2.location = (-1955.0, 132.0)
                if hasattr(node_group_description_2, 'mute'):
                    node_group_description_2.mute = False
                if hasattr(node_group_description_2, 'name'):
                    node_group_description_2.name = 'Node Group Description'
                if hasattr(node_group_description_2, 'shrink'):
                    node_group_description_2.shrink = True
                if hasattr(node_group_description_2, 'text'):
                    node_group_description_2.text = bpy.data.texts.get('Color Variation Node')
                if hasattr(node_group_description_2, 'use_custom_color'):
                    node_group_description_2.use_custom_color = True
                if hasattr(node_group_description_2, 'width'):
                    node_group_description_2.width = 400.6717529296875

                author_001_2 = node_tree2.nodes.new('NodeFrame')
                if hasattr(author_001_2, 'color'):
                    author_001_2.color = (0.015208303928375244, 0.12743757665157318, 0.18447497487068176)
                if hasattr(author_001_2, 'hide'):
                    author_001_2.hide = False
                if hasattr(author_001_2, 'label'):
                    author_001_2.label = 'By: Dr. Hacker "BE HACK 2000"'
                if hasattr(author_001_2, 'label_size'):
                    author_001_2.label_size = 16
                if hasattr(author_001_2, 'location'):
                    author_001_2.location = (-70.0, -147.0)
                if hasattr(author_001_2, 'mute'):
                    author_001_2.mute = False
                if hasattr(author_001_2, 'name'):
                    author_001_2.name = 'Author.001'
                if hasattr(author_001_2, 'shrink'):
                    author_001_2.shrink = True
                if hasattr(author_001_2, 'use_custom_color'):
                    author_001_2.use_custom_color = True
                if hasattr(author_001_2, 'width'):
                    author_001_2.width = 289.3975830078125

                unpaint_001_2 = node_tree2.nodes.new('ShaderNodeMix')
                if hasattr(unpaint_001_2, 'blend_type'):
                    unpaint_001_2.blend_type = 'DIFFERENCE'
                if hasattr(unpaint_001_2, 'clamp_factor'):
                    unpaint_001_2.clamp_factor = True
                if hasattr(unpaint_001_2, 'clamp_result'):
                    unpaint_001_2.clamp_result = False
                if hasattr(unpaint_001_2, 'color'):
                    unpaint_001_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(unpaint_001_2, 'data_type'):
                    unpaint_001_2.data_type = 'RGBA'
                if hasattr(unpaint_001_2, 'factor_mode'):
                    unpaint_001_2.factor_mode = 'UNIFORM'
                if hasattr(unpaint_001_2, 'hide'):
                    unpaint_001_2.hide = False
                if hasattr(unpaint_001_2, 'label'):
                    unpaint_001_2.label = 'Color Inverter'
                if hasattr(unpaint_001_2, 'location'):
                    unpaint_001_2.location = (-160.0, 0.0)
                if hasattr(unpaint_001_2, 'mute'):
                    unpaint_001_2.mute = False
                if hasattr(unpaint_001_2, 'name'):
                    unpaint_001_2.name = 'Unpaint.001'
                if hasattr(unpaint_001_2, 'use_custom_color'):
                    unpaint_001_2.use_custom_color = False
                if hasattr(unpaint_001_2, 'width'):
                    unpaint_001_2.width = 140.0
                input_ = next((input_ for input_ in unpaint_001_2.inputs if input_.identifier=='Factor_Float'), None)
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
                input_ = next((input_ for input_ in unpaint_001_2.inputs if input_.identifier=='Factor_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.5, 0.5, 0.5)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_001_2.inputs if input_.identifier=='A_Float'), None)
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
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_001_2.inputs if input_.identifier=='B_Float'), None)
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
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_001_2.inputs if input_.identifier=='A_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_001_2.inputs if input_.identifier=='B_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_001_2.inputs if input_.identifier=='A_Color'), None)
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
                input_ = next((input_ for input_ in unpaint_001_2.inputs if input_.identifier=='B_Color'), None)
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
                output = next((output for output in unpaint_001_2.outputs if output.identifier=='Result_Float'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in unpaint_001_2.outputs if output.identifier=='Result_Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in unpaint_001_2.outputs if output.identifier=='Result_Color'), None)
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

                group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
                if hasattr(group_output_2, 'color'):
                    group_output_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_output_2, 'hide'):
                    group_output_2.hide = False
                if hasattr(group_output_2, 'is_active_output'):
                    group_output_2.is_active_output = True
                if hasattr(group_output_2, 'location'):
                    group_output_2.location = (0.0, 0.0)
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

                group_input_002_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_002_2, 'color'):
                    group_input_002_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_002_2, 'hide'):
                    group_input_002_2.hide = False
                if hasattr(group_input_002_2, 'location'):
                    group_input_002_2.location = (-2080.0, 0.0)
                if hasattr(group_input_002_2, 'mute'):
                    group_input_002_2.mute = False
                if hasattr(group_input_002_2, 'name'):
                    group_input_002_2.name = 'Group Input.002'
                if hasattr(group_input_002_2, 'use_custom_color'):
                    group_input_002_2.use_custom_color = True
                if hasattr(group_input_002_2, 'width'):
                    group_input_002_2.width = 140.0
                if hasattr(group_input_002_2.outputs[0], 'default_value'):
                    group_input_002_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_002_2.outputs[0], 'display_shape'):
                    group_input_002_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[0], 'enabled'):
                    group_input_002_2.outputs[0].enabled = True
                if hasattr(group_input_002_2.outputs[0], 'hide'):
                    group_input_002_2.outputs[0].hide = True
                if hasattr(group_input_002_2.outputs[0], 'hide_value'):
                    group_input_002_2.outputs[0].hide_value = False
                if hasattr(group_input_002_2.outputs[0], 'name'):
                    group_input_002_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_002_2.outputs[0], 'show_expanded'):
                    group_input_002_2.outputs[0].show_expanded = False
                if hasattr(group_input_002_2.outputs[1], 'default_value'):
                    group_input_002_2.outputs[1].default_value = 0.0
                if hasattr(group_input_002_2.outputs[1], 'display_shape'):
                    group_input_002_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[1], 'enabled'):
                    group_input_002_2.outputs[1].enabled = True
                if hasattr(group_input_002_2.outputs[1], 'hide'):
                    group_input_002_2.outputs[1].hide = True
                if hasattr(group_input_002_2.outputs[1], 'hide_value'):
                    group_input_002_2.outputs[1].hide_value = True
                if hasattr(group_input_002_2.outputs[1], 'name'):
                    group_input_002_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_002_2.outputs[1], 'show_expanded'):
                    group_input_002_2.outputs[1].show_expanded = False
                if hasattr(group_input_002_2.outputs[2], 'default_value'):
                    group_input_002_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_002_2.outputs[2], 'display_shape'):
                    group_input_002_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[2], 'enabled'):
                    group_input_002_2.outputs[2].enabled = True
                if hasattr(group_input_002_2.outputs[2], 'hide'):
                    group_input_002_2.outputs[2].hide = False
                if hasattr(group_input_002_2.outputs[2], 'hide_value'):
                    group_input_002_2.outputs[2].hide_value = False
                if hasattr(group_input_002_2.outputs[2], 'name'):
                    group_input_002_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_002_2.outputs[2], 'show_expanded'):
                    group_input_002_2.outputs[2].show_expanded = False
                if hasattr(group_input_002_2.outputs[3], 'default_value'):
                    group_input_002_2.outputs[3].default_value = 0.5
                if hasattr(group_input_002_2.outputs[3], 'display_shape'):
                    group_input_002_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[3], 'enabled'):
                    group_input_002_2.outputs[3].enabled = True
                if hasattr(group_input_002_2.outputs[3], 'hide'):
                    group_input_002_2.outputs[3].hide = True
                if hasattr(group_input_002_2.outputs[3], 'hide_value'):
                    group_input_002_2.outputs[3].hide_value = False
                if hasattr(group_input_002_2.outputs[3], 'name'):
                    group_input_002_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_002_2.outputs[3], 'show_expanded'):
                    group_input_002_2.outputs[3].show_expanded = False
                if hasattr(group_input_002_2.outputs[4], 'default_value'):
                    group_input_002_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_002_2.outputs[4], 'display_shape'):
                    group_input_002_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[4], 'enabled'):
                    group_input_002_2.outputs[4].enabled = True
                if hasattr(group_input_002_2.outputs[4], 'hide'):
                    group_input_002_2.outputs[4].hide = True
                if hasattr(group_input_002_2.outputs[4], 'hide_value'):
                    group_input_002_2.outputs[4].hide_value = False
                if hasattr(group_input_002_2.outputs[4], 'name'):
                    group_input_002_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_002_2.outputs[4], 'show_expanded'):
                    group_input_002_2.outputs[4].show_expanded = False
                if hasattr(group_input_002_2.outputs[5], 'default_value'):
                    group_input_002_2.outputs[5].default_value = 0.0
                if hasattr(group_input_002_2.outputs[5], 'display_shape'):
                    group_input_002_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[5], 'enabled'):
                    group_input_002_2.outputs[5].enabled = True
                if hasattr(group_input_002_2.outputs[5], 'hide'):
                    group_input_002_2.outputs[5].hide = True
                if hasattr(group_input_002_2.outputs[5], 'hide_value'):
                    group_input_002_2.outputs[5].hide_value = True
                if hasattr(group_input_002_2.outputs[5], 'name'):
                    group_input_002_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_002_2.outputs[5], 'show_expanded'):
                    group_input_002_2.outputs[5].show_expanded = False
                if hasattr(group_input_002_2.outputs[6], 'default_value'):
                    group_input_002_2.outputs[6].default_value = 0.5
                if hasattr(group_input_002_2.outputs[6], 'display_shape'):
                    group_input_002_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[6], 'enabled'):
                    group_input_002_2.outputs[6].enabled = True
                if hasattr(group_input_002_2.outputs[6], 'hide'):
                    group_input_002_2.outputs[6].hide = True
                if hasattr(group_input_002_2.outputs[6], 'hide_value'):
                    group_input_002_2.outputs[6].hide_value = False
                if hasattr(group_input_002_2.outputs[6], 'name'):
                    group_input_002_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_002_2.outputs[6], 'show_expanded'):
                    group_input_002_2.outputs[6].show_expanded = False
                if hasattr(group_input_002_2.outputs[7], 'default_value'):
                    group_input_002_2.outputs[7].default_value = 0.0
                if hasattr(group_input_002_2.outputs[7], 'display_shape'):
                    group_input_002_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[7], 'enabled'):
                    group_input_002_2.outputs[7].enabled = True
                if hasattr(group_input_002_2.outputs[7], 'hide'):
                    group_input_002_2.outputs[7].hide = True
                if hasattr(group_input_002_2.outputs[7], 'hide_value'):
                    group_input_002_2.outputs[7].hide_value = False
                if hasattr(group_input_002_2.outputs[7], 'name'):
                    group_input_002_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_002_2.outputs[7], 'show_expanded'):
                    group_input_002_2.outputs[7].show_expanded = False
                if hasattr(group_input_002_2.outputs[8], 'default_value'):
                    group_input_002_2.outputs[8].default_value = 0.0
                if hasattr(group_input_002_2.outputs[8], 'display_shape'):
                    group_input_002_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[8], 'enabled'):
                    group_input_002_2.outputs[8].enabled = True
                if hasattr(group_input_002_2.outputs[8], 'hide'):
                    group_input_002_2.outputs[8].hide = True
                if hasattr(group_input_002_2.outputs[8], 'hide_value'):
                    group_input_002_2.outputs[8].hide_value = False
                if hasattr(group_input_002_2.outputs[8], 'name'):
                    group_input_002_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_002_2.outputs[8], 'show_expanded'):
                    group_input_002_2.outputs[8].show_expanded = False
                if hasattr(group_input_002_2.outputs[9], 'default_value'):
                    group_input_002_2.outputs[9].default_value = 1.0
                if hasattr(group_input_002_2.outputs[9], 'display_shape'):
                    group_input_002_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[9], 'enabled'):
                    group_input_002_2.outputs[9].enabled = True
                if hasattr(group_input_002_2.outputs[9], 'hide'):
                    group_input_002_2.outputs[9].hide = True
                if hasattr(group_input_002_2.outputs[9], 'hide_value'):
                    group_input_002_2.outputs[9].hide_value = False
                if hasattr(group_input_002_2.outputs[9], 'name'):
                    group_input_002_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_002_2.outputs[9], 'show_expanded'):
                    group_input_002_2.outputs[9].show_expanded = False
                if hasattr(group_input_002_2.outputs[10], 'default_value'):
                    group_input_002_2.outputs[10].default_value = 2.0
                if hasattr(group_input_002_2.outputs[10], 'display_shape'):
                    group_input_002_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[10], 'enabled'):
                    group_input_002_2.outputs[10].enabled = True
                if hasattr(group_input_002_2.outputs[10], 'hide'):
                    group_input_002_2.outputs[10].hide = True
                if hasattr(group_input_002_2.outputs[10], 'hide_value'):
                    group_input_002_2.outputs[10].hide_value = False
                if hasattr(group_input_002_2.outputs[10], 'name'):
                    group_input_002_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_002_2.outputs[10], 'show_expanded'):
                    group_input_002_2.outputs[10].show_expanded = False
                if hasattr(group_input_002_2.outputs[11], 'default_value'):
                    group_input_002_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_002_2.outputs[11], 'display_shape'):
                    group_input_002_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[11], 'enabled'):
                    group_input_002_2.outputs[11].enabled = True
                if hasattr(group_input_002_2.outputs[11], 'hide'):
                    group_input_002_2.outputs[11].hide = True
                if hasattr(group_input_002_2.outputs[11], 'hide_value'):
                    group_input_002_2.outputs[11].hide_value = False
                if hasattr(group_input_002_2.outputs[11], 'name'):
                    group_input_002_2.outputs[11].name = '    Hue'
                if hasattr(group_input_002_2.outputs[11], 'show_expanded'):
                    group_input_002_2.outputs[11].show_expanded = False
                if hasattr(group_input_002_2.outputs[12], 'default_value'):
                    group_input_002_2.outputs[12].default_value = 1.0
                if hasattr(group_input_002_2.outputs[12], 'display_shape'):
                    group_input_002_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[12], 'enabled'):
                    group_input_002_2.outputs[12].enabled = True
                if hasattr(group_input_002_2.outputs[12], 'hide'):
                    group_input_002_2.outputs[12].hide = True
                if hasattr(group_input_002_2.outputs[12], 'hide_value'):
                    group_input_002_2.outputs[12].hide_value = False
                if hasattr(group_input_002_2.outputs[12], 'name'):
                    group_input_002_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_002_2.outputs[12], 'show_expanded'):
                    group_input_002_2.outputs[12].show_expanded = False
                if hasattr(group_input_002_2.outputs[13], 'default_value'):
                    group_input_002_2.outputs[13].default_value = 0.0
                if hasattr(group_input_002_2.outputs[13], 'display_shape'):
                    group_input_002_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[13], 'enabled'):
                    group_input_002_2.outputs[13].enabled = True
                if hasattr(group_input_002_2.outputs[13], 'hide'):
                    group_input_002_2.outputs[13].hide = True
                if hasattr(group_input_002_2.outputs[13], 'hide_value'):
                    group_input_002_2.outputs[13].hide_value = True
                if hasattr(group_input_002_2.outputs[13], 'name'):
                    group_input_002_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_002_2.outputs[13], 'show_expanded'):
                    group_input_002_2.outputs[13].show_expanded = False
                if hasattr(group_input_002_2.outputs[14], 'default_value'):
                    group_input_002_2.outputs[14].default_value = 0.0
                if hasattr(group_input_002_2.outputs[14], 'display_shape'):
                    group_input_002_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[14], 'enabled'):
                    group_input_002_2.outputs[14].enabled = True
                if hasattr(group_input_002_2.outputs[14], 'hide'):
                    group_input_002_2.outputs[14].hide = True
                if hasattr(group_input_002_2.outputs[14], 'hide_value'):
                    group_input_002_2.outputs[14].hide_value = False
                if hasattr(group_input_002_2.outputs[14], 'name'):
                    group_input_002_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_002_2.outputs[14], 'show_expanded'):
                    group_input_002_2.outputs[14].show_expanded = False
                if hasattr(group_input_002_2.outputs[15], 'default_value'):
                    group_input_002_2.outputs[15].default_value = 0.0
                if hasattr(group_input_002_2.outputs[15], 'display_shape'):
                    group_input_002_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[15], 'enabled'):
                    group_input_002_2.outputs[15].enabled = True
                if hasattr(group_input_002_2.outputs[15], 'hide'):
                    group_input_002_2.outputs[15].hide = True
                if hasattr(group_input_002_2.outputs[15], 'hide_value'):
                    group_input_002_2.outputs[15].hide_value = False
                if hasattr(group_input_002_2.outputs[15], 'name'):
                    group_input_002_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_002_2.outputs[15], 'show_expanded'):
                    group_input_002_2.outputs[15].show_expanded = False
                if hasattr(group_input_002_2.outputs[16], 'default_value'):
                    group_input_002_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_002_2.outputs[16], 'display_shape'):
                    group_input_002_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[16], 'enabled'):
                    group_input_002_2.outputs[16].enabled = True
                if hasattr(group_input_002_2.outputs[16], 'hide'):
                    group_input_002_2.outputs[16].hide = True
                if hasattr(group_input_002_2.outputs[16], 'hide_value'):
                    group_input_002_2.outputs[16].hide_value = False
                if hasattr(group_input_002_2.outputs[16], 'name'):
                    group_input_002_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_002_2.outputs[16], 'show_expanded'):
                    group_input_002_2.outputs[16].show_expanded = False
                if hasattr(group_input_002_2.outputs[17], 'default_value'):
                    group_input_002_2.outputs[17].default_value = 0.5
                if hasattr(group_input_002_2.outputs[17], 'display_shape'):
                    group_input_002_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[17], 'enabled'):
                    group_input_002_2.outputs[17].enabled = True
                if hasattr(group_input_002_2.outputs[17], 'hide'):
                    group_input_002_2.outputs[17].hide = True
                if hasattr(group_input_002_2.outputs[17], 'hide_value'):
                    group_input_002_2.outputs[17].hide_value = False
                if hasattr(group_input_002_2.outputs[17], 'name'):
                    group_input_002_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_002_2.outputs[17], 'show_expanded'):
                    group_input_002_2.outputs[17].show_expanded = False
                if hasattr(group_input_002_2.outputs[18], 'default_value'):
                    group_input_002_2.outputs[18].default_value = 0.5
                if hasattr(group_input_002_2.outputs[18], 'display_shape'):
                    group_input_002_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[18], 'enabled'):
                    group_input_002_2.outputs[18].enabled = True
                if hasattr(group_input_002_2.outputs[18], 'hide'):
                    group_input_002_2.outputs[18].hide = True
                if hasattr(group_input_002_2.outputs[18], 'hide_value'):
                    group_input_002_2.outputs[18].hide_value = False
                if hasattr(group_input_002_2.outputs[18], 'name'):
                    group_input_002_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_002_2.outputs[18], 'show_expanded'):
                    group_input_002_2.outputs[18].show_expanded = False
                if hasattr(group_input_002_2.outputs[19], 'default_value'):
                    group_input_002_2.outputs[19].default_value = 0.5
                if hasattr(group_input_002_2.outputs[19], 'display_shape'):
                    group_input_002_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[19], 'enabled'):
                    group_input_002_2.outputs[19].enabled = True
                if hasattr(group_input_002_2.outputs[19], 'hide'):
                    group_input_002_2.outputs[19].hide = True
                if hasattr(group_input_002_2.outputs[19], 'hide_value'):
                    group_input_002_2.outputs[19].hide_value = False
                if hasattr(group_input_002_2.outputs[19], 'name'):
                    group_input_002_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_002_2.outputs[19], 'show_expanded'):
                    group_input_002_2.outputs[19].show_expanded = False

                map_range_004_2 = node_tree2.nodes.new('ShaderNodeMapRange')
                if hasattr(map_range_004_2, 'clamp'):
                    map_range_004_2.clamp = True
                if hasattr(map_range_004_2, 'color'):
                    map_range_004_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(map_range_004_2, 'data_type'):
                    map_range_004_2.data_type = 'FLOAT'
                if hasattr(map_range_004_2, 'hide'):
                    map_range_004_2.hide = False
                if hasattr(map_range_004_2, 'interpolation_type'):
                    map_range_004_2.interpolation_type = 'LINEAR'
                if hasattr(map_range_004_2, 'location'):
                    map_range_004_2.location = (-1440.0, -453.0)
                if hasattr(map_range_004_2, 'mute'):
                    map_range_004_2.mute = False
                if hasattr(map_range_004_2, 'name'):
                    map_range_004_2.name = 'Map Range.004'
                if hasattr(map_range_004_2, 'use_custom_color'):
                    map_range_004_2.use_custom_color = False
                if hasattr(map_range_004_2, 'width'):
                    map_range_004_2.width = 140.0
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='From Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='From Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='To Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = -3.725290298461914e-09
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='To Max'), None)
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
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='Steps'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 4.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = True
                    if hasattr(input_, 'name'):
                        input_.name = 'Vector'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='From_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='From_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='To_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='To_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_004_2.inputs if input_.identifier=='Steps_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (4.0, 4.0, 4.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in map_range_004_2.outputs if output.identifier=='Result'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in map_range_004_2.outputs if output.identifier=='Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Vector'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                map_range_2 = node_tree2.nodes.new('ShaderNodeMapRange')
                if hasattr(map_range_2, 'clamp'):
                    map_range_2.clamp = True
                if hasattr(map_range_2, 'color'):
                    map_range_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(map_range_2, 'data_type'):
                    map_range_2.data_type = 'FLOAT'
                if hasattr(map_range_2, 'hide'):
                    map_range_2.hide = False
                if hasattr(map_range_2, 'interpolation_type'):
                    map_range_2.interpolation_type = 'LINEAR'
                if hasattr(map_range_2, 'location'):
                    map_range_2.location = (-1440.0, -193.0)
                if hasattr(map_range_2, 'mute'):
                    map_range_2.mute = False
                if hasattr(map_range_2, 'name'):
                    map_range_2.name = 'Map Range'
                if hasattr(map_range_2, 'use_custom_color'):
                    map_range_2.use_custom_color = False
                if hasattr(map_range_2, 'width'):
                    map_range_2.width = 140.0
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='From Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='From Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='To Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = -2.200000047683716
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = False
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='To Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='Steps'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 4.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = True
                    if hasattr(input_, 'name'):
                        input_.name = 'Vector'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='From_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='From_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='To_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='To_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_2.inputs if input_.identifier=='Steps_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (4.0, 4.0, 4.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in map_range_2.outputs if output.identifier=='Result'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in map_range_2.outputs if output.identifier=='Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Vector'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                rainbow_saturation_2 = node_tree2.nodes.new('ShaderNodeMix')
                if hasattr(rainbow_saturation_2, 'blend_type'):
                    rainbow_saturation_2.blend_type = 'HUE'
                if hasattr(rainbow_saturation_2, 'clamp_factor'):
                    rainbow_saturation_2.clamp_factor = True
                if hasattr(rainbow_saturation_2, 'clamp_result'):
                    rainbow_saturation_2.clamp_result = False
                if hasattr(rainbow_saturation_2, 'color'):
                    rainbow_saturation_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(rainbow_saturation_2, 'data_type'):
                    rainbow_saturation_2.data_type = 'RGBA'
                if hasattr(rainbow_saturation_2, 'factor_mode'):
                    rainbow_saturation_2.factor_mode = 'UNIFORM'
                if hasattr(rainbow_saturation_2, 'hide'):
                    rainbow_saturation_2.hide = False
                if hasattr(rainbow_saturation_2, 'label'):
                    rainbow_saturation_2.label = 'Rainbow Saturation'
                if hasattr(rainbow_saturation_2, 'location'):
                    rainbow_saturation_2.location = (-1440.0, -314.0)
                if hasattr(rainbow_saturation_2, 'mute'):
                    rainbow_saturation_2.mute = False
                if hasattr(rainbow_saturation_2, 'name'):
                    rainbow_saturation_2.name = 'Rainbow Saturation'
                if hasattr(rainbow_saturation_2, 'use_custom_color'):
                    rainbow_saturation_2.use_custom_color = False
                if hasattr(rainbow_saturation_2, 'width'):
                    rainbow_saturation_2.width = 140.0
                input_ = next((input_ for input_ in rainbow_saturation_2.inputs if input_.identifier=='Factor_Float'), None)
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
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in rainbow_saturation_2.inputs if input_.identifier=='Factor_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.5, 0.5, 0.5)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in rainbow_saturation_2.inputs if input_.identifier=='A_Float'), None)
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
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in rainbow_saturation_2.inputs if input_.identifier=='B_Float'), None)
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
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in rainbow_saturation_2.inputs if input_.identifier=='A_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in rainbow_saturation_2.inputs if input_.identifier=='B_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in rainbow_saturation_2.inputs if input_.identifier=='A_Color'), None)
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
                input_ = next((input_ for input_ in rainbow_saturation_2.inputs if input_.identifier=='B_Color'), None)
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
                output = next((output for output in rainbow_saturation_2.outputs if output.identifier=='Result_Float'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in rainbow_saturation_2.outputs if output.identifier=='Result_Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in rainbow_saturation_2.outputs if output.identifier=='Result_Color'), None)
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

                group_input_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_2, 'color'):
                    group_input_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_2, 'hide'):
                    group_input_2.hide = False
                if hasattr(group_input_2, 'location'):
                    group_input_2.location = (-1440.0, 0.0)
                if hasattr(group_input_2, 'mute'):
                    group_input_2.mute = False
                if hasattr(group_input_2, 'name'):
                    group_input_2.name = 'Group Input'
                if hasattr(group_input_2, 'use_custom_color'):
                    group_input_2.use_custom_color = True
                if hasattr(group_input_2, 'width'):
                    group_input_2.width = 140.0
                if hasattr(group_input_2.outputs[0], 'default_value'):
                    group_input_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_2.outputs[0], 'display_shape'):
                    group_input_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[0], 'enabled'):
                    group_input_2.outputs[0].enabled = True
                if hasattr(group_input_2.outputs[0], 'hide'):
                    group_input_2.outputs[0].hide = True
                if hasattr(group_input_2.outputs[0], 'hide_value'):
                    group_input_2.outputs[0].hide_value = False
                if hasattr(group_input_2.outputs[0], 'name'):
                    group_input_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_2.outputs[0], 'show_expanded'):
                    group_input_2.outputs[0].show_expanded = False
                if hasattr(group_input_2.outputs[1], 'default_value'):
                    group_input_2.outputs[1].default_value = 0.0
                if hasattr(group_input_2.outputs[1], 'display_shape'):
                    group_input_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[1], 'enabled'):
                    group_input_2.outputs[1].enabled = True
                if hasattr(group_input_2.outputs[1], 'hide'):
                    group_input_2.outputs[1].hide = True
                if hasattr(group_input_2.outputs[1], 'hide_value'):
                    group_input_2.outputs[1].hide_value = True
                if hasattr(group_input_2.outputs[1], 'name'):
                    group_input_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_2.outputs[1], 'show_expanded'):
                    group_input_2.outputs[1].show_expanded = False
                if hasattr(group_input_2.outputs[2], 'default_value'):
                    group_input_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_2.outputs[2], 'display_shape'):
                    group_input_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[2], 'enabled'):
                    group_input_2.outputs[2].enabled = True
                if hasattr(group_input_2.outputs[2], 'hide'):
                    group_input_2.outputs[2].hide = True
                if hasattr(group_input_2.outputs[2], 'hide_value'):
                    group_input_2.outputs[2].hide_value = False
                if hasattr(group_input_2.outputs[2], 'name'):
                    group_input_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_2.outputs[2], 'show_expanded'):
                    group_input_2.outputs[2].show_expanded = False
                if hasattr(group_input_2.outputs[3], 'default_value'):
                    group_input_2.outputs[3].default_value = 0.5
                if hasattr(group_input_2.outputs[3], 'display_shape'):
                    group_input_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[3], 'enabled'):
                    group_input_2.outputs[3].enabled = True
                if hasattr(group_input_2.outputs[3], 'hide'):
                    group_input_2.outputs[3].hide = True
                if hasattr(group_input_2.outputs[3], 'hide_value'):
                    group_input_2.outputs[3].hide_value = False
                if hasattr(group_input_2.outputs[3], 'name'):
                    group_input_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_2.outputs[3], 'show_expanded'):
                    group_input_2.outputs[3].show_expanded = False
                if hasattr(group_input_2.outputs[4], 'default_value'):
                    group_input_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_2.outputs[4], 'display_shape'):
                    group_input_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[4], 'enabled'):
                    group_input_2.outputs[4].enabled = True
                if hasattr(group_input_2.outputs[4], 'hide'):
                    group_input_2.outputs[4].hide = True
                if hasattr(group_input_2.outputs[4], 'hide_value'):
                    group_input_2.outputs[4].hide_value = False
                if hasattr(group_input_2.outputs[4], 'name'):
                    group_input_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_2.outputs[4], 'show_expanded'):
                    group_input_2.outputs[4].show_expanded = False
                if hasattr(group_input_2.outputs[5], 'default_value'):
                    group_input_2.outputs[5].default_value = 0.0
                if hasattr(group_input_2.outputs[5], 'display_shape'):
                    group_input_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[5], 'enabled'):
                    group_input_2.outputs[5].enabled = True
                if hasattr(group_input_2.outputs[5], 'hide'):
                    group_input_2.outputs[5].hide = True
                if hasattr(group_input_2.outputs[5], 'hide_value'):
                    group_input_2.outputs[5].hide_value = True
                if hasattr(group_input_2.outputs[5], 'name'):
                    group_input_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_2.outputs[5], 'show_expanded'):
                    group_input_2.outputs[5].show_expanded = False
                if hasattr(group_input_2.outputs[6], 'default_value'):
                    group_input_2.outputs[6].default_value = 0.5
                if hasattr(group_input_2.outputs[6], 'display_shape'):
                    group_input_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[6], 'enabled'):
                    group_input_2.outputs[6].enabled = True
                if hasattr(group_input_2.outputs[6], 'hide'):
                    group_input_2.outputs[6].hide = True
                if hasattr(group_input_2.outputs[6], 'hide_value'):
                    group_input_2.outputs[6].hide_value = False
                if hasattr(group_input_2.outputs[6], 'name'):
                    group_input_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_2.outputs[6], 'show_expanded'):
                    group_input_2.outputs[6].show_expanded = False
                if hasattr(group_input_2.outputs[7], 'default_value'):
                    group_input_2.outputs[7].default_value = 0.0
                if hasattr(group_input_2.outputs[7], 'display_shape'):
                    group_input_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[7], 'enabled'):
                    group_input_2.outputs[7].enabled = True
                if hasattr(group_input_2.outputs[7], 'hide'):
                    group_input_2.outputs[7].hide = True
                if hasattr(group_input_2.outputs[7], 'hide_value'):
                    group_input_2.outputs[7].hide_value = False
                if hasattr(group_input_2.outputs[7], 'name'):
                    group_input_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_2.outputs[7], 'show_expanded'):
                    group_input_2.outputs[7].show_expanded = False
                if hasattr(group_input_2.outputs[8], 'default_value'):
                    group_input_2.outputs[8].default_value = 0.0
                if hasattr(group_input_2.outputs[8], 'display_shape'):
                    group_input_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[8], 'enabled'):
                    group_input_2.outputs[8].enabled = True
                if hasattr(group_input_2.outputs[8], 'hide'):
                    group_input_2.outputs[8].hide = True
                if hasattr(group_input_2.outputs[8], 'hide_value'):
                    group_input_2.outputs[8].hide_value = False
                if hasattr(group_input_2.outputs[8], 'name'):
                    group_input_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_2.outputs[8], 'show_expanded'):
                    group_input_2.outputs[8].show_expanded = False
                if hasattr(group_input_2.outputs[9], 'default_value'):
                    group_input_2.outputs[9].default_value = 1.0
                if hasattr(group_input_2.outputs[9], 'display_shape'):
                    group_input_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[9], 'enabled'):
                    group_input_2.outputs[9].enabled = True
                if hasattr(group_input_2.outputs[9], 'hide'):
                    group_input_2.outputs[9].hide = True
                if hasattr(group_input_2.outputs[9], 'hide_value'):
                    group_input_2.outputs[9].hide_value = False
                if hasattr(group_input_2.outputs[9], 'name'):
                    group_input_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_2.outputs[9], 'show_expanded'):
                    group_input_2.outputs[9].show_expanded = False
                if hasattr(group_input_2.outputs[10], 'default_value'):
                    group_input_2.outputs[10].default_value = 2.0
                if hasattr(group_input_2.outputs[10], 'display_shape'):
                    group_input_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[10], 'enabled'):
                    group_input_2.outputs[10].enabled = True
                if hasattr(group_input_2.outputs[10], 'hide'):
                    group_input_2.outputs[10].hide = True
                if hasattr(group_input_2.outputs[10], 'hide_value'):
                    group_input_2.outputs[10].hide_value = False
                if hasattr(group_input_2.outputs[10], 'name'):
                    group_input_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_2.outputs[10], 'show_expanded'):
                    group_input_2.outputs[10].show_expanded = False
                if hasattr(group_input_2.outputs[11], 'default_value'):
                    group_input_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_2.outputs[11], 'display_shape'):
                    group_input_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[11], 'enabled'):
                    group_input_2.outputs[11].enabled = True
                if hasattr(group_input_2.outputs[11], 'hide'):
                    group_input_2.outputs[11].hide = True
                if hasattr(group_input_2.outputs[11], 'hide_value'):
                    group_input_2.outputs[11].hide_value = False
                if hasattr(group_input_2.outputs[11], 'name'):
                    group_input_2.outputs[11].name = '    Hue'
                if hasattr(group_input_2.outputs[11], 'show_expanded'):
                    group_input_2.outputs[11].show_expanded = False
                if hasattr(group_input_2.outputs[12], 'default_value'):
                    group_input_2.outputs[12].default_value = 1.0
                if hasattr(group_input_2.outputs[12], 'display_shape'):
                    group_input_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[12], 'enabled'):
                    group_input_2.outputs[12].enabled = True
                if hasattr(group_input_2.outputs[12], 'hide'):
                    group_input_2.outputs[12].hide = True
                if hasattr(group_input_2.outputs[12], 'hide_value'):
                    group_input_2.outputs[12].hide_value = False
                if hasattr(group_input_2.outputs[12], 'name'):
                    group_input_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_2.outputs[12], 'show_expanded'):
                    group_input_2.outputs[12].show_expanded = False
                if hasattr(group_input_2.outputs[13], 'default_value'):
                    group_input_2.outputs[13].default_value = 0.0
                if hasattr(group_input_2.outputs[13], 'display_shape'):
                    group_input_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[13], 'enabled'):
                    group_input_2.outputs[13].enabled = True
                if hasattr(group_input_2.outputs[13], 'hide'):
                    group_input_2.outputs[13].hide = True
                if hasattr(group_input_2.outputs[13], 'hide_value'):
                    group_input_2.outputs[13].hide_value = True
                if hasattr(group_input_2.outputs[13], 'name'):
                    group_input_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_2.outputs[13], 'show_expanded'):
                    group_input_2.outputs[13].show_expanded = False
                if hasattr(group_input_2.outputs[14], 'default_value'):
                    group_input_2.outputs[14].default_value = 0.0
                if hasattr(group_input_2.outputs[14], 'display_shape'):
                    group_input_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[14], 'enabled'):
                    group_input_2.outputs[14].enabled = True
                if hasattr(group_input_2.outputs[14], 'hide'):
                    group_input_2.outputs[14].hide = True
                if hasattr(group_input_2.outputs[14], 'hide_value'):
                    group_input_2.outputs[14].hide_value = False
                if hasattr(group_input_2.outputs[14], 'name'):
                    group_input_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_2.outputs[14], 'show_expanded'):
                    group_input_2.outputs[14].show_expanded = False
                if hasattr(group_input_2.outputs[15], 'default_value'):
                    group_input_2.outputs[15].default_value = 0.0
                if hasattr(group_input_2.outputs[15], 'display_shape'):
                    group_input_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[15], 'enabled'):
                    group_input_2.outputs[15].enabled = True
                if hasattr(group_input_2.outputs[15], 'hide'):
                    group_input_2.outputs[15].hide = True
                if hasattr(group_input_2.outputs[15], 'hide_value'):
                    group_input_2.outputs[15].hide_value = False
                if hasattr(group_input_2.outputs[15], 'name'):
                    group_input_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_2.outputs[15], 'show_expanded'):
                    group_input_2.outputs[15].show_expanded = False
                if hasattr(group_input_2.outputs[16], 'default_value'):
                    group_input_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_2.outputs[16], 'display_shape'):
                    group_input_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[16], 'enabled'):
                    group_input_2.outputs[16].enabled = True
                if hasattr(group_input_2.outputs[16], 'hide'):
                    group_input_2.outputs[16].hide = True
                if hasattr(group_input_2.outputs[16], 'hide_value'):
                    group_input_2.outputs[16].hide_value = False
                if hasattr(group_input_2.outputs[16], 'name'):
                    group_input_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_2.outputs[16], 'show_expanded'):
                    group_input_2.outputs[16].show_expanded = False
                if hasattr(group_input_2.outputs[17], 'default_value'):
                    group_input_2.outputs[17].default_value = 0.5
                if hasattr(group_input_2.outputs[17], 'display_shape'):
                    group_input_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[17], 'enabled'):
                    group_input_2.outputs[17].enabled = True
                if hasattr(group_input_2.outputs[17], 'hide'):
                    group_input_2.outputs[17].hide = True
                if hasattr(group_input_2.outputs[17], 'hide_value'):
                    group_input_2.outputs[17].hide_value = False
                if hasattr(group_input_2.outputs[17], 'name'):
                    group_input_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_2.outputs[17], 'show_expanded'):
                    group_input_2.outputs[17].show_expanded = False
                if hasattr(group_input_2.outputs[18], 'default_value'):
                    group_input_2.outputs[18].default_value = 0.5
                if hasattr(group_input_2.outputs[18], 'display_shape'):
                    group_input_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[18], 'enabled'):
                    group_input_2.outputs[18].enabled = True
                if hasattr(group_input_2.outputs[18], 'hide'):
                    group_input_2.outputs[18].hide = False
                if hasattr(group_input_2.outputs[18], 'hide_value'):
                    group_input_2.outputs[18].hide_value = False
                if hasattr(group_input_2.outputs[18], 'name'):
                    group_input_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_2.outputs[18], 'show_expanded'):
                    group_input_2.outputs[18].show_expanded = False
                if hasattr(group_input_2.outputs[19], 'default_value'):
                    group_input_2.outputs[19].default_value = 0.5
                if hasattr(group_input_2.outputs[19], 'display_shape'):
                    group_input_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[19], 'enabled'):
                    group_input_2.outputs[19].enabled = True
                if hasattr(group_input_2.outputs[19], 'hide'):
                    group_input_2.outputs[19].hide = True
                if hasattr(group_input_2.outputs[19], 'hide_value'):
                    group_input_2.outputs[19].hide_value = False
                if hasattr(group_input_2.outputs[19], 'name'):
                    group_input_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_2.outputs[19], 'show_expanded'):
                    group_input_2.outputs[19].show_expanded = False

                map_range_001_2 = node_tree2.nodes.new('ShaderNodeMapRange')
                if hasattr(map_range_001_2, 'clamp'):
                    map_range_001_2.clamp = True
                if hasattr(map_range_001_2, 'color'):
                    map_range_001_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(map_range_001_2, 'data_type'):
                    map_range_001_2.data_type = 'FLOAT'
                if hasattr(map_range_001_2, 'hide'):
                    map_range_001_2.hide = False
                if hasattr(map_range_001_2, 'interpolation_type'):
                    map_range_001_2.interpolation_type = 'LINEAR'
                if hasattr(map_range_001_2, 'location'):
                    map_range_001_2.location = (-1440.0, -72.0)
                if hasattr(map_range_001_2, 'mute'):
                    map_range_001_2.mute = False
                if hasattr(map_range_001_2, 'name'):
                    map_range_001_2.name = 'Map Range.001'
                if hasattr(map_range_001_2, 'use_custom_color'):
                    map_range_001_2.use_custom_color = False
                if hasattr(map_range_001_2, 'width'):
                    map_range_001_2.width = 140.0
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='From Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='From Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='To Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = -2.619999885559082
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = False
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='To Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='Steps'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 9.899999618530273
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = True
                    if hasattr(input_, 'name'):
                        input_.name = 'Vector'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='From_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='From_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='To_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='To_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_001_2.inputs if input_.identifier=='Steps_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (4.0, 4.0, 4.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in map_range_001_2.outputs if output.identifier=='Result'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in map_range_001_2.outputs if output.identifier=='Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Vector'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                group_input_008_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_008_2, 'color'):
                    group_input_008_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_008_2, 'hide'):
                    group_input_008_2.hide = False
                if hasattr(group_input_008_2, 'location'):
                    group_input_008_2.location = (-1120.0, -161.0)
                if hasattr(group_input_008_2, 'mute'):
                    group_input_008_2.mute = False
                if hasattr(group_input_008_2, 'name'):
                    group_input_008_2.name = 'Group Input.008'
                if hasattr(group_input_008_2, 'use_custom_color'):
                    group_input_008_2.use_custom_color = True
                if hasattr(group_input_008_2, 'width'):
                    group_input_008_2.width = 140.0
                if hasattr(group_input_008_2.outputs[0], 'default_value'):
                    group_input_008_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_008_2.outputs[0], 'display_shape'):
                    group_input_008_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[0], 'enabled'):
                    group_input_008_2.outputs[0].enabled = True
                if hasattr(group_input_008_2.outputs[0], 'hide'):
                    group_input_008_2.outputs[0].hide = True
                if hasattr(group_input_008_2.outputs[0], 'hide_value'):
                    group_input_008_2.outputs[0].hide_value = False
                if hasattr(group_input_008_2.outputs[0], 'name'):
                    group_input_008_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_008_2.outputs[0], 'show_expanded'):
                    group_input_008_2.outputs[0].show_expanded = False
                if hasattr(group_input_008_2.outputs[1], 'default_value'):
                    group_input_008_2.outputs[1].default_value = 0.0
                if hasattr(group_input_008_2.outputs[1], 'display_shape'):
                    group_input_008_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[1], 'enabled'):
                    group_input_008_2.outputs[1].enabled = True
                if hasattr(group_input_008_2.outputs[1], 'hide'):
                    group_input_008_2.outputs[1].hide = True
                if hasattr(group_input_008_2.outputs[1], 'hide_value'):
                    group_input_008_2.outputs[1].hide_value = True
                if hasattr(group_input_008_2.outputs[1], 'name'):
                    group_input_008_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_008_2.outputs[1], 'show_expanded'):
                    group_input_008_2.outputs[1].show_expanded = False
                if hasattr(group_input_008_2.outputs[2], 'default_value'):
                    group_input_008_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_008_2.outputs[2], 'display_shape'):
                    group_input_008_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[2], 'enabled'):
                    group_input_008_2.outputs[2].enabled = True
                if hasattr(group_input_008_2.outputs[2], 'hide'):
                    group_input_008_2.outputs[2].hide = True
                if hasattr(group_input_008_2.outputs[2], 'hide_value'):
                    group_input_008_2.outputs[2].hide_value = False
                if hasattr(group_input_008_2.outputs[2], 'name'):
                    group_input_008_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_008_2.outputs[2], 'show_expanded'):
                    group_input_008_2.outputs[2].show_expanded = False
                if hasattr(group_input_008_2.outputs[3], 'default_value'):
                    group_input_008_2.outputs[3].default_value = 0.5
                if hasattr(group_input_008_2.outputs[3], 'display_shape'):
                    group_input_008_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[3], 'enabled'):
                    group_input_008_2.outputs[3].enabled = True
                if hasattr(group_input_008_2.outputs[3], 'hide'):
                    group_input_008_2.outputs[3].hide = True
                if hasattr(group_input_008_2.outputs[3], 'hide_value'):
                    group_input_008_2.outputs[3].hide_value = False
                if hasattr(group_input_008_2.outputs[3], 'name'):
                    group_input_008_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_008_2.outputs[3], 'show_expanded'):
                    group_input_008_2.outputs[3].show_expanded = False
                if hasattr(group_input_008_2.outputs[4], 'default_value'):
                    group_input_008_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_008_2.outputs[4], 'display_shape'):
                    group_input_008_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[4], 'enabled'):
                    group_input_008_2.outputs[4].enabled = True
                if hasattr(group_input_008_2.outputs[4], 'hide'):
                    group_input_008_2.outputs[4].hide = True
                if hasattr(group_input_008_2.outputs[4], 'hide_value'):
                    group_input_008_2.outputs[4].hide_value = False
                if hasattr(group_input_008_2.outputs[4], 'name'):
                    group_input_008_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_008_2.outputs[4], 'show_expanded'):
                    group_input_008_2.outputs[4].show_expanded = False
                if hasattr(group_input_008_2.outputs[5], 'default_value'):
                    group_input_008_2.outputs[5].default_value = 0.0
                if hasattr(group_input_008_2.outputs[5], 'display_shape'):
                    group_input_008_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[5], 'enabled'):
                    group_input_008_2.outputs[5].enabled = True
                if hasattr(group_input_008_2.outputs[5], 'hide'):
                    group_input_008_2.outputs[5].hide = True
                if hasattr(group_input_008_2.outputs[5], 'hide_value'):
                    group_input_008_2.outputs[5].hide_value = True
                if hasattr(group_input_008_2.outputs[5], 'name'):
                    group_input_008_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_008_2.outputs[5], 'show_expanded'):
                    group_input_008_2.outputs[5].show_expanded = False
                if hasattr(group_input_008_2.outputs[6], 'default_value'):
                    group_input_008_2.outputs[6].default_value = 0.5
                if hasattr(group_input_008_2.outputs[6], 'display_shape'):
                    group_input_008_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[6], 'enabled'):
                    group_input_008_2.outputs[6].enabled = True
                if hasattr(group_input_008_2.outputs[6], 'hide'):
                    group_input_008_2.outputs[6].hide = True
                if hasattr(group_input_008_2.outputs[6], 'hide_value'):
                    group_input_008_2.outputs[6].hide_value = False
                if hasattr(group_input_008_2.outputs[6], 'name'):
                    group_input_008_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_008_2.outputs[6], 'show_expanded'):
                    group_input_008_2.outputs[6].show_expanded = False
                if hasattr(group_input_008_2.outputs[7], 'default_value'):
                    group_input_008_2.outputs[7].default_value = 0.0
                if hasattr(group_input_008_2.outputs[7], 'display_shape'):
                    group_input_008_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[7], 'enabled'):
                    group_input_008_2.outputs[7].enabled = True
                if hasattr(group_input_008_2.outputs[7], 'hide'):
                    group_input_008_2.outputs[7].hide = True
                if hasattr(group_input_008_2.outputs[7], 'hide_value'):
                    group_input_008_2.outputs[7].hide_value = False
                if hasattr(group_input_008_2.outputs[7], 'name'):
                    group_input_008_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_008_2.outputs[7], 'show_expanded'):
                    group_input_008_2.outputs[7].show_expanded = False
                if hasattr(group_input_008_2.outputs[8], 'default_value'):
                    group_input_008_2.outputs[8].default_value = 0.0
                if hasattr(group_input_008_2.outputs[8], 'display_shape'):
                    group_input_008_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[8], 'enabled'):
                    group_input_008_2.outputs[8].enabled = True
                if hasattr(group_input_008_2.outputs[8], 'hide'):
                    group_input_008_2.outputs[8].hide = False
                if hasattr(group_input_008_2.outputs[8], 'hide_value'):
                    group_input_008_2.outputs[8].hide_value = False
                if hasattr(group_input_008_2.outputs[8], 'name'):
                    group_input_008_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_008_2.outputs[8], 'show_expanded'):
                    group_input_008_2.outputs[8].show_expanded = False
                if hasattr(group_input_008_2.outputs[9], 'default_value'):
                    group_input_008_2.outputs[9].default_value = 1.0
                if hasattr(group_input_008_2.outputs[9], 'display_shape'):
                    group_input_008_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[9], 'enabled'):
                    group_input_008_2.outputs[9].enabled = True
                if hasattr(group_input_008_2.outputs[9], 'hide'):
                    group_input_008_2.outputs[9].hide = True
                if hasattr(group_input_008_2.outputs[9], 'hide_value'):
                    group_input_008_2.outputs[9].hide_value = False
                if hasattr(group_input_008_2.outputs[9], 'name'):
                    group_input_008_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_008_2.outputs[9], 'show_expanded'):
                    group_input_008_2.outputs[9].show_expanded = False
                if hasattr(group_input_008_2.outputs[10], 'default_value'):
                    group_input_008_2.outputs[10].default_value = 2.0
                if hasattr(group_input_008_2.outputs[10], 'display_shape'):
                    group_input_008_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[10], 'enabled'):
                    group_input_008_2.outputs[10].enabled = True
                if hasattr(group_input_008_2.outputs[10], 'hide'):
                    group_input_008_2.outputs[10].hide = True
                if hasattr(group_input_008_2.outputs[10], 'hide_value'):
                    group_input_008_2.outputs[10].hide_value = False
                if hasattr(group_input_008_2.outputs[10], 'name'):
                    group_input_008_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_008_2.outputs[10], 'show_expanded'):
                    group_input_008_2.outputs[10].show_expanded = False
                if hasattr(group_input_008_2.outputs[11], 'default_value'):
                    group_input_008_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_008_2.outputs[11], 'display_shape'):
                    group_input_008_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[11], 'enabled'):
                    group_input_008_2.outputs[11].enabled = True
                if hasattr(group_input_008_2.outputs[11], 'hide'):
                    group_input_008_2.outputs[11].hide = True
                if hasattr(group_input_008_2.outputs[11], 'hide_value'):
                    group_input_008_2.outputs[11].hide_value = False
                if hasattr(group_input_008_2.outputs[11], 'name'):
                    group_input_008_2.outputs[11].name = '    Hue'
                if hasattr(group_input_008_2.outputs[11], 'show_expanded'):
                    group_input_008_2.outputs[11].show_expanded = False
                if hasattr(group_input_008_2.outputs[12], 'default_value'):
                    group_input_008_2.outputs[12].default_value = 1.0
                if hasattr(group_input_008_2.outputs[12], 'display_shape'):
                    group_input_008_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[12], 'enabled'):
                    group_input_008_2.outputs[12].enabled = True
                if hasattr(group_input_008_2.outputs[12], 'hide'):
                    group_input_008_2.outputs[12].hide = True
                if hasattr(group_input_008_2.outputs[12], 'hide_value'):
                    group_input_008_2.outputs[12].hide_value = False
                if hasattr(group_input_008_2.outputs[12], 'name'):
                    group_input_008_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_008_2.outputs[12], 'show_expanded'):
                    group_input_008_2.outputs[12].show_expanded = False
                if hasattr(group_input_008_2.outputs[13], 'default_value'):
                    group_input_008_2.outputs[13].default_value = 0.0
                if hasattr(group_input_008_2.outputs[13], 'display_shape'):
                    group_input_008_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[13], 'enabled'):
                    group_input_008_2.outputs[13].enabled = True
                if hasattr(group_input_008_2.outputs[13], 'hide'):
                    group_input_008_2.outputs[13].hide = True
                if hasattr(group_input_008_2.outputs[13], 'hide_value'):
                    group_input_008_2.outputs[13].hide_value = True
                if hasattr(group_input_008_2.outputs[13], 'name'):
                    group_input_008_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_008_2.outputs[13], 'show_expanded'):
                    group_input_008_2.outputs[13].show_expanded = False
                if hasattr(group_input_008_2.outputs[14], 'default_value'):
                    group_input_008_2.outputs[14].default_value = 0.0
                if hasattr(group_input_008_2.outputs[14], 'display_shape'):
                    group_input_008_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[14], 'enabled'):
                    group_input_008_2.outputs[14].enabled = True
                if hasattr(group_input_008_2.outputs[14], 'hide'):
                    group_input_008_2.outputs[14].hide = True
                if hasattr(group_input_008_2.outputs[14], 'hide_value'):
                    group_input_008_2.outputs[14].hide_value = False
                if hasattr(group_input_008_2.outputs[14], 'name'):
                    group_input_008_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_008_2.outputs[14], 'show_expanded'):
                    group_input_008_2.outputs[14].show_expanded = False
                if hasattr(group_input_008_2.outputs[15], 'default_value'):
                    group_input_008_2.outputs[15].default_value = 0.0
                if hasattr(group_input_008_2.outputs[15], 'display_shape'):
                    group_input_008_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[15], 'enabled'):
                    group_input_008_2.outputs[15].enabled = True
                if hasattr(group_input_008_2.outputs[15], 'hide'):
                    group_input_008_2.outputs[15].hide = False
                if hasattr(group_input_008_2.outputs[15], 'hide_value'):
                    group_input_008_2.outputs[15].hide_value = False
                if hasattr(group_input_008_2.outputs[15], 'name'):
                    group_input_008_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_008_2.outputs[15], 'show_expanded'):
                    group_input_008_2.outputs[15].show_expanded = False
                if hasattr(group_input_008_2.outputs[16], 'default_value'):
                    group_input_008_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_008_2.outputs[16], 'display_shape'):
                    group_input_008_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[16], 'enabled'):
                    group_input_008_2.outputs[16].enabled = True
                if hasattr(group_input_008_2.outputs[16], 'hide'):
                    group_input_008_2.outputs[16].hide = True
                if hasattr(group_input_008_2.outputs[16], 'hide_value'):
                    group_input_008_2.outputs[16].hide_value = False
                if hasattr(group_input_008_2.outputs[16], 'name'):
                    group_input_008_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_008_2.outputs[16], 'show_expanded'):
                    group_input_008_2.outputs[16].show_expanded = False
                if hasattr(group_input_008_2.outputs[17], 'default_value'):
                    group_input_008_2.outputs[17].default_value = 0.5
                if hasattr(group_input_008_2.outputs[17], 'display_shape'):
                    group_input_008_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[17], 'enabled'):
                    group_input_008_2.outputs[17].enabled = True
                if hasattr(group_input_008_2.outputs[17], 'hide'):
                    group_input_008_2.outputs[17].hide = True
                if hasattr(group_input_008_2.outputs[17], 'hide_value'):
                    group_input_008_2.outputs[17].hide_value = False
                if hasattr(group_input_008_2.outputs[17], 'name'):
                    group_input_008_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_008_2.outputs[17], 'show_expanded'):
                    group_input_008_2.outputs[17].show_expanded = False
                if hasattr(group_input_008_2.outputs[18], 'default_value'):
                    group_input_008_2.outputs[18].default_value = 0.5
                if hasattr(group_input_008_2.outputs[18], 'display_shape'):
                    group_input_008_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[18], 'enabled'):
                    group_input_008_2.outputs[18].enabled = True
                if hasattr(group_input_008_2.outputs[18], 'hide'):
                    group_input_008_2.outputs[18].hide = True
                if hasattr(group_input_008_2.outputs[18], 'hide_value'):
                    group_input_008_2.outputs[18].hide_value = False
                if hasattr(group_input_008_2.outputs[18], 'name'):
                    group_input_008_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_008_2.outputs[18], 'show_expanded'):
                    group_input_008_2.outputs[18].show_expanded = False
                if hasattr(group_input_008_2.outputs[19], 'default_value'):
                    group_input_008_2.outputs[19].default_value = 0.5
                if hasattr(group_input_008_2.outputs[19], 'display_shape'):
                    group_input_008_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_008_2.outputs[19], 'enabled'):
                    group_input_008_2.outputs[19].enabled = True
                if hasattr(group_input_008_2.outputs[19], 'hide'):
                    group_input_008_2.outputs[19].hide = True
                if hasattr(group_input_008_2.outputs[19], 'hide_value'):
                    group_input_008_2.outputs[19].hide_value = False
                if hasattr(group_input_008_2.outputs[19], 'name'):
                    group_input_008_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_008_2.outputs[19], 'show_expanded'):
                    group_input_008_2.outputs[19].show_expanded = False

                hue_saturation_value_2 = node_tree2.nodes.new('ShaderNodeHueSaturation')
                if hasattr(hue_saturation_value_2, 'color'):
                    hue_saturation_value_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(hue_saturation_value_2, 'hide'):
                    hue_saturation_value_2.hide = False
                if hasattr(hue_saturation_value_2, 'location'):
                    hue_saturation_value_2.location = (-1120.0, 0.0)
                if hasattr(hue_saturation_value_2, 'mute'):
                    hue_saturation_value_2.mute = False
                if hasattr(hue_saturation_value_2, 'name'):
                    hue_saturation_value_2.name = 'Hue Saturation Value'
                if hasattr(hue_saturation_value_2, 'use_custom_color'):
                    hue_saturation_value_2.use_custom_color = False
                if hasattr(hue_saturation_value_2, 'width'):
                    hue_saturation_value_2.width = 140.0
                input_ = next((input_ for input_ in hue_saturation_value_2.inputs if input_.identifier=='Hue'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.4999999701976776
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Hue'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in hue_saturation_value_2.inputs if input_.identifier=='Saturation'), None)
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
                        input_.name = 'Saturation'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in hue_saturation_value_2.inputs if input_.identifier=='Value'), None)
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
                        input_.name = 'Value'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in hue_saturation_value_2.inputs if input_.identifier=='Fac'), None)
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
                        input_.name = 'Fac'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in hue_saturation_value_2.inputs if input_.identifier=='Color'), None)
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
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in hue_saturation_value_2.outputs if output.identifier=='Color'), None)
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

                group_input_009_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_009_2, 'color'):
                    group_input_009_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_009_2, 'hide'):
                    group_input_009_2.hide = False
                if hasattr(group_input_009_2, 'location'):
                    group_input_009_2.location = (-960.0, -139.0)
                if hasattr(group_input_009_2, 'mute'):
                    group_input_009_2.mute = False
                if hasattr(group_input_009_2, 'name'):
                    group_input_009_2.name = 'Group Input.009'
                if hasattr(group_input_009_2, 'use_custom_color'):
                    group_input_009_2.use_custom_color = True
                if hasattr(group_input_009_2, 'width'):
                    group_input_009_2.width = 140.0
                if hasattr(group_input_009_2.outputs[0], 'default_value'):
                    group_input_009_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_009_2.outputs[0], 'display_shape'):
                    group_input_009_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[0], 'enabled'):
                    group_input_009_2.outputs[0].enabled = True
                if hasattr(group_input_009_2.outputs[0], 'hide'):
                    group_input_009_2.outputs[0].hide = True
                if hasattr(group_input_009_2.outputs[0], 'hide_value'):
                    group_input_009_2.outputs[0].hide_value = False
                if hasattr(group_input_009_2.outputs[0], 'name'):
                    group_input_009_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_009_2.outputs[0], 'show_expanded'):
                    group_input_009_2.outputs[0].show_expanded = False
                if hasattr(group_input_009_2.outputs[1], 'default_value'):
                    group_input_009_2.outputs[1].default_value = 0.0
                if hasattr(group_input_009_2.outputs[1], 'display_shape'):
                    group_input_009_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[1], 'enabled'):
                    group_input_009_2.outputs[1].enabled = True
                if hasattr(group_input_009_2.outputs[1], 'hide'):
                    group_input_009_2.outputs[1].hide = True
                if hasattr(group_input_009_2.outputs[1], 'hide_value'):
                    group_input_009_2.outputs[1].hide_value = True
                if hasattr(group_input_009_2.outputs[1], 'name'):
                    group_input_009_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_009_2.outputs[1], 'show_expanded'):
                    group_input_009_2.outputs[1].show_expanded = False
                if hasattr(group_input_009_2.outputs[2], 'default_value'):
                    group_input_009_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_009_2.outputs[2], 'display_shape'):
                    group_input_009_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[2], 'enabled'):
                    group_input_009_2.outputs[2].enabled = True
                if hasattr(group_input_009_2.outputs[2], 'hide'):
                    group_input_009_2.outputs[2].hide = True
                if hasattr(group_input_009_2.outputs[2], 'hide_value'):
                    group_input_009_2.outputs[2].hide_value = False
                if hasattr(group_input_009_2.outputs[2], 'name'):
                    group_input_009_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_009_2.outputs[2], 'show_expanded'):
                    group_input_009_2.outputs[2].show_expanded = False
                if hasattr(group_input_009_2.outputs[3], 'default_value'):
                    group_input_009_2.outputs[3].default_value = 0.5
                if hasattr(group_input_009_2.outputs[3], 'display_shape'):
                    group_input_009_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[3], 'enabled'):
                    group_input_009_2.outputs[3].enabled = True
                if hasattr(group_input_009_2.outputs[3], 'hide'):
                    group_input_009_2.outputs[3].hide = True
                if hasattr(group_input_009_2.outputs[3], 'hide_value'):
                    group_input_009_2.outputs[3].hide_value = False
                if hasattr(group_input_009_2.outputs[3], 'name'):
                    group_input_009_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_009_2.outputs[3], 'show_expanded'):
                    group_input_009_2.outputs[3].show_expanded = False
                if hasattr(group_input_009_2.outputs[4], 'default_value'):
                    group_input_009_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_009_2.outputs[4], 'display_shape'):
                    group_input_009_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[4], 'enabled'):
                    group_input_009_2.outputs[4].enabled = True
                if hasattr(group_input_009_2.outputs[4], 'hide'):
                    group_input_009_2.outputs[4].hide = True
                if hasattr(group_input_009_2.outputs[4], 'hide_value'):
                    group_input_009_2.outputs[4].hide_value = False
                if hasattr(group_input_009_2.outputs[4], 'name'):
                    group_input_009_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_009_2.outputs[4], 'show_expanded'):
                    group_input_009_2.outputs[4].show_expanded = False
                if hasattr(group_input_009_2.outputs[5], 'default_value'):
                    group_input_009_2.outputs[5].default_value = 0.0
                if hasattr(group_input_009_2.outputs[5], 'display_shape'):
                    group_input_009_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[5], 'enabled'):
                    group_input_009_2.outputs[5].enabled = True
                if hasattr(group_input_009_2.outputs[5], 'hide'):
                    group_input_009_2.outputs[5].hide = True
                if hasattr(group_input_009_2.outputs[5], 'hide_value'):
                    group_input_009_2.outputs[5].hide_value = True
                if hasattr(group_input_009_2.outputs[5], 'name'):
                    group_input_009_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_009_2.outputs[5], 'show_expanded'):
                    group_input_009_2.outputs[5].show_expanded = False
                if hasattr(group_input_009_2.outputs[6], 'default_value'):
                    group_input_009_2.outputs[6].default_value = 0.5
                if hasattr(group_input_009_2.outputs[6], 'display_shape'):
                    group_input_009_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[6], 'enabled'):
                    group_input_009_2.outputs[6].enabled = True
                if hasattr(group_input_009_2.outputs[6], 'hide'):
                    group_input_009_2.outputs[6].hide = True
                if hasattr(group_input_009_2.outputs[6], 'hide_value'):
                    group_input_009_2.outputs[6].hide_value = False
                if hasattr(group_input_009_2.outputs[6], 'name'):
                    group_input_009_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_009_2.outputs[6], 'show_expanded'):
                    group_input_009_2.outputs[6].show_expanded = False
                if hasattr(group_input_009_2.outputs[7], 'default_value'):
                    group_input_009_2.outputs[7].default_value = 0.0
                if hasattr(group_input_009_2.outputs[7], 'display_shape'):
                    group_input_009_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[7], 'enabled'):
                    group_input_009_2.outputs[7].enabled = True
                if hasattr(group_input_009_2.outputs[7], 'hide'):
                    group_input_009_2.outputs[7].hide = True
                if hasattr(group_input_009_2.outputs[7], 'hide_value'):
                    group_input_009_2.outputs[7].hide_value = False
                if hasattr(group_input_009_2.outputs[7], 'name'):
                    group_input_009_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_009_2.outputs[7], 'show_expanded'):
                    group_input_009_2.outputs[7].show_expanded = False
                if hasattr(group_input_009_2.outputs[8], 'default_value'):
                    group_input_009_2.outputs[8].default_value = 0.0
                if hasattr(group_input_009_2.outputs[8], 'display_shape'):
                    group_input_009_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[8], 'enabled'):
                    group_input_009_2.outputs[8].enabled = True
                if hasattr(group_input_009_2.outputs[8], 'hide'):
                    group_input_009_2.outputs[8].hide = True
                if hasattr(group_input_009_2.outputs[8], 'hide_value'):
                    group_input_009_2.outputs[8].hide_value = False
                if hasattr(group_input_009_2.outputs[8], 'name'):
                    group_input_009_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_009_2.outputs[8], 'show_expanded'):
                    group_input_009_2.outputs[8].show_expanded = False
                if hasattr(group_input_009_2.outputs[9], 'default_value'):
                    group_input_009_2.outputs[9].default_value = 1.0
                if hasattr(group_input_009_2.outputs[9], 'display_shape'):
                    group_input_009_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[9], 'enabled'):
                    group_input_009_2.outputs[9].enabled = True
                if hasattr(group_input_009_2.outputs[9], 'hide'):
                    group_input_009_2.outputs[9].hide = False
                if hasattr(group_input_009_2.outputs[9], 'hide_value'):
                    group_input_009_2.outputs[9].hide_value = False
                if hasattr(group_input_009_2.outputs[9], 'name'):
                    group_input_009_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_009_2.outputs[9], 'show_expanded'):
                    group_input_009_2.outputs[9].show_expanded = False
                if hasattr(group_input_009_2.outputs[10], 'default_value'):
                    group_input_009_2.outputs[10].default_value = 2.0
                if hasattr(group_input_009_2.outputs[10], 'display_shape'):
                    group_input_009_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[10], 'enabled'):
                    group_input_009_2.outputs[10].enabled = True
                if hasattr(group_input_009_2.outputs[10], 'hide'):
                    group_input_009_2.outputs[10].hide = True
                if hasattr(group_input_009_2.outputs[10], 'hide_value'):
                    group_input_009_2.outputs[10].hide_value = False
                if hasattr(group_input_009_2.outputs[10], 'name'):
                    group_input_009_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_009_2.outputs[10], 'show_expanded'):
                    group_input_009_2.outputs[10].show_expanded = False
                if hasattr(group_input_009_2.outputs[11], 'default_value'):
                    group_input_009_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_009_2.outputs[11], 'display_shape'):
                    group_input_009_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[11], 'enabled'):
                    group_input_009_2.outputs[11].enabled = True
                if hasattr(group_input_009_2.outputs[11], 'hide'):
                    group_input_009_2.outputs[11].hide = True
                if hasattr(group_input_009_2.outputs[11], 'hide_value'):
                    group_input_009_2.outputs[11].hide_value = False
                if hasattr(group_input_009_2.outputs[11], 'name'):
                    group_input_009_2.outputs[11].name = '    Hue'
                if hasattr(group_input_009_2.outputs[11], 'show_expanded'):
                    group_input_009_2.outputs[11].show_expanded = False
                if hasattr(group_input_009_2.outputs[12], 'default_value'):
                    group_input_009_2.outputs[12].default_value = 1.0
                if hasattr(group_input_009_2.outputs[12], 'display_shape'):
                    group_input_009_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[12], 'enabled'):
                    group_input_009_2.outputs[12].enabled = True
                if hasattr(group_input_009_2.outputs[12], 'hide'):
                    group_input_009_2.outputs[12].hide = True
                if hasattr(group_input_009_2.outputs[12], 'hide_value'):
                    group_input_009_2.outputs[12].hide_value = False
                if hasattr(group_input_009_2.outputs[12], 'name'):
                    group_input_009_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_009_2.outputs[12], 'show_expanded'):
                    group_input_009_2.outputs[12].show_expanded = False
                if hasattr(group_input_009_2.outputs[13], 'default_value'):
                    group_input_009_2.outputs[13].default_value = 0.0
                if hasattr(group_input_009_2.outputs[13], 'display_shape'):
                    group_input_009_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[13], 'enabled'):
                    group_input_009_2.outputs[13].enabled = True
                if hasattr(group_input_009_2.outputs[13], 'hide'):
                    group_input_009_2.outputs[13].hide = True
                if hasattr(group_input_009_2.outputs[13], 'hide_value'):
                    group_input_009_2.outputs[13].hide_value = True
                if hasattr(group_input_009_2.outputs[13], 'name'):
                    group_input_009_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_009_2.outputs[13], 'show_expanded'):
                    group_input_009_2.outputs[13].show_expanded = False
                if hasattr(group_input_009_2.outputs[14], 'default_value'):
                    group_input_009_2.outputs[14].default_value = 0.0
                if hasattr(group_input_009_2.outputs[14], 'display_shape'):
                    group_input_009_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[14], 'enabled'):
                    group_input_009_2.outputs[14].enabled = True
                if hasattr(group_input_009_2.outputs[14], 'hide'):
                    group_input_009_2.outputs[14].hide = True
                if hasattr(group_input_009_2.outputs[14], 'hide_value'):
                    group_input_009_2.outputs[14].hide_value = False
                if hasattr(group_input_009_2.outputs[14], 'name'):
                    group_input_009_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_009_2.outputs[14], 'show_expanded'):
                    group_input_009_2.outputs[14].show_expanded = False
                if hasattr(group_input_009_2.outputs[15], 'default_value'):
                    group_input_009_2.outputs[15].default_value = 0.0
                if hasattr(group_input_009_2.outputs[15], 'display_shape'):
                    group_input_009_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[15], 'enabled'):
                    group_input_009_2.outputs[15].enabled = True
                if hasattr(group_input_009_2.outputs[15], 'hide'):
                    group_input_009_2.outputs[15].hide = True
                if hasattr(group_input_009_2.outputs[15], 'hide_value'):
                    group_input_009_2.outputs[15].hide_value = False
                if hasattr(group_input_009_2.outputs[15], 'name'):
                    group_input_009_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_009_2.outputs[15], 'show_expanded'):
                    group_input_009_2.outputs[15].show_expanded = False
                if hasattr(group_input_009_2.outputs[16], 'default_value'):
                    group_input_009_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_009_2.outputs[16], 'display_shape'):
                    group_input_009_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[16], 'enabled'):
                    group_input_009_2.outputs[16].enabled = True
                if hasattr(group_input_009_2.outputs[16], 'hide'):
                    group_input_009_2.outputs[16].hide = True
                if hasattr(group_input_009_2.outputs[16], 'hide_value'):
                    group_input_009_2.outputs[16].hide_value = False
                if hasattr(group_input_009_2.outputs[16], 'name'):
                    group_input_009_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_009_2.outputs[16], 'show_expanded'):
                    group_input_009_2.outputs[16].show_expanded = False
                if hasattr(group_input_009_2.outputs[17], 'default_value'):
                    group_input_009_2.outputs[17].default_value = 0.5
                if hasattr(group_input_009_2.outputs[17], 'display_shape'):
                    group_input_009_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[17], 'enabled'):
                    group_input_009_2.outputs[17].enabled = True
                if hasattr(group_input_009_2.outputs[17], 'hide'):
                    group_input_009_2.outputs[17].hide = True
                if hasattr(group_input_009_2.outputs[17], 'hide_value'):
                    group_input_009_2.outputs[17].hide_value = False
                if hasattr(group_input_009_2.outputs[17], 'name'):
                    group_input_009_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_009_2.outputs[17], 'show_expanded'):
                    group_input_009_2.outputs[17].show_expanded = False
                if hasattr(group_input_009_2.outputs[18], 'default_value'):
                    group_input_009_2.outputs[18].default_value = 0.5
                if hasattr(group_input_009_2.outputs[18], 'display_shape'):
                    group_input_009_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[18], 'enabled'):
                    group_input_009_2.outputs[18].enabled = True
                if hasattr(group_input_009_2.outputs[18], 'hide'):
                    group_input_009_2.outputs[18].hide = True
                if hasattr(group_input_009_2.outputs[18], 'hide_value'):
                    group_input_009_2.outputs[18].hide_value = False
                if hasattr(group_input_009_2.outputs[18], 'name'):
                    group_input_009_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_009_2.outputs[18], 'show_expanded'):
                    group_input_009_2.outputs[18].show_expanded = False
                if hasattr(group_input_009_2.outputs[19], 'default_value'):
                    group_input_009_2.outputs[19].default_value = 0.5
                if hasattr(group_input_009_2.outputs[19], 'display_shape'):
                    group_input_009_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_009_2.outputs[19], 'enabled'):
                    group_input_009_2.outputs[19].enabled = True
                if hasattr(group_input_009_2.outputs[19], 'hide'):
                    group_input_009_2.outputs[19].hide = True
                if hasattr(group_input_009_2.outputs[19], 'hide_value'):
                    group_input_009_2.outputs[19].hide_value = False
                if hasattr(group_input_009_2.outputs[19], 'name'):
                    group_input_009_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_009_2.outputs[19], 'show_expanded'):
                    group_input_009_2.outputs[19].show_expanded = False

                bright_contrast_2 = node_tree2.nodes.new('ShaderNodeBrightContrast')
                if hasattr(bright_contrast_2, 'color'):
                    bright_contrast_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(bright_contrast_2, 'hide'):
                    bright_contrast_2.hide = False
                if hasattr(bright_contrast_2, 'location'):
                    bright_contrast_2.location = (-960.0, 0.0)
                if hasattr(bright_contrast_2, 'mute'):
                    bright_contrast_2.mute = False
                if hasattr(bright_contrast_2, 'name'):
                    bright_contrast_2.name = 'Bright/Contrast'
                if hasattr(bright_contrast_2, 'use_custom_color'):
                    bright_contrast_2.use_custom_color = False
                if hasattr(bright_contrast_2, 'width'):
                    bright_contrast_2.width = 140.0
                input_ = next((input_ for input_ in bright_contrast_2.inputs if input_.identifier=='Color'), None)
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
                input_ = next((input_ for input_ in bright_contrast_2.inputs if input_.identifier=='Bright'), None)
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
                        input_.name = 'Bright'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in bright_contrast_2.inputs if input_.identifier=='Contrast'), None)
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
                        input_.name = 'Contrast'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in bright_contrast_2.outputs if output.identifier=='Color'), None)
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

                clamp_2 = node_tree2.nodes.new('ShaderNodeClamp')
                if hasattr(clamp_2, 'clamp_type'):
                    clamp_2.clamp_type = 'MINMAX'
                if hasattr(clamp_2, 'color'):
                    clamp_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(clamp_2, 'hide'):
                    clamp_2.hide = False
                if hasattr(clamp_2, 'location'):
                    clamp_2.location = (-1280.0, -99.0)
                if hasattr(clamp_2, 'mute'):
                    clamp_2.mute = False
                if hasattr(clamp_2, 'name'):
                    clamp_2.name = 'Clamp'
                if hasattr(clamp_2, 'use_custom_color'):
                    clamp_2.use_custom_color = False
                if hasattr(clamp_2, 'width'):
                    clamp_2.width = 140.0
                input_ = next((input_ for input_ in clamp_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in clamp_2.inputs if input_.identifier=='Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in clamp_2.inputs if input_.identifier=='Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in clamp_2.outputs if output.identifier=='Result'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                dark_spots_2 = node_tree2.nodes.new('ShaderNodeMix')
                if hasattr(dark_spots_2, 'blend_type'):
                    dark_spots_2.blend_type = 'SUBTRACT'
                if hasattr(dark_spots_2, 'clamp_factor'):
                    dark_spots_2.clamp_factor = True
                if hasattr(dark_spots_2, 'clamp_result'):
                    dark_spots_2.clamp_result = True
                if hasattr(dark_spots_2, 'color'):
                    dark_spots_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(dark_spots_2, 'data_type'):
                    dark_spots_2.data_type = 'RGBA'
                if hasattr(dark_spots_2, 'factor_mode'):
                    dark_spots_2.factor_mode = 'UNIFORM'
                if hasattr(dark_spots_2, 'hide'):
                    dark_spots_2.hide = False
                if hasattr(dark_spots_2, 'label'):
                    dark_spots_2.label = 'Dark Spots'
                if hasattr(dark_spots_2, 'location'):
                    dark_spots_2.location = (-1280.0, -196.0)
                if hasattr(dark_spots_2, 'mute'):
                    dark_spots_2.mute = False
                if hasattr(dark_spots_2, 'name'):
                    dark_spots_2.name = 'Dark Spots'
                if hasattr(dark_spots_2, 'use_custom_color'):
                    dark_spots_2.use_custom_color = False
                if hasattr(dark_spots_2, 'width'):
                    dark_spots_2.width = 140.0
                input_ = next((input_ for input_ in dark_spots_2.inputs if input_.identifier=='Factor_Float'), None)
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
                input_ = next((input_ for input_ in dark_spots_2.inputs if input_.identifier=='Factor_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.5, 0.5, 0.5)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in dark_spots_2.inputs if input_.identifier=='A_Float'), None)
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
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in dark_spots_2.inputs if input_.identifier=='B_Float'), None)
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
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in dark_spots_2.inputs if input_.identifier=='A_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in dark_spots_2.inputs if input_.identifier=='B_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in dark_spots_2.inputs if input_.identifier=='A_Color'), None)
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
                input_ = next((input_ for input_ in dark_spots_2.inputs if input_.identifier=='B_Color'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.3904055953025818, 0.3904055953025818, 0.3904055953025818, 1.0)
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
                output = next((output for output in dark_spots_2.outputs if output.identifier=='Result_Float'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in dark_spots_2.outputs if output.identifier=='Result_Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in dark_spots_2.outputs if output.identifier=='Result_Color'), None)
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

                map_range_005_2 = node_tree2.nodes.new('ShaderNodeMapRange')
                if hasattr(map_range_005_2, 'clamp'):
                    map_range_005_2.clamp = True
                if hasattr(map_range_005_2, 'color'):
                    map_range_005_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(map_range_005_2, 'data_type'):
                    map_range_005_2.data_type = 'FLOAT'
                if hasattr(map_range_005_2, 'hide'):
                    map_range_005_2.hide = False
                if hasattr(map_range_005_2, 'interpolation_type'):
                    map_range_005_2.interpolation_type = 'LINEAR'
                if hasattr(map_range_005_2, 'location'):
                    map_range_005_2.location = (-1280.0, 0.0)
                if hasattr(map_range_005_2, 'mute'):
                    map_range_005_2.mute = False
                if hasattr(map_range_005_2, 'name'):
                    map_range_005_2.name = 'Map Range.005'
                if hasattr(map_range_005_2, 'use_custom_color'):
                    map_range_005_2.use_custom_color = False
                if hasattr(map_range_005_2, 'width'):
                    map_range_005_2.width = 140.0
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='From Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='From Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='To Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='To Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 2.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='Steps'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 4.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = True
                    if hasattr(input_, 'name'):
                        input_.name = 'Vector'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='From_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='From_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='To_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='To_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_005_2.inputs if input_.identifier=='Steps_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (4.0, 4.0, 4.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in map_range_005_2.outputs if output.identifier=='Result'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in map_range_005_2.outputs if output.identifier=='Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Vector'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                map_range_003_2 = node_tree2.nodes.new('ShaderNodeMapRange')
                if hasattr(map_range_003_2, 'clamp'):
                    map_range_003_2.clamp = True
                if hasattr(map_range_003_2, 'color'):
                    map_range_003_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(map_range_003_2, 'data_type'):
                    map_range_003_2.data_type = 'FLOAT'
                if hasattr(map_range_003_2, 'hide'):
                    map_range_003_2.hide = False
                if hasattr(map_range_003_2, 'interpolation_type'):
                    map_range_003_2.interpolation_type = 'LINEAR'
                if hasattr(map_range_003_2, 'location'):
                    map_range_003_2.location = (-1600.0, -235.0)
                if hasattr(map_range_003_2, 'mute'):
                    map_range_003_2.mute = False
                if hasattr(map_range_003_2, 'name'):
                    map_range_003_2.name = 'Map Range.003'
                if hasattr(map_range_003_2, 'use_custom_color'):
                    map_range_003_2.use_custom_color = False
                if hasattr(map_range_003_2, 'width'):
                    map_range_003_2.width = 140.0
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='From Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='From Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='To Min'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = -3.725290298461914e-09
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='To Max'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.15000000596046448
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='Steps'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 4.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = True
                    if hasattr(input_, 'name'):
                        input_.name = 'Vector'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='From_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='From_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'From Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='To_Min_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Min'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='To_Max_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 1.0, 1.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'To Max'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in map_range_003_2.inputs if input_.identifier=='Steps_FLOAT3'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (4.0, 4.0, 4.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Steps'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in map_range_003_2.outputs if output.identifier=='Result'), None)
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
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in map_range_003_2.outputs if output.identifier=='Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Vector'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                group_input_007_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_007_2, 'color'):
                    group_input_007_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_007_2, 'hide'):
                    group_input_007_2.hide = False
                if hasattr(group_input_007_2, 'location'):
                    group_input_007_2.location = (-1600.0, -119.0)
                if hasattr(group_input_007_2, 'mute'):
                    group_input_007_2.mute = False
                if hasattr(group_input_007_2, 'name'):
                    group_input_007_2.name = 'Group Input.007'
                if hasattr(group_input_007_2, 'use_custom_color'):
                    group_input_007_2.use_custom_color = True
                if hasattr(group_input_007_2, 'width'):
                    group_input_007_2.width = 140.0
                if hasattr(group_input_007_2.outputs[0], 'default_value'):
                    group_input_007_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_007_2.outputs[0], 'display_shape'):
                    group_input_007_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[0], 'enabled'):
                    group_input_007_2.outputs[0].enabled = True
                if hasattr(group_input_007_2.outputs[0], 'hide'):
                    group_input_007_2.outputs[0].hide = False
                if hasattr(group_input_007_2.outputs[0], 'hide_value'):
                    group_input_007_2.outputs[0].hide_value = False
                if hasattr(group_input_007_2.outputs[0], 'name'):
                    group_input_007_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_007_2.outputs[0], 'show_expanded'):
                    group_input_007_2.outputs[0].show_expanded = False
                if hasattr(group_input_007_2.outputs[1], 'default_value'):
                    group_input_007_2.outputs[1].default_value = 0.0
                if hasattr(group_input_007_2.outputs[1], 'display_shape'):
                    group_input_007_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[1], 'enabled'):
                    group_input_007_2.outputs[1].enabled = True
                if hasattr(group_input_007_2.outputs[1], 'hide'):
                    group_input_007_2.outputs[1].hide = True
                if hasattr(group_input_007_2.outputs[1], 'hide_value'):
                    group_input_007_2.outputs[1].hide_value = True
                if hasattr(group_input_007_2.outputs[1], 'name'):
                    group_input_007_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_007_2.outputs[1], 'show_expanded'):
                    group_input_007_2.outputs[1].show_expanded = False
                if hasattr(group_input_007_2.outputs[2], 'default_value'):
                    group_input_007_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_007_2.outputs[2], 'display_shape'):
                    group_input_007_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[2], 'enabled'):
                    group_input_007_2.outputs[2].enabled = True
                if hasattr(group_input_007_2.outputs[2], 'hide'):
                    group_input_007_2.outputs[2].hide = True
                if hasattr(group_input_007_2.outputs[2], 'hide_value'):
                    group_input_007_2.outputs[2].hide_value = False
                if hasattr(group_input_007_2.outputs[2], 'name'):
                    group_input_007_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_007_2.outputs[2], 'show_expanded'):
                    group_input_007_2.outputs[2].show_expanded = False
                if hasattr(group_input_007_2.outputs[3], 'default_value'):
                    group_input_007_2.outputs[3].default_value = 0.5
                if hasattr(group_input_007_2.outputs[3], 'display_shape'):
                    group_input_007_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[3], 'enabled'):
                    group_input_007_2.outputs[3].enabled = True
                if hasattr(group_input_007_2.outputs[3], 'hide'):
                    group_input_007_2.outputs[3].hide = True
                if hasattr(group_input_007_2.outputs[3], 'hide_value'):
                    group_input_007_2.outputs[3].hide_value = False
                if hasattr(group_input_007_2.outputs[3], 'name'):
                    group_input_007_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_007_2.outputs[3], 'show_expanded'):
                    group_input_007_2.outputs[3].show_expanded = False
                if hasattr(group_input_007_2.outputs[4], 'default_value'):
                    group_input_007_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_007_2.outputs[4], 'display_shape'):
                    group_input_007_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[4], 'enabled'):
                    group_input_007_2.outputs[4].enabled = True
                if hasattr(group_input_007_2.outputs[4], 'hide'):
                    group_input_007_2.outputs[4].hide = True
                if hasattr(group_input_007_2.outputs[4], 'hide_value'):
                    group_input_007_2.outputs[4].hide_value = False
                if hasattr(group_input_007_2.outputs[4], 'name'):
                    group_input_007_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_007_2.outputs[4], 'show_expanded'):
                    group_input_007_2.outputs[4].show_expanded = False
                if hasattr(group_input_007_2.outputs[5], 'default_value'):
                    group_input_007_2.outputs[5].default_value = 0.0
                if hasattr(group_input_007_2.outputs[5], 'display_shape'):
                    group_input_007_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[5], 'enabled'):
                    group_input_007_2.outputs[5].enabled = True
                if hasattr(group_input_007_2.outputs[5], 'hide'):
                    group_input_007_2.outputs[5].hide = True
                if hasattr(group_input_007_2.outputs[5], 'hide_value'):
                    group_input_007_2.outputs[5].hide_value = True
                if hasattr(group_input_007_2.outputs[5], 'name'):
                    group_input_007_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_007_2.outputs[5], 'show_expanded'):
                    group_input_007_2.outputs[5].show_expanded = False
                if hasattr(group_input_007_2.outputs[6], 'default_value'):
                    group_input_007_2.outputs[6].default_value = 0.5
                if hasattr(group_input_007_2.outputs[6], 'display_shape'):
                    group_input_007_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[6], 'enabled'):
                    group_input_007_2.outputs[6].enabled = True
                if hasattr(group_input_007_2.outputs[6], 'hide'):
                    group_input_007_2.outputs[6].hide = True
                if hasattr(group_input_007_2.outputs[6], 'hide_value'):
                    group_input_007_2.outputs[6].hide_value = False
                if hasattr(group_input_007_2.outputs[6], 'name'):
                    group_input_007_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_007_2.outputs[6], 'show_expanded'):
                    group_input_007_2.outputs[6].show_expanded = False
                if hasattr(group_input_007_2.outputs[7], 'default_value'):
                    group_input_007_2.outputs[7].default_value = 0.0
                if hasattr(group_input_007_2.outputs[7], 'display_shape'):
                    group_input_007_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[7], 'enabled'):
                    group_input_007_2.outputs[7].enabled = True
                if hasattr(group_input_007_2.outputs[7], 'hide'):
                    group_input_007_2.outputs[7].hide = True
                if hasattr(group_input_007_2.outputs[7], 'hide_value'):
                    group_input_007_2.outputs[7].hide_value = False
                if hasattr(group_input_007_2.outputs[7], 'name'):
                    group_input_007_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_007_2.outputs[7], 'show_expanded'):
                    group_input_007_2.outputs[7].show_expanded = False
                if hasattr(group_input_007_2.outputs[8], 'default_value'):
                    group_input_007_2.outputs[8].default_value = 0.0
                if hasattr(group_input_007_2.outputs[8], 'display_shape'):
                    group_input_007_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[8], 'enabled'):
                    group_input_007_2.outputs[8].enabled = True
                if hasattr(group_input_007_2.outputs[8], 'hide'):
                    group_input_007_2.outputs[8].hide = True
                if hasattr(group_input_007_2.outputs[8], 'hide_value'):
                    group_input_007_2.outputs[8].hide_value = False
                if hasattr(group_input_007_2.outputs[8], 'name'):
                    group_input_007_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_007_2.outputs[8], 'show_expanded'):
                    group_input_007_2.outputs[8].show_expanded = False
                if hasattr(group_input_007_2.outputs[9], 'default_value'):
                    group_input_007_2.outputs[9].default_value = 1.0
                if hasattr(group_input_007_2.outputs[9], 'display_shape'):
                    group_input_007_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[9], 'enabled'):
                    group_input_007_2.outputs[9].enabled = True
                if hasattr(group_input_007_2.outputs[9], 'hide'):
                    group_input_007_2.outputs[9].hide = True
                if hasattr(group_input_007_2.outputs[9], 'hide_value'):
                    group_input_007_2.outputs[9].hide_value = False
                if hasattr(group_input_007_2.outputs[9], 'name'):
                    group_input_007_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_007_2.outputs[9], 'show_expanded'):
                    group_input_007_2.outputs[9].show_expanded = False
                if hasattr(group_input_007_2.outputs[10], 'default_value'):
                    group_input_007_2.outputs[10].default_value = 2.0
                if hasattr(group_input_007_2.outputs[10], 'display_shape'):
                    group_input_007_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[10], 'enabled'):
                    group_input_007_2.outputs[10].enabled = True
                if hasattr(group_input_007_2.outputs[10], 'hide'):
                    group_input_007_2.outputs[10].hide = True
                if hasattr(group_input_007_2.outputs[10], 'hide_value'):
                    group_input_007_2.outputs[10].hide_value = False
                if hasattr(group_input_007_2.outputs[10], 'name'):
                    group_input_007_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_007_2.outputs[10], 'show_expanded'):
                    group_input_007_2.outputs[10].show_expanded = False
                if hasattr(group_input_007_2.outputs[11], 'default_value'):
                    group_input_007_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_007_2.outputs[11], 'display_shape'):
                    group_input_007_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[11], 'enabled'):
                    group_input_007_2.outputs[11].enabled = True
                if hasattr(group_input_007_2.outputs[11], 'hide'):
                    group_input_007_2.outputs[11].hide = True
                if hasattr(group_input_007_2.outputs[11], 'hide_value'):
                    group_input_007_2.outputs[11].hide_value = False
                if hasattr(group_input_007_2.outputs[11], 'name'):
                    group_input_007_2.outputs[11].name = '    Hue'
                if hasattr(group_input_007_2.outputs[11], 'show_expanded'):
                    group_input_007_2.outputs[11].show_expanded = False
                if hasattr(group_input_007_2.outputs[12], 'default_value'):
                    group_input_007_2.outputs[12].default_value = 1.0
                if hasattr(group_input_007_2.outputs[12], 'display_shape'):
                    group_input_007_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[12], 'enabled'):
                    group_input_007_2.outputs[12].enabled = True
                if hasattr(group_input_007_2.outputs[12], 'hide'):
                    group_input_007_2.outputs[12].hide = True
                if hasattr(group_input_007_2.outputs[12], 'hide_value'):
                    group_input_007_2.outputs[12].hide_value = False
                if hasattr(group_input_007_2.outputs[12], 'name'):
                    group_input_007_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_007_2.outputs[12], 'show_expanded'):
                    group_input_007_2.outputs[12].show_expanded = False
                if hasattr(group_input_007_2.outputs[13], 'default_value'):
                    group_input_007_2.outputs[13].default_value = 0.0
                if hasattr(group_input_007_2.outputs[13], 'display_shape'):
                    group_input_007_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[13], 'enabled'):
                    group_input_007_2.outputs[13].enabled = True
                if hasattr(group_input_007_2.outputs[13], 'hide'):
                    group_input_007_2.outputs[13].hide = True
                if hasattr(group_input_007_2.outputs[13], 'hide_value'):
                    group_input_007_2.outputs[13].hide_value = True
                if hasattr(group_input_007_2.outputs[13], 'name'):
                    group_input_007_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_007_2.outputs[13], 'show_expanded'):
                    group_input_007_2.outputs[13].show_expanded = False
                if hasattr(group_input_007_2.outputs[14], 'default_value'):
                    group_input_007_2.outputs[14].default_value = 0.0
                if hasattr(group_input_007_2.outputs[14], 'display_shape'):
                    group_input_007_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[14], 'enabled'):
                    group_input_007_2.outputs[14].enabled = True
                if hasattr(group_input_007_2.outputs[14], 'hide'):
                    group_input_007_2.outputs[14].hide = True
                if hasattr(group_input_007_2.outputs[14], 'hide_value'):
                    group_input_007_2.outputs[14].hide_value = False
                if hasattr(group_input_007_2.outputs[14], 'name'):
                    group_input_007_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_007_2.outputs[14], 'show_expanded'):
                    group_input_007_2.outputs[14].show_expanded = False
                if hasattr(group_input_007_2.outputs[15], 'default_value'):
                    group_input_007_2.outputs[15].default_value = 0.0
                if hasattr(group_input_007_2.outputs[15], 'display_shape'):
                    group_input_007_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[15], 'enabled'):
                    group_input_007_2.outputs[15].enabled = True
                if hasattr(group_input_007_2.outputs[15], 'hide'):
                    group_input_007_2.outputs[15].hide = True
                if hasattr(group_input_007_2.outputs[15], 'hide_value'):
                    group_input_007_2.outputs[15].hide_value = False
                if hasattr(group_input_007_2.outputs[15], 'name'):
                    group_input_007_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_007_2.outputs[15], 'show_expanded'):
                    group_input_007_2.outputs[15].show_expanded = False
                if hasattr(group_input_007_2.outputs[16], 'default_value'):
                    group_input_007_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_007_2.outputs[16], 'display_shape'):
                    group_input_007_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[16], 'enabled'):
                    group_input_007_2.outputs[16].enabled = True
                if hasattr(group_input_007_2.outputs[16], 'hide'):
                    group_input_007_2.outputs[16].hide = False
                if hasattr(group_input_007_2.outputs[16], 'hide_value'):
                    group_input_007_2.outputs[16].hide_value = False
                if hasattr(group_input_007_2.outputs[16], 'name'):
                    group_input_007_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_007_2.outputs[16], 'show_expanded'):
                    group_input_007_2.outputs[16].show_expanded = False
                if hasattr(group_input_007_2.outputs[17], 'default_value'):
                    group_input_007_2.outputs[17].default_value = 0.5
                if hasattr(group_input_007_2.outputs[17], 'display_shape'):
                    group_input_007_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[17], 'enabled'):
                    group_input_007_2.outputs[17].enabled = True
                if hasattr(group_input_007_2.outputs[17], 'hide'):
                    group_input_007_2.outputs[17].hide = True
                if hasattr(group_input_007_2.outputs[17], 'hide_value'):
                    group_input_007_2.outputs[17].hide_value = False
                if hasattr(group_input_007_2.outputs[17], 'name'):
                    group_input_007_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_007_2.outputs[17], 'show_expanded'):
                    group_input_007_2.outputs[17].show_expanded = False
                if hasattr(group_input_007_2.outputs[18], 'default_value'):
                    group_input_007_2.outputs[18].default_value = 0.5
                if hasattr(group_input_007_2.outputs[18], 'display_shape'):
                    group_input_007_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[18], 'enabled'):
                    group_input_007_2.outputs[18].enabled = True
                if hasattr(group_input_007_2.outputs[18], 'hide'):
                    group_input_007_2.outputs[18].hide = False
                if hasattr(group_input_007_2.outputs[18], 'hide_value'):
                    group_input_007_2.outputs[18].hide_value = False
                if hasattr(group_input_007_2.outputs[18], 'name'):
                    group_input_007_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_007_2.outputs[18], 'show_expanded'):
                    group_input_007_2.outputs[18].show_expanded = False
                if hasattr(group_input_007_2.outputs[19], 'default_value'):
                    group_input_007_2.outputs[19].default_value = 0.5
                if hasattr(group_input_007_2.outputs[19], 'display_shape'):
                    group_input_007_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_007_2.outputs[19], 'enabled'):
                    group_input_007_2.outputs[19].enabled = True
                if hasattr(group_input_007_2.outputs[19], 'hide'):
                    group_input_007_2.outputs[19].hide = True
                if hasattr(group_input_007_2.outputs[19], 'hide_value'):
                    group_input_007_2.outputs[19].hide_value = False
                if hasattr(group_input_007_2.outputs[19], 'name'):
                    group_input_007_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_007_2.outputs[19], 'show_expanded'):
                    group_input_007_2.outputs[19].show_expanded = False

                separate_rgb_2 = node_tree2.nodes.new('ShaderNodeSeparateColor')
                if hasattr(separate_rgb_2, 'mode'):
                    separate_rgb_2.mode = 'RGB'
                if hasattr(separate_rgb_2, 'color'):
                    separate_rgb_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(separate_rgb_2, 'hide'):
                    separate_rgb_2.hide = False
                if hasattr(separate_rgb_2, 'location'):
                    separate_rgb_2.location = (-1600.0, 0.0)
                if hasattr(separate_rgb_2, 'mute'):
                    separate_rgb_2.mute = False
                if hasattr(separate_rgb_2, 'name'):
                    separate_rgb_2.name = 'Separate RGB'
                if hasattr(separate_rgb_2, 'use_custom_color'):
                    separate_rgb_2.use_custom_color = False
                if hasattr(separate_rgb_2, 'width'):
                    separate_rgb_2.width = 140.0
                input_ = next((input_ for input_ in separate_rgb_2.inputs if input_.identifier=='Color'), None)
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
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in separate_rgb_2.outputs if output.identifier=='Red'), None)
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
                        output.name = 'Red'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in separate_rgb_2.outputs if output.identifier=='Green'), None)
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
                        output.name = 'Green'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in separate_rgb_2.outputs if output.identifier=='Blue'), None)
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
                        output.name = 'Blue'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                group_input_005_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_005_2, 'color'):
                    group_input_005_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_005_2, 'hide'):
                    group_input_005_2.hide = False
                if hasattr(group_input_005_2, 'location'):
                    group_input_005_2.location = (-1760.0, -161.0)
                if hasattr(group_input_005_2, 'mute'):
                    group_input_005_2.mute = False
                if hasattr(group_input_005_2, 'name'):
                    group_input_005_2.name = 'Group Input.005'
                if hasattr(group_input_005_2, 'use_custom_color'):
                    group_input_005_2.use_custom_color = True
                if hasattr(group_input_005_2, 'width'):
                    group_input_005_2.width = 140.0
                if hasattr(group_input_005_2.outputs[0], 'default_value'):
                    group_input_005_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_005_2.outputs[0], 'display_shape'):
                    group_input_005_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[0], 'enabled'):
                    group_input_005_2.outputs[0].enabled = True
                if hasattr(group_input_005_2.outputs[0], 'hide'):
                    group_input_005_2.outputs[0].hide = True
                if hasattr(group_input_005_2.outputs[0], 'hide_value'):
                    group_input_005_2.outputs[0].hide_value = False
                if hasattr(group_input_005_2.outputs[0], 'name'):
                    group_input_005_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_005_2.outputs[0], 'show_expanded'):
                    group_input_005_2.outputs[0].show_expanded = False
                if hasattr(group_input_005_2.outputs[1], 'default_value'):
                    group_input_005_2.outputs[1].default_value = 0.0
                if hasattr(group_input_005_2.outputs[1], 'display_shape'):
                    group_input_005_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[1], 'enabled'):
                    group_input_005_2.outputs[1].enabled = True
                if hasattr(group_input_005_2.outputs[1], 'hide'):
                    group_input_005_2.outputs[1].hide = True
                if hasattr(group_input_005_2.outputs[1], 'hide_value'):
                    group_input_005_2.outputs[1].hide_value = True
                if hasattr(group_input_005_2.outputs[1], 'name'):
                    group_input_005_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_005_2.outputs[1], 'show_expanded'):
                    group_input_005_2.outputs[1].show_expanded = False
                if hasattr(group_input_005_2.outputs[2], 'default_value'):
                    group_input_005_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_005_2.outputs[2], 'display_shape'):
                    group_input_005_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[2], 'enabled'):
                    group_input_005_2.outputs[2].enabled = True
                if hasattr(group_input_005_2.outputs[2], 'hide'):
                    group_input_005_2.outputs[2].hide = True
                if hasattr(group_input_005_2.outputs[2], 'hide_value'):
                    group_input_005_2.outputs[2].hide_value = False
                if hasattr(group_input_005_2.outputs[2], 'name'):
                    group_input_005_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_005_2.outputs[2], 'show_expanded'):
                    group_input_005_2.outputs[2].show_expanded = False
                if hasattr(group_input_005_2.outputs[3], 'default_value'):
                    group_input_005_2.outputs[3].default_value = 0.5
                if hasattr(group_input_005_2.outputs[3], 'display_shape'):
                    group_input_005_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[3], 'enabled'):
                    group_input_005_2.outputs[3].enabled = True
                if hasattr(group_input_005_2.outputs[3], 'hide'):
                    group_input_005_2.outputs[3].hide = True
                if hasattr(group_input_005_2.outputs[3], 'hide_value'):
                    group_input_005_2.outputs[3].hide_value = False
                if hasattr(group_input_005_2.outputs[3], 'name'):
                    group_input_005_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_005_2.outputs[3], 'show_expanded'):
                    group_input_005_2.outputs[3].show_expanded = False
                if hasattr(group_input_005_2.outputs[4], 'default_value'):
                    group_input_005_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_005_2.outputs[4], 'display_shape'):
                    group_input_005_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[4], 'enabled'):
                    group_input_005_2.outputs[4].enabled = True
                if hasattr(group_input_005_2.outputs[4], 'hide'):
                    group_input_005_2.outputs[4].hide = False
                if hasattr(group_input_005_2.outputs[4], 'hide_value'):
                    group_input_005_2.outputs[4].hide_value = False
                if hasattr(group_input_005_2.outputs[4], 'name'):
                    group_input_005_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_005_2.outputs[4], 'show_expanded'):
                    group_input_005_2.outputs[4].show_expanded = False
                if hasattr(group_input_005_2.outputs[5], 'default_value'):
                    group_input_005_2.outputs[5].default_value = 0.0
                if hasattr(group_input_005_2.outputs[5], 'display_shape'):
                    group_input_005_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[5], 'enabled'):
                    group_input_005_2.outputs[5].enabled = True
                if hasattr(group_input_005_2.outputs[5], 'hide'):
                    group_input_005_2.outputs[5].hide = True
                if hasattr(group_input_005_2.outputs[5], 'hide_value'):
                    group_input_005_2.outputs[5].hide_value = True
                if hasattr(group_input_005_2.outputs[5], 'name'):
                    group_input_005_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_005_2.outputs[5], 'show_expanded'):
                    group_input_005_2.outputs[5].show_expanded = False
                if hasattr(group_input_005_2.outputs[6], 'default_value'):
                    group_input_005_2.outputs[6].default_value = 0.5
                if hasattr(group_input_005_2.outputs[6], 'display_shape'):
                    group_input_005_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[6], 'enabled'):
                    group_input_005_2.outputs[6].enabled = True
                if hasattr(group_input_005_2.outputs[6], 'hide'):
                    group_input_005_2.outputs[6].hide = True
                if hasattr(group_input_005_2.outputs[6], 'hide_value'):
                    group_input_005_2.outputs[6].hide_value = False
                if hasattr(group_input_005_2.outputs[6], 'name'):
                    group_input_005_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_005_2.outputs[6], 'show_expanded'):
                    group_input_005_2.outputs[6].show_expanded = False
                if hasattr(group_input_005_2.outputs[7], 'default_value'):
                    group_input_005_2.outputs[7].default_value = 0.0
                if hasattr(group_input_005_2.outputs[7], 'display_shape'):
                    group_input_005_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[7], 'enabled'):
                    group_input_005_2.outputs[7].enabled = True
                if hasattr(group_input_005_2.outputs[7], 'hide'):
                    group_input_005_2.outputs[7].hide = True
                if hasattr(group_input_005_2.outputs[7], 'hide_value'):
                    group_input_005_2.outputs[7].hide_value = False
                if hasattr(group_input_005_2.outputs[7], 'name'):
                    group_input_005_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_005_2.outputs[7], 'show_expanded'):
                    group_input_005_2.outputs[7].show_expanded = False
                if hasattr(group_input_005_2.outputs[8], 'default_value'):
                    group_input_005_2.outputs[8].default_value = 0.0
                if hasattr(group_input_005_2.outputs[8], 'display_shape'):
                    group_input_005_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[8], 'enabled'):
                    group_input_005_2.outputs[8].enabled = True
                if hasattr(group_input_005_2.outputs[8], 'hide'):
                    group_input_005_2.outputs[8].hide = True
                if hasattr(group_input_005_2.outputs[8], 'hide_value'):
                    group_input_005_2.outputs[8].hide_value = False
                if hasattr(group_input_005_2.outputs[8], 'name'):
                    group_input_005_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_005_2.outputs[8], 'show_expanded'):
                    group_input_005_2.outputs[8].show_expanded = False
                if hasattr(group_input_005_2.outputs[9], 'default_value'):
                    group_input_005_2.outputs[9].default_value = 1.0
                if hasattr(group_input_005_2.outputs[9], 'display_shape'):
                    group_input_005_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[9], 'enabled'):
                    group_input_005_2.outputs[9].enabled = True
                if hasattr(group_input_005_2.outputs[9], 'hide'):
                    group_input_005_2.outputs[9].hide = True
                if hasattr(group_input_005_2.outputs[9], 'hide_value'):
                    group_input_005_2.outputs[9].hide_value = False
                if hasattr(group_input_005_2.outputs[9], 'name'):
                    group_input_005_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_005_2.outputs[9], 'show_expanded'):
                    group_input_005_2.outputs[9].show_expanded = False
                if hasattr(group_input_005_2.outputs[10], 'default_value'):
                    group_input_005_2.outputs[10].default_value = 2.0
                if hasattr(group_input_005_2.outputs[10], 'display_shape'):
                    group_input_005_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[10], 'enabled'):
                    group_input_005_2.outputs[10].enabled = True
                if hasattr(group_input_005_2.outputs[10], 'hide'):
                    group_input_005_2.outputs[10].hide = True
                if hasattr(group_input_005_2.outputs[10], 'hide_value'):
                    group_input_005_2.outputs[10].hide_value = False
                if hasattr(group_input_005_2.outputs[10], 'name'):
                    group_input_005_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_005_2.outputs[10], 'show_expanded'):
                    group_input_005_2.outputs[10].show_expanded = False
                if hasattr(group_input_005_2.outputs[11], 'default_value'):
                    group_input_005_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_005_2.outputs[11], 'display_shape'):
                    group_input_005_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[11], 'enabled'):
                    group_input_005_2.outputs[11].enabled = True
                if hasattr(group_input_005_2.outputs[11], 'hide'):
                    group_input_005_2.outputs[11].hide = True
                if hasattr(group_input_005_2.outputs[11], 'hide_value'):
                    group_input_005_2.outputs[11].hide_value = False
                if hasattr(group_input_005_2.outputs[11], 'name'):
                    group_input_005_2.outputs[11].name = '    Hue'
                if hasattr(group_input_005_2.outputs[11], 'show_expanded'):
                    group_input_005_2.outputs[11].show_expanded = False
                if hasattr(group_input_005_2.outputs[12], 'default_value'):
                    group_input_005_2.outputs[12].default_value = 1.0
                if hasattr(group_input_005_2.outputs[12], 'display_shape'):
                    group_input_005_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[12], 'enabled'):
                    group_input_005_2.outputs[12].enabled = True
                if hasattr(group_input_005_2.outputs[12], 'hide'):
                    group_input_005_2.outputs[12].hide = True
                if hasattr(group_input_005_2.outputs[12], 'hide_value'):
                    group_input_005_2.outputs[12].hide_value = False
                if hasattr(group_input_005_2.outputs[12], 'name'):
                    group_input_005_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_005_2.outputs[12], 'show_expanded'):
                    group_input_005_2.outputs[12].show_expanded = False
                if hasattr(group_input_005_2.outputs[13], 'default_value'):
                    group_input_005_2.outputs[13].default_value = 0.0
                if hasattr(group_input_005_2.outputs[13], 'display_shape'):
                    group_input_005_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[13], 'enabled'):
                    group_input_005_2.outputs[13].enabled = True
                if hasattr(group_input_005_2.outputs[13], 'hide'):
                    group_input_005_2.outputs[13].hide = True
                if hasattr(group_input_005_2.outputs[13], 'hide_value'):
                    group_input_005_2.outputs[13].hide_value = True
                if hasattr(group_input_005_2.outputs[13], 'name'):
                    group_input_005_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_005_2.outputs[13], 'show_expanded'):
                    group_input_005_2.outputs[13].show_expanded = False
                if hasattr(group_input_005_2.outputs[14], 'default_value'):
                    group_input_005_2.outputs[14].default_value = 0.0
                if hasattr(group_input_005_2.outputs[14], 'display_shape'):
                    group_input_005_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[14], 'enabled'):
                    group_input_005_2.outputs[14].enabled = True
                if hasattr(group_input_005_2.outputs[14], 'hide'):
                    group_input_005_2.outputs[14].hide = True
                if hasattr(group_input_005_2.outputs[14], 'hide_value'):
                    group_input_005_2.outputs[14].hide_value = False
                if hasattr(group_input_005_2.outputs[14], 'name'):
                    group_input_005_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_005_2.outputs[14], 'show_expanded'):
                    group_input_005_2.outputs[14].show_expanded = False
                if hasattr(group_input_005_2.outputs[15], 'default_value'):
                    group_input_005_2.outputs[15].default_value = 0.0
                if hasattr(group_input_005_2.outputs[15], 'display_shape'):
                    group_input_005_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[15], 'enabled'):
                    group_input_005_2.outputs[15].enabled = True
                if hasattr(group_input_005_2.outputs[15], 'hide'):
                    group_input_005_2.outputs[15].hide = True
                if hasattr(group_input_005_2.outputs[15], 'hide_value'):
                    group_input_005_2.outputs[15].hide_value = False
                if hasattr(group_input_005_2.outputs[15], 'name'):
                    group_input_005_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_005_2.outputs[15], 'show_expanded'):
                    group_input_005_2.outputs[15].show_expanded = False
                if hasattr(group_input_005_2.outputs[16], 'default_value'):
                    group_input_005_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_005_2.outputs[16], 'display_shape'):
                    group_input_005_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[16], 'enabled'):
                    group_input_005_2.outputs[16].enabled = True
                if hasattr(group_input_005_2.outputs[16], 'hide'):
                    group_input_005_2.outputs[16].hide = True
                if hasattr(group_input_005_2.outputs[16], 'hide_value'):
                    group_input_005_2.outputs[16].hide_value = False
                if hasattr(group_input_005_2.outputs[16], 'name'):
                    group_input_005_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_005_2.outputs[16], 'show_expanded'):
                    group_input_005_2.outputs[16].show_expanded = False
                if hasattr(group_input_005_2.outputs[17], 'default_value'):
                    group_input_005_2.outputs[17].default_value = 0.5
                if hasattr(group_input_005_2.outputs[17], 'display_shape'):
                    group_input_005_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[17], 'enabled'):
                    group_input_005_2.outputs[17].enabled = True
                if hasattr(group_input_005_2.outputs[17], 'hide'):
                    group_input_005_2.outputs[17].hide = True
                if hasattr(group_input_005_2.outputs[17], 'hide_value'):
                    group_input_005_2.outputs[17].hide_value = False
                if hasattr(group_input_005_2.outputs[17], 'name'):
                    group_input_005_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_005_2.outputs[17], 'show_expanded'):
                    group_input_005_2.outputs[17].show_expanded = False
                if hasattr(group_input_005_2.outputs[18], 'default_value'):
                    group_input_005_2.outputs[18].default_value = 0.5
                if hasattr(group_input_005_2.outputs[18], 'display_shape'):
                    group_input_005_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[18], 'enabled'):
                    group_input_005_2.outputs[18].enabled = True
                if hasattr(group_input_005_2.outputs[18], 'hide'):
                    group_input_005_2.outputs[18].hide = True
                if hasattr(group_input_005_2.outputs[18], 'hide_value'):
                    group_input_005_2.outputs[18].hide_value = False
                if hasattr(group_input_005_2.outputs[18], 'name'):
                    group_input_005_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_005_2.outputs[18], 'show_expanded'):
                    group_input_005_2.outputs[18].show_expanded = False
                if hasattr(group_input_005_2.outputs[19], 'default_value'):
                    group_input_005_2.outputs[19].default_value = 0.5
                if hasattr(group_input_005_2.outputs[19], 'display_shape'):
                    group_input_005_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_005_2.outputs[19], 'enabled'):
                    group_input_005_2.outputs[19].enabled = True
                if hasattr(group_input_005_2.outputs[19], 'hide'):
                    group_input_005_2.outputs[19].hide = True
                if hasattr(group_input_005_2.outputs[19], 'hide_value'):
                    group_input_005_2.outputs[19].hide_value = False
                if hasattr(group_input_005_2.outputs[19], 'name'):
                    group_input_005_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_005_2.outputs[19], 'show_expanded'):
                    group_input_005_2.outputs[19].show_expanded = False

                noise_texture_2 = node_tree2.nodes.new('ShaderNodeTexNoise')
                if hasattr(noise_texture_2, 'color'):
                    noise_texture_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(noise_texture_2, 'hide'):
                    noise_texture_2.hide = False
                if hasattr(noise_texture_2, 'location'):
                    noise_texture_2.location = (-1760.0, 0.0)
                if hasattr(noise_texture_2, 'mute'):
                    noise_texture_2.mute = False
                if hasattr(noise_texture_2, 'name'):
                    noise_texture_2.name = 'Noise Texture'
                if hasattr(noise_texture_2, 'noise_dimensions'):
                    noise_texture_2.noise_dimensions = '3D'
                if hasattr(noise_texture_2, 'use_custom_color'):
                    noise_texture_2.use_custom_color = False
                if hasattr(noise_texture_2, 'width'):
                    noise_texture_2.width = 140.0
                input_ = next((input_ for input_ in noise_texture_2.inputs if input_.identifier=='Vector'), None)
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
                input_ = next((input_ for input_ in noise_texture_2.inputs if input_.identifier=='W'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 100.79999542236328
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'W'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in noise_texture_2.inputs if input_.identifier=='Scale'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.19999998807907104
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
                input_ = next((input_ for input_ in noise_texture_2.inputs if input_.identifier=='Detail'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 16.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Detail'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in noise_texture_2.inputs if input_.identifier=='Roughness'), None)
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
                input_ = next((input_ for input_ in noise_texture_2.inputs if input_.identifier=='Distortion'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 2.7300000190734863
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
                output = next((output for output in noise_texture_2.outputs if output.identifier=='Fac'), None)
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
                        output.name = 'Fac'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in noise_texture_2.outputs if output.identifier=='Color'), None)
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

                math_2 = node_tree2.nodes.new('ShaderNodeMath')
                if hasattr(math_2, 'color'):
                    math_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(math_2, 'hide'):
                    math_2.hide = False
                if hasattr(math_2, 'label'):
                    math_2.label = 'Remap Scale'
                if hasattr(math_2, 'location'):
                    math_2.location = (-1920.0, -77.0)
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
                        input_.name = 'Value'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in math_2.inputs if input_.identifier=='Value_002'), None)
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

                group_input_004_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_004_2, 'color'):
                    group_input_004_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_004_2, 'hide'):
                    group_input_004_2.hide = False
                if hasattr(group_input_004_2, 'location'):
                    group_input_004_2.location = (-1920.0, -174.0)
                if hasattr(group_input_004_2, 'mute'):
                    group_input_004_2.mute = False
                if hasattr(group_input_004_2, 'name'):
                    group_input_004_2.name = 'Group Input.004'
                if hasattr(group_input_004_2, 'use_custom_color'):
                    group_input_004_2.use_custom_color = True
                if hasattr(group_input_004_2, 'width'):
                    group_input_004_2.width = 140.0
                if hasattr(group_input_004_2.outputs[0], 'default_value'):
                    group_input_004_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_004_2.outputs[0], 'display_shape'):
                    group_input_004_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[0], 'enabled'):
                    group_input_004_2.outputs[0].enabled = True
                if hasattr(group_input_004_2.outputs[0], 'hide'):
                    group_input_004_2.outputs[0].hide = True
                if hasattr(group_input_004_2.outputs[0], 'hide_value'):
                    group_input_004_2.outputs[0].hide_value = False
                if hasattr(group_input_004_2.outputs[0], 'name'):
                    group_input_004_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_004_2.outputs[0], 'show_expanded'):
                    group_input_004_2.outputs[0].show_expanded = False
                if hasattr(group_input_004_2.outputs[1], 'default_value'):
                    group_input_004_2.outputs[1].default_value = 0.0
                if hasattr(group_input_004_2.outputs[1], 'display_shape'):
                    group_input_004_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[1], 'enabled'):
                    group_input_004_2.outputs[1].enabled = True
                if hasattr(group_input_004_2.outputs[1], 'hide'):
                    group_input_004_2.outputs[1].hide = True
                if hasattr(group_input_004_2.outputs[1], 'hide_value'):
                    group_input_004_2.outputs[1].hide_value = True
                if hasattr(group_input_004_2.outputs[1], 'name'):
                    group_input_004_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_004_2.outputs[1], 'show_expanded'):
                    group_input_004_2.outputs[1].show_expanded = False
                if hasattr(group_input_004_2.outputs[2], 'default_value'):
                    group_input_004_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_004_2.outputs[2], 'display_shape'):
                    group_input_004_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[2], 'enabled'):
                    group_input_004_2.outputs[2].enabled = True
                if hasattr(group_input_004_2.outputs[2], 'hide'):
                    group_input_004_2.outputs[2].hide = True
                if hasattr(group_input_004_2.outputs[2], 'hide_value'):
                    group_input_004_2.outputs[2].hide_value = False
                if hasattr(group_input_004_2.outputs[2], 'name'):
                    group_input_004_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_004_2.outputs[2], 'show_expanded'):
                    group_input_004_2.outputs[2].show_expanded = False
                if hasattr(group_input_004_2.outputs[3], 'default_value'):
                    group_input_004_2.outputs[3].default_value = 0.5
                if hasattr(group_input_004_2.outputs[3], 'display_shape'):
                    group_input_004_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[3], 'enabled'):
                    group_input_004_2.outputs[3].enabled = True
                if hasattr(group_input_004_2.outputs[3], 'hide'):
                    group_input_004_2.outputs[3].hide = False
                if hasattr(group_input_004_2.outputs[3], 'hide_value'):
                    group_input_004_2.outputs[3].hide_value = False
                if hasattr(group_input_004_2.outputs[3], 'name'):
                    group_input_004_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_004_2.outputs[3], 'show_expanded'):
                    group_input_004_2.outputs[3].show_expanded = False
                if hasattr(group_input_004_2.outputs[4], 'default_value'):
                    group_input_004_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_004_2.outputs[4], 'display_shape'):
                    group_input_004_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[4], 'enabled'):
                    group_input_004_2.outputs[4].enabled = True
                if hasattr(group_input_004_2.outputs[4], 'hide'):
                    group_input_004_2.outputs[4].hide = True
                if hasattr(group_input_004_2.outputs[4], 'hide_value'):
                    group_input_004_2.outputs[4].hide_value = False
                if hasattr(group_input_004_2.outputs[4], 'name'):
                    group_input_004_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_004_2.outputs[4], 'show_expanded'):
                    group_input_004_2.outputs[4].show_expanded = False
                if hasattr(group_input_004_2.outputs[5], 'default_value'):
                    group_input_004_2.outputs[5].default_value = 0.0
                if hasattr(group_input_004_2.outputs[5], 'display_shape'):
                    group_input_004_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[5], 'enabled'):
                    group_input_004_2.outputs[5].enabled = True
                if hasattr(group_input_004_2.outputs[5], 'hide'):
                    group_input_004_2.outputs[5].hide = True
                if hasattr(group_input_004_2.outputs[5], 'hide_value'):
                    group_input_004_2.outputs[5].hide_value = True
                if hasattr(group_input_004_2.outputs[5], 'name'):
                    group_input_004_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_004_2.outputs[5], 'show_expanded'):
                    group_input_004_2.outputs[5].show_expanded = False
                if hasattr(group_input_004_2.outputs[6], 'default_value'):
                    group_input_004_2.outputs[6].default_value = 0.5
                if hasattr(group_input_004_2.outputs[6], 'display_shape'):
                    group_input_004_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[6], 'enabled'):
                    group_input_004_2.outputs[6].enabled = True
                if hasattr(group_input_004_2.outputs[6], 'hide'):
                    group_input_004_2.outputs[6].hide = True
                if hasattr(group_input_004_2.outputs[6], 'hide_value'):
                    group_input_004_2.outputs[6].hide_value = False
                if hasattr(group_input_004_2.outputs[6], 'name'):
                    group_input_004_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_004_2.outputs[6], 'show_expanded'):
                    group_input_004_2.outputs[6].show_expanded = False
                if hasattr(group_input_004_2.outputs[7], 'default_value'):
                    group_input_004_2.outputs[7].default_value = 0.0
                if hasattr(group_input_004_2.outputs[7], 'display_shape'):
                    group_input_004_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[7], 'enabled'):
                    group_input_004_2.outputs[7].enabled = True
                if hasattr(group_input_004_2.outputs[7], 'hide'):
                    group_input_004_2.outputs[7].hide = True
                if hasattr(group_input_004_2.outputs[7], 'hide_value'):
                    group_input_004_2.outputs[7].hide_value = False
                if hasattr(group_input_004_2.outputs[7], 'name'):
                    group_input_004_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_004_2.outputs[7], 'show_expanded'):
                    group_input_004_2.outputs[7].show_expanded = False
                if hasattr(group_input_004_2.outputs[8], 'default_value'):
                    group_input_004_2.outputs[8].default_value = 0.0
                if hasattr(group_input_004_2.outputs[8], 'display_shape'):
                    group_input_004_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[8], 'enabled'):
                    group_input_004_2.outputs[8].enabled = True
                if hasattr(group_input_004_2.outputs[8], 'hide'):
                    group_input_004_2.outputs[8].hide = True
                if hasattr(group_input_004_2.outputs[8], 'hide_value'):
                    group_input_004_2.outputs[8].hide_value = False
                if hasattr(group_input_004_2.outputs[8], 'name'):
                    group_input_004_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_004_2.outputs[8], 'show_expanded'):
                    group_input_004_2.outputs[8].show_expanded = False
                if hasattr(group_input_004_2.outputs[9], 'default_value'):
                    group_input_004_2.outputs[9].default_value = 1.0
                if hasattr(group_input_004_2.outputs[9], 'display_shape'):
                    group_input_004_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[9], 'enabled'):
                    group_input_004_2.outputs[9].enabled = True
                if hasattr(group_input_004_2.outputs[9], 'hide'):
                    group_input_004_2.outputs[9].hide = True
                if hasattr(group_input_004_2.outputs[9], 'hide_value'):
                    group_input_004_2.outputs[9].hide_value = False
                if hasattr(group_input_004_2.outputs[9], 'name'):
                    group_input_004_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_004_2.outputs[9], 'show_expanded'):
                    group_input_004_2.outputs[9].show_expanded = False
                if hasattr(group_input_004_2.outputs[10], 'default_value'):
                    group_input_004_2.outputs[10].default_value = 2.0
                if hasattr(group_input_004_2.outputs[10], 'display_shape'):
                    group_input_004_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[10], 'enabled'):
                    group_input_004_2.outputs[10].enabled = True
                if hasattr(group_input_004_2.outputs[10], 'hide'):
                    group_input_004_2.outputs[10].hide = True
                if hasattr(group_input_004_2.outputs[10], 'hide_value'):
                    group_input_004_2.outputs[10].hide_value = False
                if hasattr(group_input_004_2.outputs[10], 'name'):
                    group_input_004_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_004_2.outputs[10], 'show_expanded'):
                    group_input_004_2.outputs[10].show_expanded = False
                if hasattr(group_input_004_2.outputs[11], 'default_value'):
                    group_input_004_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_004_2.outputs[11], 'display_shape'):
                    group_input_004_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[11], 'enabled'):
                    group_input_004_2.outputs[11].enabled = True
                if hasattr(group_input_004_2.outputs[11], 'hide'):
                    group_input_004_2.outputs[11].hide = True
                if hasattr(group_input_004_2.outputs[11], 'hide_value'):
                    group_input_004_2.outputs[11].hide_value = False
                if hasattr(group_input_004_2.outputs[11], 'name'):
                    group_input_004_2.outputs[11].name = '    Hue'
                if hasattr(group_input_004_2.outputs[11], 'show_expanded'):
                    group_input_004_2.outputs[11].show_expanded = False
                if hasattr(group_input_004_2.outputs[12], 'default_value'):
                    group_input_004_2.outputs[12].default_value = 1.0
                if hasattr(group_input_004_2.outputs[12], 'display_shape'):
                    group_input_004_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[12], 'enabled'):
                    group_input_004_2.outputs[12].enabled = True
                if hasattr(group_input_004_2.outputs[12], 'hide'):
                    group_input_004_2.outputs[12].hide = True
                if hasattr(group_input_004_2.outputs[12], 'hide_value'):
                    group_input_004_2.outputs[12].hide_value = False
                if hasattr(group_input_004_2.outputs[12], 'name'):
                    group_input_004_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_004_2.outputs[12], 'show_expanded'):
                    group_input_004_2.outputs[12].show_expanded = False
                if hasattr(group_input_004_2.outputs[13], 'default_value'):
                    group_input_004_2.outputs[13].default_value = 0.0
                if hasattr(group_input_004_2.outputs[13], 'display_shape'):
                    group_input_004_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[13], 'enabled'):
                    group_input_004_2.outputs[13].enabled = True
                if hasattr(group_input_004_2.outputs[13], 'hide'):
                    group_input_004_2.outputs[13].hide = True
                if hasattr(group_input_004_2.outputs[13], 'hide_value'):
                    group_input_004_2.outputs[13].hide_value = True
                if hasattr(group_input_004_2.outputs[13], 'name'):
                    group_input_004_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_004_2.outputs[13], 'show_expanded'):
                    group_input_004_2.outputs[13].show_expanded = False
                if hasattr(group_input_004_2.outputs[14], 'default_value'):
                    group_input_004_2.outputs[14].default_value = 0.0
                if hasattr(group_input_004_2.outputs[14], 'display_shape'):
                    group_input_004_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[14], 'enabled'):
                    group_input_004_2.outputs[14].enabled = True
                if hasattr(group_input_004_2.outputs[14], 'hide'):
                    group_input_004_2.outputs[14].hide = True
                if hasattr(group_input_004_2.outputs[14], 'hide_value'):
                    group_input_004_2.outputs[14].hide_value = False
                if hasattr(group_input_004_2.outputs[14], 'name'):
                    group_input_004_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_004_2.outputs[14], 'show_expanded'):
                    group_input_004_2.outputs[14].show_expanded = False
                if hasattr(group_input_004_2.outputs[15], 'default_value'):
                    group_input_004_2.outputs[15].default_value = 0.0
                if hasattr(group_input_004_2.outputs[15], 'display_shape'):
                    group_input_004_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[15], 'enabled'):
                    group_input_004_2.outputs[15].enabled = True
                if hasattr(group_input_004_2.outputs[15], 'hide'):
                    group_input_004_2.outputs[15].hide = True
                if hasattr(group_input_004_2.outputs[15], 'hide_value'):
                    group_input_004_2.outputs[15].hide_value = False
                if hasattr(group_input_004_2.outputs[15], 'name'):
                    group_input_004_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_004_2.outputs[15], 'show_expanded'):
                    group_input_004_2.outputs[15].show_expanded = False
                if hasattr(group_input_004_2.outputs[16], 'default_value'):
                    group_input_004_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_004_2.outputs[16], 'display_shape'):
                    group_input_004_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[16], 'enabled'):
                    group_input_004_2.outputs[16].enabled = True
                if hasattr(group_input_004_2.outputs[16], 'hide'):
                    group_input_004_2.outputs[16].hide = True
                if hasattr(group_input_004_2.outputs[16], 'hide_value'):
                    group_input_004_2.outputs[16].hide_value = False
                if hasattr(group_input_004_2.outputs[16], 'name'):
                    group_input_004_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_004_2.outputs[16], 'show_expanded'):
                    group_input_004_2.outputs[16].show_expanded = False
                if hasattr(group_input_004_2.outputs[17], 'default_value'):
                    group_input_004_2.outputs[17].default_value = 0.5
                if hasattr(group_input_004_2.outputs[17], 'display_shape'):
                    group_input_004_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[17], 'enabled'):
                    group_input_004_2.outputs[17].enabled = True
                if hasattr(group_input_004_2.outputs[17], 'hide'):
                    group_input_004_2.outputs[17].hide = True
                if hasattr(group_input_004_2.outputs[17], 'hide_value'):
                    group_input_004_2.outputs[17].hide_value = False
                if hasattr(group_input_004_2.outputs[17], 'name'):
                    group_input_004_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_004_2.outputs[17], 'show_expanded'):
                    group_input_004_2.outputs[17].show_expanded = False
                if hasattr(group_input_004_2.outputs[18], 'default_value'):
                    group_input_004_2.outputs[18].default_value = 0.5
                if hasattr(group_input_004_2.outputs[18], 'display_shape'):
                    group_input_004_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[18], 'enabled'):
                    group_input_004_2.outputs[18].enabled = True
                if hasattr(group_input_004_2.outputs[18], 'hide'):
                    group_input_004_2.outputs[18].hide = True
                if hasattr(group_input_004_2.outputs[18], 'hide_value'):
                    group_input_004_2.outputs[18].hide_value = False
                if hasattr(group_input_004_2.outputs[18], 'name'):
                    group_input_004_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_004_2.outputs[18], 'show_expanded'):
                    group_input_004_2.outputs[18].show_expanded = False
                if hasattr(group_input_004_2.outputs[19], 'default_value'):
                    group_input_004_2.outputs[19].default_value = 0.5
                if hasattr(group_input_004_2.outputs[19], 'display_shape'):
                    group_input_004_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_004_2.outputs[19], 'enabled'):
                    group_input_004_2.outputs[19].enabled = True
                if hasattr(group_input_004_2.outputs[19], 'hide'):
                    group_input_004_2.outputs[19].hide = False
                if hasattr(group_input_004_2.outputs[19], 'hide_value'):
                    group_input_004_2.outputs[19].hide_value = False
                if hasattr(group_input_004_2.outputs[19], 'name'):
                    group_input_004_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_004_2.outputs[19], 'show_expanded'):
                    group_input_004_2.outputs[19].show_expanded = False

                texture_coordinate_2 = node_tree2.nodes.new('ShaderNodeTexCoord')
                if hasattr(texture_coordinate_2, 'color'):
                    texture_coordinate_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(texture_coordinate_2, 'from_instancer'):
                    texture_coordinate_2.from_instancer = False
                if hasattr(texture_coordinate_2, 'hide'):
                    texture_coordinate_2.hide = False
                if hasattr(texture_coordinate_2, 'location'):
                    texture_coordinate_2.location = (-1920.0, 0.0)
                if hasattr(texture_coordinate_2, 'mute'):
                    texture_coordinate_2.mute = False
                if hasattr(texture_coordinate_2, 'name'):
                    texture_coordinate_2.name = 'Texture Coordinate'
                if hasattr(texture_coordinate_2, 'use_custom_color'):
                    texture_coordinate_2.use_custom_color = False
                if hasattr(texture_coordinate_2, 'width'):
                    texture_coordinate_2.width = 140.0
                output = next((output for output in texture_coordinate_2.outputs if output.identifier=='Generated'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Generated'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in texture_coordinate_2.outputs if output.identifier=='Normal'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Normal'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in texture_coordinate_2.outputs if output.identifier=='UV'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'UV'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in texture_coordinate_2.outputs if output.identifier=='Object'), None)
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
                output = next((output for output in texture_coordinate_2.outputs if output.identifier=='Camera'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Camera'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in texture_coordinate_2.outputs if output.identifier=='Window'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Window'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in texture_coordinate_2.outputs if output.identifier=='Reflection'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = True
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Reflection'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                group_input_001_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_001_2, 'color'):
                    group_input_001_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_001_2, 'hide'):
                    group_input_001_2.hide = False
                if hasattr(group_input_001_2, 'location'):
                    group_input_001_2.location = (-800.0, 0.0)
                if hasattr(group_input_001_2, 'mute'):
                    group_input_001_2.mute = False
                if hasattr(group_input_001_2, 'name'):
                    group_input_001_2.name = 'Group Input.001'
                if hasattr(group_input_001_2, 'use_custom_color'):
                    group_input_001_2.use_custom_color = True
                if hasattr(group_input_001_2, 'width'):
                    group_input_001_2.width = 140.0
                if hasattr(group_input_001_2.outputs[0], 'default_value'):
                    group_input_001_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_001_2.outputs[0], 'display_shape'):
                    group_input_001_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[0], 'enabled'):
                    group_input_001_2.outputs[0].enabled = True
                if hasattr(group_input_001_2.outputs[0], 'hide'):
                    group_input_001_2.outputs[0].hide = True
                if hasattr(group_input_001_2.outputs[0], 'hide_value'):
                    group_input_001_2.outputs[0].hide_value = False
                if hasattr(group_input_001_2.outputs[0], 'name'):
                    group_input_001_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_001_2.outputs[0], 'show_expanded'):
                    group_input_001_2.outputs[0].show_expanded = False
                if hasattr(group_input_001_2.outputs[1], 'default_value'):
                    group_input_001_2.outputs[1].default_value = 0.0
                if hasattr(group_input_001_2.outputs[1], 'display_shape'):
                    group_input_001_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[1], 'enabled'):
                    group_input_001_2.outputs[1].enabled = True
                if hasattr(group_input_001_2.outputs[1], 'hide'):
                    group_input_001_2.outputs[1].hide = True
                if hasattr(group_input_001_2.outputs[1], 'hide_value'):
                    group_input_001_2.outputs[1].hide_value = True
                if hasattr(group_input_001_2.outputs[1], 'name'):
                    group_input_001_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_001_2.outputs[1], 'show_expanded'):
                    group_input_001_2.outputs[1].show_expanded = False
                if hasattr(group_input_001_2.outputs[2], 'default_value'):
                    group_input_001_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_001_2.outputs[2], 'display_shape'):
                    group_input_001_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[2], 'enabled'):
                    group_input_001_2.outputs[2].enabled = True
                if hasattr(group_input_001_2.outputs[2], 'hide'):
                    group_input_001_2.outputs[2].hide = True
                if hasattr(group_input_001_2.outputs[2], 'hide_value'):
                    group_input_001_2.outputs[2].hide_value = False
                if hasattr(group_input_001_2.outputs[2], 'name'):
                    group_input_001_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_001_2.outputs[2], 'show_expanded'):
                    group_input_001_2.outputs[2].show_expanded = False
                if hasattr(group_input_001_2.outputs[3], 'default_value'):
                    group_input_001_2.outputs[3].default_value = 0.5
                if hasattr(group_input_001_2.outputs[3], 'display_shape'):
                    group_input_001_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[3], 'enabled'):
                    group_input_001_2.outputs[3].enabled = True
                if hasattr(group_input_001_2.outputs[3], 'hide'):
                    group_input_001_2.outputs[3].hide = True
                if hasattr(group_input_001_2.outputs[3], 'hide_value'):
                    group_input_001_2.outputs[3].hide_value = False
                if hasattr(group_input_001_2.outputs[3], 'name'):
                    group_input_001_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_001_2.outputs[3], 'show_expanded'):
                    group_input_001_2.outputs[3].show_expanded = False
                if hasattr(group_input_001_2.outputs[4], 'default_value'):
                    group_input_001_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_001_2.outputs[4], 'display_shape'):
                    group_input_001_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[4], 'enabled'):
                    group_input_001_2.outputs[4].enabled = True
                if hasattr(group_input_001_2.outputs[4], 'hide'):
                    group_input_001_2.outputs[4].hide = True
                if hasattr(group_input_001_2.outputs[4], 'hide_value'):
                    group_input_001_2.outputs[4].hide_value = False
                if hasattr(group_input_001_2.outputs[4], 'name'):
                    group_input_001_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_001_2.outputs[4], 'show_expanded'):
                    group_input_001_2.outputs[4].show_expanded = False
                if hasattr(group_input_001_2.outputs[5], 'default_value'):
                    group_input_001_2.outputs[5].default_value = 0.0
                if hasattr(group_input_001_2.outputs[5], 'display_shape'):
                    group_input_001_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[5], 'enabled'):
                    group_input_001_2.outputs[5].enabled = True
                if hasattr(group_input_001_2.outputs[5], 'hide'):
                    group_input_001_2.outputs[5].hide = True
                if hasattr(group_input_001_2.outputs[5], 'hide_value'):
                    group_input_001_2.outputs[5].hide_value = True
                if hasattr(group_input_001_2.outputs[5], 'name'):
                    group_input_001_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_001_2.outputs[5], 'show_expanded'):
                    group_input_001_2.outputs[5].show_expanded = False
                if hasattr(group_input_001_2.outputs[6], 'default_value'):
                    group_input_001_2.outputs[6].default_value = 0.5
                if hasattr(group_input_001_2.outputs[6], 'display_shape'):
                    group_input_001_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[6], 'enabled'):
                    group_input_001_2.outputs[6].enabled = True
                if hasattr(group_input_001_2.outputs[6], 'hide'):
                    group_input_001_2.outputs[6].hide = True
                if hasattr(group_input_001_2.outputs[6], 'hide_value'):
                    group_input_001_2.outputs[6].hide_value = False
                if hasattr(group_input_001_2.outputs[6], 'name'):
                    group_input_001_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_001_2.outputs[6], 'show_expanded'):
                    group_input_001_2.outputs[6].show_expanded = False
                if hasattr(group_input_001_2.outputs[7], 'default_value'):
                    group_input_001_2.outputs[7].default_value = 0.0
                if hasattr(group_input_001_2.outputs[7], 'display_shape'):
                    group_input_001_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[7], 'enabled'):
                    group_input_001_2.outputs[7].enabled = True
                if hasattr(group_input_001_2.outputs[7], 'hide'):
                    group_input_001_2.outputs[7].hide = True
                if hasattr(group_input_001_2.outputs[7], 'hide_value'):
                    group_input_001_2.outputs[7].hide_value = False
                if hasattr(group_input_001_2.outputs[7], 'name'):
                    group_input_001_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_001_2.outputs[7], 'show_expanded'):
                    group_input_001_2.outputs[7].show_expanded = False
                if hasattr(group_input_001_2.outputs[8], 'default_value'):
                    group_input_001_2.outputs[8].default_value = 0.0
                if hasattr(group_input_001_2.outputs[8], 'display_shape'):
                    group_input_001_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[8], 'enabled'):
                    group_input_001_2.outputs[8].enabled = True
                if hasattr(group_input_001_2.outputs[8], 'hide'):
                    group_input_001_2.outputs[8].hide = True
                if hasattr(group_input_001_2.outputs[8], 'hide_value'):
                    group_input_001_2.outputs[8].hide_value = False
                if hasattr(group_input_001_2.outputs[8], 'name'):
                    group_input_001_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_001_2.outputs[8], 'show_expanded'):
                    group_input_001_2.outputs[8].show_expanded = False
                if hasattr(group_input_001_2.outputs[9], 'default_value'):
                    group_input_001_2.outputs[9].default_value = 1.0
                if hasattr(group_input_001_2.outputs[9], 'display_shape'):
                    group_input_001_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[9], 'enabled'):
                    group_input_001_2.outputs[9].enabled = True
                if hasattr(group_input_001_2.outputs[9], 'hide'):
                    group_input_001_2.outputs[9].hide = True
                if hasattr(group_input_001_2.outputs[9], 'hide_value'):
                    group_input_001_2.outputs[9].hide_value = False
                if hasattr(group_input_001_2.outputs[9], 'name'):
                    group_input_001_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_001_2.outputs[9], 'show_expanded'):
                    group_input_001_2.outputs[9].show_expanded = False
                if hasattr(group_input_001_2.outputs[10], 'default_value'):
                    group_input_001_2.outputs[10].default_value = 2.0
                if hasattr(group_input_001_2.outputs[10], 'display_shape'):
                    group_input_001_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[10], 'enabled'):
                    group_input_001_2.outputs[10].enabled = True
                if hasattr(group_input_001_2.outputs[10], 'hide'):
                    group_input_001_2.outputs[10].hide = False
                if hasattr(group_input_001_2.outputs[10], 'hide_value'):
                    group_input_001_2.outputs[10].hide_value = False
                if hasattr(group_input_001_2.outputs[10], 'name'):
                    group_input_001_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_001_2.outputs[10], 'show_expanded'):
                    group_input_001_2.outputs[10].show_expanded = False
                if hasattr(group_input_001_2.outputs[11], 'default_value'):
                    group_input_001_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_001_2.outputs[11], 'display_shape'):
                    group_input_001_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[11], 'enabled'):
                    group_input_001_2.outputs[11].enabled = True
                if hasattr(group_input_001_2.outputs[11], 'hide'):
                    group_input_001_2.outputs[11].hide = False
                if hasattr(group_input_001_2.outputs[11], 'hide_value'):
                    group_input_001_2.outputs[11].hide_value = False
                if hasattr(group_input_001_2.outputs[11], 'name'):
                    group_input_001_2.outputs[11].name = '    Hue'
                if hasattr(group_input_001_2.outputs[11], 'show_expanded'):
                    group_input_001_2.outputs[11].show_expanded = False
                if hasattr(group_input_001_2.outputs[12], 'default_value'):
                    group_input_001_2.outputs[12].default_value = 1.0
                if hasattr(group_input_001_2.outputs[12], 'display_shape'):
                    group_input_001_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[12], 'enabled'):
                    group_input_001_2.outputs[12].enabled = True
                if hasattr(group_input_001_2.outputs[12], 'hide'):
                    group_input_001_2.outputs[12].hide = False
                if hasattr(group_input_001_2.outputs[12], 'hide_value'):
                    group_input_001_2.outputs[12].hide_value = False
                if hasattr(group_input_001_2.outputs[12], 'name'):
                    group_input_001_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_001_2.outputs[12], 'show_expanded'):
                    group_input_001_2.outputs[12].show_expanded = False
                if hasattr(group_input_001_2.outputs[13], 'default_value'):
                    group_input_001_2.outputs[13].default_value = 0.0
                if hasattr(group_input_001_2.outputs[13], 'display_shape'):
                    group_input_001_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[13], 'enabled'):
                    group_input_001_2.outputs[13].enabled = True
                if hasattr(group_input_001_2.outputs[13], 'hide'):
                    group_input_001_2.outputs[13].hide = True
                if hasattr(group_input_001_2.outputs[13], 'hide_value'):
                    group_input_001_2.outputs[13].hide_value = True
                if hasattr(group_input_001_2.outputs[13], 'name'):
                    group_input_001_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_001_2.outputs[13], 'show_expanded'):
                    group_input_001_2.outputs[13].show_expanded = False
                if hasattr(group_input_001_2.outputs[14], 'default_value'):
                    group_input_001_2.outputs[14].default_value = 0.0
                if hasattr(group_input_001_2.outputs[14], 'display_shape'):
                    group_input_001_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[14], 'enabled'):
                    group_input_001_2.outputs[14].enabled = True
                if hasattr(group_input_001_2.outputs[14], 'hide'):
                    group_input_001_2.outputs[14].hide = True
                if hasattr(group_input_001_2.outputs[14], 'hide_value'):
                    group_input_001_2.outputs[14].hide_value = False
                if hasattr(group_input_001_2.outputs[14], 'name'):
                    group_input_001_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_001_2.outputs[14], 'show_expanded'):
                    group_input_001_2.outputs[14].show_expanded = False
                if hasattr(group_input_001_2.outputs[15], 'default_value'):
                    group_input_001_2.outputs[15].default_value = 0.0
                if hasattr(group_input_001_2.outputs[15], 'display_shape'):
                    group_input_001_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[15], 'enabled'):
                    group_input_001_2.outputs[15].enabled = True
                if hasattr(group_input_001_2.outputs[15], 'hide'):
                    group_input_001_2.outputs[15].hide = True
                if hasattr(group_input_001_2.outputs[15], 'hide_value'):
                    group_input_001_2.outputs[15].hide_value = False
                if hasattr(group_input_001_2.outputs[15], 'name'):
                    group_input_001_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_001_2.outputs[15], 'show_expanded'):
                    group_input_001_2.outputs[15].show_expanded = False
                if hasattr(group_input_001_2.outputs[16], 'default_value'):
                    group_input_001_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_001_2.outputs[16], 'display_shape'):
                    group_input_001_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[16], 'enabled'):
                    group_input_001_2.outputs[16].enabled = True
                if hasattr(group_input_001_2.outputs[16], 'hide'):
                    group_input_001_2.outputs[16].hide = True
                if hasattr(group_input_001_2.outputs[16], 'hide_value'):
                    group_input_001_2.outputs[16].hide_value = False
                if hasattr(group_input_001_2.outputs[16], 'name'):
                    group_input_001_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_001_2.outputs[16], 'show_expanded'):
                    group_input_001_2.outputs[16].show_expanded = False
                if hasattr(group_input_001_2.outputs[17], 'default_value'):
                    group_input_001_2.outputs[17].default_value = 0.5
                if hasattr(group_input_001_2.outputs[17], 'display_shape'):
                    group_input_001_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[17], 'enabled'):
                    group_input_001_2.outputs[17].enabled = True
                if hasattr(group_input_001_2.outputs[17], 'hide'):
                    group_input_001_2.outputs[17].hide = True
                if hasattr(group_input_001_2.outputs[17], 'hide_value'):
                    group_input_001_2.outputs[17].hide_value = False
                if hasattr(group_input_001_2.outputs[17], 'name'):
                    group_input_001_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_001_2.outputs[17], 'show_expanded'):
                    group_input_001_2.outputs[17].show_expanded = False
                if hasattr(group_input_001_2.outputs[18], 'default_value'):
                    group_input_001_2.outputs[18].default_value = 0.5
                if hasattr(group_input_001_2.outputs[18], 'display_shape'):
                    group_input_001_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[18], 'enabled'):
                    group_input_001_2.outputs[18].enabled = True
                if hasattr(group_input_001_2.outputs[18], 'hide'):
                    group_input_001_2.outputs[18].hide = True
                if hasattr(group_input_001_2.outputs[18], 'hide_value'):
                    group_input_001_2.outputs[18].hide_value = False
                if hasattr(group_input_001_2.outputs[18], 'name'):
                    group_input_001_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_001_2.outputs[18], 'show_expanded'):
                    group_input_001_2.outputs[18].show_expanded = False
                if hasattr(group_input_001_2.outputs[19], 'default_value'):
                    group_input_001_2.outputs[19].default_value = 0.5
                if hasattr(group_input_001_2.outputs[19], 'display_shape'):
                    group_input_001_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[19], 'enabled'):
                    group_input_001_2.outputs[19].enabled = True
                if hasattr(group_input_001_2.outputs[19], 'hide'):
                    group_input_001_2.outputs[19].hide = True
                if hasattr(group_input_001_2.outputs[19], 'hide_value'):
                    group_input_001_2.outputs[19].hide_value = False
                if hasattr(group_input_001_2.outputs[19], 'name'):
                    group_input_001_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_001_2.outputs[19], 'show_expanded'):
                    group_input_001_2.outputs[19].show_expanded = False

                gamma_2 = node_tree2.nodes.new('ShaderNodeGamma')
                if hasattr(gamma_2, 'color'):
                    gamma_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(gamma_2, 'hide'):
                    gamma_2.hide = False
                if hasattr(gamma_2, 'location'):
                    gamma_2.location = (-800.0, -116.0)
                if hasattr(gamma_2, 'mute'):
                    gamma_2.mute = False
                if hasattr(gamma_2, 'name'):
                    gamma_2.name = 'Gamma'
                if hasattr(gamma_2, 'use_custom_color'):
                    gamma_2.use_custom_color = False
                if hasattr(gamma_2, 'width'):
                    gamma_2.width = 140.0
                input_ = next((input_ for input_ in gamma_2.inputs if input_.identifier=='Color'), None)
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
                input_ = next((input_ for input_ in gamma_2.inputs if input_.identifier=='Gamma'), None)
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
                        input_.name = 'Gamma'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in gamma_2.outputs if output.identifier=='Color'), None)
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

                group_input_003_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_003_2, 'color'):
                    group_input_003_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_003_2, 'hide'):
                    group_input_003_2.hide = False
                if hasattr(group_input_003_2, 'location'):
                    group_input_003_2.location = (-640.0, -161.0)
                if hasattr(group_input_003_2, 'mute'):
                    group_input_003_2.mute = False
                if hasattr(group_input_003_2, 'name'):
                    group_input_003_2.name = 'Group Input.003'
                if hasattr(group_input_003_2, 'use_custom_color'):
                    group_input_003_2.use_custom_color = True
                if hasattr(group_input_003_2, 'width'):
                    group_input_003_2.width = 140.0
                if hasattr(group_input_003_2.outputs[0], 'default_value'):
                    group_input_003_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_003_2.outputs[0], 'display_shape'):
                    group_input_003_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[0], 'enabled'):
                    group_input_003_2.outputs[0].enabled = True
                if hasattr(group_input_003_2.outputs[0], 'hide'):
                    group_input_003_2.outputs[0].hide = False
                if hasattr(group_input_003_2.outputs[0], 'hide_value'):
                    group_input_003_2.outputs[0].hide_value = False
                if hasattr(group_input_003_2.outputs[0], 'name'):
                    group_input_003_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_003_2.outputs[0], 'show_expanded'):
                    group_input_003_2.outputs[0].show_expanded = False
                if hasattr(group_input_003_2.outputs[1], 'default_value'):
                    group_input_003_2.outputs[1].default_value = 0.0
                if hasattr(group_input_003_2.outputs[1], 'display_shape'):
                    group_input_003_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[1], 'enabled'):
                    group_input_003_2.outputs[1].enabled = True
                if hasattr(group_input_003_2.outputs[1], 'hide'):
                    group_input_003_2.outputs[1].hide = True
                if hasattr(group_input_003_2.outputs[1], 'hide_value'):
                    group_input_003_2.outputs[1].hide_value = True
                if hasattr(group_input_003_2.outputs[1], 'name'):
                    group_input_003_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_003_2.outputs[1], 'show_expanded'):
                    group_input_003_2.outputs[1].show_expanded = False
                if hasattr(group_input_003_2.outputs[2], 'default_value'):
                    group_input_003_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_003_2.outputs[2], 'display_shape'):
                    group_input_003_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[2], 'enabled'):
                    group_input_003_2.outputs[2].enabled = True
                if hasattr(group_input_003_2.outputs[2], 'hide'):
                    group_input_003_2.outputs[2].hide = True
                if hasattr(group_input_003_2.outputs[2], 'hide_value'):
                    group_input_003_2.outputs[2].hide_value = False
                if hasattr(group_input_003_2.outputs[2], 'name'):
                    group_input_003_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_003_2.outputs[2], 'show_expanded'):
                    group_input_003_2.outputs[2].show_expanded = False
                if hasattr(group_input_003_2.outputs[3], 'default_value'):
                    group_input_003_2.outputs[3].default_value = 0.5
                if hasattr(group_input_003_2.outputs[3], 'display_shape'):
                    group_input_003_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[3], 'enabled'):
                    group_input_003_2.outputs[3].enabled = True
                if hasattr(group_input_003_2.outputs[3], 'hide'):
                    group_input_003_2.outputs[3].hide = True
                if hasattr(group_input_003_2.outputs[3], 'hide_value'):
                    group_input_003_2.outputs[3].hide_value = False
                if hasattr(group_input_003_2.outputs[3], 'name'):
                    group_input_003_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_003_2.outputs[3], 'show_expanded'):
                    group_input_003_2.outputs[3].show_expanded = False
                if hasattr(group_input_003_2.outputs[4], 'default_value'):
                    group_input_003_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_003_2.outputs[4], 'display_shape'):
                    group_input_003_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[4], 'enabled'):
                    group_input_003_2.outputs[4].enabled = True
                if hasattr(group_input_003_2.outputs[4], 'hide'):
                    group_input_003_2.outputs[4].hide = True
                if hasattr(group_input_003_2.outputs[4], 'hide_value'):
                    group_input_003_2.outputs[4].hide_value = False
                if hasattr(group_input_003_2.outputs[4], 'name'):
                    group_input_003_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_003_2.outputs[4], 'show_expanded'):
                    group_input_003_2.outputs[4].show_expanded = False
                if hasattr(group_input_003_2.outputs[5], 'default_value'):
                    group_input_003_2.outputs[5].default_value = 0.0
                if hasattr(group_input_003_2.outputs[5], 'display_shape'):
                    group_input_003_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[5], 'enabled'):
                    group_input_003_2.outputs[5].enabled = True
                if hasattr(group_input_003_2.outputs[5], 'hide'):
                    group_input_003_2.outputs[5].hide = True
                if hasattr(group_input_003_2.outputs[5], 'hide_value'):
                    group_input_003_2.outputs[5].hide_value = True
                if hasattr(group_input_003_2.outputs[5], 'name'):
                    group_input_003_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_003_2.outputs[5], 'show_expanded'):
                    group_input_003_2.outputs[5].show_expanded = False
                if hasattr(group_input_003_2.outputs[6], 'default_value'):
                    group_input_003_2.outputs[6].default_value = 0.5
                if hasattr(group_input_003_2.outputs[6], 'display_shape'):
                    group_input_003_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[6], 'enabled'):
                    group_input_003_2.outputs[6].enabled = True
                if hasattr(group_input_003_2.outputs[6], 'hide'):
                    group_input_003_2.outputs[6].hide = True
                if hasattr(group_input_003_2.outputs[6], 'hide_value'):
                    group_input_003_2.outputs[6].hide_value = False
                if hasattr(group_input_003_2.outputs[6], 'name'):
                    group_input_003_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_003_2.outputs[6], 'show_expanded'):
                    group_input_003_2.outputs[6].show_expanded = False
                if hasattr(group_input_003_2.outputs[7], 'default_value'):
                    group_input_003_2.outputs[7].default_value = 0.0
                if hasattr(group_input_003_2.outputs[7], 'display_shape'):
                    group_input_003_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[7], 'enabled'):
                    group_input_003_2.outputs[7].enabled = True
                if hasattr(group_input_003_2.outputs[7], 'hide'):
                    group_input_003_2.outputs[7].hide = True
                if hasattr(group_input_003_2.outputs[7], 'hide_value'):
                    group_input_003_2.outputs[7].hide_value = False
                if hasattr(group_input_003_2.outputs[7], 'name'):
                    group_input_003_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_003_2.outputs[7], 'show_expanded'):
                    group_input_003_2.outputs[7].show_expanded = False
                if hasattr(group_input_003_2.outputs[8], 'default_value'):
                    group_input_003_2.outputs[8].default_value = 0.0
                if hasattr(group_input_003_2.outputs[8], 'display_shape'):
                    group_input_003_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[8], 'enabled'):
                    group_input_003_2.outputs[8].enabled = True
                if hasattr(group_input_003_2.outputs[8], 'hide'):
                    group_input_003_2.outputs[8].hide = True
                if hasattr(group_input_003_2.outputs[8], 'hide_value'):
                    group_input_003_2.outputs[8].hide_value = False
                if hasattr(group_input_003_2.outputs[8], 'name'):
                    group_input_003_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_003_2.outputs[8], 'show_expanded'):
                    group_input_003_2.outputs[8].show_expanded = False
                if hasattr(group_input_003_2.outputs[9], 'default_value'):
                    group_input_003_2.outputs[9].default_value = 1.0
                if hasattr(group_input_003_2.outputs[9], 'display_shape'):
                    group_input_003_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[9], 'enabled'):
                    group_input_003_2.outputs[9].enabled = True
                if hasattr(group_input_003_2.outputs[9], 'hide'):
                    group_input_003_2.outputs[9].hide = True
                if hasattr(group_input_003_2.outputs[9], 'hide_value'):
                    group_input_003_2.outputs[9].hide_value = False
                if hasattr(group_input_003_2.outputs[9], 'name'):
                    group_input_003_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_003_2.outputs[9], 'show_expanded'):
                    group_input_003_2.outputs[9].show_expanded = False
                if hasattr(group_input_003_2.outputs[10], 'default_value'):
                    group_input_003_2.outputs[10].default_value = 2.0
                if hasattr(group_input_003_2.outputs[10], 'display_shape'):
                    group_input_003_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[10], 'enabled'):
                    group_input_003_2.outputs[10].enabled = True
                if hasattr(group_input_003_2.outputs[10], 'hide'):
                    group_input_003_2.outputs[10].hide = True
                if hasattr(group_input_003_2.outputs[10], 'hide_value'):
                    group_input_003_2.outputs[10].hide_value = False
                if hasattr(group_input_003_2.outputs[10], 'name'):
                    group_input_003_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_003_2.outputs[10], 'show_expanded'):
                    group_input_003_2.outputs[10].show_expanded = False
                if hasattr(group_input_003_2.outputs[11], 'default_value'):
                    group_input_003_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_003_2.outputs[11], 'display_shape'):
                    group_input_003_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[11], 'enabled'):
                    group_input_003_2.outputs[11].enabled = True
                if hasattr(group_input_003_2.outputs[11], 'hide'):
                    group_input_003_2.outputs[11].hide = True
                if hasattr(group_input_003_2.outputs[11], 'hide_value'):
                    group_input_003_2.outputs[11].hide_value = False
                if hasattr(group_input_003_2.outputs[11], 'name'):
                    group_input_003_2.outputs[11].name = '    Hue'
                if hasattr(group_input_003_2.outputs[11], 'show_expanded'):
                    group_input_003_2.outputs[11].show_expanded = False
                if hasattr(group_input_003_2.outputs[12], 'default_value'):
                    group_input_003_2.outputs[12].default_value = 1.0
                if hasattr(group_input_003_2.outputs[12], 'display_shape'):
                    group_input_003_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[12], 'enabled'):
                    group_input_003_2.outputs[12].enabled = True
                if hasattr(group_input_003_2.outputs[12], 'hide'):
                    group_input_003_2.outputs[12].hide = True
                if hasattr(group_input_003_2.outputs[12], 'hide_value'):
                    group_input_003_2.outputs[12].hide_value = False
                if hasattr(group_input_003_2.outputs[12], 'name'):
                    group_input_003_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_003_2.outputs[12], 'show_expanded'):
                    group_input_003_2.outputs[12].show_expanded = False
                if hasattr(group_input_003_2.outputs[13], 'default_value'):
                    group_input_003_2.outputs[13].default_value = 0.0
                if hasattr(group_input_003_2.outputs[13], 'display_shape'):
                    group_input_003_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[13], 'enabled'):
                    group_input_003_2.outputs[13].enabled = True
                if hasattr(group_input_003_2.outputs[13], 'hide'):
                    group_input_003_2.outputs[13].hide = True
                if hasattr(group_input_003_2.outputs[13], 'hide_value'):
                    group_input_003_2.outputs[13].hide_value = True
                if hasattr(group_input_003_2.outputs[13], 'name'):
                    group_input_003_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_003_2.outputs[13], 'show_expanded'):
                    group_input_003_2.outputs[13].show_expanded = False
                if hasattr(group_input_003_2.outputs[14], 'default_value'):
                    group_input_003_2.outputs[14].default_value = 0.0
                if hasattr(group_input_003_2.outputs[14], 'display_shape'):
                    group_input_003_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[14], 'enabled'):
                    group_input_003_2.outputs[14].enabled = True
                if hasattr(group_input_003_2.outputs[14], 'hide'):
                    group_input_003_2.outputs[14].hide = False
                if hasattr(group_input_003_2.outputs[14], 'hide_value'):
                    group_input_003_2.outputs[14].hide_value = False
                if hasattr(group_input_003_2.outputs[14], 'name'):
                    group_input_003_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_003_2.outputs[14], 'show_expanded'):
                    group_input_003_2.outputs[14].show_expanded = False
                if hasattr(group_input_003_2.outputs[15], 'default_value'):
                    group_input_003_2.outputs[15].default_value = 0.0
                if hasattr(group_input_003_2.outputs[15], 'display_shape'):
                    group_input_003_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[15], 'enabled'):
                    group_input_003_2.outputs[15].enabled = True
                if hasattr(group_input_003_2.outputs[15], 'hide'):
                    group_input_003_2.outputs[15].hide = True
                if hasattr(group_input_003_2.outputs[15], 'hide_value'):
                    group_input_003_2.outputs[15].hide_value = False
                if hasattr(group_input_003_2.outputs[15], 'name'):
                    group_input_003_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_003_2.outputs[15], 'show_expanded'):
                    group_input_003_2.outputs[15].show_expanded = False
                if hasattr(group_input_003_2.outputs[16], 'default_value'):
                    group_input_003_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_003_2.outputs[16], 'display_shape'):
                    group_input_003_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[16], 'enabled'):
                    group_input_003_2.outputs[16].enabled = True
                if hasattr(group_input_003_2.outputs[16], 'hide'):
                    group_input_003_2.outputs[16].hide = True
                if hasattr(group_input_003_2.outputs[16], 'hide_value'):
                    group_input_003_2.outputs[16].hide_value = False
                if hasattr(group_input_003_2.outputs[16], 'name'):
                    group_input_003_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_003_2.outputs[16], 'show_expanded'):
                    group_input_003_2.outputs[16].show_expanded = False
                if hasattr(group_input_003_2.outputs[17], 'default_value'):
                    group_input_003_2.outputs[17].default_value = 0.5
                if hasattr(group_input_003_2.outputs[17], 'display_shape'):
                    group_input_003_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[17], 'enabled'):
                    group_input_003_2.outputs[17].enabled = True
                if hasattr(group_input_003_2.outputs[17], 'hide'):
                    group_input_003_2.outputs[17].hide = True
                if hasattr(group_input_003_2.outputs[17], 'hide_value'):
                    group_input_003_2.outputs[17].hide_value = False
                if hasattr(group_input_003_2.outputs[17], 'name'):
                    group_input_003_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_003_2.outputs[17], 'show_expanded'):
                    group_input_003_2.outputs[17].show_expanded = False
                if hasattr(group_input_003_2.outputs[18], 'default_value'):
                    group_input_003_2.outputs[18].default_value = 0.5
                if hasattr(group_input_003_2.outputs[18], 'display_shape'):
                    group_input_003_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[18], 'enabled'):
                    group_input_003_2.outputs[18].enabled = True
                if hasattr(group_input_003_2.outputs[18], 'hide'):
                    group_input_003_2.outputs[18].hide = True
                if hasattr(group_input_003_2.outputs[18], 'hide_value'):
                    group_input_003_2.outputs[18].hide_value = False
                if hasattr(group_input_003_2.outputs[18], 'name'):
                    group_input_003_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_003_2.outputs[18], 'show_expanded'):
                    group_input_003_2.outputs[18].show_expanded = False
                if hasattr(group_input_003_2.outputs[19], 'default_value'):
                    group_input_003_2.outputs[19].default_value = 0.5
                if hasattr(group_input_003_2.outputs[19], 'display_shape'):
                    group_input_003_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_003_2.outputs[19], 'enabled'):
                    group_input_003_2.outputs[19].enabled = True
                if hasattr(group_input_003_2.outputs[19], 'hide'):
                    group_input_003_2.outputs[19].hide = True
                if hasattr(group_input_003_2.outputs[19], 'hide_value'):
                    group_input_003_2.outputs[19].hide_value = False
                if hasattr(group_input_003_2.outputs[19], 'name'):
                    group_input_003_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_003_2.outputs[19], 'show_expanded'):
                    group_input_003_2.outputs[19].show_expanded = False

                hue_saturation_value_001_2 = node_tree2.nodes.new('ShaderNodeHueSaturation')
                if hasattr(hue_saturation_value_001_2, 'color'):
                    hue_saturation_value_001_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(hue_saturation_value_001_2, 'hide'):
                    hue_saturation_value_001_2.hide = False
                if hasattr(hue_saturation_value_001_2, 'location'):
                    hue_saturation_value_001_2.location = (-640.0, 0.0)
                if hasattr(hue_saturation_value_001_2, 'mute'):
                    hue_saturation_value_001_2.mute = False
                if hasattr(hue_saturation_value_001_2, 'name'):
                    hue_saturation_value_001_2.name = 'Hue Saturation Value.001'
                if hasattr(hue_saturation_value_001_2, 'use_custom_color'):
                    hue_saturation_value_001_2.use_custom_color = False
                if hasattr(hue_saturation_value_001_2, 'width'):
                    hue_saturation_value_001_2.width = 140.0
                input_ = next((input_ for input_ in hue_saturation_value_001_2.inputs if input_.identifier=='Hue'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.49999991059303284
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = False
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Hue'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in hue_saturation_value_001_2.inputs if input_.identifier=='Saturation'), None)
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
                        input_.name = 'Saturation'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in hue_saturation_value_001_2.inputs if input_.identifier=='Value'), None)
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
                        input_.name = 'Value'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in hue_saturation_value_001_2.inputs if input_.identifier=='Fac'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
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
                input_ = next((input_ for input_ in hue_saturation_value_001_2.inputs if input_.identifier=='Color'), None)
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
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in hue_saturation_value_001_2.outputs if output.identifier=='Color'), None)
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

                rgb_to_bw_2 = node_tree2.nodes.new('ShaderNodeRGBToBW')
                if hasattr(rgb_to_bw_2, 'color'):
                    rgb_to_bw_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(rgb_to_bw_2, 'hide'):
                    rgb_to_bw_2.hide = False
                if hasattr(rgb_to_bw_2, 'location'):
                    rgb_to_bw_2.location = (-480.0, -189.0)
                if hasattr(rgb_to_bw_2, 'mute'):
                    rgb_to_bw_2.mute = False
                if hasattr(rgb_to_bw_2, 'name'):
                    rgb_to_bw_2.name = 'RGB to BW'
                if hasattr(rgb_to_bw_2, 'use_custom_color'):
                    rgb_to_bw_2.use_custom_color = False
                if hasattr(rgb_to_bw_2, 'width'):
                    rgb_to_bw_2.width = 140.0
                input_ = next((input_ for input_ in rgb_to_bw_2.inputs if input_.identifier=='Color'), None)
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
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in rgb_to_bw_2.outputs if output.identifier=='Val'), None)
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
                        output.name = 'Val'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False

                group_input_010_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_010_2, 'color'):
                    group_input_010_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_010_2, 'hide'):
                    group_input_010_2.hide = False
                if hasattr(group_input_010_2, 'location'):
                    group_input_010_2.location = (-480.0, 0.0)
                if hasattr(group_input_010_2, 'mute'):
                    group_input_010_2.mute = False
                if hasattr(group_input_010_2, 'name'):
                    group_input_010_2.name = 'Group Input.010'
                if hasattr(group_input_010_2, 'use_custom_color'):
                    group_input_010_2.use_custom_color = True
                if hasattr(group_input_010_2, 'width'):
                    group_input_010_2.width = 140.0
                if hasattr(group_input_010_2.outputs[0], 'default_value'):
                    group_input_010_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_010_2.outputs[0], 'display_shape'):
                    group_input_010_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[0], 'enabled'):
                    group_input_010_2.outputs[0].enabled = True
                if hasattr(group_input_010_2.outputs[0], 'hide'):
                    group_input_010_2.outputs[0].hide = True
                if hasattr(group_input_010_2.outputs[0], 'hide_value'):
                    group_input_010_2.outputs[0].hide_value = False
                if hasattr(group_input_010_2.outputs[0], 'name'):
                    group_input_010_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_010_2.outputs[0], 'show_expanded'):
                    group_input_010_2.outputs[0].show_expanded = False
                if hasattr(group_input_010_2.outputs[1], 'default_value'):
                    group_input_010_2.outputs[1].default_value = 0.0
                if hasattr(group_input_010_2.outputs[1], 'display_shape'):
                    group_input_010_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[1], 'enabled'):
                    group_input_010_2.outputs[1].enabled = True
                if hasattr(group_input_010_2.outputs[1], 'hide'):
                    group_input_010_2.outputs[1].hide = True
                if hasattr(group_input_010_2.outputs[1], 'hide_value'):
                    group_input_010_2.outputs[1].hide_value = True
                if hasattr(group_input_010_2.outputs[1], 'name'):
                    group_input_010_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_010_2.outputs[1], 'show_expanded'):
                    group_input_010_2.outputs[1].show_expanded = False
                if hasattr(group_input_010_2.outputs[2], 'default_value'):
                    group_input_010_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_010_2.outputs[2], 'display_shape'):
                    group_input_010_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[2], 'enabled'):
                    group_input_010_2.outputs[2].enabled = True
                if hasattr(group_input_010_2.outputs[2], 'hide'):
                    group_input_010_2.outputs[2].hide = True
                if hasattr(group_input_010_2.outputs[2], 'hide_value'):
                    group_input_010_2.outputs[2].hide_value = False
                if hasattr(group_input_010_2.outputs[2], 'name'):
                    group_input_010_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_010_2.outputs[2], 'show_expanded'):
                    group_input_010_2.outputs[2].show_expanded = False
                if hasattr(group_input_010_2.outputs[3], 'default_value'):
                    group_input_010_2.outputs[3].default_value = 0.5
                if hasattr(group_input_010_2.outputs[3], 'display_shape'):
                    group_input_010_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[3], 'enabled'):
                    group_input_010_2.outputs[3].enabled = True
                if hasattr(group_input_010_2.outputs[3], 'hide'):
                    group_input_010_2.outputs[3].hide = True
                if hasattr(group_input_010_2.outputs[3], 'hide_value'):
                    group_input_010_2.outputs[3].hide_value = False
                if hasattr(group_input_010_2.outputs[3], 'name'):
                    group_input_010_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_010_2.outputs[3], 'show_expanded'):
                    group_input_010_2.outputs[3].show_expanded = False
                if hasattr(group_input_010_2.outputs[4], 'default_value'):
                    group_input_010_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_010_2.outputs[4], 'display_shape'):
                    group_input_010_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[4], 'enabled'):
                    group_input_010_2.outputs[4].enabled = True
                if hasattr(group_input_010_2.outputs[4], 'hide'):
                    group_input_010_2.outputs[4].hide = True
                if hasattr(group_input_010_2.outputs[4], 'hide_value'):
                    group_input_010_2.outputs[4].hide_value = False
                if hasattr(group_input_010_2.outputs[4], 'name'):
                    group_input_010_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_010_2.outputs[4], 'show_expanded'):
                    group_input_010_2.outputs[4].show_expanded = False
                if hasattr(group_input_010_2.outputs[5], 'default_value'):
                    group_input_010_2.outputs[5].default_value = 0.0
                if hasattr(group_input_010_2.outputs[5], 'display_shape'):
                    group_input_010_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[5], 'enabled'):
                    group_input_010_2.outputs[5].enabled = True
                if hasattr(group_input_010_2.outputs[5], 'hide'):
                    group_input_010_2.outputs[5].hide = True
                if hasattr(group_input_010_2.outputs[5], 'hide_value'):
                    group_input_010_2.outputs[5].hide_value = True
                if hasattr(group_input_010_2.outputs[5], 'name'):
                    group_input_010_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_010_2.outputs[5], 'show_expanded'):
                    group_input_010_2.outputs[5].show_expanded = False
                if hasattr(group_input_010_2.outputs[6], 'default_value'):
                    group_input_010_2.outputs[6].default_value = 0.5
                if hasattr(group_input_010_2.outputs[6], 'display_shape'):
                    group_input_010_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[6], 'enabled'):
                    group_input_010_2.outputs[6].enabled = True
                if hasattr(group_input_010_2.outputs[6], 'hide'):
                    group_input_010_2.outputs[6].hide = False
                if hasattr(group_input_010_2.outputs[6], 'hide_value'):
                    group_input_010_2.outputs[6].hide_value = False
                if hasattr(group_input_010_2.outputs[6], 'name'):
                    group_input_010_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_010_2.outputs[6], 'show_expanded'):
                    group_input_010_2.outputs[6].show_expanded = False
                if hasattr(group_input_010_2.outputs[7], 'default_value'):
                    group_input_010_2.outputs[7].default_value = 0.0
                if hasattr(group_input_010_2.outputs[7], 'display_shape'):
                    group_input_010_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[7], 'enabled'):
                    group_input_010_2.outputs[7].enabled = True
                if hasattr(group_input_010_2.outputs[7], 'hide'):
                    group_input_010_2.outputs[7].hide = True
                if hasattr(group_input_010_2.outputs[7], 'hide_value'):
                    group_input_010_2.outputs[7].hide_value = False
                if hasattr(group_input_010_2.outputs[7], 'name'):
                    group_input_010_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_010_2.outputs[7], 'show_expanded'):
                    group_input_010_2.outputs[7].show_expanded = False
                if hasattr(group_input_010_2.outputs[8], 'default_value'):
                    group_input_010_2.outputs[8].default_value = 0.0
                if hasattr(group_input_010_2.outputs[8], 'display_shape'):
                    group_input_010_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[8], 'enabled'):
                    group_input_010_2.outputs[8].enabled = True
                if hasattr(group_input_010_2.outputs[8], 'hide'):
                    group_input_010_2.outputs[8].hide = True
                if hasattr(group_input_010_2.outputs[8], 'hide_value'):
                    group_input_010_2.outputs[8].hide_value = False
                if hasattr(group_input_010_2.outputs[8], 'name'):
                    group_input_010_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_010_2.outputs[8], 'show_expanded'):
                    group_input_010_2.outputs[8].show_expanded = False
                if hasattr(group_input_010_2.outputs[9], 'default_value'):
                    group_input_010_2.outputs[9].default_value = 1.0
                if hasattr(group_input_010_2.outputs[9], 'display_shape'):
                    group_input_010_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[9], 'enabled'):
                    group_input_010_2.outputs[9].enabled = True
                if hasattr(group_input_010_2.outputs[9], 'hide'):
                    group_input_010_2.outputs[9].hide = True
                if hasattr(group_input_010_2.outputs[9], 'hide_value'):
                    group_input_010_2.outputs[9].hide_value = False
                if hasattr(group_input_010_2.outputs[9], 'name'):
                    group_input_010_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_010_2.outputs[9], 'show_expanded'):
                    group_input_010_2.outputs[9].show_expanded = False
                if hasattr(group_input_010_2.outputs[10], 'default_value'):
                    group_input_010_2.outputs[10].default_value = 2.0
                if hasattr(group_input_010_2.outputs[10], 'display_shape'):
                    group_input_010_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[10], 'enabled'):
                    group_input_010_2.outputs[10].enabled = True
                if hasattr(group_input_010_2.outputs[10], 'hide'):
                    group_input_010_2.outputs[10].hide = True
                if hasattr(group_input_010_2.outputs[10], 'hide_value'):
                    group_input_010_2.outputs[10].hide_value = False
                if hasattr(group_input_010_2.outputs[10], 'name'):
                    group_input_010_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_010_2.outputs[10], 'show_expanded'):
                    group_input_010_2.outputs[10].show_expanded = False
                if hasattr(group_input_010_2.outputs[11], 'default_value'):
                    group_input_010_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_010_2.outputs[11], 'display_shape'):
                    group_input_010_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[11], 'enabled'):
                    group_input_010_2.outputs[11].enabled = True
                if hasattr(group_input_010_2.outputs[11], 'hide'):
                    group_input_010_2.outputs[11].hide = True
                if hasattr(group_input_010_2.outputs[11], 'hide_value'):
                    group_input_010_2.outputs[11].hide_value = False
                if hasattr(group_input_010_2.outputs[11], 'name'):
                    group_input_010_2.outputs[11].name = '    Hue'
                if hasattr(group_input_010_2.outputs[11], 'show_expanded'):
                    group_input_010_2.outputs[11].show_expanded = False
                if hasattr(group_input_010_2.outputs[12], 'default_value'):
                    group_input_010_2.outputs[12].default_value = 1.0
                if hasattr(group_input_010_2.outputs[12], 'display_shape'):
                    group_input_010_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[12], 'enabled'):
                    group_input_010_2.outputs[12].enabled = True
                if hasattr(group_input_010_2.outputs[12], 'hide'):
                    group_input_010_2.outputs[12].hide = True
                if hasattr(group_input_010_2.outputs[12], 'hide_value'):
                    group_input_010_2.outputs[12].hide_value = False
                if hasattr(group_input_010_2.outputs[12], 'name'):
                    group_input_010_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_010_2.outputs[12], 'show_expanded'):
                    group_input_010_2.outputs[12].show_expanded = False
                if hasattr(group_input_010_2.outputs[13], 'default_value'):
                    group_input_010_2.outputs[13].default_value = 0.0
                if hasattr(group_input_010_2.outputs[13], 'display_shape'):
                    group_input_010_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[13], 'enabled'):
                    group_input_010_2.outputs[13].enabled = True
                if hasattr(group_input_010_2.outputs[13], 'hide'):
                    group_input_010_2.outputs[13].hide = True
                if hasattr(group_input_010_2.outputs[13], 'hide_value'):
                    group_input_010_2.outputs[13].hide_value = True
                if hasattr(group_input_010_2.outputs[13], 'name'):
                    group_input_010_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_010_2.outputs[13], 'show_expanded'):
                    group_input_010_2.outputs[13].show_expanded = False
                if hasattr(group_input_010_2.outputs[14], 'default_value'):
                    group_input_010_2.outputs[14].default_value = 0.0
                if hasattr(group_input_010_2.outputs[14], 'display_shape'):
                    group_input_010_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[14], 'enabled'):
                    group_input_010_2.outputs[14].enabled = True
                if hasattr(group_input_010_2.outputs[14], 'hide'):
                    group_input_010_2.outputs[14].hide = True
                if hasattr(group_input_010_2.outputs[14], 'hide_value'):
                    group_input_010_2.outputs[14].hide_value = False
                if hasattr(group_input_010_2.outputs[14], 'name'):
                    group_input_010_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_010_2.outputs[14], 'show_expanded'):
                    group_input_010_2.outputs[14].show_expanded = False
                if hasattr(group_input_010_2.outputs[15], 'default_value'):
                    group_input_010_2.outputs[15].default_value = 0.0
                if hasattr(group_input_010_2.outputs[15], 'display_shape'):
                    group_input_010_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[15], 'enabled'):
                    group_input_010_2.outputs[15].enabled = True
                if hasattr(group_input_010_2.outputs[15], 'hide'):
                    group_input_010_2.outputs[15].hide = True
                if hasattr(group_input_010_2.outputs[15], 'hide_value'):
                    group_input_010_2.outputs[15].hide_value = False
                if hasattr(group_input_010_2.outputs[15], 'name'):
                    group_input_010_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_010_2.outputs[15], 'show_expanded'):
                    group_input_010_2.outputs[15].show_expanded = False
                if hasattr(group_input_010_2.outputs[16], 'default_value'):
                    group_input_010_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_010_2.outputs[16], 'display_shape'):
                    group_input_010_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[16], 'enabled'):
                    group_input_010_2.outputs[16].enabled = True
                if hasattr(group_input_010_2.outputs[16], 'hide'):
                    group_input_010_2.outputs[16].hide = True
                if hasattr(group_input_010_2.outputs[16], 'hide_value'):
                    group_input_010_2.outputs[16].hide_value = False
                if hasattr(group_input_010_2.outputs[16], 'name'):
                    group_input_010_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_010_2.outputs[16], 'show_expanded'):
                    group_input_010_2.outputs[16].show_expanded = False
                if hasattr(group_input_010_2.outputs[17], 'default_value'):
                    group_input_010_2.outputs[17].default_value = 0.5
                if hasattr(group_input_010_2.outputs[17], 'display_shape'):
                    group_input_010_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[17], 'enabled'):
                    group_input_010_2.outputs[17].enabled = True
                if hasattr(group_input_010_2.outputs[17], 'hide'):
                    group_input_010_2.outputs[17].hide = True
                if hasattr(group_input_010_2.outputs[17], 'hide_value'):
                    group_input_010_2.outputs[17].hide_value = False
                if hasattr(group_input_010_2.outputs[17], 'name'):
                    group_input_010_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_010_2.outputs[17], 'show_expanded'):
                    group_input_010_2.outputs[17].show_expanded = False
                if hasattr(group_input_010_2.outputs[18], 'default_value'):
                    group_input_010_2.outputs[18].default_value = 0.5
                if hasattr(group_input_010_2.outputs[18], 'display_shape'):
                    group_input_010_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[18], 'enabled'):
                    group_input_010_2.outputs[18].enabled = True
                if hasattr(group_input_010_2.outputs[18], 'hide'):
                    group_input_010_2.outputs[18].hide = True
                if hasattr(group_input_010_2.outputs[18], 'hide_value'):
                    group_input_010_2.outputs[18].hide_value = False
                if hasattr(group_input_010_2.outputs[18], 'name'):
                    group_input_010_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_010_2.outputs[18], 'show_expanded'):
                    group_input_010_2.outputs[18].show_expanded = False
                if hasattr(group_input_010_2.outputs[19], 'default_value'):
                    group_input_010_2.outputs[19].default_value = 0.5
                if hasattr(group_input_010_2.outputs[19], 'display_shape'):
                    group_input_010_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_010_2.outputs[19], 'enabled'):
                    group_input_010_2.outputs[19].enabled = True
                if hasattr(group_input_010_2.outputs[19], 'hide'):
                    group_input_010_2.outputs[19].hide = True
                if hasattr(group_input_010_2.outputs[19], 'hide_value'):
                    group_input_010_2.outputs[19].hide_value = False
                if hasattr(group_input_010_2.outputs[19], 'name'):
                    group_input_010_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_010_2.outputs[19], 'show_expanded'):
                    group_input_010_2.outputs[19].show_expanded = False

                glowing_level_2 = node_tree2.nodes.new('ShaderNodeMix')
                if hasattr(glowing_level_2, 'blend_type'):
                    glowing_level_2.blend_type = 'MULTIPLY'
                if hasattr(glowing_level_2, 'clamp_factor'):
                    glowing_level_2.clamp_factor = True
                if hasattr(glowing_level_2, 'clamp_result'):
                    glowing_level_2.clamp_result = False
                if hasattr(glowing_level_2, 'color'):
                    glowing_level_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(glowing_level_2, 'data_type'):
                    glowing_level_2.data_type = 'RGBA'
                if hasattr(glowing_level_2, 'factor_mode'):
                    glowing_level_2.factor_mode = 'UNIFORM'
                if hasattr(glowing_level_2, 'hide'):
                    glowing_level_2.hide = False
                if hasattr(glowing_level_2, 'label'):
                    glowing_level_2.label = 'Glowing Level'
                if hasattr(glowing_level_2, 'location'):
                    glowing_level_2.location = (-480.0, -72.0)
                if hasattr(glowing_level_2, 'mute'):
                    glowing_level_2.mute = False
                if hasattr(glowing_level_2, 'name'):
                    glowing_level_2.name = 'Glowing Level'
                if hasattr(glowing_level_2, 'use_custom_color'):
                    glowing_level_2.use_custom_color = False
                if hasattr(glowing_level_2, 'width'):
                    glowing_level_2.width = 140.0
                input_ = next((input_ for input_ in glowing_level_2.inputs if input_.identifier=='Factor_Float'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = True
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glowing_level_2.inputs if input_.identifier=='Factor_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.5, 0.5, 0.5)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glowing_level_2.inputs if input_.identifier=='A_Float'), None)
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
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glowing_level_2.inputs if input_.identifier=='B_Float'), None)
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
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glowing_level_2.inputs if input_.identifier=='A_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glowing_level_2.inputs if input_.identifier=='B_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glowing_level_2.inputs if input_.identifier=='A_Color'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (1.0, 0.0, 0.015682758763432503, 1.0)
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
                input_ = next((input_ for input_ in glowing_level_2.inputs if input_.identifier=='B_Color'), None)
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
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                output = next((output for output in glowing_level_2.outputs if output.identifier=='Result_Float'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in glowing_level_2.outputs if output.identifier=='Result_Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in glowing_level_2.outputs if output.identifier=='Result_Color'), None)
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

                group_input_006_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_006_2, 'color'):
                    group_input_006_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_006_2, 'hide'):
                    group_input_006_2.hide = False
                if hasattr(group_input_006_2, 'location'):
                    group_input_006_2.location = (-320.0, 0.0)
                if hasattr(group_input_006_2, 'mute'):
                    group_input_006_2.mute = False
                if hasattr(group_input_006_2, 'name'):
                    group_input_006_2.name = 'Group Input.006'
                if hasattr(group_input_006_2, 'use_custom_color'):
                    group_input_006_2.use_custom_color = True
                if hasattr(group_input_006_2, 'width'):
                    group_input_006_2.width = 140.0
                if hasattr(group_input_006_2.outputs[0], 'default_value'):
                    group_input_006_2.outputs[0].default_value = (0.5, 0.5, 0.5, 1.0)
                if hasattr(group_input_006_2.outputs[0], 'display_shape'):
                    group_input_006_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[0], 'enabled'):
                    group_input_006_2.outputs[0].enabled = True
                if hasattr(group_input_006_2.outputs[0], 'hide'):
                    group_input_006_2.outputs[0].hide = True
                if hasattr(group_input_006_2.outputs[0], 'hide_value'):
                    group_input_006_2.outputs[0].hide_value = False
                if hasattr(group_input_006_2.outputs[0], 'name'):
                    group_input_006_2.outputs[0].name = 'Input Color'
                if hasattr(group_input_006_2.outputs[0], 'show_expanded'):
                    group_input_006_2.outputs[0].show_expanded = False
                if hasattr(group_input_006_2.outputs[1], 'default_value'):
                    group_input_006_2.outputs[1].default_value = 0.0
                if hasattr(group_input_006_2.outputs[1], 'display_shape'):
                    group_input_006_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[1], 'enabled'):
                    group_input_006_2.outputs[1].enabled = True
                if hasattr(group_input_006_2.outputs[1], 'hide'):
                    group_input_006_2.outputs[1].hide = True
                if hasattr(group_input_006_2.outputs[1], 'hide_value'):
                    group_input_006_2.outputs[1].hide_value = True
                if hasattr(group_input_006_2.outputs[1], 'name'):
                    group_input_006_2.outputs[1].name = 'COLOR VARIATION'
                if hasattr(group_input_006_2.outputs[1], 'show_expanded'):
                    group_input_006_2.outputs[1].show_expanded = False
                if hasattr(group_input_006_2.outputs[2], 'default_value'):
                    group_input_006_2.outputs[2].default_value = 0.20000000298023224
                if hasattr(group_input_006_2.outputs[2], 'display_shape'):
                    group_input_006_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[2], 'enabled'):
                    group_input_006_2.outputs[2].enabled = True
                if hasattr(group_input_006_2.outputs[2], 'hide'):
                    group_input_006_2.outputs[2].hide = True
                if hasattr(group_input_006_2.outputs[2], 'hide_value'):
                    group_input_006_2.outputs[2].hide_value = False
                if hasattr(group_input_006_2.outputs[2], 'name'):
                    group_input_006_2.outputs[2].name = '  Color Variation Scale'
                if hasattr(group_input_006_2.outputs[2], 'show_expanded'):
                    group_input_006_2.outputs[2].show_expanded = False
                if hasattr(group_input_006_2.outputs[3], 'default_value'):
                    group_input_006_2.outputs[3].default_value = 0.5
                if hasattr(group_input_006_2.outputs[3], 'display_shape'):
                    group_input_006_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[3], 'enabled'):
                    group_input_006_2.outputs[3].enabled = True
                if hasattr(group_input_006_2.outputs[3], 'hide'):
                    group_input_006_2.outputs[3].hide = True
                if hasattr(group_input_006_2.outputs[3], 'hide_value'):
                    group_input_006_2.outputs[3].hide_value = False
                if hasattr(group_input_006_2.outputs[3], 'name'):
                    group_input_006_2.outputs[3].name = '  Color Variation Distortion'
                if hasattr(group_input_006_2.outputs[3], 'show_expanded'):
                    group_input_006_2.outputs[3].show_expanded = False
                if hasattr(group_input_006_2.outputs[4], 'default_value'):
                    group_input_006_2.outputs[4].default_value = 0.20000000298023224
                if hasattr(group_input_006_2.outputs[4], 'display_shape'):
                    group_input_006_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[4], 'enabled'):
                    group_input_006_2.outputs[4].enabled = True
                if hasattr(group_input_006_2.outputs[4], 'hide'):
                    group_input_006_2.outputs[4].hide = True
                if hasattr(group_input_006_2.outputs[4], 'hide_value'):
                    group_input_006_2.outputs[4].hide_value = False
                if hasattr(group_input_006_2.outputs[4], 'name'):
                    group_input_006_2.outputs[4].name = '  Random Color Var'
                if hasattr(group_input_006_2.outputs[4], 'show_expanded'):
                    group_input_006_2.outputs[4].show_expanded = False
                if hasattr(group_input_006_2.outputs[5], 'default_value'):
                    group_input_006_2.outputs[5].default_value = 0.0
                if hasattr(group_input_006_2.outputs[5], 'display_shape'):
                    group_input_006_2.outputs[5].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[5], 'enabled'):
                    group_input_006_2.outputs[5].enabled = True
                if hasattr(group_input_006_2.outputs[5], 'hide'):
                    group_input_006_2.outputs[5].hide = True
                if hasattr(group_input_006_2.outputs[5], 'hide_value'):
                    group_input_006_2.outputs[5].hide_value = True
                if hasattr(group_input_006_2.outputs[5], 'name'):
                    group_input_006_2.outputs[5].name = 'COLOR ADJUSTMENTS'
                if hasattr(group_input_006_2.outputs[5], 'show_expanded'):
                    group_input_006_2.outputs[5].show_expanded = False
                if hasattr(group_input_006_2.outputs[6], 'default_value'):
                    group_input_006_2.outputs[6].default_value = 0.5
                if hasattr(group_input_006_2.outputs[6], 'display_shape'):
                    group_input_006_2.outputs[6].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[6], 'enabled'):
                    group_input_006_2.outputs[6].enabled = True
                if hasattr(group_input_006_2.outputs[6], 'hide'):
                    group_input_006_2.outputs[6].hide = True
                if hasattr(group_input_006_2.outputs[6], 'hide_value'):
                    group_input_006_2.outputs[6].hide_value = False
                if hasattr(group_input_006_2.outputs[6], 'name'):
                    group_input_006_2.outputs[6].name = '  Unpaint'
                if hasattr(group_input_006_2.outputs[6], 'show_expanded'):
                    group_input_006_2.outputs[6].show_expanded = False
                if hasattr(group_input_006_2.outputs[7], 'default_value'):
                    group_input_006_2.outputs[7].default_value = 0.0
                if hasattr(group_input_006_2.outputs[7], 'display_shape'):
                    group_input_006_2.outputs[7].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[7], 'enabled'):
                    group_input_006_2.outputs[7].enabled = True
                if hasattr(group_input_006_2.outputs[7], 'hide'):
                    group_input_006_2.outputs[7].hide = False
                if hasattr(group_input_006_2.outputs[7], 'hide_value'):
                    group_input_006_2.outputs[7].hide_value = False
                if hasattr(group_input_006_2.outputs[7], 'name'):
                    group_input_006_2.outputs[7].name = '  Color Inverter'
                if hasattr(group_input_006_2.outputs[7], 'show_expanded'):
                    group_input_006_2.outputs[7].show_expanded = False
                if hasattr(group_input_006_2.outputs[8], 'default_value'):
                    group_input_006_2.outputs[8].default_value = 0.0
                if hasattr(group_input_006_2.outputs[8], 'display_shape'):
                    group_input_006_2.outputs[8].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[8], 'enabled'):
                    group_input_006_2.outputs[8].enabled = True
                if hasattr(group_input_006_2.outputs[8], 'hide'):
                    group_input_006_2.outputs[8].hide = True
                if hasattr(group_input_006_2.outputs[8], 'hide_value'):
                    group_input_006_2.outputs[8].hide_value = False
                if hasattr(group_input_006_2.outputs[8], 'name'):
                    group_input_006_2.outputs[8].name = '  Contrast'
                if hasattr(group_input_006_2.outputs[8], 'show_expanded'):
                    group_input_006_2.outputs[8].show_expanded = False
                if hasattr(group_input_006_2.outputs[9], 'default_value'):
                    group_input_006_2.outputs[9].default_value = 1.0
                if hasattr(group_input_006_2.outputs[9], 'display_shape'):
                    group_input_006_2.outputs[9].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[9], 'enabled'):
                    group_input_006_2.outputs[9].enabled = True
                if hasattr(group_input_006_2.outputs[9], 'hide'):
                    group_input_006_2.outputs[9].hide = True
                if hasattr(group_input_006_2.outputs[9], 'hide_value'):
                    group_input_006_2.outputs[9].hide_value = False
                if hasattr(group_input_006_2.outputs[9], 'name'):
                    group_input_006_2.outputs[9].name = '  Gamma'
                if hasattr(group_input_006_2.outputs[9], 'show_expanded'):
                    group_input_006_2.outputs[9].show_expanded = False
                if hasattr(group_input_006_2.outputs[10], 'default_value'):
                    group_input_006_2.outputs[10].default_value = 2.0
                if hasattr(group_input_006_2.outputs[10], 'display_shape'):
                    group_input_006_2.outputs[10].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[10], 'enabled'):
                    group_input_006_2.outputs[10].enabled = True
                if hasattr(group_input_006_2.outputs[10], 'hide'):
                    group_input_006_2.outputs[10].hide = True
                if hasattr(group_input_006_2.outputs[10], 'hide_value'):
                    group_input_006_2.outputs[10].hide_value = False
                if hasattr(group_input_006_2.outputs[10], 'name'):
                    group_input_006_2.outputs[10].name = '  Hue / Sat Value'
                if hasattr(group_input_006_2.outputs[10], 'show_expanded'):
                    group_input_006_2.outputs[10].show_expanded = False
                if hasattr(group_input_006_2.outputs[11], 'default_value'):
                    group_input_006_2.outputs[11].default_value = 0.49999991059303284
                if hasattr(group_input_006_2.outputs[11], 'display_shape'):
                    group_input_006_2.outputs[11].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[11], 'enabled'):
                    group_input_006_2.outputs[11].enabled = True
                if hasattr(group_input_006_2.outputs[11], 'hide'):
                    group_input_006_2.outputs[11].hide = True
                if hasattr(group_input_006_2.outputs[11], 'hide_value'):
                    group_input_006_2.outputs[11].hide_value = False
                if hasattr(group_input_006_2.outputs[11], 'name'):
                    group_input_006_2.outputs[11].name = '    Hue'
                if hasattr(group_input_006_2.outputs[11], 'show_expanded'):
                    group_input_006_2.outputs[11].show_expanded = False
                if hasattr(group_input_006_2.outputs[12], 'default_value'):
                    group_input_006_2.outputs[12].default_value = 1.0
                if hasattr(group_input_006_2.outputs[12], 'display_shape'):
                    group_input_006_2.outputs[12].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[12], 'enabled'):
                    group_input_006_2.outputs[12].enabled = True
                if hasattr(group_input_006_2.outputs[12], 'hide'):
                    group_input_006_2.outputs[12].hide = True
                if hasattr(group_input_006_2.outputs[12], 'hide_value'):
                    group_input_006_2.outputs[12].hide_value = False
                if hasattr(group_input_006_2.outputs[12], 'name'):
                    group_input_006_2.outputs[12].name = '    Saturation'
                if hasattr(group_input_006_2.outputs[12], 'show_expanded'):
                    group_input_006_2.outputs[12].show_expanded = False
                if hasattr(group_input_006_2.outputs[13], 'default_value'):
                    group_input_006_2.outputs[13].default_value = 0.0
                if hasattr(group_input_006_2.outputs[13], 'display_shape'):
                    group_input_006_2.outputs[13].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[13], 'enabled'):
                    group_input_006_2.outputs[13].enabled = True
                if hasattr(group_input_006_2.outputs[13], 'hide'):
                    group_input_006_2.outputs[13].hide = True
                if hasattr(group_input_006_2.outputs[13], 'hide_value'):
                    group_input_006_2.outputs[13].hide_value = True
                if hasattr(group_input_006_2.outputs[13], 'name'):
                    group_input_006_2.outputs[13].name = 'BRIGHTNESS'
                if hasattr(group_input_006_2.outputs[13], 'show_expanded'):
                    group_input_006_2.outputs[13].show_expanded = False
                if hasattr(group_input_006_2.outputs[14], 'default_value'):
                    group_input_006_2.outputs[14].default_value = 0.0
                if hasattr(group_input_006_2.outputs[14], 'display_shape'):
                    group_input_006_2.outputs[14].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[14], 'enabled'):
                    group_input_006_2.outputs[14].enabled = True
                if hasattr(group_input_006_2.outputs[14], 'hide'):
                    group_input_006_2.outputs[14].hide = False
                if hasattr(group_input_006_2.outputs[14], 'hide_value'):
                    group_input_006_2.outputs[14].hide_value = False
                if hasattr(group_input_006_2.outputs[14], 'name'):
                    group_input_006_2.outputs[14].name = '  Glowing Level'
                if hasattr(group_input_006_2.outputs[14], 'show_expanded'):
                    group_input_006_2.outputs[14].show_expanded = False
                if hasattr(group_input_006_2.outputs[15], 'default_value'):
                    group_input_006_2.outputs[15].default_value = 0.0
                if hasattr(group_input_006_2.outputs[15], 'display_shape'):
                    group_input_006_2.outputs[15].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[15], 'enabled'):
                    group_input_006_2.outputs[15].enabled = True
                if hasattr(group_input_006_2.outputs[15], 'hide'):
                    group_input_006_2.outputs[15].hide = True
                if hasattr(group_input_006_2.outputs[15], 'hide_value'):
                    group_input_006_2.outputs[15].hide_value = False
                if hasattr(group_input_006_2.outputs[15], 'name'):
                    group_input_006_2.outputs[15].name = '  Brightness'
                if hasattr(group_input_006_2.outputs[15], 'show_expanded'):
                    group_input_006_2.outputs[15].show_expanded = False
                if hasattr(group_input_006_2.outputs[16], 'default_value'):
                    group_input_006_2.outputs[16].default_value = -2.200000047683716
                if hasattr(group_input_006_2.outputs[16], 'display_shape'):
                    group_input_006_2.outputs[16].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[16], 'enabled'):
                    group_input_006_2.outputs[16].enabled = True
                if hasattr(group_input_006_2.outputs[16], 'hide'):
                    group_input_006_2.outputs[16].hide = True
                if hasattr(group_input_006_2.outputs[16], 'hide_value'):
                    group_input_006_2.outputs[16].hide_value = False
                if hasattr(group_input_006_2.outputs[16], 'name'):
                    group_input_006_2.outputs[16].name = '  Dark / Bright Threshold'
                if hasattr(group_input_006_2.outputs[16], 'show_expanded'):
                    group_input_006_2.outputs[16].show_expanded = False
                if hasattr(group_input_006_2.outputs[17], 'default_value'):
                    group_input_006_2.outputs[17].default_value = 0.5
                if hasattr(group_input_006_2.outputs[17], 'display_shape'):
                    group_input_006_2.outputs[17].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[17], 'enabled'):
                    group_input_006_2.outputs[17].enabled = True
                if hasattr(group_input_006_2.outputs[17], 'hide'):
                    group_input_006_2.outputs[17].hide = True
                if hasattr(group_input_006_2.outputs[17], 'hide_value'):
                    group_input_006_2.outputs[17].hide_value = False
                if hasattr(group_input_006_2.outputs[17], 'name'):
                    group_input_006_2.outputs[17].name = '    Dark Spot Intensity'
                if hasattr(group_input_006_2.outputs[17], 'show_expanded'):
                    group_input_006_2.outputs[17].show_expanded = False
                if hasattr(group_input_006_2.outputs[18], 'default_value'):
                    group_input_006_2.outputs[18].default_value = 0.5
                if hasattr(group_input_006_2.outputs[18], 'display_shape'):
                    group_input_006_2.outputs[18].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[18], 'enabled'):
                    group_input_006_2.outputs[18].enabled = True
                if hasattr(group_input_006_2.outputs[18], 'hide'):
                    group_input_006_2.outputs[18].hide = True
                if hasattr(group_input_006_2.outputs[18], 'hide_value'):
                    group_input_006_2.outputs[18].hide_value = False
                if hasattr(group_input_006_2.outputs[18], 'name'):
                    group_input_006_2.outputs[18].name = '    Bright Spot Intensity'
                if hasattr(group_input_006_2.outputs[18], 'show_expanded'):
                    group_input_006_2.outputs[18].show_expanded = False
                if hasattr(group_input_006_2.outputs[19], 'default_value'):
                    group_input_006_2.outputs[19].default_value = 0.5
                if hasattr(group_input_006_2.outputs[19], 'display_shape'):
                    group_input_006_2.outputs[19].display_shape = 'CIRCLE'
                if hasattr(group_input_006_2.outputs[19], 'enabled'):
                    group_input_006_2.outputs[19].enabled = True
                if hasattr(group_input_006_2.outputs[19], 'hide'):
                    group_input_006_2.outputs[19].hide = True
                if hasattr(group_input_006_2.outputs[19], 'hide_value'):
                    group_input_006_2.outputs[19].hide_value = False
                if hasattr(group_input_006_2.outputs[19], 'name'):
                    group_input_006_2.outputs[19].name = '  Roughness'
                if hasattr(group_input_006_2.outputs[19], 'show_expanded'):
                    group_input_006_2.outputs[19].show_expanded = False

                unpaint_2 = node_tree2.nodes.new('ShaderNodeMix')
                if hasattr(unpaint_2, 'blend_type'):
                    unpaint_2.blend_type = 'MIX'
                if hasattr(unpaint_2, 'clamp_factor'):
                    unpaint_2.clamp_factor = True
                if hasattr(unpaint_2, 'clamp_result'):
                    unpaint_2.clamp_result = False
                if hasattr(unpaint_2, 'color'):
                    unpaint_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(unpaint_2, 'data_type'):
                    unpaint_2.data_type = 'RGBA'
                if hasattr(unpaint_2, 'factor_mode'):
                    unpaint_2.factor_mode = 'UNIFORM'
                if hasattr(unpaint_2, 'hide'):
                    unpaint_2.hide = False
                if hasattr(unpaint_2, 'label'):
                    unpaint_2.label = 'Unpaint'
                if hasattr(unpaint_2, 'location'):
                    unpaint_2.location = (-320.0, -94.0)
                if hasattr(unpaint_2, 'mute'):
                    unpaint_2.mute = False
                if hasattr(unpaint_2, 'name'):
                    unpaint_2.name = 'Unpaint'
                if hasattr(unpaint_2, 'use_custom_color'):
                    unpaint_2.use_custom_color = False
                if hasattr(unpaint_2, 'width'):
                    unpaint_2.width = 140.0
                input_ = next((input_ for input_ in unpaint_2.inputs if input_.identifier=='Factor_Float'), None)
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
                input_ = next((input_ for input_ in unpaint_2.inputs if input_.identifier=='Factor_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.5, 0.5, 0.5)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'Factor'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_2.inputs if input_.identifier=='A_Float'), None)
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
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_2.inputs if input_.identifier=='B_Float'), None)
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
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_2.inputs if input_.identifier=='A_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'A'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_2.inputs if input_.identifier=='B_Vector'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input_, 'display_shape'):
                        input_.display_shape = 'CIRCLE'
                    if hasattr(input_, 'enabled'):
                        input_.enabled = False
                    if hasattr(input_, 'hide'):
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in unpaint_2.inputs if input_.identifier=='A_Color'), None)
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
                input_ = next((input_ for input_ in unpaint_2.inputs if input_.identifier=='B_Color'), None)
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
                output = next((output for output in unpaint_2.outputs if output.identifier=='Result_Float'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in unpaint_2.outputs if output.identifier=='Result_Vector'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = (0.0, 0.0, 0.0)
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'name'):
                        output.name = 'Result'
                    if hasattr(output, 'show_expanded'):
                        output.show_expanded = False
                output = next((output for output in unpaint_2.outputs if output.identifier=='Result_Color'), None)
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

                # LINKS
                node_tree2.links.new(noise_texture_2.outputs[1], separate_rgb_2.inputs[0])
                node_tree2.links.new(noise_texture_2.outputs[1], rainbow_saturation_2.inputs[7])
                node_tree2.links.new(rainbow_saturation_2.outputs[2], dark_spots_2.inputs[6])
                node_tree2.links.new(map_range_2.outputs[0], dark_spots_2.inputs[0])
                node_tree2.links.new(separate_rgb_2.outputs[0], map_range_2.inputs[0])
                node_tree2.links.new(math_2.outputs[0], noise_texture_2.inputs[2])
                node_tree2.links.new(texture_coordinate_2.outputs[3], noise_texture_2.inputs[0])
                node_tree2.links.new(group_input_005_2.outputs[4], map_range_003_2.inputs[0])
                node_tree2.links.new(map_range_004_2.outputs[0], dark_spots_2.inputs[7])
                node_tree2.links.new(dark_spots_2.outputs[2], hue_saturation_value_2.inputs[4])
                node_tree2.links.new(map_range_001_2.outputs[0], clamp_2.inputs[0])
                node_tree2.links.new(map_range_005_2.outputs[0], hue_saturation_value_2.inputs[2])
                node_tree2.links.new(separate_rgb_2.outputs[1], map_range_001_2.inputs[0])
                node_tree2.links.new(clamp_2.outputs[0], hue_saturation_value_2.inputs[3])
                node_tree2.links.new(group_input_007_2.outputs[16], map_range_001_2.inputs[3])
                node_tree2.links.new(map_range_005_2.outputs[0], hue_saturation_value_2.inputs[1])
                node_tree2.links.new(group_input_004_2.outputs[3], noise_texture_2.inputs[5])
                node_tree2.links.new(map_range_003_2.outputs[0], rainbow_saturation_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[18], map_range_005_2.inputs[0])
                node_tree2.links.new(hue_saturation_value_2.outputs[0], bright_contrast_2.inputs[0])
                node_tree2.links.new(bright_contrast_2.outputs[0], gamma_2.inputs[0])
                node_tree2.links.new(gamma_2.outputs[0], hue_saturation_value_001_2.inputs[4])
                node_tree2.links.new(group_input_001_2.outputs[11], hue_saturation_value_001_2.inputs[0])
                node_tree2.links.new(group_input_001_2.outputs[12], hue_saturation_value_001_2.inputs[1])
                node_tree2.links.new(group_input_001_2.outputs[10], hue_saturation_value_001_2.inputs[2])
                node_tree2.links.new(hue_saturation_value_001_2.outputs[0], glowing_level_2.inputs[6])
                node_tree2.links.new(group_input_003_2.outputs[14], glowing_level_2.inputs[7])
                node_tree2.links.new(rgb_to_bw_2.outputs[0], unpaint_2.inputs[7])
                node_tree2.links.new(glowing_level_2.outputs[2], unpaint_2.inputs[6])
                node_tree2.links.new(unpaint_001_2.outputs[2], group_output_2.inputs[0])
                node_tree2.links.new(unpaint_2.outputs[2], unpaint_001_2.inputs[6])
                node_tree2.links.new(group_input_004_2.outputs[19], noise_texture_2.inputs[4])
                node_tree2.links.new(group_input_007_2.outputs[16], map_range_2.inputs[3])
                node_tree2.links.new(group_input_002_2.outputs[2], math_2.inputs[0])
                node_tree2.links.new(group_input_007_2.outputs[0], rainbow_saturation_2.inputs[6])
                node_tree2.links.new(group_input_007_2.outputs[18], map_range_004_2.inputs[0])
                node_tree2.links.new(group_input_003_2.outputs[0], rgb_to_bw_2.inputs[0])
                node_tree2.links.new(group_input_006_2.outputs[14], unpaint_001_2.inputs[7])
                node_tree2.links.new(group_input_008_2.outputs[15], bright_contrast_2.inputs[1])
                node_tree2.links.new(group_input_008_2.outputs[8], bright_contrast_2.inputs[2])
                node_tree2.links.new(group_input_009_2.outputs[9], gamma_2.inputs[1])
                node_tree2.links.new(group_input_010_2.outputs[6], unpaint_2.inputs[0])
                node_tree2.links.new(group_input_006_2.outputs[7], unpaint_001_2.inputs[0])

            color_variation_ver_3_001_1 = node_tree1.nodes.new('ShaderNodeGroup')
            if hasattr(color_variation_ver_3_001_1, 'node_tree'):
                color_variation_ver_3_001_1.node_tree = bpy.data.node_groups.get('Color Variation Ver. 3')
            if hasattr(color_variation_ver_3_001_1, 'color'):
                color_variation_ver_3_001_1.color = (0.11353799700737, 0.30544498562812805, 0.6079999804496765)
            if hasattr(color_variation_ver_3_001_1, 'hide'):
                color_variation_ver_3_001_1.hide = False
            if hasattr(color_variation_ver_3_001_1, 'label'):
                color_variation_ver_3_001_1.label = 'Color Variation Ver. 3'
            if hasattr(color_variation_ver_3_001_1, 'location'):
                color_variation_ver_3_001_1.location = (-800.0, 0.0)
            if hasattr(color_variation_ver_3_001_1, 'mute'):
                color_variation_ver_3_001_1.mute = False
            if hasattr(color_variation_ver_3_001_1, 'name'):
                color_variation_ver_3_001_1.name = 'Color Variation Ver. 3.001'
            if hasattr(color_variation_ver_3_001_1, 'use_custom_color'):
                color_variation_ver_3_001_1.use_custom_color = True
            if hasattr(color_variation_ver_3_001_1, 'width'):
                color_variation_ver_3_001_1.width = 140.0
            if hasattr(color_variation_ver_3_001_1.inputs[0], 'default_value'):
                color_variation_ver_3_001_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(color_variation_ver_3_001_1.inputs[0], 'display_shape'):
                color_variation_ver_3_001_1.inputs[0].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[0], 'enabled'):
                color_variation_ver_3_001_1.inputs[0].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[0], 'hide'):
                color_variation_ver_3_001_1.inputs[0].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[0], 'hide_value'):
                color_variation_ver_3_001_1.inputs[0].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[0], 'name'):
                color_variation_ver_3_001_1.inputs[0].name = 'Input Color'
            if hasattr(color_variation_ver_3_001_1.inputs[0], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[0].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[1], 'default_value'):
                color_variation_ver_3_001_1.inputs[1].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[1], 'display_shape'):
                color_variation_ver_3_001_1.inputs[1].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[1], 'enabled'):
                color_variation_ver_3_001_1.inputs[1].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[1], 'hide'):
                color_variation_ver_3_001_1.inputs[1].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[1], 'hide_value'):
                color_variation_ver_3_001_1.inputs[1].hide_value = True
            if hasattr(color_variation_ver_3_001_1.inputs[1], 'name'):
                color_variation_ver_3_001_1.inputs[1].name = 'COLOR VARIATION'
            if hasattr(color_variation_ver_3_001_1.inputs[1], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[1].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[2], 'default_value'):
                color_variation_ver_3_001_1.inputs[2].default_value = 6.5
            if hasattr(color_variation_ver_3_001_1.inputs[2], 'display_shape'):
                color_variation_ver_3_001_1.inputs[2].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[2], 'enabled'):
                color_variation_ver_3_001_1.inputs[2].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[2], 'hide'):
                color_variation_ver_3_001_1.inputs[2].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[2], 'hide_value'):
                color_variation_ver_3_001_1.inputs[2].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[2], 'name'):
                color_variation_ver_3_001_1.inputs[2].name = '  Color Variation Scale'
            if hasattr(color_variation_ver_3_001_1.inputs[2], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[2].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[3], 'default_value'):
                color_variation_ver_3_001_1.inputs[3].default_value = 0.15000000596046448
            if hasattr(color_variation_ver_3_001_1.inputs[3], 'display_shape'):
                color_variation_ver_3_001_1.inputs[3].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[3], 'enabled'):
                color_variation_ver_3_001_1.inputs[3].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[3], 'hide'):
                color_variation_ver_3_001_1.inputs[3].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[3], 'hide_value'):
                color_variation_ver_3_001_1.inputs[3].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[3], 'name'):
                color_variation_ver_3_001_1.inputs[3].name = '  Color Variation Distortion'
            if hasattr(color_variation_ver_3_001_1.inputs[3], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[3].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[4], 'default_value'):
                color_variation_ver_3_001_1.inputs[4].default_value = 0.7749999761581421
            if hasattr(color_variation_ver_3_001_1.inputs[4], 'display_shape'):
                color_variation_ver_3_001_1.inputs[4].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[4], 'enabled'):
                color_variation_ver_3_001_1.inputs[4].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[4], 'hide'):
                color_variation_ver_3_001_1.inputs[4].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[4], 'hide_value'):
                color_variation_ver_3_001_1.inputs[4].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[4], 'name'):
                color_variation_ver_3_001_1.inputs[4].name = '  Random Color Var'
            if hasattr(color_variation_ver_3_001_1.inputs[4], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[4].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[5], 'default_value'):
                color_variation_ver_3_001_1.inputs[5].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[5], 'display_shape'):
                color_variation_ver_3_001_1.inputs[5].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[5], 'enabled'):
                color_variation_ver_3_001_1.inputs[5].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[5], 'hide'):
                color_variation_ver_3_001_1.inputs[5].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[5], 'hide_value'):
                color_variation_ver_3_001_1.inputs[5].hide_value = True
            if hasattr(color_variation_ver_3_001_1.inputs[5], 'name'):
                color_variation_ver_3_001_1.inputs[5].name = 'COLOR ADJUSTMENTS'
            if hasattr(color_variation_ver_3_001_1.inputs[5], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[5].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[6], 'default_value'):
                color_variation_ver_3_001_1.inputs[6].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[6], 'display_shape'):
                color_variation_ver_3_001_1.inputs[6].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[6], 'enabled'):
                color_variation_ver_3_001_1.inputs[6].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[6], 'hide'):
                color_variation_ver_3_001_1.inputs[6].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[6], 'hide_value'):
                color_variation_ver_3_001_1.inputs[6].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[6], 'name'):
                color_variation_ver_3_001_1.inputs[6].name = '  Unpaint'
            if hasattr(color_variation_ver_3_001_1.inputs[6], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[6].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[7], 'default_value'):
                color_variation_ver_3_001_1.inputs[7].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[7], 'display_shape'):
                color_variation_ver_3_001_1.inputs[7].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[7], 'enabled'):
                color_variation_ver_3_001_1.inputs[7].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[7], 'hide'):
                color_variation_ver_3_001_1.inputs[7].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[7], 'hide_value'):
                color_variation_ver_3_001_1.inputs[7].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[7], 'name'):
                color_variation_ver_3_001_1.inputs[7].name = '  Color Inverter'
            if hasattr(color_variation_ver_3_001_1.inputs[7], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[7].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[8], 'default_value'):
                color_variation_ver_3_001_1.inputs[8].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[8], 'display_shape'):
                color_variation_ver_3_001_1.inputs[8].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[8], 'enabled'):
                color_variation_ver_3_001_1.inputs[8].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[8], 'hide'):
                color_variation_ver_3_001_1.inputs[8].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[8], 'hide_value'):
                color_variation_ver_3_001_1.inputs[8].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[8], 'name'):
                color_variation_ver_3_001_1.inputs[8].name = '  Contrast'
            if hasattr(color_variation_ver_3_001_1.inputs[8], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[8].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[9], 'default_value'):
                color_variation_ver_3_001_1.inputs[9].default_value = 1.0
            if hasattr(color_variation_ver_3_001_1.inputs[9], 'display_shape'):
                color_variation_ver_3_001_1.inputs[9].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[9], 'enabled'):
                color_variation_ver_3_001_1.inputs[9].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[9], 'hide'):
                color_variation_ver_3_001_1.inputs[9].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[9], 'hide_value'):
                color_variation_ver_3_001_1.inputs[9].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[9], 'name'):
                color_variation_ver_3_001_1.inputs[9].name = '  Gamma'
            if hasattr(color_variation_ver_3_001_1.inputs[9], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[9].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[10], 'default_value'):
                color_variation_ver_3_001_1.inputs[10].default_value = 1.0
            if hasattr(color_variation_ver_3_001_1.inputs[10], 'display_shape'):
                color_variation_ver_3_001_1.inputs[10].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[10], 'enabled'):
                color_variation_ver_3_001_1.inputs[10].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[10], 'hide'):
                color_variation_ver_3_001_1.inputs[10].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[10], 'hide_value'):
                color_variation_ver_3_001_1.inputs[10].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[10], 'name'):
                color_variation_ver_3_001_1.inputs[10].name = '  Hue / Sat Value'
            if hasattr(color_variation_ver_3_001_1.inputs[10], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[10].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[11], 'default_value'):
                color_variation_ver_3_001_1.inputs[11].default_value = 0.49999991059303284
            if hasattr(color_variation_ver_3_001_1.inputs[11], 'display_shape'):
                color_variation_ver_3_001_1.inputs[11].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[11], 'enabled'):
                color_variation_ver_3_001_1.inputs[11].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[11], 'hide'):
                color_variation_ver_3_001_1.inputs[11].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[11], 'hide_value'):
                color_variation_ver_3_001_1.inputs[11].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[11], 'name'):
                color_variation_ver_3_001_1.inputs[11].name = '    Hue'
            if hasattr(color_variation_ver_3_001_1.inputs[11], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[11].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[12], 'default_value'):
                color_variation_ver_3_001_1.inputs[12].default_value = 1.0
            if hasattr(color_variation_ver_3_001_1.inputs[12], 'display_shape'):
                color_variation_ver_3_001_1.inputs[12].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[12], 'enabled'):
                color_variation_ver_3_001_1.inputs[12].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[12], 'hide'):
                color_variation_ver_3_001_1.inputs[12].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[12], 'hide_value'):
                color_variation_ver_3_001_1.inputs[12].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[12], 'name'):
                color_variation_ver_3_001_1.inputs[12].name = '    Saturation'
            if hasattr(color_variation_ver_3_001_1.inputs[12], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[12].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[13], 'default_value'):
                color_variation_ver_3_001_1.inputs[13].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[13], 'display_shape'):
                color_variation_ver_3_001_1.inputs[13].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[13], 'enabled'):
                color_variation_ver_3_001_1.inputs[13].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[13], 'hide'):
                color_variation_ver_3_001_1.inputs[13].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[13], 'hide_value'):
                color_variation_ver_3_001_1.inputs[13].hide_value = True
            if hasattr(color_variation_ver_3_001_1.inputs[13], 'name'):
                color_variation_ver_3_001_1.inputs[13].name = 'BRIGHTNESS'
            if hasattr(color_variation_ver_3_001_1.inputs[13], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[13].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[14], 'default_value'):
                color_variation_ver_3_001_1.inputs[14].default_value = 1.0
            if hasattr(color_variation_ver_3_001_1.inputs[14], 'display_shape'):
                color_variation_ver_3_001_1.inputs[14].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[14], 'enabled'):
                color_variation_ver_3_001_1.inputs[14].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[14], 'hide'):
                color_variation_ver_3_001_1.inputs[14].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[14], 'hide_value'):
                color_variation_ver_3_001_1.inputs[14].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[14], 'name'):
                color_variation_ver_3_001_1.inputs[14].name = '  Glowing Level'
            if hasattr(color_variation_ver_3_001_1.inputs[14], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[14].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[15], 'default_value'):
                color_variation_ver_3_001_1.inputs[15].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[15], 'display_shape'):
                color_variation_ver_3_001_1.inputs[15].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[15], 'enabled'):
                color_variation_ver_3_001_1.inputs[15].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[15], 'hide'):
                color_variation_ver_3_001_1.inputs[15].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[15], 'hide_value'):
                color_variation_ver_3_001_1.inputs[15].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[15], 'name'):
                color_variation_ver_3_001_1.inputs[15].name = '  Brightness'
            if hasattr(color_variation_ver_3_001_1.inputs[15], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[15].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[16], 'default_value'):
                color_variation_ver_3_001_1.inputs[16].default_value = 2.5
            if hasattr(color_variation_ver_3_001_1.inputs[16], 'display_shape'):
                color_variation_ver_3_001_1.inputs[16].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[16], 'enabled'):
                color_variation_ver_3_001_1.inputs[16].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[16], 'hide'):
                color_variation_ver_3_001_1.inputs[16].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[16], 'hide_value'):
                color_variation_ver_3_001_1.inputs[16].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[16], 'name'):
                color_variation_ver_3_001_1.inputs[16].name = '  Dark / Bright Threshold'
            if hasattr(color_variation_ver_3_001_1.inputs[16], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[16].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[17], 'default_value'):
                color_variation_ver_3_001_1.inputs[17].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[17], 'display_shape'):
                color_variation_ver_3_001_1.inputs[17].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[17], 'enabled'):
                color_variation_ver_3_001_1.inputs[17].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[17], 'hide'):
                color_variation_ver_3_001_1.inputs[17].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[17], 'hide_value'):
                color_variation_ver_3_001_1.inputs[17].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[17], 'name'):
                color_variation_ver_3_001_1.inputs[17].name = '    Dark Spot Intensity'
            if hasattr(color_variation_ver_3_001_1.inputs[17], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[17].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[18], 'default_value'):
                color_variation_ver_3_001_1.inputs[18].default_value = 0.0
            if hasattr(color_variation_ver_3_001_1.inputs[18], 'display_shape'):
                color_variation_ver_3_001_1.inputs[18].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[18], 'enabled'):
                color_variation_ver_3_001_1.inputs[18].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[18], 'hide'):
                color_variation_ver_3_001_1.inputs[18].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[18], 'hide_value'):
                color_variation_ver_3_001_1.inputs[18].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[18], 'name'):
                color_variation_ver_3_001_1.inputs[18].name = '    Bright Spot Intensity'
            if hasattr(color_variation_ver_3_001_1.inputs[18], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[18].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.inputs[19], 'default_value'):
                color_variation_ver_3_001_1.inputs[19].default_value = 0.5
            if hasattr(color_variation_ver_3_001_1.inputs[19], 'display_shape'):
                color_variation_ver_3_001_1.inputs[19].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.inputs[19], 'enabled'):
                color_variation_ver_3_001_1.inputs[19].enabled = True
            if hasattr(color_variation_ver_3_001_1.inputs[19], 'hide'):
                color_variation_ver_3_001_1.inputs[19].hide = False
            if hasattr(color_variation_ver_3_001_1.inputs[19], 'hide_value'):
                color_variation_ver_3_001_1.inputs[19].hide_value = False
            if hasattr(color_variation_ver_3_001_1.inputs[19], 'name'):
                color_variation_ver_3_001_1.inputs[19].name = '  Roughness'
            if hasattr(color_variation_ver_3_001_1.inputs[19], 'show_expanded'):
                color_variation_ver_3_001_1.inputs[19].show_expanded = False
            if hasattr(color_variation_ver_3_001_1.outputs[0], 'default_value'):
                color_variation_ver_3_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            if hasattr(color_variation_ver_3_001_1.outputs[0], 'display_shape'):
                color_variation_ver_3_001_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(color_variation_ver_3_001_1.outputs[0], 'enabled'):
                color_variation_ver_3_001_1.outputs[0].enabled = True
            if hasattr(color_variation_ver_3_001_1.outputs[0], 'hide'):
                color_variation_ver_3_001_1.outputs[0].hide = False
            if hasattr(color_variation_ver_3_001_1.outputs[0], 'hide_value'):
                color_variation_ver_3_001_1.outputs[0].hide_value = False
            if hasattr(color_variation_ver_3_001_1.outputs[0], 'name'):
                color_variation_ver_3_001_1.outputs[0].name = 'Color'
            if hasattr(color_variation_ver_3_001_1.outputs[0], 'show_expanded'):
                color_variation_ver_3_001_1.outputs[0].show_expanded = False

            group_input_1 = node_tree1.nodes.new('NodeGroupInput')
            if hasattr(group_input_1, 'color'):
                group_input_1.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
            if hasattr(group_input_1, 'hide'):
                group_input_1.hide = False
            if hasattr(group_input_1, 'location'):
                group_input_1.location = (-960.0, -114.0)
            if hasattr(group_input_1, 'mute'):
                group_input_1.mute = False
            if hasattr(group_input_1, 'name'):
                group_input_1.name = 'Group Input'
            if hasattr(group_input_1, 'use_custom_color'):
                group_input_1.use_custom_color = True
            if hasattr(group_input_1, 'width'):
                group_input_1.width = 140.0
            if hasattr(group_input_1.outputs[0], 'default_value'):
                group_input_1.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_1.outputs[0], 'display_shape'):
                group_input_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[0], 'enabled'):
                group_input_1.outputs[0].enabled = True
            if hasattr(group_input_1.outputs[0], 'hide'):
                group_input_1.outputs[0].hide = False
            if hasattr(group_input_1.outputs[0], 'hide_value'):
                group_input_1.outputs[0].hide_value = False
            if hasattr(group_input_1.outputs[0], 'name'):
                group_input_1.outputs[0].name = 'Base Color'
            if hasattr(group_input_1.outputs[0], 'show_expanded'):
                group_input_1.outputs[0].show_expanded = False
            if hasattr(group_input_1.outputs[1], 'default_value'):
                group_input_1.outputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_1.outputs[1], 'display_shape'):
                group_input_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[1], 'enabled'):
                group_input_1.outputs[1].enabled = True
            if hasattr(group_input_1.outputs[1], 'hide'):
                group_input_1.outputs[1].hide = True
            if hasattr(group_input_1.outputs[1], 'hide_value'):
                group_input_1.outputs[1].hide_value = False
            if hasattr(group_input_1.outputs[1], 'name'):
                group_input_1.outputs[1].name = 'Transparent Color'
            if hasattr(group_input_1.outputs[1], 'show_expanded'):
                group_input_1.outputs[1].show_expanded = False
            if hasattr(group_input_1.outputs[2], 'default_value'):
                group_input_1.outputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(group_input_1.outputs[2], 'display_shape'):
                group_input_1.outputs[2].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[2], 'enabled'):
                group_input_1.outputs[2].enabled = True
            if hasattr(group_input_1.outputs[2], 'hide'):
                group_input_1.outputs[2].hide = True
            if hasattr(group_input_1.outputs[2], 'hide_value'):
                group_input_1.outputs[2].hide_value = False
            if hasattr(group_input_1.outputs[2], 'name'):
                group_input_1.outputs[2].name = 'Reflection Color'
            if hasattr(group_input_1.outputs[2], 'show_expanded'):
                group_input_1.outputs[2].show_expanded = False
            if hasattr(group_input_1.outputs[3], 'default_value'):
                group_input_1.outputs[3].default_value = 0.25
            if hasattr(group_input_1.outputs[3], 'display_shape'):
                group_input_1.outputs[3].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[3], 'enabled'):
                group_input_1.outputs[3].enabled = True
            if hasattr(group_input_1.outputs[3], 'hide'):
                group_input_1.outputs[3].hide = True
            if hasattr(group_input_1.outputs[3], 'hide_value'):
                group_input_1.outputs[3].hide_value = False
            if hasattr(group_input_1.outputs[3], 'name'):
                group_input_1.outputs[3].name = 'Reflection Factor'
            if hasattr(group_input_1.outputs[3], 'show_expanded'):
                group_input_1.outputs[3].show_expanded = False
            if hasattr(group_input_1.outputs[4], 'default_value'):
                group_input_1.outputs[4].default_value = 0.0
            if hasattr(group_input_1.outputs[4], 'display_shape'):
                group_input_1.outputs[4].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[4], 'enabled'):
                group_input_1.outputs[4].enabled = True
            if hasattr(group_input_1.outputs[4], 'hide'):
                group_input_1.outputs[4].hide = False
            if hasattr(group_input_1.outputs[4], 'hide_value'):
                group_input_1.outputs[4].hide_value = True
            if hasattr(group_input_1.outputs[4], 'name'):
                group_input_1.outputs[4].name = 'COLOR VARIATION'
            if hasattr(group_input_1.outputs[4], 'show_expanded'):
                group_input_1.outputs[4].show_expanded = False
            if hasattr(group_input_1.outputs[5], 'default_value'):
                group_input_1.outputs[5].default_value = 6.5
            if hasattr(group_input_1.outputs[5], 'display_shape'):
                group_input_1.outputs[5].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[5], 'enabled'):
                group_input_1.outputs[5].enabled = True
            if hasattr(group_input_1.outputs[5], 'hide'):
                group_input_1.outputs[5].hide = False
            if hasattr(group_input_1.outputs[5], 'hide_value'):
                group_input_1.outputs[5].hide_value = False
            if hasattr(group_input_1.outputs[5], 'name'):
                group_input_1.outputs[5].name = '  Color Variation Scale'
            if hasattr(group_input_1.outputs[5], 'show_expanded'):
                group_input_1.outputs[5].show_expanded = False
            if hasattr(group_input_1.outputs[6], 'default_value'):
                group_input_1.outputs[6].default_value = 0.15000000596046448
            if hasattr(group_input_1.outputs[6], 'display_shape'):
                group_input_1.outputs[6].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[6], 'enabled'):
                group_input_1.outputs[6].enabled = True
            if hasattr(group_input_1.outputs[6], 'hide'):
                group_input_1.outputs[6].hide = False
            if hasattr(group_input_1.outputs[6], 'hide_value'):
                group_input_1.outputs[6].hide_value = False
            if hasattr(group_input_1.outputs[6], 'name'):
                group_input_1.outputs[6].name = '  Color Variation Distortion'
            if hasattr(group_input_1.outputs[6], 'show_expanded'):
                group_input_1.outputs[6].show_expanded = False
            if hasattr(group_input_1.outputs[7], 'default_value'):
                group_input_1.outputs[7].default_value = 0.7749999761581421
            if hasattr(group_input_1.outputs[7], 'display_shape'):
                group_input_1.outputs[7].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[7], 'enabled'):
                group_input_1.outputs[7].enabled = True
            if hasattr(group_input_1.outputs[7], 'hide'):
                group_input_1.outputs[7].hide = False
            if hasattr(group_input_1.outputs[7], 'hide_value'):
                group_input_1.outputs[7].hide_value = False
            if hasattr(group_input_1.outputs[7], 'name'):
                group_input_1.outputs[7].name = '  Random Color Var'
            if hasattr(group_input_1.outputs[7], 'show_expanded'):
                group_input_1.outputs[7].show_expanded = False
            if hasattr(group_input_1.outputs[8], 'default_value'):
                group_input_1.outputs[8].default_value = 0.0
            if hasattr(group_input_1.outputs[8], 'display_shape'):
                group_input_1.outputs[8].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[8], 'enabled'):
                group_input_1.outputs[8].enabled = True
            if hasattr(group_input_1.outputs[8], 'hide'):
                group_input_1.outputs[8].hide = False
            if hasattr(group_input_1.outputs[8], 'hide_value'):
                group_input_1.outputs[8].hide_value = True
            if hasattr(group_input_1.outputs[8], 'name'):
                group_input_1.outputs[8].name = 'COLOR ADJUSTMENTS'
            if hasattr(group_input_1.outputs[8], 'show_expanded'):
                group_input_1.outputs[8].show_expanded = False
            if hasattr(group_input_1.outputs[9], 'default_value'):
                group_input_1.outputs[9].default_value = 0.0
            if hasattr(group_input_1.outputs[9], 'display_shape'):
                group_input_1.outputs[9].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[9], 'enabled'):
                group_input_1.outputs[9].enabled = True
            if hasattr(group_input_1.outputs[9], 'hide'):
                group_input_1.outputs[9].hide = False
            if hasattr(group_input_1.outputs[9], 'hide_value'):
                group_input_1.outputs[9].hide_value = False
            if hasattr(group_input_1.outputs[9], 'name'):
                group_input_1.outputs[9].name = '  Unpaint'
            if hasattr(group_input_1.outputs[9], 'show_expanded'):
                group_input_1.outputs[9].show_expanded = False
            if hasattr(group_input_1.outputs[10], 'default_value'):
                group_input_1.outputs[10].default_value = 0.0
            if hasattr(group_input_1.outputs[10], 'display_shape'):
                group_input_1.outputs[10].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[10], 'enabled'):
                group_input_1.outputs[10].enabled = True
            if hasattr(group_input_1.outputs[10], 'hide'):
                group_input_1.outputs[10].hide = False
            if hasattr(group_input_1.outputs[10], 'hide_value'):
                group_input_1.outputs[10].hide_value = False
            if hasattr(group_input_1.outputs[10], 'name'):
                group_input_1.outputs[10].name = '  Color Inverter'
            if hasattr(group_input_1.outputs[10], 'show_expanded'):
                group_input_1.outputs[10].show_expanded = False
            if hasattr(group_input_1.outputs[11], 'default_value'):
                group_input_1.outputs[11].default_value = 0.0
            if hasattr(group_input_1.outputs[11], 'display_shape'):
                group_input_1.outputs[11].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[11], 'enabled'):
                group_input_1.outputs[11].enabled = True
            if hasattr(group_input_1.outputs[11], 'hide'):
                group_input_1.outputs[11].hide = False
            if hasattr(group_input_1.outputs[11], 'hide_value'):
                group_input_1.outputs[11].hide_value = False
            if hasattr(group_input_1.outputs[11], 'name'):
                group_input_1.outputs[11].name = '  Contrast'
            if hasattr(group_input_1.outputs[11], 'show_expanded'):
                group_input_1.outputs[11].show_expanded = False
            if hasattr(group_input_1.outputs[12], 'default_value'):
                group_input_1.outputs[12].default_value = 1.0
            if hasattr(group_input_1.outputs[12], 'display_shape'):
                group_input_1.outputs[12].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[12], 'enabled'):
                group_input_1.outputs[12].enabled = True
            if hasattr(group_input_1.outputs[12], 'hide'):
                group_input_1.outputs[12].hide = False
            if hasattr(group_input_1.outputs[12], 'hide_value'):
                group_input_1.outputs[12].hide_value = False
            if hasattr(group_input_1.outputs[12], 'name'):
                group_input_1.outputs[12].name = '  Gamma'
            if hasattr(group_input_1.outputs[12], 'show_expanded'):
                group_input_1.outputs[12].show_expanded = False
            if hasattr(group_input_1.outputs[13], 'default_value'):
                group_input_1.outputs[13].default_value = 1.0
            if hasattr(group_input_1.outputs[13], 'display_shape'):
                group_input_1.outputs[13].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[13], 'enabled'):
                group_input_1.outputs[13].enabled = True
            if hasattr(group_input_1.outputs[13], 'hide'):
                group_input_1.outputs[13].hide = False
            if hasattr(group_input_1.outputs[13], 'hide_value'):
                group_input_1.outputs[13].hide_value = False
            if hasattr(group_input_1.outputs[13], 'name'):
                group_input_1.outputs[13].name = '  Hue / Sat Value'
            if hasattr(group_input_1.outputs[13], 'show_expanded'):
                group_input_1.outputs[13].show_expanded = False
            if hasattr(group_input_1.outputs[14], 'default_value'):
                group_input_1.outputs[14].default_value = 0.49999991059303284
            if hasattr(group_input_1.outputs[14], 'display_shape'):
                group_input_1.outputs[14].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[14], 'enabled'):
                group_input_1.outputs[14].enabled = True
            if hasattr(group_input_1.outputs[14], 'hide'):
                group_input_1.outputs[14].hide = False
            if hasattr(group_input_1.outputs[14], 'hide_value'):
                group_input_1.outputs[14].hide_value = False
            if hasattr(group_input_1.outputs[14], 'name'):
                group_input_1.outputs[14].name = '    Hue'
            if hasattr(group_input_1.outputs[14], 'show_expanded'):
                group_input_1.outputs[14].show_expanded = False
            if hasattr(group_input_1.outputs[15], 'default_value'):
                group_input_1.outputs[15].default_value = 1.0
            if hasattr(group_input_1.outputs[15], 'display_shape'):
                group_input_1.outputs[15].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[15], 'enabled'):
                group_input_1.outputs[15].enabled = True
            if hasattr(group_input_1.outputs[15], 'hide'):
                group_input_1.outputs[15].hide = False
            if hasattr(group_input_1.outputs[15], 'hide_value'):
                group_input_1.outputs[15].hide_value = False
            if hasattr(group_input_1.outputs[15], 'name'):
                group_input_1.outputs[15].name = '    Saturation'
            if hasattr(group_input_1.outputs[15], 'show_expanded'):
                group_input_1.outputs[15].show_expanded = False
            if hasattr(group_input_1.outputs[16], 'default_value'):
                group_input_1.outputs[16].default_value = 0.0
            if hasattr(group_input_1.outputs[16], 'display_shape'):
                group_input_1.outputs[16].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[16], 'enabled'):
                group_input_1.outputs[16].enabled = True
            if hasattr(group_input_1.outputs[16], 'hide'):
                group_input_1.outputs[16].hide = False
            if hasattr(group_input_1.outputs[16], 'hide_value'):
                group_input_1.outputs[16].hide_value = True
            if hasattr(group_input_1.outputs[16], 'name'):
                group_input_1.outputs[16].name = 'BRIGHTNESS'
            if hasattr(group_input_1.outputs[16], 'show_expanded'):
                group_input_1.outputs[16].show_expanded = False
            if hasattr(group_input_1.outputs[17], 'default_value'):
                group_input_1.outputs[17].default_value = 1.0
            if hasattr(group_input_1.outputs[17], 'display_shape'):
                group_input_1.outputs[17].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[17], 'enabled'):
                group_input_1.outputs[17].enabled = True
            if hasattr(group_input_1.outputs[17], 'hide'):
                group_input_1.outputs[17].hide = False
            if hasattr(group_input_1.outputs[17], 'hide_value'):
                group_input_1.outputs[17].hide_value = False
            if hasattr(group_input_1.outputs[17], 'name'):
                group_input_1.outputs[17].name = '  Glowing Level'
            if hasattr(group_input_1.outputs[17], 'show_expanded'):
                group_input_1.outputs[17].show_expanded = False
            if hasattr(group_input_1.outputs[18], 'default_value'):
                group_input_1.outputs[18].default_value = 0.0
            if hasattr(group_input_1.outputs[18], 'display_shape'):
                group_input_1.outputs[18].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[18], 'enabled'):
                group_input_1.outputs[18].enabled = True
            if hasattr(group_input_1.outputs[18], 'hide'):
                group_input_1.outputs[18].hide = False
            if hasattr(group_input_1.outputs[18], 'hide_value'):
                group_input_1.outputs[18].hide_value = False
            if hasattr(group_input_1.outputs[18], 'name'):
                group_input_1.outputs[18].name = '  Brightness'
            if hasattr(group_input_1.outputs[18], 'show_expanded'):
                group_input_1.outputs[18].show_expanded = False
            if hasattr(group_input_1.outputs[19], 'default_value'):
                group_input_1.outputs[19].default_value = 2.5
            if hasattr(group_input_1.outputs[19], 'display_shape'):
                group_input_1.outputs[19].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[19], 'enabled'):
                group_input_1.outputs[19].enabled = True
            if hasattr(group_input_1.outputs[19], 'hide'):
                group_input_1.outputs[19].hide = False
            if hasattr(group_input_1.outputs[19], 'hide_value'):
                group_input_1.outputs[19].hide_value = False
            if hasattr(group_input_1.outputs[19], 'name'):
                group_input_1.outputs[19].name = '  Dark / Bright Threshold'
            if hasattr(group_input_1.outputs[19], 'show_expanded'):
                group_input_1.outputs[19].show_expanded = False
            if hasattr(group_input_1.outputs[20], 'default_value'):
                group_input_1.outputs[20].default_value = 0.0
            if hasattr(group_input_1.outputs[20], 'display_shape'):
                group_input_1.outputs[20].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[20], 'enabled'):
                group_input_1.outputs[20].enabled = True
            if hasattr(group_input_1.outputs[20], 'hide'):
                group_input_1.outputs[20].hide = False
            if hasattr(group_input_1.outputs[20], 'hide_value'):
                group_input_1.outputs[20].hide_value = False
            if hasattr(group_input_1.outputs[20], 'name'):
                group_input_1.outputs[20].name = '    Dark Spot Intensity'
            if hasattr(group_input_1.outputs[20], 'show_expanded'):
                group_input_1.outputs[20].show_expanded = False
            if hasattr(group_input_1.outputs[21], 'default_value'):
                group_input_1.outputs[21].default_value = 0.0
            if hasattr(group_input_1.outputs[21], 'display_shape'):
                group_input_1.outputs[21].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[21], 'enabled'):
                group_input_1.outputs[21].enabled = True
            if hasattr(group_input_1.outputs[21], 'hide'):
                group_input_1.outputs[21].hide = False
            if hasattr(group_input_1.outputs[21], 'hide_value'):
                group_input_1.outputs[21].hide_value = False
            if hasattr(group_input_1.outputs[21], 'name'):
                group_input_1.outputs[21].name = '    Bright Spot Intensity'
            if hasattr(group_input_1.outputs[21], 'show_expanded'):
                group_input_1.outputs[21].show_expanded = False
            if hasattr(group_input_1.outputs[22], 'default_value'):
                group_input_1.outputs[22].default_value = 0.10000000149011612
            if hasattr(group_input_1.outputs[22], 'display_shape'):
                group_input_1.outputs[22].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[22], 'enabled'):
                group_input_1.outputs[22].enabled = True
            if hasattr(group_input_1.outputs[22], 'hide'):
                group_input_1.outputs[22].hide = True
            if hasattr(group_input_1.outputs[22], 'hide_value'):
                group_input_1.outputs[22].hide_value = False
            if hasattr(group_input_1.outputs[22], 'name'):
                group_input_1.outputs[22].name = 'Blend'
            if hasattr(group_input_1.outputs[22], 'show_expanded'):
                group_input_1.outputs[22].show_expanded = False
            if hasattr(group_input_1.outputs[23], 'default_value'):
                group_input_1.outputs[23].default_value = 0.47999998927116394
            if hasattr(group_input_1.outputs[23], 'display_shape'):
                group_input_1.outputs[23].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[23], 'enabled'):
                group_input_1.outputs[23].enabled = True
            if hasattr(group_input_1.outputs[23], 'hide'):
                group_input_1.outputs[23].hide = True
            if hasattr(group_input_1.outputs[23], 'hide_value'):
                group_input_1.outputs[23].hide_value = False
            if hasattr(group_input_1.outputs[23], 'name'):
                group_input_1.outputs[23].name = 'Roughness'
            if hasattr(group_input_1.outputs[23], 'show_expanded'):
                group_input_1.outputs[23].show_expanded = False
            if hasattr(group_input_1.outputs[24], 'default_value'):
                group_input_1.outputs[24].default_value = 0.125
            if hasattr(group_input_1.outputs[24], 'display_shape'):
                group_input_1.outputs[24].display_shape = 'CIRCLE'
            if hasattr(group_input_1.outputs[24], 'enabled'):
                group_input_1.outputs[24].enabled = True
            if hasattr(group_input_1.outputs[24], 'hide'):
                group_input_1.outputs[24].hide = True
            if hasattr(group_input_1.outputs[24], 'hide_value'):
                group_input_1.outputs[24].hide_value = False
            if hasattr(group_input_1.outputs[24], 'name'):
                group_input_1.outputs[24].name = 'Falloff Strength'
            if hasattr(group_input_1.outputs[24], 'show_expanded'):
                group_input_1.outputs[24].show_expanded = False

            node_tree2 = bpy.data.node_groups.get('Micro Roughness')
            if not node_tree2:
                node_tree2 = bpy.data.node_groups.new('Micro Roughness', 'ShaderNodeTree')
                for node in node_tree2.nodes:
                    node_tree2.nodes.remove(node)
                # INPUTS
                input = node_tree2.inputs.new('NodeSocketFloat', 'Roughness')
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
                    input.name = 'Roughness'
                input = node_tree2.inputs.new('NodeSocketFloat', '    Multiplier')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 1.0
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 10000.0
                if hasattr(input, 'min_value'):
                    input.min_value = -10000.0
                if hasattr(input, 'name'):
                    input.name = '    Multiplier'
                input = node_tree2.inputs.new('NodeSocketFloat', 'Falloff Strength')
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
                    input.name = 'Falloff Strength'
                input = node_tree2.inputs.new('NodeSocketVector', 'Normal')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = (0.0, 0.0, 0.0)
                if hasattr(input, 'hide_value'):
                    input.hide_value = True
                if hasattr(input, 'max_value'):
                    input.max_value = 1.0
                if hasattr(input, 'min_value'):
                    input.min_value = -1.0
                if hasattr(input, 'name'):
                    input.name = 'Normal'
                # OUTPUTS
                output = node_tree2.outputs.new('NodeSocketFloat', 'Roughness')
                if hasattr(output, 'attribute_domain'):
                    output.attribute_domain = 'POINT'
                if hasattr(output, 'default_value'):
                    output.default_value = 0.5
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'max_value'):
                    output.max_value = 3.4028234663852886e+38
                if hasattr(output, 'min_value'):
                    output.min_value = -3.4028234663852886e+38
                if hasattr(output, 'name'):
                    output.name = 'Roughness'
                # NODES
                micro_roughness_node_2 = node_tree2.nodes.new('NodeFrame')
                if hasattr(micro_roughness_node_2, 'color'):
                    micro_roughness_node_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(micro_roughness_node_2, 'hide'):
                    micro_roughness_node_2.hide = False
                if hasattr(micro_roughness_node_2, 'label'):
                    micro_roughness_node_2.label = 'MICRO ROUGHNESS NODE'
                if hasattr(micro_roughness_node_2, 'label_size'):
                    micro_roughness_node_2.label_size = 15
                if hasattr(micro_roughness_node_2, 'location'):
                    micro_roughness_node_2.location = (-546.0, 129.9498748779297)
                if hasattr(micro_roughness_node_2, 'mute'):
                    micro_roughness_node_2.mute = False
                if hasattr(micro_roughness_node_2, 'name'):
                    micro_roughness_node_2.name = 'MICRO ROUGHNESS NODE'
                if hasattr(micro_roughness_node_2, 'shrink'):
                    micro_roughness_node_2.shrink = True
                if hasattr(micro_roughness_node_2, 'text'):
                    micro_roughness_node_2.text = bpy.data.texts.get('Micro Roughness  Node.002')
                if hasattr(micro_roughness_node_2, 'use_custom_color'):
                    micro_roughness_node_2.use_custom_color = True
                if hasattr(micro_roughness_node_2, 'width'):
                    micro_roughness_node_2.width = 400.0

                author_2 = node_tree2.nodes.new('NodeFrame')
                if hasattr(author_2, 'color'):
                    author_2.color = (0.015208303928375244, 0.12743757665157318, 0.18447497487068176)
                if hasattr(author_2, 'hide'):
                    author_2.hide = False
                if hasattr(author_2, 'label'):
                    author_2.label = 'By: Dr. Hacker "BE HACK 2000"'
                if hasattr(author_2, 'label_size'):
                    author_2.label_size = 16
                if hasattr(author_2, 'location'):
                    author_2.location = (-3.0, -83.0)
                if hasattr(author_2, 'mute'):
                    author_2.mute = False
                if hasattr(author_2, 'name'):
                    author_2.name = 'Author'
                if hasattr(author_2, 'shrink'):
                    author_2.shrink = True
                if hasattr(author_2, 'use_custom_color'):
                    author_2.use_custom_color = True
                if hasattr(author_2, 'width'):
                    author_2.width = 285.8720703125

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
                    mix_2.location = (-160.0, 0.0)
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
                        input_.hide = True
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
                        input_.hide = True
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
                        input_.hide = True
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
                        input_.hide = True
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
                        input_.hide = True
                    if hasattr(input_, 'hide_value'):
                        input_.hide_value = False
                    if hasattr(input_, 'name'):
                        input_.name = 'B'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='A_Color'), None)
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
                input_ = next((input_ for input_ in mix_2.inputs if input_.identifier=='B_Color'), None)
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
                output = next((output for output in mix_2.outputs if output.identifier=='Result_Float'), None)
                if output:
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'display_shape'):
                        output.display_shape = 'CIRCLE'
                    if hasattr(output, 'enabled'):
                        output.enabled = False
                    if hasattr(output, 'hide'):
                        output.hide = True
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
                        output.hide = True
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

                group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
                if hasattr(group_output_2, 'color'):
                    group_output_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_output_2, 'hide'):
                    group_output_2.hide = False
                if hasattr(group_output_2, 'is_active_output'):
                    group_output_2.is_active_output = True
                if hasattr(group_output_2, 'location'):
                    group_output_2.location = (0.0, 0.0)
                if hasattr(group_output_2, 'mute'):
                    group_output_2.mute = False
                if hasattr(group_output_2, 'name'):
                    group_output_2.name = 'Group Output'
                if hasattr(group_output_2, 'use_custom_color'):
                    group_output_2.use_custom_color = True
                if hasattr(group_output_2, 'width'):
                    group_output_2.width = 140.0
                if hasattr(group_output_2.inputs[0], 'default_value'):
                    group_output_2.inputs[0].default_value = 0.5
                if hasattr(group_output_2.inputs[0], 'display_shape'):
                    group_output_2.inputs[0].display_shape = 'CIRCLE'
                if hasattr(group_output_2.inputs[0], 'enabled'):
                    group_output_2.inputs[0].enabled = True
                if hasattr(group_output_2.inputs[0], 'hide'):
                    group_output_2.inputs[0].hide = False
                if hasattr(group_output_2.inputs[0], 'hide_value'):
                    group_output_2.inputs[0].hide_value = False
                if hasattr(group_output_2.inputs[0], 'name'):
                    group_output_2.inputs[0].name = 'Roughness'
                if hasattr(group_output_2.inputs[0], 'show_expanded'):
                    group_output_2.inputs[0].show_expanded = False

                math_2 = node_tree2.nodes.new('ShaderNodeMath')
                if hasattr(math_2, 'color'):
                    math_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(math_2, 'hide'):
                    math_2.hide = False
                if hasattr(math_2, 'location'):
                    math_2.location = (-320.0, -214.0)
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
                input_ = next((input_ for input_ in math_2.inputs if input_.identifier=='Value_002'), None)
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

                math_002_2 = node_tree2.nodes.new('ShaderNodeMath')
                if hasattr(math_002_2, 'color'):
                    math_002_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(math_002_2, 'hide'):
                    math_002_2.hide = False
                if hasattr(math_002_2, 'location'):
                    math_002_2.location = (-320.0, -95.0)
                if hasattr(math_002_2, 'mute'):
                    math_002_2.mute = False
                if hasattr(math_002_2, 'name'):
                    math_002_2.name = 'Math.002'
                if hasattr(math_002_2, 'operation'):
                    math_002_2.operation = 'MULTIPLY'
                if hasattr(math_002_2, 'use_clamp'):
                    math_002_2.use_clamp = False
                if hasattr(math_002_2, 'use_custom_color'):
                    math_002_2.use_custom_color = False
                if hasattr(math_002_2, 'width'):
                    math_002_2.width = 140.0
                input_ = next((input_ for input_ in math_002_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in math_002_2.inputs if input_.identifier=='Value_001'), None)
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
                input_ = next((input_ for input_ in math_002_2.inputs if input_.identifier=='Value_002'), None)
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
                output = next((output for output in math_002_2.outputs if output.identifier=='Value'), None)
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

                group_input_001_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_001_2, 'color'):
                    group_input_001_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_001_2, 'hide'):
                    group_input_001_2.hide = False
                if hasattr(group_input_001_2, 'location'):
                    group_input_001_2.location = (-640.0, 0.0)
                if hasattr(group_input_001_2, 'mute'):
                    group_input_001_2.mute = False
                if hasattr(group_input_001_2, 'name'):
                    group_input_001_2.name = 'Group Input.001'
                if hasattr(group_input_001_2, 'use_custom_color'):
                    group_input_001_2.use_custom_color = True
                if hasattr(group_input_001_2, 'width'):
                    group_input_001_2.width = 140.0
                if hasattr(group_input_001_2.outputs[0], 'default_value'):
                    group_input_001_2.outputs[0].default_value = 0.5
                if hasattr(group_input_001_2.outputs[0], 'display_shape'):
                    group_input_001_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[0], 'enabled'):
                    group_input_001_2.outputs[0].enabled = True
                if hasattr(group_input_001_2.outputs[0], 'hide'):
                    group_input_001_2.outputs[0].hide = True
                if hasattr(group_input_001_2.outputs[0], 'hide_value'):
                    group_input_001_2.outputs[0].hide_value = False
                if hasattr(group_input_001_2.outputs[0], 'name'):
                    group_input_001_2.outputs[0].name = 'Roughness'
                if hasattr(group_input_001_2.outputs[0], 'show_expanded'):
                    group_input_001_2.outputs[0].show_expanded = False
                if hasattr(group_input_001_2.outputs[1], 'default_value'):
                    group_input_001_2.outputs[1].default_value = 1.0
                if hasattr(group_input_001_2.outputs[1], 'display_shape'):
                    group_input_001_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[1], 'enabled'):
                    group_input_001_2.outputs[1].enabled = True
                if hasattr(group_input_001_2.outputs[1], 'hide'):
                    group_input_001_2.outputs[1].hide = True
                if hasattr(group_input_001_2.outputs[1], 'hide_value'):
                    group_input_001_2.outputs[1].hide_value = False
                if hasattr(group_input_001_2.outputs[1], 'name'):
                    group_input_001_2.outputs[1].name = '    Multiplier'
                if hasattr(group_input_001_2.outputs[1], 'show_expanded'):
                    group_input_001_2.outputs[1].show_expanded = False
                if hasattr(group_input_001_2.outputs[2], 'default_value'):
                    group_input_001_2.outputs[2].default_value = 0.5
                if hasattr(group_input_001_2.outputs[2], 'display_shape'):
                    group_input_001_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[2], 'enabled'):
                    group_input_001_2.outputs[2].enabled = True
                if hasattr(group_input_001_2.outputs[2], 'hide'):
                    group_input_001_2.outputs[2].hide = False
                if hasattr(group_input_001_2.outputs[2], 'hide_value'):
                    group_input_001_2.outputs[2].hide_value = False
                if hasattr(group_input_001_2.outputs[2], 'name'):
                    group_input_001_2.outputs[2].name = 'Falloff Strength'
                if hasattr(group_input_001_2.outputs[2], 'show_expanded'):
                    group_input_001_2.outputs[2].show_expanded = False
                if hasattr(group_input_001_2.outputs[3], 'default_value'):
                    group_input_001_2.outputs[3].default_value = (0.0, 0.0, 0.0)
                if hasattr(group_input_001_2.outputs[3], 'display_shape'):
                    group_input_001_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[3], 'enabled'):
                    group_input_001_2.outputs[3].enabled = True
                if hasattr(group_input_001_2.outputs[3], 'hide'):
                    group_input_001_2.outputs[3].hide = True
                if hasattr(group_input_001_2.outputs[3], 'hide_value'):
                    group_input_001_2.outputs[3].hide_value = True
                if hasattr(group_input_001_2.outputs[3], 'name'):
                    group_input_001_2.outputs[3].name = 'Normal'
                if hasattr(group_input_001_2.outputs[3], 'show_expanded'):
                    group_input_001_2.outputs[3].show_expanded = False

                fresnel_2 = node_tree2.nodes.new('ShaderNodeFresnel')
                if hasattr(fresnel_2, 'color'):
                    fresnel_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(fresnel_2, 'hide'):
                    fresnel_2.hide = False
                if hasattr(fresnel_2, 'location'):
                    fresnel_2.location = (-320.0, 0.0)
                if hasattr(fresnel_2, 'mute'):
                    fresnel_2.mute = False
                if hasattr(fresnel_2, 'name'):
                    fresnel_2.name = 'Fresnel'
                if hasattr(fresnel_2, 'use_custom_color'):
                    fresnel_2.use_custom_color = False
                if hasattr(fresnel_2, 'width'):
                    fresnel_2.width = 140.0
                input_ = next((input_ for input_ in fresnel_2.inputs if input_.identifier=='IOR'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.4500000476837158
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
                input_ = next((input_ for input_ in fresnel_2.inputs if input_.identifier=='Normal'), None)
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
                output = next((output for output in fresnel_2.outputs if output.identifier=='Fac'), None)
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

                group_input_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_2, 'color'):
                    group_input_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_2, 'hide'):
                    group_input_2.hide = False
                if hasattr(group_input_2, 'location'):
                    group_input_2.location = (-480.0, 0.0)
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
                    group_input_2.outputs[0].name = 'Roughness'
                if hasattr(group_input_2.outputs[0], 'show_expanded'):
                    group_input_2.outputs[0].show_expanded = False
                if hasattr(group_input_2.outputs[1], 'default_value'):
                    group_input_2.outputs[1].default_value = 1.0
                if hasattr(group_input_2.outputs[1], 'display_shape'):
                    group_input_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[1], 'enabled'):
                    group_input_2.outputs[1].enabled = True
                if hasattr(group_input_2.outputs[1], 'hide'):
                    group_input_2.outputs[1].hide = False
                if hasattr(group_input_2.outputs[1], 'hide_value'):
                    group_input_2.outputs[1].hide_value = False
                if hasattr(group_input_2.outputs[1], 'name'):
                    group_input_2.outputs[1].name = '    Multiplier'
                if hasattr(group_input_2.outputs[1], 'show_expanded'):
                    group_input_2.outputs[1].show_expanded = False
                if hasattr(group_input_2.outputs[2], 'default_value'):
                    group_input_2.outputs[2].default_value = 0.5
                if hasattr(group_input_2.outputs[2], 'display_shape'):
                    group_input_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[2], 'enabled'):
                    group_input_2.outputs[2].enabled = True
                if hasattr(group_input_2.outputs[2], 'hide'):
                    group_input_2.outputs[2].hide = True
                if hasattr(group_input_2.outputs[2], 'hide_value'):
                    group_input_2.outputs[2].hide_value = False
                if hasattr(group_input_2.outputs[2], 'name'):
                    group_input_2.outputs[2].name = 'Falloff Strength'
                if hasattr(group_input_2.outputs[2], 'show_expanded'):
                    group_input_2.outputs[2].show_expanded = False
                if hasattr(group_input_2.outputs[3], 'default_value'):
                    group_input_2.outputs[3].default_value = (0.0, 0.0, 0.0)
                if hasattr(group_input_2.outputs[3], 'display_shape'):
                    group_input_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[3], 'enabled'):
                    group_input_2.outputs[3].enabled = True
                if hasattr(group_input_2.outputs[3], 'hide'):
                    group_input_2.outputs[3].hide = False
                if hasattr(group_input_2.outputs[3], 'hide_value'):
                    group_input_2.outputs[3].hide_value = True
                if hasattr(group_input_2.outputs[3], 'name'):
                    group_input_2.outputs[3].name = 'Normal'
                if hasattr(group_input_2.outputs[3], 'show_expanded'):
                    group_input_2.outputs[3].show_expanded = False

                math_001_2 = node_tree2.nodes.new('ShaderNodeMath')
                if hasattr(math_001_2, 'color'):
                    math_001_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(math_001_2, 'hide'):
                    math_001_2.hide = False
                if hasattr(math_001_2, 'label'):
                    math_001_2.label = 'invert'
                if hasattr(math_001_2, 'location'):
                    math_001_2.location = (-480.0, -116.0)
                if hasattr(math_001_2, 'mute'):
                    math_001_2.mute = False
                if hasattr(math_001_2, 'name'):
                    math_001_2.name = 'Math.001'
                if hasattr(math_001_2, 'operation'):
                    math_001_2.operation = 'SUBTRACT'
                if hasattr(math_001_2, 'use_clamp'):
                    math_001_2.use_clamp = False
                if hasattr(math_001_2, 'use_custom_color'):
                    math_001_2.use_custom_color = False
                if hasattr(math_001_2, 'width'):
                    math_001_2.width = 140.0
                input_ = next((input_ for input_ in math_001_2.inputs if input_.identifier=='Value'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 1.0
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
                input_ = next((input_ for input_ in math_001_2.inputs if input_.identifier=='Value_001'), None)
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
                input_ = next((input_ for input_ in math_001_2.inputs if input_.identifier=='Value_002'), None)
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
                output = next((output for output in math_001_2.outputs if output.identifier=='Value'), None)
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
                node_tree2.links.new(math_2.outputs[0], mix_2.inputs[7])
                node_tree2.links.new(fresnel_2.outputs[0], mix_2.inputs[0])
                node_tree2.links.new(math_001_2.outputs[0], math_2.inputs[1])
                node_tree2.links.new(group_input_2.outputs[0], math_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[3], fresnel_2.inputs[1])
                node_tree2.links.new(math_002_2.outputs[0], mix_2.inputs[6])
                node_tree2.links.new(mix_2.outputs[2], group_output_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[0], math_002_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[1], math_002_2.inputs[1])
                node_tree2.links.new(group_input_001_2.outputs[2], math_001_2.inputs[1])

            micro_roughness_1 = node_tree1.nodes.new('ShaderNodeGroup')
            if hasattr(micro_roughness_1, 'node_tree'):
                micro_roughness_1.node_tree = bpy.data.node_groups.get('Micro Roughness')
            if hasattr(micro_roughness_1, 'color'):
                micro_roughness_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            if hasattr(micro_roughness_1, 'hide'):
                micro_roughness_1.hide = False
            if hasattr(micro_roughness_1, 'label'):
                micro_roughness_1.label = 'Micro Roughness'
            if hasattr(micro_roughness_1, 'location'):
                micro_roughness_1.location = (-960.0, 0.0)
            if hasattr(micro_roughness_1, 'mute'):
                micro_roughness_1.mute = False
            if hasattr(micro_roughness_1, 'name'):
                micro_roughness_1.name = 'Micro Roughness'
            if hasattr(micro_roughness_1, 'use_custom_color'):
                micro_roughness_1.use_custom_color = True
            if hasattr(micro_roughness_1, 'width'):
                micro_roughness_1.width = 140.0
            if hasattr(micro_roughness_1.inputs[0], 'default_value'):
                micro_roughness_1.inputs[0].default_value = 0.47999998927116394
            if hasattr(micro_roughness_1.inputs[0], 'display_shape'):
                micro_roughness_1.inputs[0].display_shape = 'CIRCLE'
            if hasattr(micro_roughness_1.inputs[0], 'enabled'):
                micro_roughness_1.inputs[0].enabled = True
            if hasattr(micro_roughness_1.inputs[0], 'hide'):
                micro_roughness_1.inputs[0].hide = False
            if hasattr(micro_roughness_1.inputs[0], 'hide_value'):
                micro_roughness_1.inputs[0].hide_value = False
            if hasattr(micro_roughness_1.inputs[0], 'name'):
                micro_roughness_1.inputs[0].name = 'Roughness'
            if hasattr(micro_roughness_1.inputs[0], 'show_expanded'):
                micro_roughness_1.inputs[0].show_expanded = False
            if hasattr(micro_roughness_1.inputs[1], 'default_value'):
                micro_roughness_1.inputs[1].default_value = 1.0
            if hasattr(micro_roughness_1.inputs[1], 'display_shape'):
                micro_roughness_1.inputs[1].display_shape = 'CIRCLE'
            if hasattr(micro_roughness_1.inputs[1], 'enabled'):
                micro_roughness_1.inputs[1].enabled = True
            if hasattr(micro_roughness_1.inputs[1], 'hide'):
                micro_roughness_1.inputs[1].hide = True
            if hasattr(micro_roughness_1.inputs[1], 'hide_value'):
                micro_roughness_1.inputs[1].hide_value = False
            if hasattr(micro_roughness_1.inputs[1], 'name'):
                micro_roughness_1.inputs[1].name = '    Multiplier'
            if hasattr(micro_roughness_1.inputs[1], 'show_expanded'):
                micro_roughness_1.inputs[1].show_expanded = False
            if hasattr(micro_roughness_1.inputs[2], 'default_value'):
                micro_roughness_1.inputs[2].default_value = 0.125
            if hasattr(micro_roughness_1.inputs[2], 'display_shape'):
                micro_roughness_1.inputs[2].display_shape = 'CIRCLE'
            if hasattr(micro_roughness_1.inputs[2], 'enabled'):
                micro_roughness_1.inputs[2].enabled = True
            if hasattr(micro_roughness_1.inputs[2], 'hide'):
                micro_roughness_1.inputs[2].hide = False
            if hasattr(micro_roughness_1.inputs[2], 'hide_value'):
                micro_roughness_1.inputs[2].hide_value = False
            if hasattr(micro_roughness_1.inputs[2], 'name'):
                micro_roughness_1.inputs[2].name = 'Falloff Strength'
            if hasattr(micro_roughness_1.inputs[2], 'show_expanded'):
                micro_roughness_1.inputs[2].show_expanded = False
            if hasattr(micro_roughness_1.inputs[3], 'default_value'):
                micro_roughness_1.inputs[3].default_value = (0.0, 0.0, 0.0)
            if hasattr(micro_roughness_1.inputs[3], 'display_shape'):
                micro_roughness_1.inputs[3].display_shape = 'CIRCLE'
            if hasattr(micro_roughness_1.inputs[3], 'enabled'):
                micro_roughness_1.inputs[3].enabled = True
            if hasattr(micro_roughness_1.inputs[3], 'hide'):
                micro_roughness_1.inputs[3].hide = True
            if hasattr(micro_roughness_1.inputs[3], 'hide_value'):
                micro_roughness_1.inputs[3].hide_value = True
            if hasattr(micro_roughness_1.inputs[3], 'name'):
                micro_roughness_1.inputs[3].name = 'Normal'
            if hasattr(micro_roughness_1.inputs[3], 'show_expanded'):
                micro_roughness_1.inputs[3].show_expanded = False
            if hasattr(micro_roughness_1.outputs[0], 'default_value'):
                micro_roughness_1.outputs[0].default_value = 0.5
            if hasattr(micro_roughness_1.outputs[0], 'display_shape'):
                micro_roughness_1.outputs[0].display_shape = 'CIRCLE'
            if hasattr(micro_roughness_1.outputs[0], 'enabled'):
                micro_roughness_1.outputs[0].enabled = True
            if hasattr(micro_roughness_1.outputs[0], 'hide'):
                micro_roughness_1.outputs[0].hide = False
            if hasattr(micro_roughness_1.outputs[0], 'hide_value'):
                micro_roughness_1.outputs[0].hide_value = False
            if hasattr(micro_roughness_1.outputs[0], 'name'):
                micro_roughness_1.outputs[0].name = 'Roughness'
            if hasattr(micro_roughness_1.outputs[0], 'show_expanded'):
                micro_roughness_1.outputs[0].show_expanded = False

            node_tree2 = bpy.data.node_groups.get('Reflection')
            if not node_tree2:
                node_tree2 = bpy.data.node_groups.new('Reflection', 'ShaderNodeTree')
                for node in node_tree2.nodes:
                    node_tree2.nodes.remove(node)
                # INPUTS
                input = node_tree2.inputs.new('NodeSocketShader', 'Shader')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'name'):
                    input.name = 'Shader'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', 'Roughness')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = 0.10000000149011612
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'max_value'):
                    input.max_value = 1.0
                if hasattr(input, 'min_value'):
                    input.min_value = 0.0
                if hasattr(input, 'name'):
                    input.name = 'Roughness'
                input = node_tree2.inputs.new('NodeSocketColor', 'Reflection Color')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = (1.0, 1.0, 1.0, 1.0)
                if hasattr(input, 'hide_value'):
                    input.hide_value = False
                if hasattr(input, 'name'):
                    input.name = 'Reflection Color'
                input = node_tree2.inputs.new('NodeSocketFloatFactor', 'Reflection Factor')
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
                    input.name = 'Reflection Factor'
                input = node_tree2.inputs.new('NodeSocketVector', 'Normal')
                if hasattr(input, 'attribute_domain'):
                    input.attribute_domain = 'POINT'
                if hasattr(input, 'default_value'):
                    input.default_value = (0.0, 0.0, 0.0)
                if hasattr(input, 'hide_value'):
                    input.hide_value = True
                if hasattr(input, 'max_value'):
                    input.max_value = 1.0
                if hasattr(input, 'min_value'):
                    input.min_value = -1.0
                if hasattr(input, 'name'):
                    input.name = 'Normal'
                # OUTPUTS
                output = node_tree2.outputs.new('NodeSocketShader', 'Shader')
                if hasattr(output, 'attribute_domain'):
                    output.attribute_domain = 'POINT'
                if hasattr(output, 'hide_value'):
                    output.hide_value = False
                if hasattr(output, 'name'):
                    output.name = 'Shader'
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
                reflection_node_2 = node_tree2.nodes.new('NodeFrame')
                if hasattr(reflection_node_2, 'color'):
                    reflection_node_2.color = (0.6079999804496765, 0.5312550067901611, 0.4991360008716583)
                if hasattr(reflection_node_2, 'hide'):
                    reflection_node_2.hide = False
                if hasattr(reflection_node_2, 'label'):
                    reflection_node_2.label = 'REFLECTION NODE'
                if hasattr(reflection_node_2, 'label_size'):
                    reflection_node_2.label_size = 15
                if hasattr(reflection_node_2, 'location'):
                    reflection_node_2.location = (-665.5011596679688, 151.8383331298828)
                if hasattr(reflection_node_2, 'mute'):
                    reflection_node_2.mute = False
                if hasattr(reflection_node_2, 'name'):
                    reflection_node_2.name = 'REFLECTION NODE'
                if hasattr(reflection_node_2, 'shrink'):
                    reflection_node_2.shrink = True
                if hasattr(reflection_node_2, 'text'):
                    reflection_node_2.text = bpy.data.texts.get('Reflection Node')
                if hasattr(reflection_node_2, 'use_custom_color'):
                    reflection_node_2.use_custom_color = True
                if hasattr(reflection_node_2, 'width'):
                    reflection_node_2.width = 400.0

                author_2 = node_tree2.nodes.new('NodeFrame')
                if hasattr(author_2, 'color'):
                    author_2.color = (0.015208303928375244, 0.12743757665157318, 0.18447497487068176)
                if hasattr(author_2, 'hide'):
                    author_2.hide = False
                if hasattr(author_2, 'label'):
                    author_2.label = 'By: Dr. Hacker "BE HACK 2000"'
                if hasattr(author_2, 'label_size'):
                    author_2.label_size = 16
                if hasattr(author_2, 'location'):
                    author_2.location = (-70.0, -87.0)
                if hasattr(author_2, 'mute'):
                    author_2.mute = False
                if hasattr(author_2, 'name'):
                    author_2.name = 'Author'
                if hasattr(author_2, 'shrink'):
                    author_2.shrink = True
                if hasattr(author_2, 'use_custom_color'):
                    author_2.use_custom_color = True
                if hasattr(author_2, 'width'):
                    author_2.width = 290.4298095703125

                math_2 = node_tree2.nodes.new('ShaderNodeMath')
                if hasattr(math_2, 'color'):
                    math_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(math_2, 'hide'):
                    math_2.hide = False
                if hasattr(math_2, 'location'):
                    math_2.location = (-640.0, 0.0)
                if hasattr(math_2, 'mute'):
                    math_2.mute = False
                if hasattr(math_2, 'name'):
                    math_2.name = 'Math'
                if hasattr(math_2, 'operation'):
                    math_2.operation = 'POWER'
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
                        input_.default_value = 2.0
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
                input_ = next((input_ for input_ in math_2.inputs if input_.identifier=='Value_002'), None)
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

                group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
                if hasattr(group_output_2, 'color'):
                    group_output_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_output_2, 'hide'):
                    group_output_2.hide = False
                if hasattr(group_output_2, 'is_active_output'):
                    group_output_2.is_active_output = True
                if hasattr(group_output_2, 'location'):
                    group_output_2.location = (0.0, 0.0)
                if hasattr(group_output_2, 'mute'):
                    group_output_2.mute = False
                if hasattr(group_output_2, 'name'):
                    group_output_2.name = 'Group Output'
                if hasattr(group_output_2, 'use_custom_color'):
                    group_output_2.use_custom_color = True
                if hasattr(group_output_2, 'width'):
                    group_output_2.width = 140.0
                if hasattr(group_output_2.inputs[1], 'default_value'):
                    group_output_2.inputs[1].default_value = (0.0, 0.0, 0.0, 0.0)
                if hasattr(group_output_2.inputs[1], 'display_shape'):
                    group_output_2.inputs[1].display_shape = 'CIRCLE'
                if hasattr(group_output_2.inputs[1], 'enabled'):
                    group_output_2.inputs[1].enabled = True
                if hasattr(group_output_2.inputs[1], 'hide'):
                    group_output_2.inputs[1].hide = False
                if hasattr(group_output_2.inputs[1], 'hide_value'):
                    group_output_2.inputs[1].hide_value = False
                if hasattr(group_output_2.inputs[1], 'name'):
                    group_output_2.inputs[1].name = 'Color'
                if hasattr(group_output_2.inputs[1], 'show_expanded'):
                    group_output_2.inputs[1].show_expanded = False

                group_input_002_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_002_2, 'color'):
                    group_input_002_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_002_2, 'hide'):
                    group_input_002_2.hide = False
                if hasattr(group_input_002_2, 'location'):
                    group_input_002_2.location = (-800.0, 0.0)
                if hasattr(group_input_002_2, 'mute'):
                    group_input_002_2.mute = False
                if hasattr(group_input_002_2, 'name'):
                    group_input_002_2.name = 'Group Input.002'
                if hasattr(group_input_002_2, 'use_custom_color'):
                    group_input_002_2.use_custom_color = True
                if hasattr(group_input_002_2, 'width'):
                    group_input_002_2.width = 140.0
                if hasattr(group_input_002_2.outputs[1], 'default_value'):
                    group_input_002_2.outputs[1].default_value = 0.20000000298023224
                if hasattr(group_input_002_2.outputs[1], 'display_shape'):
                    group_input_002_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[1], 'enabled'):
                    group_input_002_2.outputs[1].enabled = True
                if hasattr(group_input_002_2.outputs[1], 'hide'):
                    group_input_002_2.outputs[1].hide = False
                if hasattr(group_input_002_2.outputs[1], 'hide_value'):
                    group_input_002_2.outputs[1].hide_value = False
                if hasattr(group_input_002_2.outputs[1], 'name'):
                    group_input_002_2.outputs[1].name = 'Roughness'
                if hasattr(group_input_002_2.outputs[1], 'show_expanded'):
                    group_input_002_2.outputs[1].show_expanded = False
                if hasattr(group_input_002_2.outputs[2], 'default_value'):
                    group_input_002_2.outputs[2].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
                if hasattr(group_input_002_2.outputs[2], 'display_shape'):
                    group_input_002_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[2], 'enabled'):
                    group_input_002_2.outputs[2].enabled = True
                if hasattr(group_input_002_2.outputs[2], 'hide'):
                    group_input_002_2.outputs[2].hide = True
                if hasattr(group_input_002_2.outputs[2], 'hide_value'):
                    group_input_002_2.outputs[2].hide_value = False
                if hasattr(group_input_002_2.outputs[2], 'name'):
                    group_input_002_2.outputs[2].name = 'Reflection Color'
                if hasattr(group_input_002_2.outputs[2], 'show_expanded'):
                    group_input_002_2.outputs[2].show_expanded = False
                if hasattr(group_input_002_2.outputs[3], 'default_value'):
                    group_input_002_2.outputs[3].default_value = 1.0
                if hasattr(group_input_002_2.outputs[3], 'display_shape'):
                    group_input_002_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[3], 'enabled'):
                    group_input_002_2.outputs[3].enabled = True
                if hasattr(group_input_002_2.outputs[3], 'hide'):
                    group_input_002_2.outputs[3].hide = True
                if hasattr(group_input_002_2.outputs[3], 'hide_value'):
                    group_input_002_2.outputs[3].hide_value = False
                if hasattr(group_input_002_2.outputs[3], 'name'):
                    group_input_002_2.outputs[3].name = 'Reflection Factor'
                if hasattr(group_input_002_2.outputs[3], 'show_expanded'):
                    group_input_002_2.outputs[3].show_expanded = False
                if hasattr(group_input_002_2.outputs[4], 'default_value'):
                    group_input_002_2.outputs[4].default_value = (0.0, 0.0, 0.0)
                if hasattr(group_input_002_2.outputs[4], 'display_shape'):
                    group_input_002_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_002_2.outputs[4], 'enabled'):
                    group_input_002_2.outputs[4].enabled = True
                if hasattr(group_input_002_2.outputs[4], 'hide'):
                    group_input_002_2.outputs[4].hide = True
                if hasattr(group_input_002_2.outputs[4], 'hide_value'):
                    group_input_002_2.outputs[4].hide_value = True
                if hasattr(group_input_002_2.outputs[4], 'name'):
                    group_input_002_2.outputs[4].name = 'Normal'
                if hasattr(group_input_002_2.outputs[4], 'show_expanded'):
                    group_input_002_2.outputs[4].show_expanded = False

                mix_shader_2 = node_tree2.nodes.new('ShaderNodeMixShader')
                if hasattr(mix_shader_2, 'color'):
                    mix_shader_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(mix_shader_2, 'hide'):
                    mix_shader_2.hide = False
                if hasattr(mix_shader_2, 'location'):
                    mix_shader_2.location = (-160.0, 0.0)
                if hasattr(mix_shader_2, 'mute'):
                    mix_shader_2.mute = False
                if hasattr(mix_shader_2, 'name'):
                    mix_shader_2.name = 'Mix Shader'
                if hasattr(mix_shader_2, 'use_custom_color'):
                    mix_shader_2.use_custom_color = False
                if hasattr(mix_shader_2, 'width'):
                    mix_shader_2.width = 140.0
                input_ = next((input_ for input_ in mix_shader_2.inputs if input_.identifier=='Fac'), None)
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

                group_input_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_2, 'color'):
                    group_input_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_2, 'hide'):
                    group_input_2.hide = False
                if hasattr(group_input_2, 'location'):
                    group_input_2.location = (-480.0, 0.0)
                if hasattr(group_input_2, 'mute'):
                    group_input_2.mute = False
                if hasattr(group_input_2, 'name'):
                    group_input_2.name = 'Group Input'
                if hasattr(group_input_2, 'use_custom_color'):
                    group_input_2.use_custom_color = True
                if hasattr(group_input_2, 'width'):
                    group_input_2.width = 140.0
                if hasattr(group_input_2.outputs[1], 'default_value'):
                    group_input_2.outputs[1].default_value = 0.20000000298023224
                if hasattr(group_input_2.outputs[1], 'display_shape'):
                    group_input_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[1], 'enabled'):
                    group_input_2.outputs[1].enabled = True
                if hasattr(group_input_2.outputs[1], 'hide'):
                    group_input_2.outputs[1].hide = True
                if hasattr(group_input_2.outputs[1], 'hide_value'):
                    group_input_2.outputs[1].hide_value = False
                if hasattr(group_input_2.outputs[1], 'name'):
                    group_input_2.outputs[1].name = 'Roughness'
                if hasattr(group_input_2.outputs[1], 'show_expanded'):
                    group_input_2.outputs[1].show_expanded = False
                if hasattr(group_input_2.outputs[2], 'default_value'):
                    group_input_2.outputs[2].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
                if hasattr(group_input_2.outputs[2], 'display_shape'):
                    group_input_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[2], 'enabled'):
                    group_input_2.outputs[2].enabled = True
                if hasattr(group_input_2.outputs[2], 'hide'):
                    group_input_2.outputs[2].hide = False
                if hasattr(group_input_2.outputs[2], 'hide_value'):
                    group_input_2.outputs[2].hide_value = False
                if hasattr(group_input_2.outputs[2], 'name'):
                    group_input_2.outputs[2].name = 'Reflection Color'
                if hasattr(group_input_2.outputs[2], 'show_expanded'):
                    group_input_2.outputs[2].show_expanded = False
                if hasattr(group_input_2.outputs[3], 'default_value'):
                    group_input_2.outputs[3].default_value = 1.0
                if hasattr(group_input_2.outputs[3], 'display_shape'):
                    group_input_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[3], 'enabled'):
                    group_input_2.outputs[3].enabled = True
                if hasattr(group_input_2.outputs[3], 'hide'):
                    group_input_2.outputs[3].hide = False
                if hasattr(group_input_2.outputs[3], 'hide_value'):
                    group_input_2.outputs[3].hide_value = False
                if hasattr(group_input_2.outputs[3], 'name'):
                    group_input_2.outputs[3].name = 'Reflection Factor'
                if hasattr(group_input_2.outputs[3], 'show_expanded'):
                    group_input_2.outputs[3].show_expanded = False
                if hasattr(group_input_2.outputs[4], 'default_value'):
                    group_input_2.outputs[4].default_value = (0.0, 0.0, 0.0)
                if hasattr(group_input_2.outputs[4], 'display_shape'):
                    group_input_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_2.outputs[4], 'enabled'):
                    group_input_2.outputs[4].enabled = True
                if hasattr(group_input_2.outputs[4], 'hide'):
                    group_input_2.outputs[4].hide = False
                if hasattr(group_input_2.outputs[4], 'hide_value'):
                    group_input_2.outputs[4].hide_value = True
                if hasattr(group_input_2.outputs[4], 'name'):
                    group_input_2.outputs[4].name = 'Normal'
                if hasattr(group_input_2.outputs[4], 'show_expanded'):
                    group_input_2.outputs[4].show_expanded = False

                math_001_2 = node_tree2.nodes.new('ShaderNodeMath')
                if hasattr(math_001_2, 'color'):
                    math_001_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(math_001_2, 'hide'):
                    math_001_2.hide = False
                if hasattr(math_001_2, 'location'):
                    math_001_2.location = (-480.0, -116.0)
                if hasattr(math_001_2, 'mute'):
                    math_001_2.mute = False
                if hasattr(math_001_2, 'name'):
                    math_001_2.name = 'Math.001'
                if hasattr(math_001_2, 'operation'):
                    math_001_2.operation = 'POWER'
                if hasattr(math_001_2, 'use_clamp'):
                    math_001_2.use_clamp = False
                if hasattr(math_001_2, 'use_custom_color'):
                    math_001_2.use_custom_color = False
                if hasattr(math_001_2, 'width'):
                    math_001_2.width = 140.0
                input_ = next((input_ for input_ in math_001_2.inputs if input_.identifier=='Value'), None)
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
                input_ = next((input_ for input_ in math_001_2.inputs if input_.identifier=='Value_001'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.5
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
                input_ = next((input_ for input_ in math_001_2.inputs if input_.identifier=='Value_002'), None)
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
                output = next((output for output in math_001_2.outputs if output.identifier=='Value'), None)
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

                glossy_bsdf_2 = node_tree2.nodes.new('ShaderNodeBsdfGlossy')
                if hasattr(glossy_bsdf_2, 'color'):
                    glossy_bsdf_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                if hasattr(glossy_bsdf_2, 'distribution'):
                    glossy_bsdf_2.distribution = 'GGX'
                if hasattr(glossy_bsdf_2, 'hide'):
                    glossy_bsdf_2.hide = False
                if hasattr(glossy_bsdf_2, 'location'):
                    glossy_bsdf_2.location = (-320.0, -213.0)
                if hasattr(glossy_bsdf_2, 'mute'):
                    glossy_bsdf_2.mute = False
                if hasattr(glossy_bsdf_2, 'name'):
                    glossy_bsdf_2.name = 'Glossy BSDF'
                if hasattr(glossy_bsdf_2, 'use_custom_color'):
                    glossy_bsdf_2.use_custom_color = False
                if hasattr(glossy_bsdf_2, 'width'):
                    glossy_bsdf_2.width = 140.0
                input_ = next((input_ for input_ in glossy_bsdf_2.inputs if input_.identifier=='Color'), None)
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
                        input_.name = 'Color'
                    if hasattr(input_, 'show_expanded'):
                        input_.show_expanded = False
                input_ = next((input_ for input_ in glossy_bsdf_2.inputs if input_.identifier=='Roughness'), None)
                if input_:
                    if hasattr(input_, 'default_value'):
                        input_.default_value = 0.4472135901451111
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
                input_ = next((input_ for input_ in glossy_bsdf_2.inputs if input_.identifier=='Normal'), None)
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
                input_ = next((input_ for input_ in glossy_bsdf_2.inputs if input_.identifier=='Weight'), None)
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

                group_input_001_2 = node_tree2.nodes.new('NodeGroupInput')
                if hasattr(group_input_001_2, 'color'):
                    group_input_001_2.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                if hasattr(group_input_001_2, 'hide'):
                    group_input_001_2.hide = False
                if hasattr(group_input_001_2, 'location'):
                    group_input_001_2.location = (-320.0, -141.0)
                if hasattr(group_input_001_2, 'mute'):
                    group_input_001_2.mute = False
                if hasattr(group_input_001_2, 'name'):
                    group_input_001_2.name = 'Group Input.001'
                if hasattr(group_input_001_2, 'use_custom_color'):
                    group_input_001_2.use_custom_color = True
                if hasattr(group_input_001_2, 'width'):
                    group_input_001_2.width = 140.0
                if hasattr(group_input_001_2.outputs[1], 'default_value'):
                    group_input_001_2.outputs[1].default_value = 0.20000000298023224
                if hasattr(group_input_001_2.outputs[1], 'display_shape'):
                    group_input_001_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[1], 'enabled'):
                    group_input_001_2.outputs[1].enabled = True
                if hasattr(group_input_001_2.outputs[1], 'hide'):
                    group_input_001_2.outputs[1].hide = True
                if hasattr(group_input_001_2.outputs[1], 'hide_value'):
                    group_input_001_2.outputs[1].hide_value = False
                if hasattr(group_input_001_2.outputs[1], 'name'):
                    group_input_001_2.outputs[1].name = 'Roughness'
                if hasattr(group_input_001_2.outputs[1], 'show_expanded'):
                    group_input_001_2.outputs[1].show_expanded = False
                if hasattr(group_input_001_2.outputs[2], 'default_value'):
                    group_input_001_2.outputs[2].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
                if hasattr(group_input_001_2.outputs[2], 'display_shape'):
                    group_input_001_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[2], 'enabled'):
                    group_input_001_2.outputs[2].enabled = True
                if hasattr(group_input_001_2.outputs[2], 'hide'):
                    group_input_001_2.outputs[2].hide = True
                if hasattr(group_input_001_2.outputs[2], 'hide_value'):
                    group_input_001_2.outputs[2].hide_value = False
                if hasattr(group_input_001_2.outputs[2], 'name'):
                    group_input_001_2.outputs[2].name = 'Reflection Color'
                if hasattr(group_input_001_2.outputs[2], 'show_expanded'):
                    group_input_001_2.outputs[2].show_expanded = False
                if hasattr(group_input_001_2.outputs[3], 'default_value'):
                    group_input_001_2.outputs[3].default_value = 1.0
                if hasattr(group_input_001_2.outputs[3], 'display_shape'):
                    group_input_001_2.outputs[3].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[3], 'enabled'):
                    group_input_001_2.outputs[3].enabled = True
                if hasattr(group_input_001_2.outputs[3], 'hide'):
                    group_input_001_2.outputs[3].hide = True
                if hasattr(group_input_001_2.outputs[3], 'hide_value'):
                    group_input_001_2.outputs[3].hide_value = False
                if hasattr(group_input_001_2.outputs[3], 'name'):
                    group_input_001_2.outputs[3].name = 'Reflection Factor'
                if hasattr(group_input_001_2.outputs[3], 'show_expanded'):
                    group_input_001_2.outputs[3].show_expanded = False
                if hasattr(group_input_001_2.outputs[4], 'default_value'):
                    group_input_001_2.outputs[4].default_value = (0.0, 0.0, 0.0)
                if hasattr(group_input_001_2.outputs[4], 'display_shape'):
                    group_input_001_2.outputs[4].display_shape = 'CIRCLE'
                if hasattr(group_input_001_2.outputs[4], 'enabled'):
                    group_input_001_2.outputs[4].enabled = True
                if hasattr(group_input_001_2.outputs[4], 'hide'):
                    group_input_001_2.outputs[4].hide = True
                if hasattr(group_input_001_2.outputs[4], 'hide_value'):
                    group_input_001_2.outputs[4].hide_value = True
                if hasattr(group_input_001_2.outputs[4], 'name'):
                    group_input_001_2.outputs[4].name = 'Normal'
                if hasattr(group_input_001_2.outputs[4], 'show_expanded'):
                    group_input_001_2.outputs[4].show_expanded = False

                node_tree3 = bpy.data.node_groups.get('Fresnel')
                if not node_tree3:
                    node_tree3 = bpy.data.node_groups.new('Fresnel', 'ShaderNodeTree')
                    for node in node_tree3.nodes:
                        node_tree3.nodes.remove(node)
                    # INPUTS
                    input = node_tree3.inputs.new('NodeSocketFloatFactor', 'Roughness')
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
                        input.name = 'Roughness'
                    input = node_tree3.inputs.new('NodeSocketFloatFactor', 'Fac')
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
                        input.name = 'Fac'
                    input = node_tree3.inputs.new('NodeSocketFloat', 'Rim')
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
                        input.name = 'Rim'
                    input = node_tree3.inputs.new('NodeSocketVector', 'Normal')
                    if hasattr(input, 'attribute_domain'):
                        input.attribute_domain = 'POINT'
                    if hasattr(input, 'default_value'):
                        input.default_value = (0.0, 0.0, 0.0)
                    if hasattr(input, 'hide_value'):
                        input.hide_value = True
                    if hasattr(input, 'max_value'):
                        input.max_value = 1.0
                    if hasattr(input, 'min_value'):
                        input.min_value = -1.0
                    if hasattr(input, 'name'):
                        input.name = 'Normal'
                    # OUTPUTS
                    output = node_tree3.outputs.new('NodeSocketFloatFactor', 'Fresnel')
                    if hasattr(output, 'attribute_domain'):
                        output.attribute_domain = 'POINT'
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'max_value'):
                        output.max_value = 1.0
                    if hasattr(output, 'min_value'):
                        output.min_value = 0.0
                    if hasattr(output, 'name'):
                        output.name = 'Fresnel'
                    output = node_tree3.outputs.new('NodeSocketFloat', 'Metallic Rim')
                    if hasattr(output, 'attribute_domain'):
                        output.attribute_domain = 'POINT'
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'max_value'):
                        output.max_value = 0.0
                    if hasattr(output, 'min_value'):
                        output.min_value = 0.0
                    if hasattr(output, 'name'):
                        output.name = 'Metallic Rim'
                    output = node_tree3.outputs.new('NodeSocketFloat', 'Metallic Fresnel')
                    if hasattr(output, 'attribute_domain'):
                        output.attribute_domain = 'POINT'
                    if hasattr(output, 'default_value'):
                        output.default_value = 0.0
                    if hasattr(output, 'hide_value'):
                        output.hide_value = False
                    if hasattr(output, 'max_value'):
                        output.max_value = 0.0
                    if hasattr(output, 'min_value'):
                        output.min_value = 0.0
                    if hasattr(output, 'name'):
                        output.name = 'Metallic Fresnel'
                    # NODES
                    frensel_node_3 = node_tree3.nodes.new('NodeFrame')
                    if hasattr(frensel_node_3, 'color'):
                        frensel_node_3.color = (0.0, 0.5738130211830139, 0.6080020070075989)
                    if hasattr(frensel_node_3, 'hide'):
                        frensel_node_3.hide = False
                    if hasattr(frensel_node_3, 'label'):
                        frensel_node_3.label = 'FRENSEL NODE'
                    if hasattr(frensel_node_3, 'label_size'):
                        frensel_node_3.label_size = 15
                    if hasattr(frensel_node_3, 'location'):
                        frensel_node_3.location = (-721.0, 155.279052734375)
                    if hasattr(frensel_node_3, 'mute'):
                        frensel_node_3.mute = False
                    if hasattr(frensel_node_3, 'name'):
                        frensel_node_3.name = 'FRENSEL NODE'
                    if hasattr(frensel_node_3, 'shrink'):
                        frensel_node_3.shrink = True
                    if hasattr(frensel_node_3, 'text'):
                        frensel_node_3.text = bpy.data.texts.get('Frensel Node')
                    if hasattr(frensel_node_3, 'use_custom_color'):
                        frensel_node_3.use_custom_color = True
                    if hasattr(frensel_node_3, 'width'):
                        frensel_node_3.width = 400.0

                    author_3 = node_tree3.nodes.new('NodeFrame')
                    if hasattr(author_3, 'color'):
                        author_3.color = (0.015208303928375244, 0.12743757665157318, 0.18447497487068176)
                    if hasattr(author_3, 'hide'):
                        author_3.hide = False
                    if hasattr(author_3, 'label'):
                        author_3.label = 'By: Dr. Hacker "BE HACK 2000"'
                    if hasattr(author_3, 'label_size'):
                        author_3.label_size = 16
                    if hasattr(author_3, 'location'):
                        author_3.location = (-70.0, -147.0)
                    if hasattr(author_3, 'mute'):
                        author_3.mute = False
                    if hasattr(author_3, 'name'):
                        author_3.name = 'Author'
                    if hasattr(author_3, 'shrink'):
                        author_3.shrink = True
                    if hasattr(author_3, 'use_custom_color'):
                        author_3.use_custom_color = True
                    if hasattr(author_3, 'width'):
                        author_3.width = 290.4298095703125

                    layer_weight_001_3 = node_tree3.nodes.new('ShaderNodeLayerWeight')
                    if hasattr(layer_weight_001_3, 'color'):
                        layer_weight_001_3.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                    if hasattr(layer_weight_001_3, 'hide'):
                        layer_weight_001_3.hide = False
                    if hasattr(layer_weight_001_3, 'location'):
                        layer_weight_001_3.location = (-320.0, -117.0)
                    if hasattr(layer_weight_001_3, 'mute'):
                        layer_weight_001_3.mute = False
                    if hasattr(layer_weight_001_3, 'name'):
                        layer_weight_001_3.name = 'Layer Weight.001'
                    if hasattr(layer_weight_001_3, 'use_custom_color'):
                        layer_weight_001_3.use_custom_color = False
                    if hasattr(layer_weight_001_3, 'width'):
                        layer_weight_001_3.width = 140.0
                    input_ = next((input_ for input_ in layer_weight_001_3.inputs if input_.identifier=='Blend'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = 0.4999999701976776
                        if hasattr(input_, 'display_shape'):
                            input_.display_shape = 'CIRCLE'
                        if hasattr(input_, 'enabled'):
                            input_.enabled = True
                        if hasattr(input_, 'hide'):
                            input_.hide = False
                        if hasattr(input_, 'hide_value'):
                            input_.hide_value = False
                        if hasattr(input_, 'name'):
                            input_.name = 'Blend'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in layer_weight_001_3.inputs if input_.identifier=='Normal'), None)
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
                    output = next((output for output in layer_weight_001_3.outputs if output.identifier=='Fresnel'), None)
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
                    output = next((output for output in layer_weight_001_3.outputs if output.identifier=='Facing'), None)
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

                    math_001_3 = node_tree3.nodes.new('ShaderNodeMath')
                    if hasattr(math_001_3, 'color'):
                        math_001_3.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                    if hasattr(math_001_3, 'hide'):
                        math_001_3.hide = False
                    if hasattr(math_001_3, 'location'):
                        math_001_3.location = (-160.0, -97.0)
                    if hasattr(math_001_3, 'mute'):
                        math_001_3.mute = False
                    if hasattr(math_001_3, 'name'):
                        math_001_3.name = 'Math.001'
                    if hasattr(math_001_3, 'operation'):
                        math_001_3.operation = 'SUBTRACT'
                    if hasattr(math_001_3, 'use_clamp'):
                        math_001_3.use_clamp = True
                    if hasattr(math_001_3, 'use_custom_color'):
                        math_001_3.use_custom_color = False
                    if hasattr(math_001_3, 'width'):
                        math_001_3.width = 140.0
                    input_ = next((input_ for input_ in math_001_3.inputs if input_.identifier=='Value'), None)
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
                    input_ = next((input_ for input_ in math_001_3.inputs if input_.identifier=='Value_001'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = 0.032999999821186066
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
                    input_ = next((input_ for input_ in math_001_3.inputs if input_.identifier=='Value_002'), None)
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
                    output = next((output for output in math_001_3.outputs if output.identifier=='Value'), None)
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

                    layer_weight_3 = node_tree3.nodes.new('ShaderNodeLayerWeight')
                    if hasattr(layer_weight_3, 'color'):
                        layer_weight_3.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                    if hasattr(layer_weight_3, 'hide'):
                        layer_weight_3.hide = False
                    if hasattr(layer_weight_3, 'location'):
                        layer_weight_3.location = (-320.0, 0.0)
                    if hasattr(layer_weight_3, 'mute'):
                        layer_weight_3.mute = False
                    if hasattr(layer_weight_3, 'name'):
                        layer_weight_3.name = 'Layer Weight'
                    if hasattr(layer_weight_3, 'use_custom_color'):
                        layer_weight_3.use_custom_color = False
                    if hasattr(layer_weight_3, 'width'):
                        layer_weight_3.width = 140.0
                    input_ = next((input_ for input_ in layer_weight_3.inputs if input_.identifier=='Blend'), None)
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
                            input_.name = 'Blend'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in layer_weight_3.inputs if input_.identifier=='Normal'), None)
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
                    output = next((output for output in layer_weight_3.outputs if output.identifier=='Fresnel'), None)
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
                    output = next((output for output in layer_weight_3.outputs if output.identifier=='Facing'), None)
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

                    math_3 = node_tree3.nodes.new('ShaderNodeMath')
                    if hasattr(math_3, 'color'):
                        math_3.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                    if hasattr(math_3, 'hide'):
                        math_3.hide = False
                    if hasattr(math_3, 'location'):
                        math_3.location = (-160.0, 0.0)
                    if hasattr(math_3, 'mute'):
                        math_3.mute = False
                    if hasattr(math_3, 'name'):
                        math_3.name = 'Math'
                    if hasattr(math_3, 'operation'):
                        math_3.operation = 'POWER'
                    if hasattr(math_3, 'use_clamp'):
                        math_3.use_clamp = True
                    if hasattr(math_3, 'use_custom_color'):
                        math_3.use_custom_color = False
                    if hasattr(math_3, 'width'):
                        math_3.width = 140.0
                    input_ = next((input_ for input_ in math_3.inputs if input_.identifier=='Value'), None)
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
                    input_ = next((input_ for input_ in math_3.inputs if input_.identifier=='Value_001'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = 2.5
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
                    input_ = next((input_ for input_ in math_3.inputs if input_.identifier=='Value_002'), None)
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
                    output = next((output for output in math_3.outputs if output.identifier=='Value'), None)
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

                    group_output_3 = node_tree3.nodes.new('NodeGroupOutput')
                    if hasattr(group_output_3, 'color'):
                        group_output_3.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                    if hasattr(group_output_3, 'hide'):
                        group_output_3.hide = False
                    if hasattr(group_output_3, 'is_active_output'):
                        group_output_3.is_active_output = True
                    if hasattr(group_output_3, 'location'):
                        group_output_3.location = (0.0, 0.0)
                    if hasattr(group_output_3, 'mute'):
                        group_output_3.mute = False
                    if hasattr(group_output_3, 'name'):
                        group_output_3.name = 'Group Output'
                    if hasattr(group_output_3, 'use_custom_color'):
                        group_output_3.use_custom_color = True
                    if hasattr(group_output_3, 'width'):
                        group_output_3.width = 140.0
                    if hasattr(group_output_3.inputs[0], 'default_value'):
                        group_output_3.inputs[0].default_value = 0.0
                    if hasattr(group_output_3.inputs[0], 'display_shape'):
                        group_output_3.inputs[0].display_shape = 'CIRCLE'
                    if hasattr(group_output_3.inputs[0], 'enabled'):
                        group_output_3.inputs[0].enabled = True
                    if hasattr(group_output_3.inputs[0], 'hide'):
                        group_output_3.inputs[0].hide = False
                    if hasattr(group_output_3.inputs[0], 'hide_value'):
                        group_output_3.inputs[0].hide_value = False
                    if hasattr(group_output_3.inputs[0], 'name'):
                        group_output_3.inputs[0].name = 'Fresnel'
                    if hasattr(group_output_3.inputs[0], 'show_expanded'):
                        group_output_3.inputs[0].show_expanded = False
                    if hasattr(group_output_3.inputs[1], 'default_value'):
                        group_output_3.inputs[1].default_value = 0.0
                    if hasattr(group_output_3.inputs[1], 'display_shape'):
                        group_output_3.inputs[1].display_shape = 'CIRCLE'
                    if hasattr(group_output_3.inputs[1], 'enabled'):
                        group_output_3.inputs[1].enabled = True
                    if hasattr(group_output_3.inputs[1], 'hide'):
                        group_output_3.inputs[1].hide = False
                    if hasattr(group_output_3.inputs[1], 'hide_value'):
                        group_output_3.inputs[1].hide_value = False
                    if hasattr(group_output_3.inputs[1], 'name'):
                        group_output_3.inputs[1].name = 'Metallic Rim'
                    if hasattr(group_output_3.inputs[1], 'show_expanded'):
                        group_output_3.inputs[1].show_expanded = False
                    if hasattr(group_output_3.inputs[2], 'default_value'):
                        group_output_3.inputs[2].default_value = 0.0
                    if hasattr(group_output_3.inputs[2], 'display_shape'):
                        group_output_3.inputs[2].display_shape = 'CIRCLE'
                    if hasattr(group_output_3.inputs[2], 'enabled'):
                        group_output_3.inputs[2].enabled = True
                    if hasattr(group_output_3.inputs[2], 'hide'):
                        group_output_3.inputs[2].hide = False
                    if hasattr(group_output_3.inputs[2], 'hide_value'):
                        group_output_3.inputs[2].hide_value = False
                    if hasattr(group_output_3.inputs[2], 'name'):
                        group_output_3.inputs[2].name = 'Metallic Fresnel'
                    if hasattr(group_output_3.inputs[2], 'show_expanded'):
                        group_output_3.inputs[2].show_expanded = False

                    group_input_001_3 = node_tree3.nodes.new('NodeGroupInput')
                    if hasattr(group_input_001_3, 'color'):
                        group_input_001_3.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                    if hasattr(group_input_001_3, 'hide'):
                        group_input_001_3.hide = False
                    if hasattr(group_input_001_3, 'location'):
                        group_input_001_3.location = (-800.0, 0.0)
                    if hasattr(group_input_001_3, 'mute'):
                        group_input_001_3.mute = False
                    if hasattr(group_input_001_3, 'name'):
                        group_input_001_3.name = 'Group Input.001'
                    if hasattr(group_input_001_3, 'use_custom_color'):
                        group_input_001_3.use_custom_color = True
                    if hasattr(group_input_001_3, 'width'):
                        group_input_001_3.width = 140.0
                    if hasattr(group_input_001_3.outputs[0], 'default_value'):
                        group_input_001_3.outputs[0].default_value = 0.5
                    if hasattr(group_input_001_3.outputs[0], 'display_shape'):
                        group_input_001_3.outputs[0].display_shape = 'CIRCLE'
                    if hasattr(group_input_001_3.outputs[0], 'enabled'):
                        group_input_001_3.outputs[0].enabled = True
                    if hasattr(group_input_001_3.outputs[0], 'hide'):
                        group_input_001_3.outputs[0].hide = True
                    if hasattr(group_input_001_3.outputs[0], 'hide_value'):
                        group_input_001_3.outputs[0].hide_value = False
                    if hasattr(group_input_001_3.outputs[0], 'name'):
                        group_input_001_3.outputs[0].name = 'Roughness'
                    if hasattr(group_input_001_3.outputs[0], 'show_expanded'):
                        group_input_001_3.outputs[0].show_expanded = False
                    if hasattr(group_input_001_3.outputs[1], 'default_value'):
                        group_input_001_3.outputs[1].default_value = 1.0
                    if hasattr(group_input_001_3.outputs[1], 'display_shape'):
                        group_input_001_3.outputs[1].display_shape = 'CIRCLE'
                    if hasattr(group_input_001_3.outputs[1], 'enabled'):
                        group_input_001_3.outputs[1].enabled = True
                    if hasattr(group_input_001_3.outputs[1], 'hide'):
                        group_input_001_3.outputs[1].hide = True
                    if hasattr(group_input_001_3.outputs[1], 'hide_value'):
                        group_input_001_3.outputs[1].hide_value = False
                    if hasattr(group_input_001_3.outputs[1], 'name'):
                        group_input_001_3.outputs[1].name = 'Fac'
                    if hasattr(group_input_001_3.outputs[1], 'show_expanded'):
                        group_input_001_3.outputs[1].show_expanded = False
                    if hasattr(group_input_001_3.outputs[2], 'default_value'):
                        group_input_001_3.outputs[2].default_value = 0.5
                    if hasattr(group_input_001_3.outputs[2], 'display_shape'):
                        group_input_001_3.outputs[2].display_shape = 'CIRCLE'
                    if hasattr(group_input_001_3.outputs[2], 'enabled'):
                        group_input_001_3.outputs[2].enabled = True
                    if hasattr(group_input_001_3.outputs[2], 'hide'):
                        group_input_001_3.outputs[2].hide = True
                    if hasattr(group_input_001_3.outputs[2], 'hide_value'):
                        group_input_001_3.outputs[2].hide_value = False
                    if hasattr(group_input_001_3.outputs[2], 'name'):
                        group_input_001_3.outputs[2].name = 'Rim'
                    if hasattr(group_input_001_3.outputs[2], 'show_expanded'):
                        group_input_001_3.outputs[2].show_expanded = False
                    if hasattr(group_input_001_3.outputs[3], 'default_value'):
                        group_input_001_3.outputs[3].default_value = (0.0, 0.0, 0.0)
                    if hasattr(group_input_001_3.outputs[3], 'display_shape'):
                        group_input_001_3.outputs[3].display_shape = 'CIRCLE'
                    if hasattr(group_input_001_3.outputs[3], 'enabled'):
                        group_input_001_3.outputs[3].enabled = True
                    if hasattr(group_input_001_3.outputs[3], 'hide'):
                        group_input_001_3.outputs[3].hide = False
                    if hasattr(group_input_001_3.outputs[3], 'hide_value'):
                        group_input_001_3.outputs[3].hide_value = True
                    if hasattr(group_input_001_3.outputs[3], 'name'):
                        group_input_001_3.outputs[3].name = 'Normal'
                    if hasattr(group_input_001_3.outputs[3], 'show_expanded'):
                        group_input_001_3.outputs[3].show_expanded = False

                    mix_3 = node_tree3.nodes.new('ShaderNodeMix')
                    if hasattr(mix_3, 'blend_type'):
                        mix_3.blend_type = 'MIX'
                    if hasattr(mix_3, 'clamp_factor'):
                        mix_3.clamp_factor = True
                    if hasattr(mix_3, 'clamp_result'):
                        mix_3.clamp_result = False
                    if hasattr(mix_3, 'color'):
                        mix_3.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                    if hasattr(mix_3, 'data_type'):
                        mix_3.data_type = 'RGBA'
                    if hasattr(mix_3, 'factor_mode'):
                        mix_3.factor_mode = 'UNIFORM'
                    if hasattr(mix_3, 'hide'):
                        mix_3.hide = False
                    if hasattr(mix_3, 'location'):
                        mix_3.location = (-480.0, -189.0)
                    if hasattr(mix_3, 'mute'):
                        mix_3.mute = False
                    if hasattr(mix_3, 'name'):
                        mix_3.name = 'Mix'
                    if hasattr(mix_3, 'use_custom_color'):
                        mix_3.use_custom_color = False
                    if hasattr(mix_3, 'width'):
                        mix_3.width = 140.0
                    input_ = next((input_ for input_ in mix_3.inputs if input_.identifier=='Factor_Float'), None)
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
                    input_ = next((input_ for input_ in mix_3.inputs if input_.identifier=='Factor_Vector'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = (0.5, 0.5, 0.5)
                        if hasattr(input_, 'display_shape'):
                            input_.display_shape = 'CIRCLE'
                        if hasattr(input_, 'enabled'):
                            input_.enabled = False
                        if hasattr(input_, 'hide'):
                            input_.hide = True
                        if hasattr(input_, 'hide_value'):
                            input_.hide_value = False
                        if hasattr(input_, 'name'):
                            input_.name = 'Factor'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in mix_3.inputs if input_.identifier=='A_Float'), None)
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
                            input_.name = 'A'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in mix_3.inputs if input_.identifier=='B_Float'), None)
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
                            input_.name = 'B'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in mix_3.inputs if input_.identifier=='A_Vector'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = (0.0, 0.0, 0.0)
                        if hasattr(input_, 'display_shape'):
                            input_.display_shape = 'CIRCLE'
                        if hasattr(input_, 'enabled'):
                            input_.enabled = False
                        if hasattr(input_, 'hide'):
                            input_.hide = True
                        if hasattr(input_, 'hide_value'):
                            input_.hide_value = False
                        if hasattr(input_, 'name'):
                            input_.name = 'A'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in mix_3.inputs if input_.identifier=='B_Vector'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = (0.0, 0.0, 0.0)
                        if hasattr(input_, 'display_shape'):
                            input_.display_shape = 'CIRCLE'
                        if hasattr(input_, 'enabled'):
                            input_.enabled = False
                        if hasattr(input_, 'hide'):
                            input_.hide = True
                        if hasattr(input_, 'hide_value'):
                            input_.hide_value = False
                        if hasattr(input_, 'name'):
                            input_.name = 'B'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in mix_3.inputs if input_.identifier=='A_Color'), None)
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
                    input_ = next((input_ for input_ in mix_3.inputs if input_.identifier=='B_Color'), None)
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
                    output = next((output for output in mix_3.outputs if output.identifier=='Result_Float'), None)
                    if output:
                        if hasattr(output, 'default_value'):
                            output.default_value = 0.0
                        if hasattr(output, 'display_shape'):
                            output.display_shape = 'CIRCLE'
                        if hasattr(output, 'enabled'):
                            output.enabled = False
                        if hasattr(output, 'hide'):
                            output.hide = True
                        if hasattr(output, 'hide_value'):
                            output.hide_value = False
                        if hasattr(output, 'name'):
                            output.name = 'Result'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in mix_3.outputs if output.identifier=='Result_Vector'), None)
                    if output:
                        if hasattr(output, 'default_value'):
                            output.default_value = (0.0, 0.0, 0.0)
                        if hasattr(output, 'display_shape'):
                            output.display_shape = 'CIRCLE'
                        if hasattr(output, 'enabled'):
                            output.enabled = False
                        if hasattr(output, 'hide'):
                            output.hide = True
                        if hasattr(output, 'hide_value'):
                            output.hide_value = False
                        if hasattr(output, 'name'):
                            output.name = 'Result'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in mix_3.outputs if output.identifier=='Result_Color'), None)
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

                    group_input_3 = node_tree3.nodes.new('NodeGroupInput')
                    if hasattr(group_input_3, 'color'):
                        group_input_3.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                    if hasattr(group_input_3, 'hide'):
                        group_input_3.hide = False
                    if hasattr(group_input_3, 'location'):
                        group_input_3.location = (-480.0, 0.0)
                    if hasattr(group_input_3, 'mute'):
                        group_input_3.mute = False
                    if hasattr(group_input_3, 'name'):
                        group_input_3.name = 'Group Input'
                    if hasattr(group_input_3, 'use_custom_color'):
                        group_input_3.use_custom_color = True
                    if hasattr(group_input_3, 'width'):
                        group_input_3.width = 140.0
                    if hasattr(group_input_3.outputs[0], 'default_value'):
                        group_input_3.outputs[0].default_value = 0.5
                    if hasattr(group_input_3.outputs[0], 'display_shape'):
                        group_input_3.outputs[0].display_shape = 'CIRCLE'
                    if hasattr(group_input_3.outputs[0], 'enabled'):
                        group_input_3.outputs[0].enabled = True
                    if hasattr(group_input_3.outputs[0], 'hide'):
                        group_input_3.outputs[0].hide = True
                    if hasattr(group_input_3.outputs[0], 'hide_value'):
                        group_input_3.outputs[0].hide_value = False
                    if hasattr(group_input_3.outputs[0], 'name'):
                        group_input_3.outputs[0].name = 'Roughness'
                    if hasattr(group_input_3.outputs[0], 'show_expanded'):
                        group_input_3.outputs[0].show_expanded = False
                    if hasattr(group_input_3.outputs[1], 'default_value'):
                        group_input_3.outputs[1].default_value = 1.0
                    if hasattr(group_input_3.outputs[1], 'display_shape'):
                        group_input_3.outputs[1].display_shape = 'CIRCLE'
                    if hasattr(group_input_3.outputs[1], 'enabled'):
                        group_input_3.outputs[1].enabled = True
                    if hasattr(group_input_3.outputs[1], 'hide'):
                        group_input_3.outputs[1].hide = True
                    if hasattr(group_input_3.outputs[1], 'hide_value'):
                        group_input_3.outputs[1].hide_value = False
                    if hasattr(group_input_3.outputs[1], 'name'):
                        group_input_3.outputs[1].name = 'Fac'
                    if hasattr(group_input_3.outputs[1], 'show_expanded'):
                        group_input_3.outputs[1].show_expanded = False
                    if hasattr(group_input_3.outputs[2], 'default_value'):
                        group_input_3.outputs[2].default_value = 0.5
                    if hasattr(group_input_3.outputs[2], 'display_shape'):
                        group_input_3.outputs[2].display_shape = 'CIRCLE'
                    if hasattr(group_input_3.outputs[2], 'enabled'):
                        group_input_3.outputs[2].enabled = True
                    if hasattr(group_input_3.outputs[2], 'hide'):
                        group_input_3.outputs[2].hide = False
                    if hasattr(group_input_3.outputs[2], 'hide_value'):
                        group_input_3.outputs[2].hide_value = False
                    if hasattr(group_input_3.outputs[2], 'name'):
                        group_input_3.outputs[2].name = 'Rim'
                    if hasattr(group_input_3.outputs[2], 'show_expanded'):
                        group_input_3.outputs[2].show_expanded = False
                    if hasattr(group_input_3.outputs[3], 'default_value'):
                        group_input_3.outputs[3].default_value = (0.0, 0.0, 0.0)
                    if hasattr(group_input_3.outputs[3], 'display_shape'):
                        group_input_3.outputs[3].display_shape = 'CIRCLE'
                    if hasattr(group_input_3.outputs[3], 'enabled'):
                        group_input_3.outputs[3].enabled = True
                    if hasattr(group_input_3.outputs[3], 'hide'):
                        group_input_3.outputs[3].hide = False
                    if hasattr(group_input_3.outputs[3], 'hide_value'):
                        group_input_3.outputs[3].hide_value = True
                    if hasattr(group_input_3.outputs[3], 'name'):
                        group_input_3.outputs[3].name = 'Normal'
                    if hasattr(group_input_3.outputs[3], 'show_expanded'):
                        group_input_3.outputs[3].show_expanded = False

                    rgb_curves_3 = node_tree3.nodes.new('ShaderNodeRGBCurve')
                    if hasattr(rgb_curves_3, 'color'):
                        rgb_curves_3.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                    if hasattr(rgb_curves_3, 'hide'):
                        rgb_curves_3.hide = False
                    if hasattr(rgb_curves_3, 'location'):
                        rgb_curves_3.location = (-480.0, -94.0)
                    if hasattr(rgb_curves_3, 'mapping'):
                        if hasattr(rgb_curves_3.mapping, 'black_level'):
                            rgb_curves_3.mapping.black_level = (0.0, 0.0, 0.0)
                        if hasattr(rgb_curves_3.mapping, 'clip_max_x'):
                            rgb_curves_3.mapping.clip_max_x = 1.0
                        if hasattr(rgb_curves_3.mapping, 'clip_max_y'):
                            rgb_curves_3.mapping.clip_max_y = 1.0
                        if hasattr(rgb_curves_3.mapping, 'clip_min_x'):
                            rgb_curves_3.mapping.clip_min_x = 0.0
                        if hasattr(rgb_curves_3.mapping, 'clip_min_y'):
                            rgb_curves_3.mapping.clip_min_y = 0.0
                        if hasattr(rgb_curves_3.mapping, 'curves'):
                            if hasattr(rgb_curves_3.mapping.curves[0], 'points'):
                                if 0 >= len(rgb_curves_3.mapping.curves[0].points):
                                    rgb_curves_3.mapping.curves[0].points.new(0.0, 0.0)
                                if hasattr(rgb_curves_3.mapping.curves[0].points[0], 'handle_type'):
                                    rgb_curves_3.mapping.curves[0].points[0].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[0].points[0], 'location'):
                                    rgb_curves_3.mapping.curves[0].points[0].location = (0.0, 0.0)
                                if hasattr(rgb_curves_3.mapping.curves[0].points[0], 'select'):
                                    rgb_curves_3.mapping.curves[0].points[0].select = False
                                if 1 >= len(rgb_curves_3.mapping.curves[0].points):
                                    rgb_curves_3.mapping.curves[0].points.new(1.0, 1.0)
                                if hasattr(rgb_curves_3.mapping.curves[0].points[1], 'handle_type'):
                                    rgb_curves_3.mapping.curves[0].points[1].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[0].points[1], 'location'):
                                    rgb_curves_3.mapping.curves[0].points[1].location = (1.0, 1.0)
                                if hasattr(rgb_curves_3.mapping.curves[0].points[1], 'select'):
                                    rgb_curves_3.mapping.curves[0].points[1].select = False
                            if hasattr(rgb_curves_3.mapping.curves[1], 'points'):
                                if 0 >= len(rgb_curves_3.mapping.curves[1].points):
                                    rgb_curves_3.mapping.curves[1].points.new(0.0, 0.0)
                                if hasattr(rgb_curves_3.mapping.curves[1].points[0], 'handle_type'):
                                    rgb_curves_3.mapping.curves[1].points[0].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[1].points[0], 'location'):
                                    rgb_curves_3.mapping.curves[1].points[0].location = (0.0, 0.0)
                                if hasattr(rgb_curves_3.mapping.curves[1].points[0], 'select'):
                                    rgb_curves_3.mapping.curves[1].points[0].select = False
                                if 1 >= len(rgb_curves_3.mapping.curves[1].points):
                                    rgb_curves_3.mapping.curves[1].points.new(1.0, 1.0)
                                if hasattr(rgb_curves_3.mapping.curves[1].points[1], 'handle_type'):
                                    rgb_curves_3.mapping.curves[1].points[1].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[1].points[1], 'location'):
                                    rgb_curves_3.mapping.curves[1].points[1].location = (1.0, 1.0)
                                if hasattr(rgb_curves_3.mapping.curves[1].points[1], 'select'):
                                    rgb_curves_3.mapping.curves[1].points[1].select = False
                            if hasattr(rgb_curves_3.mapping.curves[2], 'points'):
                                if 0 >= len(rgb_curves_3.mapping.curves[2].points):
                                    rgb_curves_3.mapping.curves[2].points.new(0.0, 0.0)
                                if hasattr(rgb_curves_3.mapping.curves[2].points[0], 'handle_type'):
                                    rgb_curves_3.mapping.curves[2].points[0].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[2].points[0], 'location'):
                                    rgb_curves_3.mapping.curves[2].points[0].location = (0.0, 0.0)
                                if hasattr(rgb_curves_3.mapping.curves[2].points[0], 'select'):
                                    rgb_curves_3.mapping.curves[2].points[0].select = False
                                if 1 >= len(rgb_curves_3.mapping.curves[2].points):
                                    rgb_curves_3.mapping.curves[2].points.new(1.0, 1.0)
                                if hasattr(rgb_curves_3.mapping.curves[2].points[1], 'handle_type'):
                                    rgb_curves_3.mapping.curves[2].points[1].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[2].points[1], 'location'):
                                    rgb_curves_3.mapping.curves[2].points[1].location = (1.0, 1.0)
                                if hasattr(rgb_curves_3.mapping.curves[2].points[1], 'select'):
                                    rgb_curves_3.mapping.curves[2].points[1].select = False
                            if hasattr(rgb_curves_3.mapping.curves[3], 'points'):
                                if 0 >= len(rgb_curves_3.mapping.curves[3].points):
                                    rgb_curves_3.mapping.curves[3].points.new(0.0, 0.0)
                                if hasattr(rgb_curves_3.mapping.curves[3].points[0], 'handle_type'):
                                    rgb_curves_3.mapping.curves[3].points[0].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[3].points[0], 'location'):
                                    rgb_curves_3.mapping.curves[3].points[0].location = (0.0, 0.0)
                                if hasattr(rgb_curves_3.mapping.curves[3].points[0], 'select'):
                                    rgb_curves_3.mapping.curves[3].points[0].select = False
                                if 1 >= len(rgb_curves_3.mapping.curves[3].points):
                                    rgb_curves_3.mapping.curves[3].points.new(0.5, 0.33000001311302185)
                                if hasattr(rgb_curves_3.mapping.curves[3].points[1], 'handle_type'):
                                    rgb_curves_3.mapping.curves[3].points[1].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[3].points[1], 'location'):
                                    rgb_curves_3.mapping.curves[3].points[1].location = (0.5, 0.33000001311302185)
                                if hasattr(rgb_curves_3.mapping.curves[3].points[1], 'select'):
                                    rgb_curves_3.mapping.curves[3].points[1].select = True
                                if 2 >= len(rgb_curves_3.mapping.curves[3].points):
                                    rgb_curves_3.mapping.curves[3].points.new(1.0, 1.0)
                                if hasattr(rgb_curves_3.mapping.curves[3].points[2], 'handle_type'):
                                    rgb_curves_3.mapping.curves[3].points[2].handle_type = 'AUTO'
                                if hasattr(rgb_curves_3.mapping.curves[3].points[2], 'location'):
                                    rgb_curves_3.mapping.curves[3].points[2].location = (1.0, 1.0)
                                if hasattr(rgb_curves_3.mapping.curves[3].points[2], 'select'):
                                    rgb_curves_3.mapping.curves[3].points[2].select = False
                        if hasattr(rgb_curves_3.mapping, 'extend'):
                            rgb_curves_3.mapping.extend = 'EXTRAPOLATED'
                        if hasattr(rgb_curves_3.mapping, 'tone'):
                            rgb_curves_3.mapping.tone = 'STANDARD'
                        if hasattr(rgb_curves_3.mapping, 'use_clip'):
                            rgb_curves_3.mapping.use_clip = True
                        if hasattr(rgb_curves_3.mapping, 'white_level'):
                            rgb_curves_3.mapping.white_level = (1.0, 1.0, 1.0)
                    if hasattr(rgb_curves_3, 'mute'):
                        rgb_curves_3.mute = False
                    if hasattr(rgb_curves_3, 'name'):
                        rgb_curves_3.name = 'RGB Curves'
                    if hasattr(rgb_curves_3, 'use_custom_color'):
                        rgb_curves_3.use_custom_color = False
                    if hasattr(rgb_curves_3, 'width'):
                        rgb_curves_3.width = 140.0
                    input_ = next((input_ for input_ in rgb_curves_3.inputs if input_.identifier=='Fac'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = 1.0
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
                    input_ = next((input_ for input_ in rgb_curves_3.inputs if input_.identifier=='Color'), None)
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
                            input_.name = 'Color'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    output = next((output for output in rgb_curves_3.outputs if output.identifier=='Color'), None)
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

                    geometry_001_3 = node_tree3.nodes.new('ShaderNodeNewGeometry')
                    if hasattr(geometry_001_3, 'color'):
                        geometry_001_3.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                    if hasattr(geometry_001_3, 'hide'):
                        geometry_001_3.hide = False
                    if hasattr(geometry_001_3, 'location'):
                        geometry_001_3.location = (-640.0, -189.0)
                    if hasattr(geometry_001_3, 'mute'):
                        geometry_001_3.mute = False
                    if hasattr(geometry_001_3, 'name'):
                        geometry_001_3.name = 'Geometry.001'
                    if hasattr(geometry_001_3, 'use_custom_color'):
                        geometry_001_3.use_custom_color = False
                    if hasattr(geometry_001_3, 'width'):
                        geometry_001_3.width = 140.0
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='Position'), None)
                    if output:
                        if hasattr(output, 'default_value'):
                            output.default_value = (0.0, 0.0, 0.0)
                        if hasattr(output, 'display_shape'):
                            output.display_shape = 'CIRCLE'
                        if hasattr(output, 'enabled'):
                            output.enabled = True
                        if hasattr(output, 'hide'):
                            output.hide = True
                        if hasattr(output, 'hide_value'):
                            output.hide_value = False
                        if hasattr(output, 'name'):
                            output.name = 'Position'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='Normal'), None)
                    if output:
                        if hasattr(output, 'default_value'):
                            output.default_value = (0.0, 0.0, 0.0)
                        if hasattr(output, 'display_shape'):
                            output.display_shape = 'CIRCLE'
                        if hasattr(output, 'enabled'):
                            output.enabled = True
                        if hasattr(output, 'hide'):
                            output.hide = True
                        if hasattr(output, 'hide_value'):
                            output.hide_value = False
                        if hasattr(output, 'name'):
                            output.name = 'Normal'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='Tangent'), None)
                    if output:
                        if hasattr(output, 'default_value'):
                            output.default_value = (0.0, 0.0, 0.0)
                        if hasattr(output, 'display_shape'):
                            output.display_shape = 'CIRCLE'
                        if hasattr(output, 'enabled'):
                            output.enabled = True
                        if hasattr(output, 'hide'):
                            output.hide = True
                        if hasattr(output, 'hide_value'):
                            output.hide_value = False
                        if hasattr(output, 'name'):
                            output.name = 'Tangent'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='True Normal'), None)
                    if output:
                        if hasattr(output, 'default_value'):
                            output.default_value = (0.0, 0.0, 0.0)
                        if hasattr(output, 'display_shape'):
                            output.display_shape = 'CIRCLE'
                        if hasattr(output, 'enabled'):
                            output.enabled = True
                        if hasattr(output, 'hide'):
                            output.hide = True
                        if hasattr(output, 'hide_value'):
                            output.hide_value = False
                        if hasattr(output, 'name'):
                            output.name = 'True Normal'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='Incoming'), None)
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
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='Parametric'), None)
                    if output:
                        if hasattr(output, 'default_value'):
                            output.default_value = (0.0, 0.0, 0.0)
                        if hasattr(output, 'display_shape'):
                            output.display_shape = 'CIRCLE'
                        if hasattr(output, 'enabled'):
                            output.enabled = True
                        if hasattr(output, 'hide'):
                            output.hide = True
                        if hasattr(output, 'hide_value'):
                            output.hide_value = False
                        if hasattr(output, 'name'):
                            output.name = 'Parametric'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='Backfacing'), None)
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
                            output.name = 'Backfacing'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='Pointiness'), None)
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
                            output.name = 'Pointiness'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False
                    output = next((output for output in geometry_001_3.outputs if output.identifier=='Random Per Island'), None)
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
                            output.name = 'Random Per Island'
                        if hasattr(output, 'show_expanded'):
                            output.show_expanded = False

                    group_input_002_3 = node_tree3.nodes.new('NodeGroupInput')
                    if hasattr(group_input_002_3, 'color'):
                        group_input_002_3.color = (0.6152219772338867, 0.6094059944152832, 0.45547398924827576)
                    if hasattr(group_input_002_3, 'hide'):
                        group_input_002_3.hide = False
                    if hasattr(group_input_002_3, 'location'):
                        group_input_002_3.location = (-640.0, 0.0)
                    if hasattr(group_input_002_3, 'mute'):
                        group_input_002_3.mute = False
                    if hasattr(group_input_002_3, 'name'):
                        group_input_002_3.name = 'Group Input.002'
                    if hasattr(group_input_002_3, 'use_custom_color'):
                        group_input_002_3.use_custom_color = True
                    if hasattr(group_input_002_3, 'width'):
                        group_input_002_3.width = 140.0
                    if hasattr(group_input_002_3.outputs[0], 'default_value'):
                        group_input_002_3.outputs[0].default_value = 0.5
                    if hasattr(group_input_002_3.outputs[0], 'display_shape'):
                        group_input_002_3.outputs[0].display_shape = 'CIRCLE'
                    if hasattr(group_input_002_3.outputs[0], 'enabled'):
                        group_input_002_3.outputs[0].enabled = True
                    if hasattr(group_input_002_3.outputs[0], 'hide'):
                        group_input_002_3.outputs[0].hide = False
                    if hasattr(group_input_002_3.outputs[0], 'hide_value'):
                        group_input_002_3.outputs[0].hide_value = False
                    if hasattr(group_input_002_3.outputs[0], 'name'):
                        group_input_002_3.outputs[0].name = 'Roughness'
                    if hasattr(group_input_002_3.outputs[0], 'show_expanded'):
                        group_input_002_3.outputs[0].show_expanded = False
                    if hasattr(group_input_002_3.outputs[1], 'default_value'):
                        group_input_002_3.outputs[1].default_value = 1.0
                    if hasattr(group_input_002_3.outputs[1], 'display_shape'):
                        group_input_002_3.outputs[1].display_shape = 'CIRCLE'
                    if hasattr(group_input_002_3.outputs[1], 'enabled'):
                        group_input_002_3.outputs[1].enabled = True
                    if hasattr(group_input_002_3.outputs[1], 'hide'):
                        group_input_002_3.outputs[1].hide = False
                    if hasattr(group_input_002_3.outputs[1], 'hide_value'):
                        group_input_002_3.outputs[1].hide_value = False
                    if hasattr(group_input_002_3.outputs[1], 'name'):
                        group_input_002_3.outputs[1].name = 'Fac'
                    if hasattr(group_input_002_3.outputs[1], 'show_expanded'):
                        group_input_002_3.outputs[1].show_expanded = False
                    if hasattr(group_input_002_3.outputs[2], 'default_value'):
                        group_input_002_3.outputs[2].default_value = 0.5
                    if hasattr(group_input_002_3.outputs[2], 'display_shape'):
                        group_input_002_3.outputs[2].display_shape = 'CIRCLE'
                    if hasattr(group_input_002_3.outputs[2], 'enabled'):
                        group_input_002_3.outputs[2].enabled = True
                    if hasattr(group_input_002_3.outputs[2], 'hide'):
                        group_input_002_3.outputs[2].hide = True
                    if hasattr(group_input_002_3.outputs[2], 'hide_value'):
                        group_input_002_3.outputs[2].hide_value = False
                    if hasattr(group_input_002_3.outputs[2], 'name'):
                        group_input_002_3.outputs[2].name = 'Rim'
                    if hasattr(group_input_002_3.outputs[2], 'show_expanded'):
                        group_input_002_3.outputs[2].show_expanded = False
                    if hasattr(group_input_002_3.outputs[3], 'default_value'):
                        group_input_002_3.outputs[3].default_value = (0.0, 0.0, 0.0)
                    if hasattr(group_input_002_3.outputs[3], 'display_shape'):
                        group_input_002_3.outputs[3].display_shape = 'CIRCLE'
                    if hasattr(group_input_002_3.outputs[3], 'enabled'):
                        group_input_002_3.outputs[3].enabled = True
                    if hasattr(group_input_002_3.outputs[3], 'hide'):
                        group_input_002_3.outputs[3].hide = True
                    if hasattr(group_input_002_3.outputs[3], 'hide_value'):
                        group_input_002_3.outputs[3].hide_value = True
                    if hasattr(group_input_002_3.outputs[3], 'name'):
                        group_input_002_3.outputs[3].name = 'Normal'
                    if hasattr(group_input_002_3.outputs[3], 'show_expanded'):
                        group_input_002_3.outputs[3].show_expanded = False

                    bump_001_3 = node_tree3.nodes.new('ShaderNodeBump')
                    if hasattr(bump_001_3, 'color'):
                        bump_001_3.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                    if hasattr(bump_001_3, 'hide'):
                        bump_001_3.hide = False
                    if hasattr(bump_001_3, 'invert'):
                        bump_001_3.invert = False
                    if hasattr(bump_001_3, 'location'):
                        bump_001_3.location = (-640.0, -94.0)
                    if hasattr(bump_001_3, 'mute'):
                        bump_001_3.mute = False
                    if hasattr(bump_001_3, 'name'):
                        bump_001_3.name = 'Bump.001'
                    if hasattr(bump_001_3, 'use_custom_color'):
                        bump_001_3.use_custom_color = False
                    if hasattr(bump_001_3, 'width'):
                        bump_001_3.width = 140.0
                    input_ = next((input_ for input_ in bump_001_3.inputs if input_.identifier=='Strength'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = 1.0
                        if hasattr(input_, 'display_shape'):
                            input_.display_shape = 'CIRCLE'
                        if hasattr(input_, 'enabled'):
                            input_.enabled = True
                        if hasattr(input_, 'hide'):
                            input_.hide = True
                        if hasattr(input_, 'hide_value'):
                            input_.hide_value = False
                        if hasattr(input_, 'name'):
                            input_.name = 'Strength'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in bump_001_3.inputs if input_.identifier=='Distance'), None)
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
                            input_.name = 'Distance'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in bump_001_3.inputs if input_.identifier=='Height'), None)
                    if input_:
                        if hasattr(input_, 'default_value'):
                            input_.default_value = 1.0
                        if hasattr(input_, 'display_shape'):
                            input_.display_shape = 'CIRCLE'
                        if hasattr(input_, 'enabled'):
                            input_.enabled = True
                        if hasattr(input_, 'hide'):
                            input_.hide = True
                        if hasattr(input_, 'hide_value'):
                            input_.hide_value = True
                        if hasattr(input_, 'name'):
                            input_.name = 'Height'
                        if hasattr(input_, 'show_expanded'):
                            input_.show_expanded = False
                    input_ = next((input_ for input_ in bump_001_3.inputs if input_.identifier=='Normal'), None)
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
                    output = next((output for output in bump_001_3.outputs if output.identifier=='Normal'), None)
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

                    # LINKS
                    node_tree3.links.new(layer_weight_3.outputs[1], math_3.inputs[0])
                    node_tree3.links.new(math_3.outputs[0], group_output_3.inputs[1])
                    node_tree3.links.new(group_input_3.outputs[2], layer_weight_3.inputs[0])
                    node_tree3.links.new(geometry_001_3.outputs[4], mix_3.inputs[7])
                    node_tree3.links.new(layer_weight_001_3.outputs[0], math_001_3.inputs[0])
                    node_tree3.links.new(layer_weight_001_3.outputs[0], group_output_3.inputs[0])
                    node_tree3.links.new(bump_001_3.outputs[0], mix_3.inputs[6])
                    node_tree3.links.new(mix_3.outputs[2], layer_weight_001_3.inputs[1])
                    node_tree3.links.new(group_input_3.outputs[3], layer_weight_3.inputs[1])
                    node_tree3.links.new(math_001_3.outputs[0], group_output_3.inputs[2])
                    node_tree3.links.new(rgb_curves_3.outputs[0], layer_weight_001_3.inputs[0])
                    node_tree3.links.new(group_input_001_3.outputs[3], bump_001_3.inputs[3])
                    node_tree3.links.new(group_input_002_3.outputs[0], mix_3.inputs[0])
                    node_tree3.links.new(group_input_002_3.outputs[1], rgb_curves_3.inputs[1])

                fresnel_2 = node_tree2.nodes.new('ShaderNodeGroup')
                if hasattr(fresnel_2, 'node_tree'):
                    fresnel_2.node_tree = bpy.data.node_groups.get('Fresnel')
                if hasattr(fresnel_2, 'color'):
                    fresnel_2.color = (0.22681938111782074, 0.6080002188682556, 0.6080002188682556)
                if hasattr(fresnel_2, 'hide'):
                    fresnel_2.hide = False
                if hasattr(fresnel_2, 'label'):
                    fresnel_2.label = 'Fresnel'
                if hasattr(fresnel_2, 'location'):
                    fresnel_2.location = (-320.0, 0.0)
                if hasattr(fresnel_2, 'mute'):
                    fresnel_2.mute = False
                if hasattr(fresnel_2, 'name'):
                    fresnel_2.name = 'Fresnel'
                if hasattr(fresnel_2, 'use_custom_color'):
                    fresnel_2.use_custom_color = True
                if hasattr(fresnel_2, 'width'):
                    fresnel_2.width = 140.0
                if hasattr(fresnel_2.inputs[0], 'default_value'):
                    fresnel_2.inputs[0].default_value = 0.0
                if hasattr(fresnel_2.inputs[0], 'display_shape'):
                    fresnel_2.inputs[0].display_shape = 'CIRCLE'
                if hasattr(fresnel_2.inputs[0], 'enabled'):
                    fresnel_2.inputs[0].enabled = True
                if hasattr(fresnel_2.inputs[0], 'hide'):
                    fresnel_2.inputs[0].hide = False
                if hasattr(fresnel_2.inputs[0], 'hide_value'):
                    fresnel_2.inputs[0].hide_value = False
                if hasattr(fresnel_2.inputs[0], 'name'):
                    fresnel_2.inputs[0].name = 'Roughness'
                if hasattr(fresnel_2.inputs[0], 'show_expanded'):
                    fresnel_2.inputs[0].show_expanded = False
                if hasattr(fresnel_2.inputs[1], 'default_value'):
                    fresnel_2.inputs[1].default_value = 0.33000001311302185
                if hasattr(fresnel_2.inputs[1], 'display_shape'):
                    fresnel_2.inputs[1].display_shape = 'CIRCLE'
                if hasattr(fresnel_2.inputs[1], 'enabled'):
                    fresnel_2.inputs[1].enabled = True
                if hasattr(fresnel_2.inputs[1], 'hide'):
                    fresnel_2.inputs[1].hide = False
                if hasattr(fresnel_2.inputs[1], 'hide_value'):
                    fresnel_2.inputs[1].hide_value = False
                if hasattr(fresnel_2.inputs[1], 'name'):
                    fresnel_2.inputs[1].name = 'Fac'
                if hasattr(fresnel_2.inputs[1], 'show_expanded'):
                    fresnel_2.inputs[1].show_expanded = False
                if hasattr(fresnel_2.inputs[2], 'default_value'):
                    fresnel_2.inputs[2].default_value = 0.5
                if hasattr(fresnel_2.inputs[2], 'display_shape'):
                    fresnel_2.inputs[2].display_shape = 'CIRCLE'
                if hasattr(fresnel_2.inputs[2], 'enabled'):
                    fresnel_2.inputs[2].enabled = True
                if hasattr(fresnel_2.inputs[2], 'hide'):
                    fresnel_2.inputs[2].hide = True
                if hasattr(fresnel_2.inputs[2], 'hide_value'):
                    fresnel_2.inputs[2].hide_value = False
                if hasattr(fresnel_2.inputs[2], 'name'):
                    fresnel_2.inputs[2].name = 'Rim'
                if hasattr(fresnel_2.inputs[2], 'show_expanded'):
                    fresnel_2.inputs[2].show_expanded = False
                if hasattr(fresnel_2.inputs[3], 'default_value'):
                    fresnel_2.inputs[3].default_value = (0.0, 0.0, 0.0)
                if hasattr(fresnel_2.inputs[3], 'display_shape'):
                    fresnel_2.inputs[3].display_shape = 'CIRCLE'
                if hasattr(fresnel_2.inputs[3], 'enabled'):
                    fresnel_2.inputs[3].enabled = True
                if hasattr(fresnel_2.inputs[3], 'hide'):
                    fresnel_2.inputs[3].hide = False
                if hasattr(fresnel_2.inputs[3], 'hide_value'):
                    fresnel_2.inputs[3].hide_value = True
                if hasattr(fresnel_2.inputs[3], 'name'):
                    fresnel_2.inputs[3].name = 'Normal'
                if hasattr(fresnel_2.inputs[3], 'show_expanded'):
                    fresnel_2.inputs[3].show_expanded = False
                if hasattr(fresnel_2.outputs[0], 'default_value'):
                    fresnel_2.outputs[0].default_value = 0.0
                if hasattr(fresnel_2.outputs[0], 'display_shape'):
                    fresnel_2.outputs[0].display_shape = 'CIRCLE'
                if hasattr(fresnel_2.outputs[0], 'enabled'):
                    fresnel_2.outputs[0].enabled = True
                if hasattr(fresnel_2.outputs[0], 'hide'):
                    fresnel_2.outputs[0].hide = False
                if hasattr(fresnel_2.outputs[0], 'hide_value'):
                    fresnel_2.outputs[0].hide_value = False
                if hasattr(fresnel_2.outputs[0], 'name'):
                    fresnel_2.outputs[0].name = 'Fresnel'
                if hasattr(fresnel_2.outputs[0], 'show_expanded'):
                    fresnel_2.outputs[0].show_expanded = False
                if hasattr(fresnel_2.outputs[1], 'default_value'):
                    fresnel_2.outputs[1].default_value = 0.0
                if hasattr(fresnel_2.outputs[1], 'display_shape'):
                    fresnel_2.outputs[1].display_shape = 'CIRCLE'
                if hasattr(fresnel_2.outputs[1], 'enabled'):
                    fresnel_2.outputs[1].enabled = True
                if hasattr(fresnel_2.outputs[1], 'hide'):
                    fresnel_2.outputs[1].hide = True
                if hasattr(fresnel_2.outputs[1], 'hide_value'):
                    fresnel_2.outputs[1].hide_value = False
                if hasattr(fresnel_2.outputs[1], 'name'):
                    fresnel_2.outputs[1].name = 'Metallic Rim'
                if hasattr(fresnel_2.outputs[1], 'show_expanded'):
                    fresnel_2.outputs[1].show_expanded = False
                if hasattr(fresnel_2.outputs[2], 'default_value'):
                    fresnel_2.outputs[2].default_value = 0.0
                if hasattr(fresnel_2.outputs[2], 'display_shape'):
                    fresnel_2.outputs[2].display_shape = 'CIRCLE'
                if hasattr(fresnel_2.outputs[2], 'enabled'):
                    fresnel_2.outputs[2].enabled = True
                if hasattr(fresnel_2.outputs[2], 'hide'):
                    fresnel_2.outputs[2].hide = True
                if hasattr(fresnel_2.outputs[2], 'hide_value'):
                    fresnel_2.outputs[2].hide_value = False
                if hasattr(fresnel_2.outputs[2], 'name'):
                    fresnel_2.outputs[2].name = 'Metallic Fresnel'
                if hasattr(fresnel_2.outputs[2], 'show_expanded'):
                    fresnel_2.outputs[2].show_expanded = False

                # LINKS
                node_tree2.links.new(glossy_bsdf_2.outputs[0], mix_shader_2.inputs[2])
                node_tree2.links.new(mix_shader_2.outputs[0], group_output_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[4], glossy_bsdf_2.inputs[2])
                node_tree2.links.new(fresnel_2.outputs[0], group_output_2.inputs[1])
                node_tree2.links.new(group_input_2.outputs[2], glossy_bsdf_2.inputs[0])
                node_tree2.links.new(math_001_2.outputs[0], glossy_bsdf_2.inputs[1])
                node_tree2.links.new(fresnel_2.outputs[0], mix_shader_2.inputs[0])
                node_tree2.links.new(math_2.outputs[0], math_001_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[4], fresnel_2.inputs[3])
                node_tree2.links.new(group_input_2.outputs[3], fresnel_2.inputs[1])
                node_tree2.links.new(math_2.outputs[0], fresnel_2.inputs[0])
                node_tree2.links.new(group_input_001_2.outputs[0], mix_shader_2.inputs[1])
                node_tree2.links.new(group_input_002_2.outputs[1], math_2.inputs[0])

            reflection_001_1 = node_tree1.nodes.new('ShaderNodeGroup')
            if hasattr(reflection_001_1, 'node_tree'):
                reflection_001_1.node_tree = bpy.data.node_groups.get('Reflection')
            if hasattr(reflection_001_1, 'color'):
                reflection_001_1.color = (0.6080002188682556, 0.5312551856040955, 0.49913641810417175)
            if hasattr(reflection_001_1, 'hide'):
                reflection_001_1.hide = False
            if hasattr(reflection_001_1, 'label'):
                reflection_001_1.label = 'Reflection'
            if hasattr(reflection_001_1, 'location'):
                reflection_001_1.location = (-160.0, 0.0)
            if hasattr(reflection_001_1, 'mute'):
                reflection_001_1.mute = False
            if hasattr(reflection_001_1, 'name'):
                reflection_001_1.name = 'Reflection.001'
            if hasattr(reflection_001_1, 'use_custom_color'):
                reflection_001_1.use_custom_color = True
            if hasattr(reflection_001_1, 'width'):
                reflection_001_1.width = 140.0
            if hasattr(reflection_001_1.inputs[1], 'default_value'):
                reflection_001_1.inputs[1].default_value = 0.5
            if hasattr(reflection_001_1.inputs[1], 'display_shape'):
                reflection_001_1.inputs[1].display_shape = 'CIRCLE'
            if hasattr(reflection_001_1.inputs[1], 'enabled'):
                reflection_001_1.inputs[1].enabled = True
            if hasattr(reflection_001_1.inputs[1], 'hide'):
                reflection_001_1.inputs[1].hide = False
            if hasattr(reflection_001_1.inputs[1], 'hide_value'):
                reflection_001_1.inputs[1].hide_value = False
            if hasattr(reflection_001_1.inputs[1], 'name'):
                reflection_001_1.inputs[1].name = 'Roughness'
            if hasattr(reflection_001_1.inputs[1], 'show_expanded'):
                reflection_001_1.inputs[1].show_expanded = False
            if hasattr(reflection_001_1.inputs[2], 'default_value'):
                reflection_001_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            if hasattr(reflection_001_1.inputs[2], 'display_shape'):
                reflection_001_1.inputs[2].display_shape = 'CIRCLE'
            if hasattr(reflection_001_1.inputs[2], 'enabled'):
                reflection_001_1.inputs[2].enabled = True
            if hasattr(reflection_001_1.inputs[2], 'hide'):
                reflection_001_1.inputs[2].hide = False
            if hasattr(reflection_001_1.inputs[2], 'hide_value'):
                reflection_001_1.inputs[2].hide_value = False
            if hasattr(reflection_001_1.inputs[2], 'name'):
                reflection_001_1.inputs[2].name = 'Reflection Color'
            if hasattr(reflection_001_1.inputs[2], 'show_expanded'):
                reflection_001_1.inputs[2].show_expanded = False
            if hasattr(reflection_001_1.inputs[3], 'default_value'):
                reflection_001_1.inputs[3].default_value = 0.25
            if hasattr(reflection_001_1.inputs[3], 'display_shape'):
                reflection_001_1.inputs[3].display_shape = 'CIRCLE'
            if hasattr(reflection_001_1.inputs[3], 'enabled'):
                reflection_001_1.inputs[3].enabled = True
            if hasattr(reflection_001_1.inputs[3], 'hide'):
                reflection_001_1.inputs[3].hide = False
            if hasattr(reflection_001_1.inputs[3], 'hide_value'):
                reflection_001_1.inputs[3].hide_value = False
            if hasattr(reflection_001_1.inputs[3], 'name'):
                reflection_001_1.inputs[3].name = 'Reflection Factor'
            if hasattr(reflection_001_1.inputs[3], 'show_expanded'):
                reflection_001_1.inputs[3].show_expanded = False
            if hasattr(reflection_001_1.inputs[4], 'default_value'):
                reflection_001_1.inputs[4].default_value = (0.0, 0.0, 0.0)
            if hasattr(reflection_001_1.inputs[4], 'display_shape'):
                reflection_001_1.inputs[4].display_shape = 'CIRCLE'
            if hasattr(reflection_001_1.inputs[4], 'enabled'):
                reflection_001_1.inputs[4].enabled = True
            if hasattr(reflection_001_1.inputs[4], 'hide'):
                reflection_001_1.inputs[4].hide = True
            if hasattr(reflection_001_1.inputs[4], 'hide_value'):
                reflection_001_1.inputs[4].hide_value = True
            if hasattr(reflection_001_1.inputs[4], 'name'):
                reflection_001_1.inputs[4].name = 'Normal'
            if hasattr(reflection_001_1.inputs[4], 'show_expanded'):
                reflection_001_1.inputs[4].show_expanded = False
            if hasattr(reflection_001_1.outputs[1], 'default_value'):
                reflection_001_1.outputs[1].default_value = (0.0, 0.0, 0.0, 0.0)
            if hasattr(reflection_001_1.outputs[1], 'display_shape'):
                reflection_001_1.outputs[1].display_shape = 'CIRCLE'
            if hasattr(reflection_001_1.outputs[1], 'enabled'):
                reflection_001_1.outputs[1].enabled = True
            if hasattr(reflection_001_1.outputs[1], 'hide'):
                reflection_001_1.outputs[1].hide = True
            if hasattr(reflection_001_1.outputs[1], 'hide_value'):
                reflection_001_1.outputs[1].hide_value = False
            if hasattr(reflection_001_1.outputs[1], 'name'):
                reflection_001_1.outputs[1].name = 'Color'
            if hasattr(reflection_001_1.outputs[1], 'show_expanded'):
                reflection_001_1.outputs[1].show_expanded = False

            # LINKS
            node_tree1.links.new(layer_weight_1.outputs[0], mix_shader_1.inputs[0])
            node_tree1.links.new(transparent_bsdf_1.outputs[0], mix_shader_001_1.inputs[1])
            node_tree1.links.new(diffuse_bsdf_1.outputs[0], mix_shader_1.inputs[2])
            node_tree1.links.new(color_variation_ver_3_001_1.outputs[0], diffuse_bsdf_1.inputs[0])
            node_tree1.links.new(glossy_bsdf_1.outputs[0], mix_shader_001_1.inputs[2])
            node_tree1.links.new(color_variation_ver_3_001_1.outputs[0], glossy_bsdf_1.inputs[0])
            node_tree1.links.new(micro_roughness_1.outputs[0], math_1.inputs[0])
            node_tree1.links.new(mix_shader_1.outputs[0], reflection_001_1.inputs[0])
            node_tree1.links.new(mix_shader_001_1.outputs[0], mix_shader_1.inputs[1])
            node_tree1.links.new(micro_roughness_1.outputs[0], reflection_001_1.inputs[1])
            node_tree1.links.new(micro_roughness_1.outputs[0], glossy_bsdf_1.inputs[1])
            node_tree1.links.new(math_1.outputs[0], diffuse_bsdf_1.inputs[1])
            node_tree1.links.new(reflection_001_1.outputs[0], group_output_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[0], color_variation_ver_3_001_1.inputs[0])
            node_tree1.links.new(group_input_001_1.outputs[1], transparent_bsdf_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[4], color_variation_ver_3_001_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[5], color_variation_ver_3_001_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[6], color_variation_ver_3_001_1.inputs[3])
            node_tree1.links.new(group_input_1.outputs[7], color_variation_ver_3_001_1.inputs[4])
            node_tree1.links.new(group_input_1.outputs[8], color_variation_ver_3_001_1.inputs[5])
            node_tree1.links.new(group_input_1.outputs[9], color_variation_ver_3_001_1.inputs[6])
            node_tree1.links.new(group_input_1.outputs[10], color_variation_ver_3_001_1.inputs[7])
            node_tree1.links.new(group_input_1.outputs[11], color_variation_ver_3_001_1.inputs[8])
            node_tree1.links.new(group_input_1.outputs[12], color_variation_ver_3_001_1.inputs[9])
            node_tree1.links.new(group_input_1.outputs[13], color_variation_ver_3_001_1.inputs[10])
            node_tree1.links.new(group_input_1.outputs[14], color_variation_ver_3_001_1.inputs[11])
            node_tree1.links.new(group_input_1.outputs[15], color_variation_ver_3_001_1.inputs[12])
            node_tree1.links.new(group_input_1.outputs[16], color_variation_ver_3_001_1.inputs[13])
            node_tree1.links.new(group_input_1.outputs[17], color_variation_ver_3_001_1.inputs[14])
            node_tree1.links.new(group_input_1.outputs[18], color_variation_ver_3_001_1.inputs[15])
            node_tree1.links.new(group_input_1.outputs[19], color_variation_ver_3_001_1.inputs[16])
            node_tree1.links.new(group_input_1.outputs[20], color_variation_ver_3_001_1.inputs[17])
            node_tree1.links.new(group_input_1.outputs[21], color_variation_ver_3_001_1.inputs[18])
            node_tree1.links.new(micro_roughness_1.outputs[0], color_variation_ver_3_001_1.inputs[19])
            node_tree1.links.new(group_input_002_1.outputs[23], micro_roughness_1.inputs[0])
            node_tree1.links.new(group_input_002_1.outputs[24], micro_roughness_1.inputs[2])
            node_tree1.links.new(group_input_003_1.outputs[22], layer_weight_1.inputs[0])
            node_tree1.links.new(group_input_004_1.outputs[2], reflection_001_1.inputs[2])
            node_tree1.links.new(group_input_004_1.outputs[3], reflection_001_1.inputs[3])

        blister_plastic_transparent_sheen__0 = node_tree0.nodes.new('ShaderNodeGroup')
        if hasattr(blister_plastic_transparent_sheen__0, 'node_tree'):
            blister_plastic_transparent_sheen__0.node_tree = bpy.data.node_groups.get('Blister Plastic (Transparent Sheen)')
        if hasattr(blister_plastic_transparent_sheen__0, 'color'):
            blister_plastic_transparent_sheen__0.color = (0.015206839889287949, 0.1274333894252777, 0.18446779251098633)
        if hasattr(blister_plastic_transparent_sheen__0, 'hide'):
            blister_plastic_transparent_sheen__0.hide = False
        if hasattr(blister_plastic_transparent_sheen__0, 'label'):
            blister_plastic_transparent_sheen__0.label = 'Blister Plastic (Transparent Sheen)'
        if hasattr(blister_plastic_transparent_sheen__0, 'location'):
            blister_plastic_transparent_sheen__0.location = (-10.0, 0.0)
        if hasattr(blister_plastic_transparent_sheen__0, 'mute'):
            blister_plastic_transparent_sheen__0.mute = False
        if hasattr(blister_plastic_transparent_sheen__0, 'name'):
            blister_plastic_transparent_sheen__0.name = 'Blister Plastic (Transparent Sheen)'
        if hasattr(blister_plastic_transparent_sheen__0, 'use_custom_color'):
            blister_plastic_transparent_sheen__0.use_custom_color = True
        if hasattr(blister_plastic_transparent_sheen__0, 'width'):
            blister_plastic_transparent_sheen__0.width = 240.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[0], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[0].default_value = (0.9130977988243103, 0.9130979776382446, 0.9130988717079163, 1.0)
        if hasattr(blister_plastic_transparent_sheen__0.inputs[0], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[0].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[0], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[0].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[0], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[0].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[0], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[0].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[0], 'name'):
            blister_plastic_transparent_sheen__0.inputs[0].name = 'Base Color'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[0], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[0].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[1], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[1].default_value = (0.864982545375824, 0.8649828433990479, 0.864983320236206, 1.0)
        if hasattr(blister_plastic_transparent_sheen__0.inputs[1], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[1].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[1], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[1].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[1], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[1].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[1], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[1].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[1], 'name'):
            blister_plastic_transparent_sheen__0.inputs[1].name = 'Transparent Color'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[1], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[1].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[2], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[2].default_value = (0.6181623935699463, 0.6181623935699463, 0.6181638240814209, 1.0)
        if hasattr(blister_plastic_transparent_sheen__0.inputs[2], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[2].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[2], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[2].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[2], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[2].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[2], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[2].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[2], 'name'):
            blister_plastic_transparent_sheen__0.inputs[2].name = 'Reflection Color'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[2], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[2].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[3], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[3].default_value = 0.25
        if hasattr(blister_plastic_transparent_sheen__0.inputs[3], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[3].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[3], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[3].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[3], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[3].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[3], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[3].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[3], 'name'):
            blister_plastic_transparent_sheen__0.inputs[3].name = 'Reflection Factor'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[3], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[3].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[4], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[4].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[4], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[4].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[4], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[4].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[4], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[4].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[4], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[4].hide_value = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[4], 'name'):
            blister_plastic_transparent_sheen__0.inputs[4].name = 'COLOR VARIATION'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[4], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[4].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[5], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[5].default_value = 6.5
        if hasattr(blister_plastic_transparent_sheen__0.inputs[5], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[5].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[5], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[5].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[5], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[5].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[5], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[5].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[5], 'name'):
            blister_plastic_transparent_sheen__0.inputs[5].name = '  Color Variation Scale'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[5], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[5].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[6], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[6].default_value = 0.15000000596046448
        if hasattr(blister_plastic_transparent_sheen__0.inputs[6], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[6].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[6], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[6].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[6], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[6].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[6], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[6].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[6], 'name'):
            blister_plastic_transparent_sheen__0.inputs[6].name = '  Color Variation Distortion'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[6], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[6].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[7], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[7].default_value = 0.7749999761581421
        if hasattr(blister_plastic_transparent_sheen__0.inputs[7], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[7].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[7], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[7].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[7], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[7].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[7], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[7].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[7], 'name'):
            blister_plastic_transparent_sheen__0.inputs[7].name = '  Random Color Var'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[7], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[7].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[8], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[8].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[8], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[8].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[8], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[8].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[8], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[8].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[8], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[8].hide_value = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[8], 'name'):
            blister_plastic_transparent_sheen__0.inputs[8].name = 'COLOR ADJUSTMENTS'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[8], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[8].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[9], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[9].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[9], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[9].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[9], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[9].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[9], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[9].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[9], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[9].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[9], 'name'):
            blister_plastic_transparent_sheen__0.inputs[9].name = '  Unpaint'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[9], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[9].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[10], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[10].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[10], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[10].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[10], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[10].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[10], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[10].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[10], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[10].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[10], 'name'):
            blister_plastic_transparent_sheen__0.inputs[10].name = '  Color Inverter'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[10], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[10].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[11], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[11].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[11], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[11].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[11], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[11].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[11], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[11].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[11], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[11].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[11], 'name'):
            blister_plastic_transparent_sheen__0.inputs[11].name = '  Contrast'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[11], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[11].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[12], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[12].default_value = 1.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[12], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[12].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[12], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[12].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[12], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[12].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[12], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[12].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[12], 'name'):
            blister_plastic_transparent_sheen__0.inputs[12].name = '  Gamma'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[12], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[12].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[13], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[13].default_value = 1.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[13], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[13].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[13], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[13].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[13], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[13].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[13], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[13].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[13], 'name'):
            blister_plastic_transparent_sheen__0.inputs[13].name = '  Hue / Sat Value'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[13], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[13].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[14], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[14].default_value = 0.49999991059303284
        if hasattr(blister_plastic_transparent_sheen__0.inputs[14], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[14].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[14], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[14].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[14], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[14].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[14], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[14].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[14], 'name'):
            blister_plastic_transparent_sheen__0.inputs[14].name = '    Hue'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[14], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[14].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[15], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[15].default_value = 1.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[15], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[15].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[15], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[15].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[15], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[15].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[15], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[15].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[15], 'name'):
            blister_plastic_transparent_sheen__0.inputs[15].name = '    Saturation'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[15], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[15].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[16], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[16].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[16], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[16].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[16], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[16].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[16], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[16].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[16], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[16].hide_value = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[16], 'name'):
            blister_plastic_transparent_sheen__0.inputs[16].name = 'BRIGHTNESS'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[16], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[16].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[17], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[17].default_value = 1.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[17], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[17].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[17], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[17].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[17], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[17].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[17], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[17].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[17], 'name'):
            blister_plastic_transparent_sheen__0.inputs[17].name = '  Glowing Level'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[17], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[17].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[18], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[18].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[18], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[18].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[18], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[18].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[18], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[18].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[18], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[18].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[18], 'name'):
            blister_plastic_transparent_sheen__0.inputs[18].name = '  Brightness'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[18], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[18].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[19], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[19].default_value = 2.5
        if hasattr(blister_plastic_transparent_sheen__0.inputs[19], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[19].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[19], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[19].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[19], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[19].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[19], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[19].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[19], 'name'):
            blister_plastic_transparent_sheen__0.inputs[19].name = '  Dark / Bright Threshold'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[19], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[19].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[20], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[20].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[20], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[20].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[20], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[20].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[20], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[20].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[20], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[20].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[20], 'name'):
            blister_plastic_transparent_sheen__0.inputs[20].name = '    Dark Spot Intensity'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[20], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[20].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[21], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[21].default_value = 0.0
        if hasattr(blister_plastic_transparent_sheen__0.inputs[21], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[21].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[21], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[21].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[21], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[21].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[21], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[21].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[21], 'name'):
            blister_plastic_transparent_sheen__0.inputs[21].name = '    Bright Spot Intensity'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[21], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[21].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[22], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[22].default_value = 0.10000000149011612
        if hasattr(blister_plastic_transparent_sheen__0.inputs[22], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[22].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[22], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[22].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[22], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[22].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[22], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[22].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[22], 'name'):
            blister_plastic_transparent_sheen__0.inputs[22].name = 'Blend'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[22], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[22].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[23], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[23].default_value = 0.47999998927116394
        if hasattr(blister_plastic_transparent_sheen__0.inputs[23], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[23].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[23], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[23].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[23], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[23].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[23], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[23].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[23], 'name'):
            blister_plastic_transparent_sheen__0.inputs[23].name = 'Roughness'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[23], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[23].show_expanded = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[24], 'default_value'):
            blister_plastic_transparent_sheen__0.inputs[24].default_value = 0.125
        if hasattr(blister_plastic_transparent_sheen__0.inputs[24], 'display_shape'):
            blister_plastic_transparent_sheen__0.inputs[24].display_shape = 'CIRCLE'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[24], 'enabled'):
            blister_plastic_transparent_sheen__0.inputs[24].enabled = True
        if hasattr(blister_plastic_transparent_sheen__0.inputs[24], 'hide'):
            blister_plastic_transparent_sheen__0.inputs[24].hide = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[24], 'hide_value'):
            blister_plastic_transparent_sheen__0.inputs[24].hide_value = False
        if hasattr(blister_plastic_transparent_sheen__0.inputs[24], 'name'):
            blister_plastic_transparent_sheen__0.inputs[24].name = 'Falloff Strength'
        if hasattr(blister_plastic_transparent_sheen__0.inputs[24], 'show_expanded'):
            blister_plastic_transparent_sheen__0.inputs[24].show_expanded = False

        # LINKS
        node_tree0.links.new(blister_plastic_transparent_sheen__0.outputs[0], material_output_0.inputs[0])


        return blister_plastic_transparent_sheen_
        # # TO ACTIVE
        # selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
        # for obj in selected_objects:
        #     obj.active_material = blister_plastic_transparent_sheen_
