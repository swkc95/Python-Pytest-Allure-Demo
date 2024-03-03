from faker import Faker
import random
import lib.misc.variables as v
fake = Faker('pl_PL')


class Message(object):
    def __init__(self, customer):
        self.name = f"{customer.first_name} {customer.last_name}"
        self.email = customer.email
        self.phone = customer.phone
        self.subject = f"{v.CONTACT_SUBJECT} {random.randrange(10000)}"
        self.text = f"{v.CONTACT_MESSAGE} {random.randrange(10000)}"

    def __str__(self):
        attributes = vars(self)
        return "message = " + str(attributes)
