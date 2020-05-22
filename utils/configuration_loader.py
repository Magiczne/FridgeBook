import json


def load_configuration(file: str):
    with open(file) as f:
        return json.load(f)
