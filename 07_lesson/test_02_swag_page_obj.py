import pytest
from selenium import webdriver
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage
from pages.TotalPage import TotalPage
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(20)
    yield driver
    print(driver)
    driver.quit()


def test_swag_site(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.fill_filds()
    auth_page.submit_form()

    main_page = MainPage(driver)
    main_page.add_to_cart()
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    order_page = OrderPage(driver)
    order_page.fill_filds()
    order_page.continue_click()

    total_page = TotalPage(driver)
    total_page.total_result()
