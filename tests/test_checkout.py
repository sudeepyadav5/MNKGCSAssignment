from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


def test_checkout(driver, config):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)

    # Step 1: Login
    driver.get(config['url'])
    login_page.login(config['username'], config['password'])

    # Step 2: Go to checkout
    checkout_page.start_checkout()
    checkout_page.fill_checkout_information()
    checkout_page.complete_order()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(checkout_page.SUCCESS_MESSAGE)
    )

    assert checkout_page.get_success_message() == "Thank you for your order!"
