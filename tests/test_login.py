import pytest
from pages.login_page import LoginPage

URL = "https://www.saucedemo.com/"

TEST_DATA = [
    ("standard_user", "secret_sauce", "success", "inventory"),
    ("locked_out_user", "secret_sauce", "fail", "Sorry, this user has been locked out"),
    ("problem_user", "secret_sauce", "success", "inventory"),
    ("performance_glitch_user", "secret_sauce", "success", "inventory"),
]

@pytest.mark.parametrize("username, password, status, expected_output", TEST_DATA)
def test_login_scenarios(page, username, password, status, expected_output):
    login = LoginPage(page)
    login.navigate_to(URL)
    
    print(f"🧪 Testing user: {username}")
    login.login(username, password)
    
    if status == "success":
        assert expected_output in page.url, f"User {username} failed to login!"
    else:
        error_msg = login.get_error_message()
        assert expected_output in error_msg, f"Error message mismatch for {username}"