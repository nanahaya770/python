# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def test_calculator():

#     driver = webdriver.Chrome(
#         service=ChromeService(ChromeDriverManager().install())
#     )

#     driver.get(
#         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
#     )

#     calc = driver.find_element(By.CSS_SELECTOR, '#delay')
#     calc.clear()
#     calc.send_keys("45")

#     driver.find_element(
#         By.XPATH,
#         '//*[@id="calculator"]/div[2]/span[1]'  # 7
#     ).click()
#     driver.find_element(
#         By.XPATH,
#         '//*[@id="calculator"]/div[2]/span[4]'  # +
#     ).click()
#     driver.find_element(
#         By.XPATH,
#         '//*[@id="calculator"]/div[2]/span[2]'  # 8
#     ).click()
#     driver.find_element(
#         By.XPATH,
#         '//*[@id="calculator"]/div[2]/span[15]'  # =
#     ).click()
#     screen = driver.find_element(By.XPATH, '//div[@class="screen"]')

#     waiter = WebDriverWait(driver, 47)

#     waiter.until(
#         EC.text_to_be_present_in_element(
#             (By.XPATH, '//div[@class="screen"]'),
#             "15"
#         )
#     )
#     screen_text = screen.text
#     assert screen_text == "15"


# test_calculator()
