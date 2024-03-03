from selenium.webdriver.common.by import By
from lib.pages.base_page_object import BasePage


class AdminLoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.site_url = "/#/admin"
        self.locator_dictionary.update(self.page_locator_dictionary)

    def login(self, username, password):
        self.find_element("username_field").send_keys(username)
        self.find_element("password_field").send_keys(password)
        self.find_element("login_button").click()

    page_locator_dictionary = {
        "banner_button": (By.CSS_SELECTOR, 'div[data-target="#collapseBanner"]>button'),
        "username_field": (By.CSS_SELECTOR, '#username'),
        "username_validation_border": (By.CSS_SELECTOR, '#username[style="border: 1px solid red;"]'),
        "password_field": (By.CSS_SELECTOR, '#password'),
        "password_validation_border": (By.CSS_SELECTOR, '#password[style="border: 1px solid red;"]'),
        "login_button": (By.CSS_SELECTOR, '#doLogin')
    }
