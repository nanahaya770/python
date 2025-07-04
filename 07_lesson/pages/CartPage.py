# нажать чекаут
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CHECKOUT_XPATH = '//*[@id="checkout"]'

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 5)
        self.driver = driver

    def chekout_click(self):
        self.driver.find_element(By.XPATH, self.CHECKOUT_XPATH).click()
