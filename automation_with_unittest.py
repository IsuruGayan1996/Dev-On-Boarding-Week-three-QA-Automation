import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test(unittest.TestCase):
    def setUp(self):
        self.service = Service(
            executable_path='/home/isuru/Desktop/Isuru/python/selenium/chrome drivers/chromedriver_linux64/chromedriver')
        self.driver = webdriver.Chrome(service=self.service)

    def tearDown(self):
        self.driver.quit()

    def test_testcase1(self):
        self.driver.get(
            "file:///home/isuru/Desktop/Isuru/Prodoscore%20Project/Technical%20KT/Third%20week/Front-End-Dev--On-Boarding-Week3/index.html")

        time.sleep(3)

        expected_pin_count = 12

        actual_pin_count = len(self.driver.find_elements(By.XPATH, "//*[@id='pins-table']/tbody/tr"))

        assert actual_pin_count == expected_pin_count, f"Expected {expected_pin_count} pins, but found {actual_pin_count} pins."

        rows = actual_pin_count
        cols = len(self.driver.find_elements(By.XPATH, "//*[@id='pins-table']/tbody/tr[1]/td"))

        print("PIN_ID     TITLE     BODY     IMAGE     USER_ID     ADDED_DATE")
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                value = self.driver.find_element(By.XPATH,
                                                 "//*[@id='pins-table']/tbody/tr[" + str(row) + "]/td[" + str(
                                                     col) + "]").text
                print(value, end='     ')
                assert value != "", "Pin attributes should not be empty."
            print()

    def test_testcase2(self):
        self.driver.get(
            "file:///home/isuru/Desktop/Isuru/Prodoscore%20Project/Technical%20KT/Third%20week/Front-End-Dev--On-Boarding-Week3/index.html")

        time.sleep(3)

        element = self.driver.find_element(By.XPATH, "//*[@id='pins-table']/tbody/tr[1]/td[3]")
        element.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "modal")))

        pin_id = self.driver.find_element(By.XPATH, "//*[@id='pin-id']").text
        title = self.driver.find_element(By.XPATH, "//*[@id='pin-title']").text
        body = self.driver.find_element(By.XPATH, "//*[@id='pin-body']").text
        user_id = self.driver.find_element(By.XPATH, "//*[@id='pin-user-id']").text
        added_date = self.driver.find_element(By.XPATH, "//*[@id='pin-added-date']").text

        assert pin_id != "", "pin id should not be empty."
        assert title != "", "pin title should not be empty."
        assert body != "", "pin body should not be empty."
        assert user_id != "", "pin user id should not be empty."
        assert added_date != "", "pin added date should not be empty."

        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
