from playwright.sync_api import Page
from locators.funds_summary_locators import ASSETS_DISTRIBUTION_TAB, SCRAP_TABLE
from utils.dictionaries.ticker import TICKER

class AssetsTab:

    allocation_table = ASSETS_DISTRIBUTION_TAB['ALLOCATION']
    exposure_table = ASSETS_DISTRIBUTION_TAB['EXPOSURE']
    holdings_table = ASSETS_DISTRIBUTION_TAB['HOLDINGS']
    capital_table = ASSETS_DISTRIBUTION_TAB['CAPITAL']

    def __init__(self, page: Page):
        self.page = page

    def scrap_data(self):
        data = {}
        data["allocation"] = self.scrap_allocation()
        data["exposure"] = self.scrap_exposure()
        data["holdings"] = self.scrap_holdings()
        data["capital"] = self.scrap_capital()
        return data
    
    def scrap_allocation(self):
        allocation = {
            "variable": 1,
            "fixed": 2,
            "cash": 3,
            "others": 4,
            "unclassified": 5}
        
        for key, value in allocation.items():
            allocation[key] = self.page.query_selector(self.allocation_table + SCRAP_TABLE['VALUE'](value, 3)).inner_text()
        
        return allocation

    def scrap_exposure(self):
        exposure = []
        
        for i in range(5):
            item = {}
            item["country"] = self.page.query_selector(self.exposure_table + SCRAP_TABLE['VALUE'](i+1, 1)).inner_text()
            item["allocation"] = self.page.query_selector(self.exposure_table + SCRAP_TABLE['VALUE'](i+1, 2)).inner_text()
            exposure.append(item)

        return exposure
    
    def scrap_holdings(self):
        holdings = []
        
        for i in range(5):
            item = {}
            item["name"] = self.page.query_selector(self.holdings_table + SCRAP_TABLE['VALUE'](i+1, 1)).inner_text()
            item["ticker"] = TICKER.get(item["name"])
            item["sector"] = self.page.query_selector(self.holdings_table + SCRAP_TABLE['VALUE'](i+1, 2)).inner_text()
            item["country"] = self.page.query_selector(self.holdings_table + SCRAP_TABLE['VALUE'](i+1, 3)).inner_text()
            item["allocation"] = self.page.query_selector(self.holdings_table + SCRAP_TABLE['VALUE'](i+1, 4)).inner_text()
            holdings.append(item)

        return holdings
    
    def scrap_capital(self):
        capital = {
            "giant": 1,
            "large": 2,
            "mid": 3,
            "small": 4
        }
        
        for key, value in capital.items():
            # print(f"{capital[key]}: {value}")
            capital[key] = self.page.query_selector(self.capital_table + SCRAP_TABLE['VALUE'](value, 2)).inner_text()
        
        return capital
        
