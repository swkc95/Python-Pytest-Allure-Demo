from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
import lib.misc.variables as v


class BasePage(object):

    locator_dictionary = {}

    def __init__(self, browser):
        self.base_url = v.BASE_URL
        self.browser = browser
        self.timeout = 10
        self.site_url = ""
        self.format_variable = None

    def set_format_variable(self, string):
        self.format_variable = string

    def locator_formatter(self, locator, format_variable):
        locator_list = list(locator)
        locator_list[1] = locator_list[1].format(format_variable)
        return tuple(locator_list)

    def find_element(self, locator_key, frmt=None):
        try:
            if locator_key in self.locator_dictionary.keys():
                locator = self.locator_dictionary[locator_key]
                if frmt is not None:
                    locator = self.locator_formatter(locator, frmt)

                try:
                    WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(locator))
                except(TimeoutException, StaleElementReferenceException, ElementClickInterceptedException):
                    print(f"{locator_key} is not present")
                return self.browser.find_element(*locator)

        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(locator_key)

    def wait_for_invisibility(self, locator_key, frmt=None):
        try:
            if locator_key in self.locator_dictionary.keys():
                locator = self.locator_dictionary[locator_key]
                if frmt is not None:
                    locator = self.locator_formatter(locator, frmt)

                try:
                    WebDriverWait(self.browser, self.timeout).until(EC.invisibility_of_element_located(locator))
                except(TimeoutException, StaleElementReferenceException, ElementClickInterceptedException):
                    print(f"{locator_key} is still visible")

        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(locator_key)

    def hover(self, target):
        ActionChains(self.browser).move_to_element(target).perform()
        sleep(1)

    def scroll_into(self, target):
        self.browser.execute_script("arguments[0].scrollIntoView();", target)

    def visit(self):
        self.browser.get(self.base_url + self.site_url)

    def __getattr__(self, locator):
        return self.find_element(locator, frmt=self.format_variable)

    def method_missing(self, locator):
        print(f"{locator} not found in locator_dictionary!")
