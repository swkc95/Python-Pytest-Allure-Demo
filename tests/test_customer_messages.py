from lib.pages import MainPage, AdminLoginPage, AdminLayout, AdminMessagesPage
from lib.classes.class_customer import Customer
from lib.classes.class_message import Message
from lib.classes.class_api import APIRequests
import lib.misc.variables as v
from time import sleep
import pytest
import allure


@allure.title("Customer sending messages via contact form")
@allure.feature("Customer sending messages via contact form")
@allure.tag("Customer")
@pytest.mark.customer
class TestCustomerBooking:
    @allure.title("Customer sends a message through the contact form, message is visible for the admin")
    @allure.description("Customer is on the main page\n"
                        "Customer scrolls down to the contact form to send a message\n"
                        "Customer sends a valid message through the contact form\n"
                        "Admin logs in\n"
                        "Admin sees a new message in the mailbox\n"
                        "Admin sees the message content")
    @allure.testcase("TC-7")
    def test_customer_message(self, browser):
        # Customer is on the main page
        customer = Customer()
        page = MainPage(browser)
        page.visit()
        page.banner_button.click()

        # Customer scrolls down to the contact form to send a message
        message = Message(customer)
        page = MainPage(browser)
        page.scroll_into(page.contact_form_name_field)

        # Customer sends a valid message through the contact form
        page.fill_message_form(message)

        # Admin logs in
        page = AdminLoginPage(browser)
        page.visit()
        page.login(v.ADMIN_USERNAME, v.ADMIN_PASSWORD)

        # Admin sees a new message in the mailbox
        page = AdminLayout(browser)
        page.inbox_tab.click()
        page = AdminMessagesPage(browser)
        page.set_format_variable(message.name)
        page.message_by_name.click()

        # Admin sees the message content
        sleep(1)  # workaround for dynamically loaded text nodes - could not target them via selenium waits
        assert message.name in page.message_author_field.text
        assert message.email in page.message_email_field.text
        assert message.subject in page.message_subject_field.text
        assert message.text in page.message_text_field.text
        assert message.phone in page.message_phone_field.text

    @allure.title("Customer attempts to send a message through the contact form with invalid email")
    @allure.description("Customer is on the main page\n"
                        "Customer scrolls down to the contact form to send a message\n"
                        "Customer sends a message through the contact form with invalid email\n"
                        "Customer sees a message about invalid mail formatting\n"
                        "[API] New message has not been registered in the database")
    @allure.testcase("TC-8")
    def test_customer_message_failed_email(self, browser, strings):
        # Customer is on the main page
        customer = Customer()
        page = MainPage(browser)
        page.visit()
        page.banner_button.click()

        # Customer scrolls down to the contact form to send a message
        message = Message(customer)
        page.scroll_into(page.contact_form_name_field)

        # Customer sends a message through the contact form with invalid email
        message.email = v.INVALID_EMAIL
        page.fill_message_form(message)

        # Customer sees a message about invalid mail formatting
        assert strings.VALIDATION_CONTACT_FORM_EMAIL_INVALID in page.contact_form_validation_field.text

        # [API] New message has not been registered in the database
        messages = APIRequests.get_messages()
        assert f'"subject":"{message.subject}"' not in messages
