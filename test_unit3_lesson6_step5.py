import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


class TestLogin:

    @pytest.mark.parametrize('endpoint', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_login_to_stepik(self, browser, endpoint):
        link = f"https://stepik.org/lesson/{endpoint}/step/1"
        browser.get(link)

        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//nav/a[@id='ember35']"))).click()
        email = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div/input[@name='login']")))
        email.send_keys("m_djamalov@mail.ru")
        password = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div/input[@name='password']")))
        password.send_keys("Aa12345^")
        submit_login = browser.find_element(By.XPATH, "//div//button[@type='submit']")
        submit_login.click()

        # Ввести ответ в поле и нажать на "Отправить"
        text_field = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                    "//div/textarea[@placeholder = 'Напишите ваш ответ здесь...']")))
        text_field.clear()
        text_field.send_keys(str(math.log(int(time.time()))))
        time.sleep(1)
        send_answer = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                    "//div/button[@class = 'submit-submission']")))
        send_answer.click()
        time.sleep(3)

        # Находим текст сообщения на отправленный ответ
        actual_answer = WebDriverWait(browser, 70).until(EC.visibility_of_element_located((By.XPATH,
                                                    "//div/p[@class = 'smart-hints__hint']"))).text
        assert actual_answer == "Correct!"
        print(actual_answer)
