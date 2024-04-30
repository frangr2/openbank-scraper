import json
from portfolio import PORTFOLIO
from utils.dictionaries import TICKER
from utils.load_data import load_json_data

ticker = TICKER

for isin in PORTFOLIO.keys():
    # Load data from the corresponding JSON file
    data = load_json_data(f"funds/{isin}")

    # Aggregate holdings
    i = 0
    for holding_data in data["assets_distribution"]["holdings"]:
        name = holding_data["name"]
        if name not in TICKER:
            ticker[name] = "unknown"
            data["assets_distribution"]["holdings"][i]["ticker"] = "unknown"
        else:
            data["assets_distribution"]["holdings"][i]["ticker"] = ticker[name]
        i += 1
    with open(f"funds/{isin}.json", "w") as f:
        json.dump(data, f, indent=4)

with open("utils/dictionaries/ticker.py", "w") as f:
    f.write("TICKER = " + str(ticker))
