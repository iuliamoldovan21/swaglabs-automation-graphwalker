from selenium.webdriver.common.by import By

from tests.pages.base import BasePage


class CartPage(BasePage):

    _checkout_button_locator = (By.CSS_SELECTOR, "a.btn_action.checkout_button")
    _continue_shopping_locator = (By.CSS_SELECTOR, "a.btn_secondary")

    def go_to_checkout_information(self):
        print('Go to checkout information page')
        self.find_element(*self._checkout_button_locator).click()

    def click_continue_shopping_button(self):
        self.find_element(*self._continue_shopping_locator).click()

