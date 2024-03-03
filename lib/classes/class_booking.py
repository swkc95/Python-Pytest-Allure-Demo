from faker import Faker
from datetime import timedelta
from lib.misc.functions import first_day_of_next_month

fake = Faker('pl_PL')


class Booking(object):
    def __init__(self, customer, room, nights):
        for key, value in vars(customer).items():
            setattr(self, key, value)
        self.room = room.number
        self.start_date = first_day_of_next_month().strftime("%Y-%m-%d")
        self.nights = nights
        self.end_date = (first_day_of_next_month() + timedelta(self.nights)).strftime("%Y-%m-%d")
        self.price = room.price

    def __str__(self):
        attributes = vars(self)
        return "booking = " + str(attributes)
