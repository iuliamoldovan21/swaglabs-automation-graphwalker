from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(Page):
    _total_items_in_cart_locator = (By.CSS_SELECTOR, "div #shopping_cart_container span")
    _cart_button_locator = (By.CSS_SELECTOR, "div #shopping_cart_container svg")
    _burger_menu_locator = (By.CSS_SELECTOR, ".bm-burger-button")
    _reset_app_state_locator = (By.CSS_SELECTOR, "#reset_sidebar_link")
    _navigation_page_locator = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    _logout_locator = (By.ID, "logout_sidebar_link")
    _cart_label_locator = (By.CSS_SELECTOR, ".subheader")
    _cancel_button_locator = (By.CSS_SELECTOR, "a.cart_cancel_link")

    # _products_added_to_cart_indexes_list = []
    _current_product_index = -1

    _current_product = {'id': None, 'name': None, 'price': None}
    index_in_dict = 0
    _products_added_to_cart_dict = {}

    def __init__(self, selenium, base_url=None, timeout=50, **url_kwargs):
        super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)

    @property
    def total_items_in_cart(self):
        return int(self.find_element(*self._total_items_in_cart_locator).text)

    @property
    def get_page_subheader(self):
        return self.find_element(*self._cart_label_locator).text

    def open_cart(self):
        print('Open cart')
        self.find_element(*self._cart_button_locator).click()

    def click_on_cancel_order_button(self):
        self.find_element(*self._cancel_button_locator).click()

    # def next_test_case(self):
    #     self.find_element(*self._burger_menu_locator).click()
    #     self.find_element(*self._reset_app_state_locator).click()
    #     self.find_element(*self._navigation_page_locator).click()

    def open_side_menu(self):
        self.find_element(*self._burger_menu_locator).click()

    def logout(self):
        print('Logout')
        self.open_side_menu()
        self.find_element(*self._logout_locator).click()

    def go_to_homepage_page_from_menu(self):
        self.find_element(*self._burger_menu_locator).click()
        self.find_element(*self._navigation_page_locator).click()

    # @property
    # def is_element_added_in_cart_list(self):
    #     # print("Index curent pe care il verific: {}".format(self._current_product_index))
    #     if self._current_product_index in self._products_added_to_cart_indexes_list:
    #         return True
    #     return False
