# script for loading custom materials into crystal well

import importlib
# from . import default

def material_loader(custom_material="default"):
    custom_material = custom_material
    print("Custom_material",custom_material)
    # try:
    material = importlib.import_module("." + custom_material,package="blvcw.custom_materials")
    # except Exception as e:
    #     print(f'Could not load material, does not exist: {custom_material}')
    return material.Material  
    