from data import classes
from data.game import sys
from data import items


def main():
    mage = classes.Mage()
    enemy = classes.Enemy()

    mage.add_item(items.Potion())
    mage.add_item(items.Weapon())

    sys.battle(mage, enemy)


done = False
while not done:
    main()
    done = True
