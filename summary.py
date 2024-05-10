import matplotlib.pyplot as plt
from portfolio import PORTFOLIO
from utils import import_from_json

# Calcular el total invertido en la cartera
if sum(PORTFOLIO.values()) != 100:
    raise Exception("Portfolio is not correctly balanced")


aggregate_exposure = {}
aggregate_holdings = {}
aggregate_capital = {"giant": 0, "large": 0, "mid": 0, "small": 0, "micro": 0}
aggregate_allocation = {
    "variable": 0,
    "fixed": 0,
    "cash": 0,
    "others": 0,
    "unclassified": 0,
}
# For each fund in the portfolio
for isin, amount in PORTFOLIO.items():
    if amount != 0:
        # Load data from the corresponding JSON file
        data = import_from_json(f"funds/{isin}")
        balanced_amount = amount / 100

        # Aggregate exposure
        allocation_total = 0
        for exposure_data in data["assets_distribution"]["exposure"]:
            country = exposure_data["country"]
            allocation = (
                float(exposure_data["allocation"].replace("%", "").replace(",", "."))
                * balanced_amount
            )
            if country in aggregate_exposure:
                aggregate_exposure[country] += allocation
            else:
                aggregate_exposure[country] = allocation

        # Aggregate holdings
        for holding_data in data["assets_distribution"]["holdings"]:
            ticker = holding_data["ticker"]
            allocation = (
                float(holding_data["allocation"].replace("%", "").replace(",", "."))
                * balanced_amount
            )
            if ticker in aggregate_holdings:
                aggregate_holdings[ticker] += allocation
            else:
                aggregate_holdings[ticker] = allocation

        # Aggregate capital
        for key, value in data["assets_distribution"]["capital"].items():
            aggregate_capital[key] += (
                float(value.replace("%", "").replace(",", ".")) * balanced_amount
            )

        # Aggregate allocation
        for key, value in data["assets_distribution"]["allocation"].items():
            aggregate_allocation[key] += (
                float(value.replace("%", "").replace(",", ".")) * balanced_amount
            )

# Plot aggregate exposure
plt.figure(figsize=(10, 6))
# Sort aggregate exposure by value (descending order)
sorted_aggregate_exposure = dict(
    sorted(aggregate_exposure.items(), key=lambda item: item[1], reverse=True)
)
sorted_aggregate_holdings = dict(
    sorted(aggregate_holdings.items(), key=lambda item: item[1], reverse=True)
)
plt.bar(sorted_aggregate_exposure.keys(), sorted_aggregate_exposure.values())
plt.title("Aggregate Portfolio Exposure by Country")
plt.xlabel("Country")
plt.ylabel("Ponderation (%)")
plt.xticks(rotation=45, ha="right")
plt.savefig("portfolio/graphics/aggregate_exposure.png")

# Plot aggregate holdings
plt.figure(figsize=(12, 8))
plt.bar(sorted_aggregate_holdings.keys(), sorted_aggregate_holdings.values())
plt.title("Aggregate Portfolio Holdings")
plt.xlabel("Ponderation (%)")
plt.ylabel("Holdings")
plt.xticks(rotation=45, ha="right")
plt.savefig("portfolio/graphics/aggregate_holdings.png")

# Plot aggregate capital
plt.figure(figsize=(8, 6))
plt.pie(aggregate_capital.values(), labels=aggregate_capital.keys(), autopct="%1.1f%%")
plt.title("Aggregate Portfolio Capital")
plt.savefig("portfolio/graphics/aggregate_capital.png")

# Plot the aggregate allocation
plt.figure(figsize=(8, 6))
plt.bar(aggregate_allocation.keys(), aggregate_allocation.values())
plt.title("Aggregate Portfolio Allocation")
# plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.savefig("portfolio/graphics/aggregate_allocation.png")

# Show the chart
# plt.show()
