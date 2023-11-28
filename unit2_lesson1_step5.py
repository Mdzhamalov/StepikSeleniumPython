from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    browser.find_element(By.XPATH, "//div/input[@type = 'checkbox']").click()
    browser.find_element(By.XPATH, "//div/input[@id = 'robotsRule']").click()
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
