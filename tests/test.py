import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from tests.pages.base import BasePage
from tests.pages.login import LoginPage
from tests.pages.home import HomePage
from tests.pages.cart import CartPage
from tests.pages.product import ProductPage

HEADLESS = True
BASE_URL = "https://www.saucedemo.com/index.html"

driver = None


def setUpRun():
    """Setup the webdriver."""

    global driver

    options = Options()
    if HEADLESS:
        options.add_argument('-headless')

    print("Create a new Firefox session")
    driver = webdriver.Firefox()

    print("Set implicitly wait")
    driver.implicitly_wait(35)
#    print("Window size: {width}x{height}".format(**driver.get_window_size()))
    driver.maximize_window()

def tearDownRun():
    """Close the webdriver."""
    global driver
    print("Close the Firefox session")
    driver.quit()


class BaseModel(unittest.TestCase):
    """Contains common methods for all models."""

    def setUpModel(self):
        global driver
        print("Set up for: {}".format(type(self).__name__))
        self.driver = driver

    def e_do_nothing(self):
        pass

    def e_open_cart(self):
        page = BasePage(self.driver)
        page.open_cart()

    def v_cart_open(self):
       page = CartPage(self.driver)
       self.assertTrue(page.is_cart_open, "Cart page should be open")


class NavigationModel(BaseModel):
    product_index = 0;

    def v_login_page(self):
        page = LoginPage(self.driver)
        self.assertTrue(page.is_login_button_present, "Login button should be present.")

    def v_homepage(self):
        page = HomePage(self.driver)
        self.assertTrue(page.is_homepage_open, "Homepage should be open.")

    def v_homepage_product_added_to_cart(self):
        page = HomePage(self.driver)
        self.assertTrue(page.is_product_added_to_cart, "Product should be added to cart.")

    def v_product_page(self):
        page = ProductPage(self.driver)
        self.assertTrue(page.is_product_page_open, "Product page should be open")

    def v_product_added_to_cart_from_product_page(self):
        page = ProductPage(self.driver)
        self.assertTrue(page.is_product_added_to_cart, "Product should be added to cart")

    def v_product_removed(self):
        page = ProductPage(self.driver)
        self.assertTrue(page.is_product_removed_from_cart, "Product should be removed from cart")

    def e_load_login_page(self):
        print("Load  the login page of site from: {}".format(BASE_URL))
        page = LoginPage(self.driver, BASE_URL)
        page.open()
        self.driver.set_page_load_timeout(20)

    def e_perform_login(self):
        page = LoginPage(self.driver)
        page.login(username="standard_user", password="secret_sauce")

    def e_add_to_cart_from_homepage(self):
        page = HomePage(self.driver)
        self.product_index = page.add_to_cart_random_product()

    def e_open_product_page(self):
        page = HomePage(self.driver)
        page.open_product_page()

    def e_add_product_to_cart_from_product_page(self):
        page = ProductPage(self.driver)
        page.add_product_to_cart()

    def e_remove_product_from_cart(self):
        page = ProductPage(self.driver)
        page.remove_product_from_cart()


#command:    altwalker online -m models/navigation.json "a_star(reached_vertex(v_cart_open))" tests