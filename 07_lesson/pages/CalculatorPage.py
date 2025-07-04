from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.fields = {
            'delay': '45'
        }
        self.buttons_xpath = {
            '7': '//*[@id="calculator"]/div[2]/span[1]',
            '+': '//*[@id="calculator"]/div[2]/span[4]',
            '8': '//*[@id="calculator"]/div[2]/span[2]',
            '=': '//*[@id="calculator"]/div[2]/span[15]'
        }
        self.result = '15'

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    def set_delay(self):
        calc = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        calc.clear()
        calc.send_keys(self.fields.get('delay'))

    def do_calc(self):
        self.driver.find_element(By.XPATH, self.buttons_xpath.get('7')).click()
        self.driver.find_element(By.XPATH, self.buttons_xpath.get('+')).click()
        self.driver.find_element(By.XPATH, self.buttons_xpath.get('8')).click()
        self.driver.find_element(By.XPATH, self.buttons_xpath.get('=')).click()

    def expected_result(self):
        waiter = WebDriverWait(self.driver, self.fields.get('delay'))
        waiter.until(
            EC.text_to_be_present_in_element((
                By.XPATH, '//div[@class="screen"]'), self.result)
        )
        screen = self.driver.find_element(By.XPATH, '//div[@class="screen"]')
        screen_text = screen.text
        if screen_text == self.result:
            return True
        else:
            return False
