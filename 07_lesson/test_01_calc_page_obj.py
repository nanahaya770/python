import pytest
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(15)
    # driver.maximize_window()
    yield driver
    print(driver)
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.set_delay()
    calculator_page.do_calc()
    assert calculator_page.expected_result()
