from random import randint

from selenium.webdriver.common.by import By

from tests.pages.base import BasePage


class HomePage(BasePage):
    _products_label_locator = (By.CSS_SELECTOR, ".product_label")
    _products_locator = (By.CSS_SELECTOR, ".inventory_list div.inventory_item")
    _products_title_locator = (By.CSS_SELECTOR, ".inventory_list div.inventory_item .inventory_item_name")
    _products_price_locator = (By.CSS_SELECTOR, ".inventory_list div.inventory_item .inventory_item_price")
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
        # self._products_added_to_cart_indexes_list.append(product_index)

        BasePage.index_in_dict += 1
        BasePage._products_added_to_cart_dict[BasePage.index_in_dict] = {}
        BasePage._products_added_to_cart_dict[BasePage.index_in_dict]['id'] = str(product_index)
        BasePage._products_added_to_cart_dict[BasePage.index_in_dict]['name'] = self.find_elements(
            *self._products_title_locator)[product_index].text
        BasePage._products_added_to_cart_dict[BasePage.index_in_dict]['price'] = self.find_elements(
            *self._products_price_locator)[product_index].text

        print("Index in dictionar produse:")
        print(BasePage.index_in_dict)

        print("Produse actuale in cos:")
        print(BasePage._products_added_to_cart_dict)

    def add_to_cart_random_product(self):
        product_index = randint(0, self.products_count - 1)
        # while product_index in self._products_added_to_cart_indexes_list:
        #     product_index = randint(0, self.products_count - 1)
        #     print(product_index)

        while any(d['id'] == str(product_index) for d in BasePage._products_added_to_cart_dict.values()):
            product_index = randint(0, self.products_count - 1)

        # print("Lista indecsi produse: ")
        # print(*self._products_added_to_cart_indexes_list)
        print("Index produs de adaugat: {}".format(product_index))
        self.add_to_cart_product(product_index)

    def open_random_product_page(self):
        product_index = randint(0, self.products_count - 1)
        print('Index produs curent:')
        print(product_index)

        BasePage._current_product_index = product_index
        BasePage._current_product['id'] = str(product_index)
        BasePage._current_product['name'] = self.find_elements(*self._products_title_locator)[product_index].text
        BasePage._current_product['price'] = self.find_elements(*self._products_price_locator)[product_index].text
        # print("Index curent: {}".format(self._current_product_index))
        print("Produs curent: {}".format(self._current_product))

        self.find_elements(*self._products_title_locator)[product_index].click()

        # print("Lista indecsi produse: ")
        # print(*self._products_added_to_cart_indexes_list)

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
