from data.classes import Player
from data.game import generate_random_number, generate_dangerous_number


class Knight(Player):

    def __init__(self):
        super().__init__(
            name="Knight",
            attack=generate_random_number(max=7),
            defense=generate_random_number(max=5),
            luck=generate_random_number(max=3)
        )

    def power_boost(self):
        if not self.luck <= 1:
            self.attack += generate_random_number(max=3)
            self.defense += generate_random_number(max=3)
            self.luck += generate_dangerous_number(val=3)
            if self.luck < 1:
                self.luck = 1
