from selenium.webdriver.common.by import By

from tests.pages.base import BasePage


class CartPage(BasePage):

    _cart_label_locator = (By.CSS_SELECTOR, ".subheader")

    @property
    def is_cart_open(self):
        return self.is_element_present(*self._cart_label_locator)
