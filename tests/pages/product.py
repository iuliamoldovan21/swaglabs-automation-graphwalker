from selenium.webdriver.common.by import By

from tests.pages.base import BasePage


class ProductPage(BasePage):
    _back_to_homepage_locator = (By.CSS_SELECTOR, ".inventory_details_back_button")
    _add_to_cart_product_button_locator = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
    _remove_from_cart_button_locator = (By.CSS_SELECTOR, "button.btn_secondary.btn_inventory")
    _product_image_locator = (By.CSS_SELECTOR, "img.inventory_details_img")
    _product_name_locator = (By.CSS_SELECTOR, ".inventory_details_name")
    _product_price_locator = (By.CSS_SELECTOR, ".inventory_details_price")

    @property
    def is_back_button_present(self):
        return self.is_element_present(*self._back_to_homepage_locator)

    @property
    def is_remove_button_present(self):
        return self.is_element_present(*self._remove_from_cart_button_locator)

    @property
    def is_add_to_cart_button_present(self):
        return self.is_element_present(*self._add_to_cart_product_button_locator)

    @property
    def is_product_details_same_as_in_homepage(self):
        product_in_product_page = {'id': str(BasePage._current_product_index),
                                   'name': self.find_element(*self._product_name_locator).text,
                                   'price': self.find_element(*self._product_price_locator).text}
        return BasePage._current_product == product_in_product_page

    def add_product_to_cart_from_product_page(self):
        # self._products_added_to_cart_indexes_list.append(self._current_product_index)

        BasePage.index_in_dict += 1
        BasePage._products_added_to_cart_dict[BasePage.index_in_dict] = {}
        BasePage._products_added_to_cart_dict[BasePage.index_in_dict]['id'] = str(BasePage._current_product_index)
        BasePage._products_added_to_cart_dict[BasePage.index_in_dict]['name'] = self.find_element(
            *self._product_name_locator).text
        BasePage._products_added_to_cart_dict[BasePage.index_in_dict]['price'] = self.find_element(
            *self._product_price_locator).text

        # print("Index in dictionar produse:")
        # print(BasePage.index_in_dict)

        self.find_element(*self._add_to_cart_product_button_locator).click()

        # print("Lista indecsi produse: ")
        # print(*self._products_added_to_cart_indexes_list)
        print("Produse actuale in cos:")
        print(BasePage._products_added_to_cart_dict)

    def add_product_to_cart_if_not_added(self):
        # if self._current_product_index not in self._products_added_to_cart_indexes_list:
        # if self.is_element_present(*self._add_to_cart_product_button_locator):
        if not any(d['id'] == str(BasePage._current_product_index) for d in
                   BasePage._products_added_to_cart_dict.values()):
            self.add_product_to_cart_from_product_page()
        else:
            pass

    def remove_product_from_cart(self):
        self.find_element(*self._remove_from_cart_button_locator).click()
        # self._products_added_to_cart_indexes_list.remove(self._current_product_index)

        # del BasePage._products_added_to_cart_dict[BasePage._current_product_index]
        delete_product_dict = {a: b for a, b in BasePage._products_added_to_cart_dict.items() if
                               b['id'] != str(BasePage._current_product_index)}
        BasePage._products_added_to_cart_dict = delete_product_dict
        # BasePage.index_in_dict -= 1

        # print(BasePage.index_in_dict)
        # print("Lista indecsi produse: ")
        # print(*self._products_added_to_cart_indexes_list)
        print("Produse actuale in cos:")
        print(BasePage._products_added_to_cart_dict)

    def click_back_to_homepage_button(self):
        self.find_element(*self._back_to_homepage_locator).click()
