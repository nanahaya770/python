# нажать чекаут
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CHECKOUT_XPATH = '//*[@id="checkout"]'

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.XPATH, self.CHECKOUT_XPATH).click()
