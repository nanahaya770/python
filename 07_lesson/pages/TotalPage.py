# сверить что тотал равен заявленной сумме
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TotalPage:
    def __init__(self, driver):
        self.driver = driver

    def total_result(self):
        self.wait = WebDriverWait(self.driver, 6)
        total = self.driver.find_element(
            By.XPATH,
            '//div[@class="summary_total_label"]'
        )
        total_text = total.text
        print(total_text.split()[1])

        self.driver.close()

        assert total_text.split()[1] == "$58.29"
