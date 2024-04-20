from playwright.sync_api import Page
from locators.cookies_modal_locators import COOKIES_MODAL

class CookiesModalPage:

    def __init__(self, page: Page):
        self.page = page

    def accept_cookies(self):
        self.page.click(COOKIES_MODAL['ACCEPT'])
    
    def reject_cookies(self):
        self.page.click(COOKIES_MODAL['REJECT'])