from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(Page):
    def __init__(self, selenium, base_url=None, timeout=50, **url_kwargs):
        super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)