from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(Page):

#    _total_items_in_cart_locator = (By.CSS_SELECTOR, "div #shopping_cart_container span")
    _cart_button_locator = (By.CSS_SELECTOR, "div #shopping_cart_container svg")
    _burger_menu_locator = (By.CSS_SELECTOR, ".bm-burger-button")

    def __init__(self, selenium, base_url=None, timeout=50, **url_kwargs):
        super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)

#   def total_items_in_cart(self):
#        return int(self.find_element(*self._total_items_in_cart_locator).text)

    def open_cart(self):
        self.find_element(*self._cart_button_locator).click()

