# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager


# def test_shop():

#     # Запуск браузера с автоматической установкой совместимого драйвера
#     driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     # Пример: откроем сайт
#     driver.get("https://www.saucedemo.com/")

#     user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
#     user_name.send_keys("standard_user")

#     password = driver.find_element(By.XPATH, '//*[@id="password"]')
#     password.send_keys("secret_sauce")

#     driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#     driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
#     driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
#     driver.find_element(
#         By.XPATH,
#         '/html/body/div/div/div/div[1]/div[1]/div[3]/a'
#     ).click()
#     driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

#     first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
#     first_name.send_keys("Адам")

#     last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
#     last_name.send_keys("Захаров")

#     postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
#     postal_code.send_keys("101000")

#     # postal_code
#     driver.find_element(By.XPATH, '//input[@id="continue"]').click()

#     total = driver.find_element(
#         By.XPATH,
#         '//div[@class="summary_total_label"]'
#     )
#     total_text = total.text
#     # print(total_text.split()[1])

#     driver.close()

#     assert total_text.split()[1] == "$58.29"


# test_shop()
