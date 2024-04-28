import json
import matplotlib.pyplot as plt
from portfolio.portfolio import PORTFOLIO


# Cargar datos desde el archivo JSON
def load_data(isin):
    with open(f"funds/{isin}.json") as f:
        return json.load(f)


# Calcular el total invertido en la cartera
total_invested = sum(PORTFOLIO.values())


# Function to calculate weights
def calculate_weight(amount):
    return amount / total_invested


# Calculate portfolio weights
weights = {isin: calculate_weight(amount) for isin, amount in PORTFOLIO.items()}
print(f"{weights}")


# Function to calculate weights for holdings
def calculate_holdings_weight(amount, total_fund):
    return amount / total_fund


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
        data = load_data(isin)

        # Aggregate exposure
        allocation_total = 0
        for exposure_data in data["assets_distribution"]["exposure"]:
            country = exposure_data["country"]
            allocation = (
                float(exposure_data["allocation"].replace("%", "").replace(",", "."))
                * weights[isin]
            )
            if country in aggregate_exposure:
                aggregate_exposure[country] += allocation
            else:
                aggregate_exposure[country] = allocation
            allocation_total += allocation / weights[isin]
        print(f"ISIN: {isin}, Allocation: {allocation_total}")

        # Aggregate holdings
        for holding_data in data["assets_distribution"]["holdings"]:
            country = holding_data["country"]
            allocation = (
                float(holding_data["allocation"].replace("%", "").replace(",", "."))
                * weights[isin]
            )
            if country in aggregate_holdings:
                aggregate_holdings[country] += allocation
            else:
                aggregate_holdings[country] = allocation

        # Aggregate capital
        # for key, value in data['assets_distribution']['capital'].items():
        #     aggregate_capital[key] += float(value.replace("%", "").replace(",", ".")) * weights[isin]

        # Aggregate allocation
        for key, value in data["assets_distribution"]["allocation"].items():
            aggregate_allocation[key] += (
                float(value.replace("%", "").replace(",", ".")) * weights[isin]
            )

print(f"{sum(aggregate_exposure.values())}")
print(f"{sum(aggregate_holdings.values())}")
print(f"{sum(aggregate_capital.values())}")
print(f"{sum(aggregate_allocation.values())}")
print(f"{aggregate_exposure}")
print(f"{aggregate_holdings}")
# print(f"{aggregate_capital}")
print(f"{aggregate_allocation}")

# Plot aggregate exposure
plt.figure(figsize=(10, 6))
# Sort aggregate exposure by value (descending order)
sorted_aggregate_exposure = dict(
    sorted(aggregate_exposure.items(), key=lambda item: item[1], reverse=True)
)
plt.bar(sorted_aggregate_exposure.keys(), sorted_aggregate_exposure.values())
plt.title("Aggregate Portfolio Exposure by Country")
plt.xlabel("Country")
plt.ylabel("Ponderation (%)")
plt.xticks(rotation=45, ha="right")
plt.savefig("portfolio/aggregate_exposure.png")

# Plot aggregate holdings
# plt.figure(figsize=(12, 8))
# plt.barh(aggregate_holdings.keys(), aggregate_holdings.values())
# plt.title('Aggregate Portfolio Holdings')
# plt.xlabel('Ponderation (%)')
# plt.ylabel('Holdings')
# plt.savefig('portfolio/aggregate_holdings.png')

# Plot aggregate capital
# plt.figure(figsize=(8, 6))
# plt.pie(aggregate_capital.values(), labels=aggregate_capital.keys(), autopct='%1.1f%%')
# plt.title('Aggregate Portfolio Capital')
# plt.savefig('portfolio/aggregate_capital.png')

# Plot the aggregate allocation
plt.figure(figsize=(8, 6))
plt.bar(aggregate_allocation.keys(), aggregate_allocation.values())
plt.title("Aggregate Portfolio Allocation")
# plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.savefig("portfolio/aggregate_allocation.png")

# Show the chart
# plt.show()
