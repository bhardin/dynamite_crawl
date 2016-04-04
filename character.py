import random
from weapon import Weapon


class Character:
    min_hit_points = 5
    max_hit_points = 8
    weapon = Weapon(name='sword')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.hit_points = random.randint(self.min_hit_points,
                                         self.max_hit_points)

    def initiative(self):
        return random.randint(1, 10)

    def is_dead(self):
        if self.hit_points <= 0:
            return True

        return False

    def takes_damage(self, damage):
        self.hit_points -= damage
        return self.hit_points

    def attack(self, opponent, attack_type):
        multiplier = random.randint(1, 2)

        print("{} attacks with a {}".format(self.name, attack_type))

        damage = self.weapon.damage * multiplier
        opponent.takes_damage(damage)

        return damage


class Monster(Character):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = min_hit_points * 2
    max_experience = max_hit_points * 2


class Troll(Monster):
    weapon = Weapon(name='club')
    min_hit_points = 5
    max_hit_points = 8

    regeneration = True
