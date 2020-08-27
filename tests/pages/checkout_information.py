from selenium.webdriver.common.by import By
from tests.pages.base import BasePage


class CheckoutInformationPage(BasePage):
    _first_name_input_locator = (By.CSS_SELECTOR, "input#first-name")
    _last_name_input_locator = (By.CSS_SELECTOR, "input#last-name")
    _postal_code_input_locator = (By.CSS_SELECTOR, "input#postal-code")
    _continue_button_locator = (By.CSS_SELECTOR, "input.btn_primary.cart_button")

    @property
    def is_continue_button_present(self):
        return self.is_element_present(*self._continue_button_locator)

    def fill_in_information_form(self, first_name="", last_name="", postal_code=""):
        self.find_element(*self._first_name_input_locator).clear()
        self.find_element(*self._first_name_input_locator).send_keys(first_name)
        self.find_element(*self._last_name_input_locator).clear()
        self.find_element(*self._last_name_input_locator).send_keys(last_name)
        self.find_element(*self._postal_code_input_locator).clear()
        self.find_element(*self._postal_code_input_locator).send_keys(postal_code)
        self.find_element(*self._continue_button_locator).click()

    def go_to_checkout_overview(self):
        print('Go to checkout overview page')
        self.find_element(*self._continue_button_locator).click()
