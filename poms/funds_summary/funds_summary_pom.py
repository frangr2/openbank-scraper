from datetime import datetime
from playwright.sync_api import Page
from locators.funds_summary_locators import FUNDS_SUMMARY
from poms.funds_summary.tabs.assets_pom import AssetsTab
from poms.funds_summary.tabs.commissions_pom import CommissionsTab
from poms.funds_summary.tabs.generic_info_pom import GenericInfoTab
from poms.funds_summary.tabs.profitability_pom import ProfitabilatyTab


class FundsInfoPage:

    def __init__(self, page: Page):
        self.page = page

    def open_tab(self, tab: str):
        self.page.click(FUNDS_SUMMARY[tab])

    def scrap_data(self, isin: str):
        data = {
            "isin": isin,
            "assets_distribution": self.scrap_assets_distribution(),
            "updated_at": datetime.now().strftime("%d/%m/%Y"),
        }
        return data

    # def scrap_generic_info(self):
    #     self.open_tab("GENERIC_INFO_TAB")
    #     generic_info = GenericInfoTab(self.page)
    #     generic_info.scrap_data()

    def scrap_assets_distribution(self):
        self.open_tab("ASSETS_DISTRIBUTION_TAB")
        assets_tab = AssetsTab(self.page)
        data = assets_tab.scrap_data()
        return data

    def scrap_profitability(self):
        self.open_tab("PROFITABILITY_TAB")
        profitability_tab = ProfitabilatyTab(self.page)
        profitability_tab.scrap_data()

    def scrap_commissions(self):
        self.open_tab("COMMISSIONS_TAB")
        commissions_tab = CommissionsTab(self.page)
        commissions_tab.scrap_data()
