from random import randint

from selenium.webdriver.common.by import By

from tests.pages.base import BasePage


class HomePage(BasePage):

    _products_label_locator = (By.CSS_SELECTOR, ".product_label")
    _products_locator = (By.CSS_SELECTOR, ".inventory_list div.inventory_item")
    _products_title_locator = (By.CSS_SELECTOR, ".inventory_list div.inventory_item .inventory_item_name")
    _add_to_cart_product_button_locator = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
    _remove_from_cart_button_locator = (By.CSS_SELECTOR, "button.btn_secondary.btn_inventory")
    _product_image_locator = (By.CSS_SELECTOR, "img.inventory_item_img")
    _broken_image_url = (By.CSS_SELECTOR, "[src*='WithGarbageOnItToBreakTheUrl']")

    @property
    def is_homepage_open(self):
        return self.is_element_present(*self._products_label_locator)

    @property
    def products_count(self):
        return len(self.find_elements(*self._products_locator))

    @property
    def is_product_added_to_cart(self):
        #        product = self.find_elements(*self._products_locator)[2]
        #        _remove_button_for_product_locator = product.find_element(*self._remove_from_cart_button_locator)
        return self.is_element_present(*self._remove_from_cart_button_locator)

    def add_to_cart_product(self, product_index):
        product = self.find_elements(*self._products_locator)[product_index]
        product.find_element(*self._add_to_cart_product_button_locator).click()
#        return product_index

    def add_to_cart_random_product(self):
        # product_index = randint(0, self.products_count - 1)
        product_index = 2
        return self.add_to_cart_product(product_index)

    def open_product_page(self):
        product_index = 2
        self.find_elements(*self._products_title_locator)[product_index].click()



#    @property
#    def is_product_image_present_on_homepage(self):
#        all_products = self.find_elements(*self._products_locator)
#        for product in all_products:
#            if self.is_element_present(product.find_element(*self._broken_image_url)):
#                return self.false
#        return self.true

#    @property
#    def is_product_price_present_on_navigation_page(self):
#        all_products = self.find_elements(*self._products_locator)
#        for product in all_products:
#            if self.is_element_present()
