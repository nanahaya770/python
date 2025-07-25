import pytest
from selenium import webdriver
from pages.FormPage import FormPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()

from sqlalchemy import create_engine, text

try:
    engine = create_engine("postgresql://postgres:770@localhost:5432/postgres")
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Соединение с БД успешно!", list(result))
except Exception as e:
    print("❌ Ошибка подключения:", e)
