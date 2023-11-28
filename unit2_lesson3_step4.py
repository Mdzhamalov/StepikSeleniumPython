import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    alert = browser.switch_to.alert
    alert.accept()

    get_x_value = browser.find_element(By.XPATH, "//label/span[@id='input_value']")
    x = get_x_value.text
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    print(browser.switch_to.alert.text.split(': ')[-1])


finally:
    time.sleep(4)
    browser.quit()
