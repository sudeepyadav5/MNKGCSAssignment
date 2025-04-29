import time

import pytest
from selenium import webdriver
import json
import os


@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.json")
    with open(config_path) as f:
        return json.load(f)


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    yield driver
    time.sleep(5)
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs['driver']
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)