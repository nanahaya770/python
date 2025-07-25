# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


# def test_form():

#     # Запуск браузера с автоматической установкой совместимого драйвера
#     driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
#     # Пример: откроем сайт
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

#     first_name = driver.find_element(By.XPATH, '//input[@name="first-name"]')
#     first_name.send_keys("Иван")

#     last_name = driver.find_element(By.XPATH, '//input[@name="last-name"]')
#     last_name.send_keys("Петров")

#     addres = driver.find_element(By.XPATH, '//input[@name="address"]')
#     addres.send_keys("Ленина,55-3")

#     email = driver.find_element(By.XPATH, '//input[@name="e-mail"]')
#     email.send_keys("test@skypro.com")

#     phone_number = driver.find_element(By.XPATH, '//input[@name="phone"]')
#     phone_number.send_keys(+7985899998787)

#     # zip_code = driver.find_element(By.XPATH, '//input[@name="zip-code"]')

#     city = driver.find_element(By.XPATH, '//input[@name="city"]')
#     city.send_keys("Москва")

#     country = driver.find_element(By.XPATH, '//input[@name="country"]')
#     country.send_keys("Россия")

#     job_position = driver.find_element(
#         By.XPATH,
#         '//input[@name="job-position"]'
#     )
#     job_position.send_keys("QA")

#     company = driver.find_element(By.XPATH, '//input[@name="company"]')
#     company.send_keys("SkyPro")

#     driver.find_element(By.XPATH, '//button[@type="submit"]').click()

#     driver.implicitly_wait(30)

#     zip_code = driver.find_element(By.XPATH, '//div[@id="zip-code"]')
#     zip_code_color = zip_code.value_of_css_property("background-color")
#     assert zip_code_color == "rgba(248, 215, 218, 1)"

#     first_name = driver.find_element(By.XPATH, '//div[@id="first-name"]')
#     first_name_color = first_name.value_of_css_property("background-color")
#     assert first_name_color == "rgba(209, 231, 221, 1)"

#     last_name = driver.find_element(By.XPATH, '//div[@id="last-name"]')
#     last_name_color = last_name.value_of_css_property("background-color")
#     assert last_name_color == "rgba(209, 231, 221, 1)"

#     addres = driver.find_element(By.XPATH, '//div[@id="address"]')
#     addres_color = addres.value_of_css_property("background-color")
#     assert addres_color == "rgba(209, 231, 221, 1)"

#     email = driver.find_element(By.XPATH, '//div[@id="e-mail"]')
#     email_color = email.value_of_css_property("background-color")
#     assert email_color == "rgba(209, 231, 221, 1)"

#     phone_number = driver.find_element(By.XPATH, '//div[@id="phone"]')
#     phone_number_color = phone_number.value_of_css_property("background-color")
#     assert phone_number_color == "rgba(209, 231, 221, 1)"

#     city = driver.find_element(By.XPATH, '//div[@id="city"]')
#     city_color = city.value_of_css_property("background-color")
#     assert city_color == "rgba(209, 231, 221, 1)"

#     country = driver.find_element(By.XPATH, '//div[@id="country"]')
#     country_color = country.value_of_css_property("background-color")
#     assert country_color == "rgba(209, 231, 221, 1)"

#     job_position = driver.find_element(By.XPATH, '//div[@id="job-position"]')
#     job_position_color = job_position.value_of_css_property("background-color")
#     assert job_position_color == "rgba(209, 231, 221, 1)"

#     company = driver.find_element(By.XPATH, '//div[@id="company"]')
#     company_color = company.value_of_css_property("background-color")
#     assert company_color == "rgba(209, 231, 221, 1)"


# test_form()
