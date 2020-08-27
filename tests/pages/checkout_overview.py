from selenium.webdriver.common.by import By
from tests.pages.base import BasePage


class CheckoutOverviewPage(BasePage):
    _finish_button_locator = (By.CSS_SELECTOR, "a.btn_action.cart_button")

    @property
    def is_finish_button_present(self):
        return self.find_element(*self._finish_button_locator)

    def click_finish_button(self):
        self.find_element(*self._finish_button_locator).click()

    def finish_order(self):
        self.click_finish_button()
        self._products_added_to_cart_indexes_list.clear()
        self._current_product_index = -1
