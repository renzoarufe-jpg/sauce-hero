import pytest
from pages.login_page import LoginPage

URL = "https://www.saucedemo.com/"
USER = "standard_user"
PASS = "secret_sauce"

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate_to(URL)
    
    login.login(USER, PASS)
    
    assert "inventory" in page.url, "Login failed: Not redirected to inventory"

def test_locked_out_user(page):
    login = LoginPage(page)
    login.navigate_to(URL)

    login.login("locked_out_user", PASS)
    
    error = login.get_error_message()
    assert "Sorry, this user has been locked out" in error