from playwright.sync_api import sync_playwright
from poms import CookiesModalPage, FundsInfoPage
from funds.isin_collection import ISIN_COLLECTION
from utils import export_to_json


def scrape_index_fund_data(isin: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(
            f"https://www.openbank.es/fund/{isin}"
        )  # Cambia la URL por la página que quieras scrapear

        cookies_modal_page = CookiesModalPage(page)
        cookies_modal_page.reject_cookies()
        cookies_modal_page.page.wait_for_timeout(3000)

        funds_info_page = FundsInfoPage(page)
        data = funds_info_page.scrap_data(isin)
        funds_info_page.page.wait_for_timeout(3000)

        browser.close()

        return data


if __name__ == "__main__":

    for isin in ISIN_COLLECTION:
        scraped_data = scrape_index_fund_data(isin)
        export_to_json(f"funds/{isin}.json", scraped_data)
