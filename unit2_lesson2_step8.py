from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//div/input[@name = 'firstname']")
    first_name.send_keys("John")
    last_name = browser.find_element(By.XPATH, "//div/input[@name = 'lastname']")
    last_name.send_keys("Gold")
    email = browser.find_element(By.XPATH, "//div/input[@name = 'email']")
    email.send_keys("John.Gold@test.com")

    # Create .txt file
    with open("testM.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file

    # Upload .txt file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'testM.txt'
    file_path = os.path.join(current_dir, file_name)
    upload = browser.find_element(By.XPATH, '//input[@id = "file"]')
    upload.send_keys(file_path)


    browser.find_element(By.XPATH, "//button[@type = 'submit']").click()


finally:
    time.sleep(10)
    browser.quit()
