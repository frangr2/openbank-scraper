import json


def load_json_data(path):
    with open(f"{path}.json") as f:
        return json.load(f)
