import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from tests.pages.base import BasePage
from tests.pages.login import LoginPage
from tests.pages.home import HomePage
from tests.pages.cart import CartPage
from tests.pages.product import ProductPage
from tests.pages.checkout_information import CheckoutInformationPage
from tests.pages.checkout_overview import CheckoutOverviewPage
from tests.pages.finish import FinishPage

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
        page = BasePage(self.driver)
        self.assertEqual(page.get_page_subheader, "Your Cart", "Cart page should be open")
        # self.assertTrue(page.is_certain_page_open, "Cart page should be open")

    #     assert ca nr prod in cos la icon = nr prod in pagina cosului

    def v_homepage(self):
        page = HomePage(self.driver)
        self.assertTrue(page.is_homepage_open, "Homepage should be open.")


class LoginModel(BaseModel):
    def v_login_page(self):
        page = LoginPage(self.driver)
        self.assertTrue(page.is_login_button_present, "Login button should be present.")

    def v_homepage(self):
        page = HomePage(self.driver)
        self.assertTrue(page.is_homepage_open, "Homepage should be open.")

    def e_fill_in_empty_password(self):
        print("Login attempt with empty password")
        page = LoginPage(self.driver)
        page.login(username="standard_user", password="")

    def e_fill_in_empty_username(self):
        print("Login attempt with empty username")
        page = LoginPage(self.driver)
        page.login(username="", password="secret_sauce")

    def e_fill_in_forbidden_user(self):
        print("Login attempt with locked out user")
        page = LoginPage(self.driver)
        page.login(username="locked_out_user", password="secret_sauce")

    def e_fill_in_invalid_credentials(self):
        print("Login attempt with invalid credentials")
        page = LoginPage(self.driver)
        page.login(username="user", password="password")

    def e_fill_in_standard_user(self):
        print("Login as standard user")
        page = LoginPage(self.driver)
        page.login(username="standard_user", password="secret_sauce")

    def e_logout(self):
        print("Log out")
        page = BasePage(self.driver)
        page.logout()

    def e_load_login_page(self):
        print("Load  the login page of site from: {}".format(BASE_URL))
        page = LoginPage(self.driver, BASE_URL)
        page.open()
        self.driver.set_page_load_timeout(20)


class NavigationModel(BaseModel):

    def v_homepage_product_added_to_cart(self):
        page = HomePage(self.driver)
        self.assertTrue(page.is_product_added_to_cart, "Product should be added to cart.")

    def v_product_page(self):
        page = ProductPage(self.driver)
        self.assertTrue(page.is_back_button_present, "Back button should be present")
        self.assertTrue(page.is_product_details_same_as_in_homepage,
                        "Product details in product page should match the one in homepage")

    def v_product_added_to_cart_from_product_page(self):
        product_page = ProductPage(self.driver)
        base_page = BasePage(self.driver)
        print("Items in cart: {}".format(product_page.total_items_in_cart))
        # to remove maybe next line
        # self.assertTrue(product_page.is_element_added_in_cart_list, "Product is not added to list")
        self.assertTrue(product_page.is_remove_button_present, "Remove button should be present")

    def v_product_removed(self):
        page = ProductPage(self.driver)
        self.assertTrue(page.is_add_to_cart_button_present, "Add to cart button should be present")

    def e_add_to_cart_from_homepage(self):
        print("Add to cart product from homepage")
        page = HomePage(self.driver)
        # self.product_index = page.add_to_cart_random_product()
        page.add_to_cart_random_product()

        print("Items in cart: {}".format(page.total_items_in_cart))

    def e_open_product_page(self):
        print("Open product page")
        page = HomePage(self.driver)
        page.open_random_product_page()

    def e_add_product_to_cart_from_product_page_if_not_added(self):
        page = ProductPage(self.driver)
        page.add_product_to_cart_if_not_added()
        print("Items in cart: {}".format(page.total_items_in_cart))

    def e_remove_product_from_cart(self):
        page = ProductPage(self.driver)
        page.remove_product_from_cart()
        # print("Items in cart: {}".format(page.total_items_in_cart))

    # def e_next_test_case(self):
    #     page = BasePage(self.driver)
    #     page.next_test_case()

    def e_go_from_cart_to_homepage(self):
        print("Go back to homepage")
        page = CartPage(self.driver)
        page.click_continue_shopping_button()

    def e_go_from_product_page_to_homepage(self):
        print("Go back to homepage")
        page = ProductPage(self.driver)
        page.click_back_to_homepage_button()

    def e_add_product_to_cart_from_product_page(self):
        page = ProductPage(self.driver)
        page.add_product_to_cart_from_product_page()


class CheckoutModel(BaseModel):
    def v_checkout_information(self):
        page = CheckoutInformationPage(self.driver)
        self.assertTrue(page.is_continue_button_present, "Continue button should be present")
        self.assertEqual(page.get_page_subheader, "Checkout: Your Information",
                         "Checkout information page should be open")

    def v_checkout_overview(self):
        page = CheckoutOverviewPage(self.driver)
        self.assertTrue(page.is_finish_button_present, "Finish button should be present")
        self.assertEqual(page.get_page_subheader, "Checkout: Overview", "Checkout overview page should be open")

    #

    #     check total amount to pay

    def v_finish_page(self):
        page = FinishPage(self.driver)
        self.assertEqual(page.get_page_subheader, "Finish", "Finished order page should be open")

    def e_go_to_checkout_information(self):
        print("Go to checkout information page")
        page = CartPage(self.driver)
        page.go_to_checkout_information()

    def e_fill_in_checkout_information(self):
        print("Fill in checkout personal information")
        page = CheckoutInformationPage(self.driver)
        page.fill_in_information_form(first_name="Jhon", last_name="Grey", postal_code="05002")

    def e_fill_in_empty_fields(self):
        print("Fill in checkout information with empty fields")
        page = CheckoutInformationPage(self.driver)
        page.fill_in_information_form(first_name="", last_name="", postal_code="")

    def e_fill_in_empty_first_name(self):
        print("Fill in checkout information with empty first name")
        page = CheckoutInformationPage(self.driver)
        page.fill_in_information_form(first_name="", last_name="Grey", postal_code="05002")

    def e_fill_in_empty_last_name(self):
        print("Fill in checkout information with empty last name ")
        page = CheckoutInformationPage(self.driver)
        page.fill_in_information_form(first_name="Jhon", last_name="", postal_code="05002")

    def e_fill_in_empty_postal_code(self):
        print("Fill in checkout information with empty postal code")
        page = CheckoutInformationPage(self.driver)
        page.fill_in_information_form(first_name="Jhon", last_name="Grey", postal_code="")

    def e_finish_order(self):
        print("Finish order")
        page = CheckoutOverviewPage(self.driver)
        page.finish_order()

    def e_cancel_order(self):
        print("Cancel order")
        page = BasePage(self.driver)
        page.click_on_cancel_order_button()

    def e_go_to_homepage_from_menu(self):
        print("Go to homepage")
        page = BasePage(self.driver)
        page.go_to_homepage_page_from_menu()

# command:    altwalker online -m models/navigation.json "a_star(reached_vertex(v_cart_open))" tests
#  altwalker online -m models/login.json "random(edge_coverage(100))" tests
# altwalker online -m models/navigation.json "random(edge_coverage(100))" tests

# altwalker online -m models/login.json "a_star(reached_vertex(v_homepage))" -m models/navigation.json "random(edge_coverage(100))" tests
# altwalker online -m models/login.json "a_star(reached_vertex(v_homepage))" -m models/navigation.json "weighted_random(reached_vertex(v_product_added_to_cart_from_product_page))" tests
# altwalker online -m models/login.json "a_star(reached_vertex(v_homepage))" -m models/navigation.json "a_star(reached_vertex(v_cart_open))" -m models/checkout.json "random(edge_coverage(100))" tests
