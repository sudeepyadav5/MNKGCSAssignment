from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.form_page import FormPage
from faker import Faker

fake = Faker()


def test_form_submission(driver, config):
    driver.get(config["url"])
    login_page = LoginPage(driver)
    login_page.login(config["username"], config["password"])

    # Navigate to checkout (add item first if needed)
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()  # add to cart
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    driver.find_element(By.ID,"checkout").click()

    form_page = FormPage(driver)
    form_page.fill_checkout_form(fake.first_name(), fake.last_name(), fake.postcode())

    assert form_page.is_form_submitted().is_displayed(), "Form Submission is Failed!"
