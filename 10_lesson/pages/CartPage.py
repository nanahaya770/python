# нажать чекаут
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class CartPage:
    """
    Класс страницы с корзиной
    """
    CHECKOUT_XPATH = '//*[@id="checkout"]'

    def __init__(self, driver: WebDriver) -> None:
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    @allure.step("нажатие на кнопку checkout")
    def checkout(self) -> None:
        """
        Функция для предварительной проверки
        """
        self.driver.find_element(By.XPATH, self.CHECKOUT_XPATH).click()
