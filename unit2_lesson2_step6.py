from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    browser.find_element(By.ID, 'robotCheckbox').click()
    submit_button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    browser.find_element(By.ID, 'robotsRule').click()
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
