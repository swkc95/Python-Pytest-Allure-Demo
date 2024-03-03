from faker import Faker

fake = Faker('pl_PL')


class Customer(object):
    def __init__(self):
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = fake.ascii_safe_email()
        self.phone = fake.numerify(text='+48.%%%%%%%%%')

    def __str__(self):
        attributes = vars(self)
        return "customer = " + str(attributes)
