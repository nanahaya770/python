from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    SAUCE_LABS_BACKPACK_ID = "add-to-cart-sauce-labs-backpack"
    SAUCE_LABS_BOLT_T_SHIRT_ID = "add-to-cart-sauce-labs-bolt-t-shirt"
    SAUCE_LABS_ONESIE_ID = "add-to-cart-sauce-labs-onesie"
    CART_XPATH = '//*[@id="shopping_cart_container"]/a'

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 20)
        self.driver = driver

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((
                By.ID, self.SAUCE_LABS_BACKPACK_ID))).click()
        self.wait.until(
            EC.element_to_be_clickable((
                By.ID, self.SAUCE_LABS_BOLT_T_SHIRT_ID))).click()
        self.wait.until(
            EC.element_to_be_clickable((
                By.ID, self.SAUCE_LABS_ONESIE_ID))).click()

    def go_to_cart(self):
        self.driver.find_element(By.XPATH, self.CART_XPATH).click()
