# script for loading custom materials into crystal well

import importlib


def material_loader(custom_material="plastic"):
    custom_material = custom_material
    print("Loading custom_material:", custom_material)
    try:
        material = importlib.import_module("." + custom_material, package="blvcw.custom_materials")
    except Exception:
        print(f'Failed to load material: {e}')
    return material.Material
