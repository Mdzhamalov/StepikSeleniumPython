import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestModuleThree(unittest.TestCase):

    def test_link_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//div/input[@placeholder='Input your first name']")
        input1.send_keys("John")
        input2 = browser.find_element(By.XPATH, "//div/input[@placeholder='Input your last name']")
        input2.send_keys("Gold")
        input3 = browser.find_element(By.XPATH, "//div/input[@placeholder='Input your email']")
        input3.send_keys("John.Gold@test.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Welcome text is Wrong')

        time.sleep(5)
        browser.quit()

    def test_link_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//div/input[@placeholder='Input your first name']")
        input1.send_keys("John")
        input2 = browser.find_element(By.XPATH, "//div/input[@placeholder='Input your last name']")
        input2.send_keys("Gold")
        input3 = browser.find_element(By.XPATH, "//div/input[@placeholder='Input your email']")
        input3.send_keys("John.Gold@test.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Welcome text is Wrong')

        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
