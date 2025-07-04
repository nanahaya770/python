import pytest
from selenium import webdriver
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage
from pages.TotalPage import TotalPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    # driver.maximize_window()
    yield driver
    print(driver)
    driver.quit()


def test_swag_site(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.fill_filds()
    time.sleep(3)
    auth_page.submit_form()
    time.sleep(3)

    main_page = MainPage(driver)
    main_page.add_to_cart()
    time.sleep(3)
    main_page.go_to_cart()
    time.sleep(3)

    cart_page = CartPage(driver)
    cart_page.chekout_click()
    time.sleep(3)

    order_page = OrderPage(driver)
    order_page.fill_filds()
    time.sleep(3)
    order_page.continue_click()
    time.sleep(3)

    total_page = TotalPage(driver)
    total_page.total_result()

    # driver.close()

    # assert total == $58.29
