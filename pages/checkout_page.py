from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BTN = "#checkout"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP_CODE = "#postal-code"
    CONTINUE_BTN = "#continue"
    FINISH_BTN = "#finish"
    SUCCESS_MSG = ".complete-header"

    def start_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def fill_info(self, first_name, last_name, zip_code):
        self.fill_text(self.FIRST_NAME, first_name)
        self.fill_text(self.LAST_NAME, last_name)
        self.fill_text(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def finish_purchase(self):
        self.click(self.FINISH_BTN)
    
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)