from data.classes import Player
from data.game import generate_random_number


class Mage(Player):

    def __init__(self):
        super().__init__(
            name="Mage",
            luck=generate_random_number(max=5),
            attack=generate_random_number(max=3),
            defense=generate_random_number(max=7)
        )

    def heal(self, val):
        self.health += val

    def boost_defense(self, val):
        self.defense += val

    def boost_attack(self, val):
        self.defense += val

