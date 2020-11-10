from data.items import Item
from data.game import generate_stat, generate_dangerous_number


class Potion(Item):

    def __init__(self, luck=None):
        super().__init__()
        self.affected_stat = generate_stat()
        self.effect = generate_dangerous_number(val=5, luck=luck)
        self.name = f"{self.effect} {self.affected_stat} Potion"

    def __repr__(self):
        return self.name
