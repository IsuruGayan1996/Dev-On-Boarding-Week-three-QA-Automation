from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class QAAutomation:
    def __init__(self):
        self.service = Service(
            executable_path='/home/isuru/Desktop/Isuru/python/selenium/chrome drivers/chromedriver_linux64/chromedriver')
        self.driver = webdriver.Chrome(service=self.service)

    def get_driver(self):
        return self.driver

    def test_case1(self):
        driver = QAAutomation().get_driver()
        driver.get(
            "file:///home/isuru/Desktop/Isuru/Prodoscore%20Project/Technical%20KT/Third%20week/Front-End-Dev--On-Boarding-Week3/index.html")

        time.sleep(3)

        expected_pin_count = 12

        actual_pin_count = len(driver.find_elements(By.XPATH, "//*[@id='pins-table']/tbody/tr"))

        assert actual_pin_count == expected_pin_count, f"Expected {expected_pin_count} pins, but found {actual_pin_count} pins."

        rows = actual_pin_count
        cols = len(driver.find_elements(By.XPATH, "//*[@id='pins-table']/tbody/tr[1]/td"))

        print("PIN_ID     TITLE     BODY     IMAGE     USER_ID     ADDED_DATE")
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                value = driver.find_element(By.XPATH,
                                            "//*[@id='pins-table']/tbody/tr[" + str(row) + "]/td[" + str(
                                                col) + "]").text
                print(value, end='     ')
                assert value != "", "Pin attributes should not be empty."
            print()

        driver.quit()

    def test_case2(self):
        driver = QAAutomation().get_driver()
        driver.get(
            "file:///home/isuru/Desktop/Isuru/Prodoscore%20Project/Technical%20KT/Third%20week/Front-End-Dev--On-Boarding-Week3/index.html")

        time.sleep(3)

        element = driver.find_element(By.XPATH, "//*[@id='pins-table']/tbody/tr[1]/td[3]")
        element.click()

        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "modal")))

        pin_id = driver.find_element(By.XPATH, "//*[@id='pin-id']").text
        title = driver.find_element(By.XPATH, "//*[@id='pin-title']").text
        body = driver.find_element(By.XPATH, "//*[@id='pin-body']").text
        user_id = driver.find_element(By.XPATH, "//*[@id='pin-user-id']").text
        added_date = driver.find_element(By.XPATH, "//*[@id='pin-added-date']").text

        assert pin_id != "", "pin id should not be empty."
        assert title != "", "pin title should not be empty."
        assert body != "", "pin body should not be empty."
        assert user_id != "", "pin user id should not be empty."
        assert added_date != "", "pin added date should not be empty."

        time.sleep(3)
        driver.quit()


obj = QAAutomation()
obj.test_case1()
obj.test_case2()
