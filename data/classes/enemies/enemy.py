from data import items
from data.game import sys
import random


def generate_enemy_type():
    return random.choice(["Orc", "Thief", "Skeleton"])


class Enemy:

    def __init__(self):
        self.name = generate_enemy_type()
        self.health = 100
        self.stats = {}
        if self.name == "Orc":
            self.attack = sys.generate_random_number(max=7)
            self.defense = sys.generate_random_number(max=5)
            self.luck = sys.generate_random_number(max=3)
        if self.name == "Thief":
            self.attack = sys.generate_random_number(max=3)
            self.defense = sys.generate_random_number(max=5)
            self.luck = sys.generate_random_number(max=7)
        if self.name == "Skeleton":
            self.attack = sys.generate_random_number(max=3)
            self.defense = sys.generate_random_number(max=7)
            self.luck = sys.generate_random_number(max=5)

        self.weapon = items.Weapon()

    def __repr__(self):
        self.set_stats()
        return str(self.stats)

    def set_stats(self):
        for k, v in vars(self).items():
            if k not in ("__"):
                self.stats.setdefault(k, v)

        return self.stats
