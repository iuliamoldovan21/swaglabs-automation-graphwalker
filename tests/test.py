import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from tests.pages.login import LoginPage
from tests.pages.navigation import NavigationPage

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
    driver = webdriver.Firefox(options=options)

    print("Set implicitly wait")
    driver.implicitly_wait(15)
    print("Window size: {width}x{height}".format(**driver.get_window_size()))


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


class NavigationModel(BaseModel):

    def v_login_page(self):
        page = LoginPage(self.driver)
        self.assertTrue(page.is_login_button_present, "Login button should be present.")

    def v_navigation_page(self):
        page = NavigationPage(self.driver)
        self.assertTrue(page.is_navigation_page_open)

    def e_load_login_page(self):
        print("Load  the login page of site from: {}".format(BASE_URL))
        page = LoginPage(self.driver, BASE_URL)
        page.open()

    def e_perform_login(self):
        page = LoginPage(self.driver, BASE_URL)
        page.login(username="standard_user", password="secret_sauce")


#   def e_add_to_cart_from_navigation_page(self):
#     page = NavigationPage(self.driver)
#     page.add_to_cart_random_product()""
