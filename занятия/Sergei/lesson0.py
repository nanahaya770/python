# Помощь с ДЗ - установка seleniumif __name__ == '__main__':
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # from webdriver_manager.chrome import ChromeDriverManager
    # import time

    # driver = webdriver.Chrome(
    #     service=ChromeService(ChromeDriverManager().install())
    # )

    # driver.get(
    #     "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    # )

    # calculator_page = CalculatorPage(driver)
    # calculator_page.set_delay()
    # time.sleep(3)
    # calculator_page.do_calc()
    # time.sleep(3)
    # assert calculator_page.expected_result()
    # time.sleep(3)

from sqlalchemy import create_engine 


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_db_connection():
    names = db.table_names()
    assert names[1] == 'app_users'