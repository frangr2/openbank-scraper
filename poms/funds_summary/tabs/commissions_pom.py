from playwright.sync_api import Page

class CommissionsTab:

    def __init__(self, page: Page):
        self.page = page

    def scrap_data(self):
        return