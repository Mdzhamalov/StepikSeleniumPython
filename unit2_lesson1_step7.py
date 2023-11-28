from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    get_img = browser.find_element(By.XPATH, "//h2/img[@id='treasure']")
    x_value = get_img.get_attribute('valuex')
    x = x_value
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    browser.find_element(By.XPATH, "//div/input[@type = 'checkbox']").click()
    browser.find_element(By.XPATH, "//div/input[@id = 'robotsRule']").click()
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
