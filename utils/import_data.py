import json


def import_json(path):
    with open(f"{path}.json") as f:
        return json.load(f)
