from playwright.sync_api import Page
from locators.funds_summary_locators import ASSETS_DISTRIBUTION_TAB, SCRAP_TABLE

class AssetsTab:

    def __init__(self, page: Page):
        self.page = page

    def scrap_data(self):
        # print(f"{ASSETS_DISTRIBUTION_TAB['EXPOSURE']}")
        print(f"{ASSETS_DISTRIBUTION_TAB['ALLOCATION'] + SCRAP_TABLE['KEY'](1)}")
        print(f"Hola: {self.page.query_selector(ASSETS_DISTRIBUTION_TAB['ALLOCATION'] + SCRAP_TABLE['KEY'](3)).inner_text()}")
        data = self.page.query_selector(ASSETS_DISTRIBUTION_TAB['ALLOCATION'] + SCRAP_TABLE['KEY'](3)).inner_text()
        return data