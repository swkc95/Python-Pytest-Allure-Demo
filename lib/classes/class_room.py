import lib.misc.variables as v
from faker import Faker
import random
fake = Faker('pl_PL')


class Room(object):
    def __init__(self):
        self.id = random.randrange(1000)
        self.number = str(200 + random.randrange(100))
        self.type = random.choice(v.ROOM_TYPE_LIST)
        self.is_accessible = True
        self.image = v.SAMPLE_ROOM_IMAGE
        self.description = v.SAMPLE_ROOM_DESCRIPTION
        self.price = str(500 + random.randrange(100))
        self.features = random.sample(v.ROOM_FEATURES_LIST, random.randint(0, len(v.ROOM_FEATURES_LIST)))

    def __str__(self):
        attributes = vars(self)
        return "room = " + str(attributes)
