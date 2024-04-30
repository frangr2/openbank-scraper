import json


def export_to_json(path: str, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
