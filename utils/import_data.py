import json


def import_from_json(path):
    with open(f"{path}.json") as f:
        return json.load(f)
