from data.items import Item
from .. import game


class Weapon(Item):

    def __init__(self):
        super().__init__()
        self.damage = game.generate_random_number(max=5)
        self.type = game.generate_weapon()
        self.name = f"+{self.damage} {self.type}"

    def __repr__(self):
        return self.name
