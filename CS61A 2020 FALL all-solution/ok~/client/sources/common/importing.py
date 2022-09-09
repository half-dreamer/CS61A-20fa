import importlib
import os

def load_module(filepath):
    module_name = path_to_module_string(filepath)
    return importlib.import_module(module_name)

def path_to_module_string(filepath):
    filepath = filepath.replace('.py', '')
    module_components = []
    while filepath:
        filepath, component = os.path.split(filepath)
        module_components.insert(0, component)
    return '.'.join(module_components)
