from data.classes import Player
from data.game import generate_random_number, generate_dangerous_number


class Thief(Player):

    def __init__(self):
        super().__init__(
            name="Thief",
            luck=generate_random_number(max=7),
            attack=generate_random_number(max=3),
            defense=generate_random_number(max=5)
        )

    def last_resort(self):
        self.attack += generate_random_number(max=6)
        self.defense += generate_dangerous_number(val=6)