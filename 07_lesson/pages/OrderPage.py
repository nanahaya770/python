#  заполнить поля
# нажать на кнопку континиу
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    FIRSTNAME_XPATH = '//input[@id="first-name"]'
    LAST_NAME_XPATH = '//input[@id="last-name"]'
    POST_CODE_XPATH = '//input[@id="postal-code"]'
    BUTTON_CONTINUE_XPATH = '//input[@id="continue"]'

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 6)
        self.driver = driver
        self.fields = {
            'first-name': "Адам",
            'last-name': "Захаров",
            'postal-code': "101000"
        }

    # def open(self):
    #     self.driver.get("https://www.saucedemo.com/")

    def fill_filds(self):

        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, self.FIRSTNAME_XPATH))).send_keys(
                    self.fields.get('first-name'))
        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, self.LAST_NAME_XPATH))).send_keys(
                    self.fields.get('last-name'))
        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, self.POST_CODE_XPATH))).send_keys(
                    self.fields.get('postal-code'))

    def continue_click(self):
        self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, self.BUTTON_CONTINUE_XPATH))).click()
