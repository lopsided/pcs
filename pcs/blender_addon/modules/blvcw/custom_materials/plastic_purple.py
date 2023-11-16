import bpy

class Material():
    def __init__(self):
        pass
    
    def load():

        # MATERIAL
        plastic_shader = bpy.data.materials.new(name='Plastic Shader')
        plastic_shader.use_nodes = True
        node_tree0 = plastic_shader.node_tree

        for node in node_tree0.nodes:
            node_tree0.nodes.remove(node)
        # NODES
        colorramp_0 = node_tree0.nodes.new('ShaderNodeValToRGB')
        if hasattr(colorramp_0, 'color'):
            colorramp_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(colorramp_0, 'color_ramp'):
            if hasattr(colorramp_0.color_ramp, 'color_mode'):
                colorramp_0.color_ramp.color_mode = 'RGB'
            if hasattr(colorramp_0.color_ramp, 'elements'):
                if 0 >= len(colorramp_0.color_ramp.elements):
                    colorramp_0.color_ramp.elements.new(0.0)
                if hasattr(colorramp_0.color_ramp.elements[0], 'alpha'):
                    colorramp_0.color_ramp.elements[0].alpha = 1.0
                if hasattr(colorramp_0.color_ramp.elements[0], 'color'):
                    colorramp_0.color_ramp.elements[0].color = (1.0, 0.27618643641471863, 0.0, 1.0)
                if hasattr(colorramp_0.color_ramp.elements[0], 'position'):
                    colorramp_0.color_ramp.elements[0].position = 0.0
                if 1 >= len(colorramp_0.color_ramp.elements):
                    colorramp_0.color_ramp.elements.new(1.0)
                if hasattr(colorramp_0.color_ramp.elements[1], 'alpha'):
                    colorramp_0.color_ramp.elements[1].alpha = 1.0
                if hasattr(colorramp_0.color_ramp.elements[1], 'color'):
                    colorramp_0.color_ramp.elements[1].color = (0.008505395613610744, 0.0, 1.0, 1.0)
                if hasattr(colorramp_0.color_ramp.elements[1], 'position'):
                    colorramp_0.color_ramp.elements[1].position = 1.0
            if hasattr(colorramp_0.color_ramp, 'hue_interpolation'):
                colorramp_0.color_ramp.hue_interpolation = 'NEAR'
            if hasattr(colorramp_0.color_ramp, 'interpolation'):
                colorramp_0.color_ramp.interpolation = 'LINEAR'
        if hasattr(colorramp_0, 'hide'):
            colorramp_0.hide = False
        if hasattr(colorramp_0, 'location'):
            colorramp_0.location = (-1655.1617431640625, 33.277099609375)
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

        mapping_0 = node_tree0.nodes.new('ShaderNodeMapping')
        if hasattr(mapping_0, 'color'):
            mapping_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(mapping_0, 'hide'):
            mapping_0.hide = False
        if hasattr(mapping_0, 'location'):
            mapping_0.location = (-1933.5325927734375, 30.773080825805664)
        if hasattr(mapping_0, 'mute'):
            mapping_0.mute = False
        if hasattr(mapping_0, 'name'):
            mapping_0.name = 'Mapping'
        if hasattr(mapping_0, 'use_custom_color'):
            mapping_0.use_custom_color = False
        if hasattr(mapping_0, 'vector_type'):
            mapping_0.vector_type = 'POINT'
        if hasattr(mapping_0, 'width'):
            mapping_0.width = 240.0
        input_ = next((input_ for input_ in mapping_0.inputs if input_.identifier=='Vector'), None)
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
        input_ = next((input_ for input_ in mapping_0.inputs if input_.identifier=='Location'), None)
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
                input_.name = 'Location'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in mapping_0.inputs if input_.identifier=='Rotation'), None)
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
                input_.name = 'Rotation'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        input_ = next((input_ for input_ in mapping_0.inputs if input_.identifier=='Scale'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (1.0, 1.0, 1.0)
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
        output = next((output for output in mapping_0.outputs if output.identifier=='Vector'), None)
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
                output.name = 'Vector'
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
                    colorramp_001_0.color_ramp.elements.new(0.45454561710357666)
                if hasattr(colorramp_001_0.color_ramp.elements[0], 'alpha'):
                    colorramp_001_0.color_ramp.elements[0].alpha = 1.0
                if hasattr(colorramp_001_0.color_ramp.elements[0], 'color'):
                    colorramp_001_0.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
                if hasattr(colorramp_001_0.color_ramp.elements[0], 'position'):
                    colorramp_001_0.color_ramp.elements[0].position = 0.45454561710357666
                if 1 >= len(colorramp_001_0.color_ramp.elements):
                    colorramp_001_0.color_ramp.elements.new(0.5772731900215149)
                if hasattr(colorramp_001_0.color_ramp.elements[1], 'alpha'):
                    colorramp_001_0.color_ramp.elements[1].alpha = 1.0
                if hasattr(colorramp_001_0.color_ramp.elements[1], 'color'):
                    colorramp_001_0.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
                if hasattr(colorramp_001_0.color_ramp.elements[1], 'position'):
                    colorramp_001_0.color_ramp.elements[1].position = 0.5772731900215149
            if hasattr(colorramp_001_0.color_ramp, 'hue_interpolation'):
                colorramp_001_0.color_ramp.hue_interpolation = 'NEAR'
            if hasattr(colorramp_001_0.color_ramp, 'interpolation'):
                colorramp_001_0.color_ramp.interpolation = 'LINEAR'
        if hasattr(colorramp_001_0, 'hide'):
            colorramp_001_0.hide = False
        if hasattr(colorramp_001_0, 'location'):
            colorramp_001_0.location = (-2216.451416015625, 27.62938117980957)
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

        geometry_0 = node_tree0.nodes.new('ShaderNodeNewGeometry')
        if hasattr(geometry_0, 'color'):
            geometry_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(geometry_0, 'hide'):
            geometry_0.hide = False
        if hasattr(geometry_0, 'location'):
            geometry_0.location = (-2384.55078125, 30.44498634338379)
        if hasattr(geometry_0, 'mute'):
            geometry_0.mute = False
        if hasattr(geometry_0, 'name'):
            geometry_0.name = 'Geometry'
        if hasattr(geometry_0, 'use_custom_color'):
            geometry_0.use_custom_color = False
        if hasattr(geometry_0, 'width'):
            geometry_0.width = 140.0
        output = next((output for output in geometry_0.outputs if output.identifier=='Position'), None)
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
        output = next((output for output in geometry_0.outputs if output.identifier=='Normal'), None)
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
        output = next((output for output in geometry_0.outputs if output.identifier=='Tangent'), None)
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
        output = next((output for output in geometry_0.outputs if output.identifier=='True Normal'), None)
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
        output = next((output for output in geometry_0.outputs if output.identifier=='Incoming'), None)
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
        output = next((output for output in geometry_0.outputs if output.identifier=='Parametric'), None)
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
        output = next((output for output in geometry_0.outputs if output.identifier=='Backfacing'), None)
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
        output = next((output for output in geometry_0.outputs if output.identifier=='Pointiness'), None)
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
        output = next((output for output in geometry_0.outputs if output.identifier=='Random Per Island'), None)
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

        math_0 = node_tree0.nodes.new('ShaderNodeMath')
        if hasattr(math_0, 'color'):
            math_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(math_0, 'hide'):
            math_0.hide = False
        if hasattr(math_0, 'location'):
            math_0.location = (-2085.400390625, 415.70458984375)
        if hasattr(math_0, 'mute'):
            math_0.mute = False
        if hasattr(math_0, 'name'):
            math_0.name = 'Math'
        if hasattr(math_0, 'operation'):
            math_0.operation = 'ADD'
        if hasattr(math_0, 'use_clamp'):
            math_0.use_clamp = False
        if hasattr(math_0, 'use_custom_color'):
            math_0.use_custom_color = False
        if hasattr(math_0, 'width'):
            math_0.width = 140.0
        input_ = next((input_ for input_ in math_0.inputs if input_.identifier=='Value'), None)
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
        input_ = next((input_ for input_ in math_0.inputs if input_.identifier=='Value_001'), None)
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
        input_ = next((input_ for input_ in math_0.inputs if input_.identifier=='Value_002'), None)
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
                input_.name = 'Value'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in math_0.outputs if output.identifier=='Value'), None)
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

        math_001_0 = node_tree0.nodes.new('ShaderNodeMath')
        if hasattr(math_001_0, 'color'):
            math_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(math_001_0, 'hide'):
            math_001_0.hide = False
        if hasattr(math_001_0, 'location'):
            math_001_0.location = (-1865.4002685546875, 435.70458984375)
        if hasattr(math_001_0, 'mute'):
            math_001_0.mute = False
        if hasattr(math_001_0, 'name'):
            math_001_0.name = 'Math.001'
        if hasattr(math_001_0, 'operation'):
            math_001_0.operation = 'ADD'
        if hasattr(math_001_0, 'use_clamp'):
            math_001_0.use_clamp = False
        if hasattr(math_001_0, 'use_custom_color'):
            math_001_0.use_custom_color = False
        if hasattr(math_001_0, 'width'):
            math_001_0.width = 140.0
        input_ = next((input_ for input_ in math_001_0.inputs if input_.identifier=='Value'), None)
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
        input_ = next((input_ for input_ in math_001_0.inputs if input_.identifier=='Value_001'), None)
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
        input_ = next((input_ for input_ in math_001_0.inputs if input_.identifier=='Value_002'), None)
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
                input_.name = 'Value'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in math_001_0.outputs if output.identifier=='Value'), None)
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

        light_path_0 = node_tree0.nodes.new('ShaderNodeLightPath')
        if hasattr(light_path_0, 'color'):
            light_path_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(light_path_0, 'hide'):
            light_path_0.hide = False
        if hasattr(light_path_0, 'location'):
            light_path_0.location = (-2365.400390625, 455.70458984375)
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

        math_003_0 = node_tree0.nodes.new('ShaderNodeMath')
        if hasattr(math_003_0, 'color'):
            math_003_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(math_003_0, 'hide'):
            math_003_0.hide = False
        if hasattr(math_003_0, 'location'):
            math_003_0.location = (-2085.400390625, 255.70458984375)
        if hasattr(math_003_0, 'mute'):
            math_003_0.mute = False
        if hasattr(math_003_0, 'name'):
            math_003_0.name = 'Math.003'
        if hasattr(math_003_0, 'operation'):
            math_003_0.operation = 'MAXIMUM'
        if hasattr(math_003_0, 'use_clamp'):
            math_003_0.use_clamp = False
        if hasattr(math_003_0, 'use_custom_color'):
            math_003_0.use_custom_color = False
        if hasattr(math_003_0, 'width'):
            math_003_0.width = 140.0
        input_ = next((input_ for input_ in math_003_0.inputs if input_.identifier=='Value'), None)
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
        input_ = next((input_ for input_ in math_003_0.inputs if input_.identifier=='Value_001'), None)
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
        input_ = next((input_ for input_ in math_003_0.inputs if input_.identifier=='Value_002'), None)
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
                input_.name = 'Value'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in math_003_0.outputs if output.identifier=='Value'), None)
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

        math_002_0 = node_tree0.nodes.new('ShaderNodeMath')
        if hasattr(math_002_0, 'color'):
            math_002_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(math_002_0, 'hide'):
            math_002_0.hide = False
        if hasattr(math_002_0, 'location'):
            math_002_0.location = (-1865.4002685546875, 235.70458984375)
        if hasattr(math_002_0, 'mute'):
            math_002_0.mute = False
        if hasattr(math_002_0, 'name'):
            math_002_0.name = 'Math.002'
        if hasattr(math_002_0, 'operation'):
            math_002_0.operation = 'MULTIPLY'
        if hasattr(math_002_0, 'use_clamp'):
            math_002_0.use_clamp = False
        if hasattr(math_002_0, 'use_custom_color'):
            math_002_0.use_custom_color = False
        if hasattr(math_002_0, 'width'):
            math_002_0.width = 140.0
        input_ = next((input_ for input_ in math_002_0.inputs if input_.identifier=='Value'), None)
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
        input_ = next((input_ for input_ in math_002_0.inputs if input_.identifier=='Value_001'), None)
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
        input_ = next((input_ for input_ in math_002_0.inputs if input_.identifier=='Value_002'), None)
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
                input_.name = 'Value'
            if hasattr(input_, 'show_expanded'):
                input_.show_expanded = False
        output = next((output for output in math_002_0.outputs if output.identifier=='Value'), None)
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

        transparent_bsdf_0 = node_tree0.nodes.new('ShaderNodeBsdfTransparent')
        if hasattr(transparent_bsdf_0, 'color'):
            transparent_bsdf_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(transparent_bsdf_0, 'hide'):
            transparent_bsdf_0.hide = False
        if hasattr(transparent_bsdf_0, 'location'):
            transparent_bsdf_0.location = (-1252.1143798828125, 126.01356506347656)
        if hasattr(transparent_bsdf_0, 'mute'):
            transparent_bsdf_0.mute = False
        if hasattr(transparent_bsdf_0, 'name'):
            transparent_bsdf_0.name = 'Transparent BSDF'
        if hasattr(transparent_bsdf_0, 'use_custom_color'):
            transparent_bsdf_0.use_custom_color = False
        if hasattr(transparent_bsdf_0, 'width'):
            transparent_bsdf_0.width = 140.0
        input_ = next((input_ for input_ in transparent_bsdf_0.inputs if input_.identifier=='Color'), None)
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
        input_ = next((input_ for input_ in transparent_bsdf_0.inputs if input_.identifier=='Weight'), None)
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

        glass_bsdf_0 = node_tree0.nodes.new('ShaderNodeBsdfGlass')
        if hasattr(glass_bsdf_0, 'color'):
            glass_bsdf_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(glass_bsdf_0, 'distribution'):
            glass_bsdf_0.distribution = 'GGX'
        if hasattr(glass_bsdf_0, 'hide'):
            glass_bsdf_0.hide = False
        if hasattr(glass_bsdf_0, 'location'):
            glass_bsdf_0.location = (-1252.1143798828125, 306.0135498046875)
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
                input_.default_value = 0.2846153974533081
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
                input_.default_value = 1.1500000953674316
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
            mix_shader_0.location = (-972.7406005859375, 236.24526977539062)
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
            add_shader_0.location = (-752.1144409179688, 242.93020629882812)
        if hasattr(add_shader_0, 'mute'):
            add_shader_0.mute = False
        if hasattr(add_shader_0, 'name'):
            add_shader_0.name = 'Add Shader'
        if hasattr(add_shader_0, 'use_custom_color'):
            add_shader_0.use_custom_color = False
        if hasattr(add_shader_0, 'width'):
            add_shader_0.width = 140.0

        glossy_bsdf_0 = node_tree0.nodes.new('ShaderNodeBsdfGlossy')
        if hasattr(glossy_bsdf_0, 'color'):
            glossy_bsdf_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(glossy_bsdf_0, 'distribution'):
            glossy_bsdf_0.distribution = 'BECKMANN'
        if hasattr(glossy_bsdf_0, 'hide'):
            glossy_bsdf_0.hide = False
        if hasattr(glossy_bsdf_0, 'location'):
            glossy_bsdf_0.location = (-1251.5650634765625, 42.1640625)
        if hasattr(glossy_bsdf_0, 'mute'):
            glossy_bsdf_0.mute = False
        if hasattr(glossy_bsdf_0, 'name'):
            glossy_bsdf_0.name = 'Glossy BSDF'
        if hasattr(glossy_bsdf_0, 'use_custom_color'):
            glossy_bsdf_0.use_custom_color = False
        if hasattr(glossy_bsdf_0, 'width'):
            glossy_bsdf_0.width = 150.0
        input_ = next((input_ for input_ in glossy_bsdf_0.inputs if input_.identifier=='Color'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = (0.8000000715255737, 0.5271148681640625, 0.0, 1.0)
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
        input_ = next((input_ for input_ in glossy_bsdf_0.inputs if input_.identifier=='Roughness'), None)
        if input_:
            if hasattr(input_, 'default_value'):
                input_.default_value = 0.06923073530197144
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
        input_ = next((input_ for input_ in glossy_bsdf_0.inputs if input_.identifier=='Normal'), None)
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
        input_ = next((input_ for input_ in glossy_bsdf_0.inputs if input_.identifier=='Weight'), None)
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

        material_output_0 = node_tree0.nodes.new('ShaderNodeOutputMaterial')
        if hasattr(material_output_0, 'color'):
            material_output_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        if hasattr(material_output_0, 'hide'):
            material_output_0.hide = False
        if hasattr(material_output_0, 'is_active_output'):
            material_output_0.is_active_output = True
        if hasattr(material_output_0, 'location'):
            material_output_0.location = (-567.20361328125, 286.0198974609375)
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
        node_tree0.links.new(glass_bsdf_0.outputs[0], mix_shader_0.inputs[1])
        node_tree0.links.new(transparent_bsdf_0.outputs[0], mix_shader_0.inputs[2])
        node_tree0.links.new(light_path_0.outputs[1], math_0.inputs[0])
        node_tree0.links.new(light_path_0.outputs[2], math_0.inputs[1])
        node_tree0.links.new(light_path_0.outputs[3], math_001_0.inputs[1])
        node_tree0.links.new(math_0.outputs[0], math_001_0.inputs[0])
        node_tree0.links.new(math_001_0.outputs[0], math_002_0.inputs[0])
        node_tree0.links.new(math_002_0.outputs[0], mix_shader_0.inputs[0])
        node_tree0.links.new(math_003_0.outputs[0], math_002_0.inputs[1])
        node_tree0.links.new(light_path_0.outputs[1], math_003_0.inputs[0])
        node_tree0.links.new(light_path_0.outputs[5], math_003_0.inputs[1])
        node_tree0.links.new(mapping_0.outputs[0], colorramp_0.inputs[0])
        node_tree0.links.new(mix_shader_0.outputs[0], add_shader_0.inputs[0])
        node_tree0.links.new(colorramp_0.outputs[0], transparent_bsdf_0.inputs[0])
        node_tree0.links.new(colorramp_0.outputs[0], glass_bsdf_0.inputs[0])
        node_tree0.links.new(geometry_0.outputs[7], colorramp_001_0.inputs[0])
        node_tree0.links.new(colorramp_001_0.outputs[0], mapping_0.inputs[0])
        node_tree0.links.new(add_shader_0.outputs[0], material_output_0.inputs[0])
        node_tree0.links.new(glossy_bsdf_0.outputs[0], add_shader_0.inputs[1])
        node_tree0.links.new(colorramp_0.outputs[0], glossy_bsdf_0.inputs[0])

        # # TO ACTIVE
        # selected_objects = (obj for obj in bpy.data.objects if obj.select_get())
        # for obj in selected_objects:
        #     obj.active_material = plastic_shader

        return plastic_shader