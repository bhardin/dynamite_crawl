import random


class Weapon:
    damage = random.randint(2, 5)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
