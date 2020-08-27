from selenium.webdriver.common.by import By
from tests.pages.base import BasePage


class FinishPage(BasePage):
    _finished_order_message = (By.CSS_SELECTOR, "h2.complete-header")

    # @property
    # def is_finish_order_page_open(self):
    #     return self.is_element_present(*self._finished_order_message)