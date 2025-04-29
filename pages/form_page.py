from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormPage(BasePage):
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    POSTALCODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def fill_checkout_form(self, firstname, lastname, postalcode):
        self.enter_text(self.FIRSTNAME_INPUT, firstname)
        self.enter_text(self.LASTNAME_INPUT, lastname)
        self.enter_text(self.POSTALCODE_INPUT, postalcode)
        self.click(self.CONTINUE_BUTTON)
        self.click(self.FINISH_BUTTON)

    def is_form_submitted(self):
        return self.find_element(self.SUCCESS_MSG)
