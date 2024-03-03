from lib.pages import MainPage, BookingConfirmationModal, BookingModal
from lib.classes.class_room import Room
from lib.classes.class_customer import Customer
from lib.classes.class_booking import Booking
from lib.classes.class_api import APIRequests
import pytest
import allure


@allure.title("Customer booking a room")
@allure.feature("Customer booking a room")
@allure.tag("Customer")
@pytest.mark.customer
class TestCustomerBooking:
    @allure.title("Customer successfully books a room")
    @allure.description("[API] New random room added\n"
                        "Customer is on the main page\n"
                        "Customer clicks to book the new room\n"
                        "Customer sends a valid booking request\n"
                        "Customer sees confirmation message about successful booking\n"
                        "[API] New booking is registered in the database")
    @allure.testcase("TC-5")
    def test_customer_booking_room(self, browser, strings):
        # [API] New random room added
        room = Room()
        APIRequests.create_room(room)

        # Customer is on the main page
        customer = Customer()
        page = MainPage(browser)
        page.visit()
        page.banner_button.click()

        # Customer clicks to book the new room
        booking = Booking(customer, room, 5)
        page.start_booking(booking)

        # Customer sends a valid booking request
        page = BookingModal(browser)
        page.fill_booking_form(booking)
        page.choose_booking_date(booking)
        page.booking_form_submit_button.click()

        # Customer sees confirmation message about successful booking
        page = BookingConfirmationModal(browser)
        assert page.title_field.text == strings.CONFIRMATION_BOOKING_SUCCESSFUL_PRIMARY
        assert page.text_field.text == strings.CONFIRMATION_BOOKING_SUCCESSFUL_SECONDARY

        # [API] New booking is registered in the database
        bookings = APIRequests.get_bookings()
        assert f'"firstname":"{booking.first_name}","lastname":"{booking.last_name}"' in bookings

    @allure.title("Customer attempts to book a room without passing phone number")
    @allure.description("[API] New random room added\n"
                        "Customer is on the main page\n"
                        "Customer clicks to book the new room\n"
                        "Customer sends a booking request with invalid phone number\n"
                        "Customer sees validation message about invalid phone number\n"
                        "[API] New booking has not been registered in the database")
    @allure.testcase("TC-6")
    def test_customer_booking_room_failed_phone(self, browser, strings):
        # [API] New random room added
        room = Room()
        APIRequests.create_room(room)

        # Customer is on the main page
        customer = Customer()
        page = MainPage(browser)
        page.visit()
        page.banner_button.click()

        # Customer clicks to book the new room
        booking = Booking(customer, room, 5)
        page.start_booking(booking)

        # Customer sends a booking request with invalid phone number
        page = BookingModal(browser)
        booking.phone = ""
        page.fill_booking_form(booking)
        page.choose_booking_date(booking)
        page.booking_form_submit_button.click()

        # Customer sees validation message about invalid phone number
        assert strings.VALIDATION_BOOKING_FORM_PHONE_EMPTY in page.booking_form_validation_field.text
        assert strings.VALIDATION_BOOKING_FORM_PHONE_LENGTH in page.booking_form_validation_field.text

        # [API] New booking has not been registered in the database
        bookings = APIRequests.get_bookings()
        assert f'"firstname":"{booking.first_name}","lastname":"{booking.last_name}"' not in bookings

