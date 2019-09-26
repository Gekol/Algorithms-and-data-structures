from faker import Faker
from random import choice
import json


class Item:
    def __init__(self, key, name, count):
        self.key = key
        self.name = name
        self.count = count

    def __repr__(self):
        return "Item({}, {}, {})".format(self.key, self.name, self.count)


def gen():
    fake = Faker()
    fake.seed(1437)
    data = []

    key_name = []
    for i in range(20):
        key_name.append((fake.pystr(min_chars=8, max_chars=8), fake.first_name()))

    for i in range(100):
        key, name = choice(key_name)
        count = fake.pyint(min_value=0, max_value=1000, step=1)
        data.append(Item(key, name, count))

    with open('data_new.json', 'w') as outfile:
        json.dump([ob.__dict__ for ob in data], outfile)
