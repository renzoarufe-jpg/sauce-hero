from playwright.sync_api import Page, Locator

class BasePage:
    """wrapper for common playwright methods with added logging or error handling"""
    
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)

    def get_element(self, selector: str) -> Locator:
        return self.page.locator(selector)
    
    def click(self, selector: str):
        self.get_element(selector).click()

    def fill_text(self, selector: str, text: str):
        self.get_element(selector).fill(text)
    
    def get_text(self, selector: str) -> str:
        return self.get_element(selector).inner_text()