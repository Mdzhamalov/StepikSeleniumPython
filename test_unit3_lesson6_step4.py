import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:

    def test_login_to_stepik(self, browser):
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//nav/a[@id='ember35']"))).click()
        email = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/input[@name='login']")))
        email.send_keys("m_djamalov@mail.ru")
        password = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/input[@name='password']")))
        password.send_keys("Aa12345^")
        submit = browser.find_element(By.XPATH, "//div//button[@type='submit']")
        submit.click()

        actual = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH,
                 "//div[@title='parametrisation test']"))).text
        expected = "parametrisation test"
        assert actual == expected






