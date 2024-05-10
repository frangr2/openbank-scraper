import json
import subprocess
from portfolio import PORTFOLIO
from utils.dictionaries import TICKER
from utils.import_data import import_from_json


def update_ticker_and_write_data(data, isin):
    """
    Update ticker information for holdings in the given data and write the updated data to a JSON file.
    """
    holdings = data["assets_distribution"]["holdings"]
    for holding_data in holdings:
        name = holding_data["name"]
        holding_data["ticker"] = TICKER.get(name, "unknown")
        if name not in TICKER:
            TICKER[name] = "unknown"
    with open(f"funds/{isin}.json", "w") as f:
        json.dump(data, f, indent=4)


def update_ticker_file(ticker):
    """
    Update the TICKER dictionary in the ticker.py file.
    """
    with open("utils/dictionaries/ticker.py", "w") as f:
        f.write(f"TICKER = {ticker}")


def run_black_on_file(file_path):
    """
    Run Black formatter on the given file.
    """
    try:
        subprocess.run(["black", file_path], check=True)
        print("Black se ha ejecutado correctamente.")
    except subprocess.CalledProcessError as e:
        print("Ha ocurrido un error al ejecutar Black:", e)


if __name__ == "__main__":
    for isin, data in PORTFOLIO.items():
        fund_data = import_from_json(f"funds/{isin}")
        update_ticker_and_write_data(fund_data, isin)

    update_ticker_file(TICKER)
    run_black_on_file("utils/dictionaries/ticker.py")
