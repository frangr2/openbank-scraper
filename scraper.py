from playwright.sync_api import sync_playwright
from poms.cookies.cookies_modal_pom import CookiesModalPage
from poms.funds_summary.funds_summary_pom import FundsInfoPage
import json


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


def export_to_json(isin: str, data):
    with open(f"{isin}.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    scraped_data = scrape_index_fund_data("LU0996179007")
    export_to_json("LU0996179007", scraped_data)
