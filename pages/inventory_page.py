from pages.base_page import BasePage

class InventoryPage(BasePage):
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    page_title = ".title"

    def add_to_cart(self, item_name):
        item_slug = item_name.lower().replace(" ", "-")
        selector = f"#add-to-cart-{item_slug}"
        
        self.click(selector)

    def get_cart_count(self):
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)