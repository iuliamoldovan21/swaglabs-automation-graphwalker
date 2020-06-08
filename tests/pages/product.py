from selenium.webdriver.common.by import By

from tests.pages.base import BasePage


class ProductPage(BasePage):
    _back_to_homepage_locator = (By.CSS_SELECTOR, ".inventory_details_back_button")
    _add_to_cart_product_button_locator = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
    _remove_from_cart_button_locator = (By.CSS_SELECTOR, "button.btn_secondary.btn_inventory")

    @property
    def is_product_page_open(self):
        return self.is_element_present(*self._back_to_homepage_locator)

    @property
    def is_product_added_to_cart(self):
        return self.is_element_present(*self._remove_from_cart_button_locator)

    @property
    def is_product_removed_from_cart(self):
        return self.is_element_present(*self._add_to_cart_product_button_locator)

    def add_product_to_cart(self):
        self.find_element(*self._add_to_cart_product_button_locator).click()

    def remove_product_from_cart(self):
        self.find_element(*self._remove_from_cart_button_locator).click()