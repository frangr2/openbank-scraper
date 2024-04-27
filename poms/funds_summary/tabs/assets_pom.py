from playwright.sync_api import Page
from locators.funds_summary_locators import ASSETS_DISTRIBUTION_TAB, SCRAP_TABLE
from utils.dictionaries.ticker import TICKER


class AssetsTab:

    allocation_table = ASSETS_DISTRIBUTION_TAB["ALLOCATION"]
    exposure_table = ASSETS_DISTRIBUTION_TAB["EXPOSURE"]
    holdings_table = ASSETS_DISTRIBUTION_TAB["HOLDINGS"]
    capital_table = ASSETS_DISTRIBUTION_TAB["CAPITAL"]

    def __init__(self, page: Page):
        self.page = page

    def scrap_data(self):
        data = {
            "allocation": self.scrap_allocation(),
            "exposure": self.scrap_exposure(),
            "holdings": self.scrap_holdings(),
            "capital": self.scrap_capital(),
        }
        return data

    def scrap_allocation(self):
        allocations = {
            "variable": 1,
            "fixed": 2,
            "cash": 3,
            "others": 4,
            "unclassified": 5,
        }

        allocation_data = {}

        for key, value in allocations.items():
            allocation_data[key] = self.page.query_selector(
                self.allocation_table + SCRAP_TABLE["VALUE"](value, 3)
            ).inner_text()

        return allocation_data

    def scrap_exposure(self):
        exposure_data = []

        for i in range(5):
            selector_country = self.exposure_table + SCRAP_TABLE["VALUE"](i + 1, 1)
            selector_allocation = self.exposure_table + SCRAP_TABLE["VALUE"](i + 1, 2)

            country = self.page.query_selector(selector_country).inner_text()
            allocation = self.page.query_selector(selector_allocation).inner_text()

            exposure_data.append({"country": country, "allocation": allocation})

        return exposure_data

    def scrap_holdings(self):
        holdings_data = []

        for i in range(5):
            selector_name = self.holdings_table + SCRAP_TABLE["VALUE"](i + 1, 1)
            selector_sector = self.holdings_table + SCRAP_TABLE["VALUE"](i + 1, 2)
            selector_country = self.holdings_table + SCRAP_TABLE["VALUE"](i + 1, 3)
            selector_allocation = self.holdings_table + SCRAP_TABLE["VALUE"](i + 1, 4)

            name = self.page.query_selector(selector_name).inner_text()
            ticker = TICKER.get(name)
            sector = self.page.query_selector(selector_sector).inner_text()
            country = self.page.query_selector(selector_country).inner_text()
            allocation = self.page.query_selector(selector_allocation).inner_text()

            holdings_data.append(
                {
                    "name": name,
                    "ticker": ticker,
                    "sector": sector,
                    "country": country,
                    "allocation": allocation,
                }
            )

        return holdings_data

    def scrap_capital(self):
        capitals = {"giant": 1, "large": 2, "mid": 3, "small": 4}

        capital_data = {}

        for key, value in capitals.items():
            selector = self.capital_table + SCRAP_TABLE["VALUE"](value, 2)
            capital_data[key] = self.page.query_selector(selector).inner_text()

        return capital_data
