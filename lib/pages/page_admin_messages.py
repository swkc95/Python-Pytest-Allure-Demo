from selenium.webdriver.common.by import By
from lib.pages.page_admin_layout import AdminLayout


class AdminMessagesPage(AdminLayout):
    def __init__(self, browser):
        super().__init__(browser)
        self.site_url = "/#/admin/messages"
        self.locator_dictionary.update(self.page_locator_dictionary)

    page_locator_dictionary = {
        "message_by_name": (By.XPATH, '//p[contains(text(), "{}")]'),
        "message_author_field": (By.XPATH, '//div[@data-testid="message"]//span[contains(text(), "From")]/..'),
        "message_email_field": (By.XPATH, '//div[@data-testid="message"]//span[contains(text(), "Email")]/..'),
        "message_subject_field": (By.XPATH, '//div[@data-testid="message"]/div[3]//span'),
        "message_text_field": (By.XPATH, '//div[@data-testid="message"]/div[4]//p'),
        "message_phone_field": (By.XPATH, '//div[@data-testid="message"]//span[contains(text(), "Phone")]/..')
    }
