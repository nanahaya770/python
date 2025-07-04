from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    USERNAME_XPATH = '//*[@id="user-name"]'
    PASSWORD_XPATH = '//*[@id="password"]'
    LOGIN_BUTTON_XPATH = '//*[@id="login-button"]'

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 5)
        self.driver = driver
        self.fields = {
            'user-name': "standard_user",
            'password': "secret_sauce",
        }

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def fill_filds(self):

        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, self.USERNAME_XPATH))).send_keys(self.fields.get('user-name'))
        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH, self.PASSWORD_XPATH))).send_keys(self.fields.get('password'))

    def submit_form(self):
        self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH, self.LOGIN_BUTTON_XPATH))).click()
