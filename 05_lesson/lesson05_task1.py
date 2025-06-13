import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Запуск браузера с автоматической установкой совместимого драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Пример: откроем сайт
driver.get("http://uitestingplayground.com/classattr")
driver.find_element(
    By.XPATH,
    (
        "//button[contains(concat(' ', normalize-space(@class), ' '), "
        "' btn-primary ')]"
    )
).click()
time.sleep(10)

# driver.quit()
