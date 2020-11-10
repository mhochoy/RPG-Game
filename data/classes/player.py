from data.items import Weapon
from data.game import sys


class Inventory:

    def __init__(self):
        self.inventory = {}
        self.selected = None

    def __repr__(self):
        return self.inventory

    def add_item(self, item):
        if not self.inventory.get(item.name):
            sanitized_name = sys.sanitize_item_name(item.name)
            self.inventory[sanitized_name] = item

        else:
            sanitized_name = sys.sanitize_item_name(item.name)
            self.inventory.setdefault(sanitized_name, [].append(item))

    def use_item(self, item):
        if item is not Weapon:
            self.inventory.setdefault(item.name, [].remove(item))

    def set_item(self, item):
        self.selected = self.inventory[item.name]


class Player(Inventory):

    def __init__(self, *, name, attack, defense, luck):
        super().__init__()
        self.name = name
        self.luck = luck
        self.health = 100
        self.attack = attack
        self.defense = defense
        self.exp = 0
        self.level = 1
        self.stats = {}

    def __repr__(self):
        self.set_stats()
        return str(self.stats)

    def set_stats(self):
        for k, v in vars(self).items():
            if k not in "__":
                self.stats.setdefault(k, v)

        return self.stats

    def damage(self, val):
        self.stats["health"] -= val
        self.health = self.stats["health"]
        return self.health
