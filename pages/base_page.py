from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def dismiss_google_password_alert(self):
        try:
            time.sleep(2)
            pyautogui.press('tab')
            pyautogui.press('enter')
        except Exception as e:
            print(f"No popup or error found dismissing: {e}")
