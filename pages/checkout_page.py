from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    ADD_TO_CART = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Checkout']")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "h2[class='complete-header']")

    def start_checkout(self):
        self.click(self.ADD_TO_CART)
        self.click(self.CART_ICON)
        self.click(self.CHECKOUT_BUTTON)

    def fill_checkout_information(self):
        self.send_keys(self.FIRST_NAME_INPUT, "Sudeep")
        self.send_keys(self.LAST_NAME_INPUT, "Yadav")
        self.send_keys(self.POSTAL_CODE_INPUT, "394221")
        self.click(self.CONTINUE_BUTTON)

    def complete_order(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
