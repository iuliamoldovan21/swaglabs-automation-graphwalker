from random import randint

from selenium.webdriver.common.by import By

from tests.pages.base import BasePage


class NavigationPage(BasePage):

    _products_label_locator = (By.CSS_SELECTOR, ".product_label")
    _products_locator = (By.CSS_SELECTOR, ".inventory_list div.inventory_item")

    @property
    def is_navigation_page_open(self):
        return self.is_element_present(*self._products_label_locator)

    @property
    def products_count(self):
        return len(self.find_elements(*self._products_locator))

    def add_to_cart_random_product(self):
        product_index = randint(0, self.products_count - 1)
        return self.add_to_cart_random_product(product_index)