import yaml
import os

def read_config(path_to_yaml : str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content
