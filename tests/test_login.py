from pages.login_page import LoginPage
import pytest


# @pytest.fixture
def test_valid_login(driver, config):
    driver.get(config["url"])
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])
    assert login_page.is_logged_in().is_displayed(), "Login Failed!"


