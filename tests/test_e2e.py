from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage # <--- Import nuevo

URL = "https://www.saucedemo.com/"
USER = "standard_user"
PASS = "secret_sauce"

def test_full_purchase_flow(page):
    login = LoginPage(page)
    login.navigate_to(URL)
    login.login(USER, PASS)
    
    inventory = InventoryPage(page)
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Bike Light")
    inventory.go_to_cart()
    
    checkout = CheckoutPage(page)
    checkout.start_checkout()
    
    print("📝 Filling shipping info...")
    checkout.fill_info("Renzo", "Arufe", "3360") 
    
    print("💳 Completing purchase...")
    checkout.finish_purchase()
    
    success_msg = checkout.get_success_message()
    print(f"🎉 Result: {success_msg}")
    
    assert "Thank you for your order!" in success_msg