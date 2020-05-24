from selenium.webdriver.common.by import By

from tests.pages.base import BasePage


class LoginPage(BasePage):

    _username_locator = (By.CSS_SELECTOR, '#user-name')
    _password_locator = (By.CSS_SELECTOR, '#password')
    _login_button_locator = (By.CSS_SELECTOR, ".btn_action")

    def __init__(self, selenium, base_url=None, timeout=10, **url_kwargs):
        super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)

    def login(self, username="", password=""):
        print("Fill login credentials")
        self.find_element(*self._username_locator).clear()
        self.find_element(*self._username_locator).send_keys(username)
        self.find_element(*self._password_locator).clear()
        self.find_element(*self._password_locator).send_keys(password)
        self.find_element(*self._login_button_locator).click()

    @property
    def is_login_button_present(self):
        return self.is_element_present(*self._login_button_locator)

