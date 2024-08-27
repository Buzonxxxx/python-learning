import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from seleniumPytest.pages.login_page import LoginPage

def test_valid_login(driver, config):
    login_page = LoginPage(driver)
    login_page.login(
        config['CREDENTIALS']['valid_username'],
        config['CREDENTIALS']['valid_password']
    )
    assert "Welcome to the Secure Area. When you are done click logout below." in driver.page_source
    

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("invalid@example.com", "wrongpassword")
    assert "Your username is invalid!" in login_page.get_error_message()

@pytest.mark.parametrize("username,password,expected_error", [
    ("", "password123", "Your username is invalid!"),
    ("user@example.com", "", "Your username is invalid!"),
    ("invalid@example.com", "wrongpass", "Your username is invalid!")
])
def test_login_errors(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()
