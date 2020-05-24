import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from tests.pages.login import LoginPage


class LoginTest(unittest.TestCase):
    _username_locator = (By.CSS_SELECTOR, '#user-name')
    _password_locator = (By.CSS_SELECTOR, '#password')
    _login_button_locator = (By.CSS_SELECTOR, ".btn_action")

    def setUp(self):
        self.driver = webdriver.Firefox()
        print("Firefox Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_something(self):

        self.driver.get("https://www.saucedemo.com/index.html")
        self.driver.set_page_load_timeout(20)

        print("Fill login credentials")
        try:
            page = LoginPage(self.driver)
            page.login(username="standard_user", password="secret_sauce")
        except Exception as e:
            print("Exception occured " + e)

    def tearDown(self):

        print("------------------------------------------------------------------")
        print("Test Environment Destroyed")
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
