import random
import time


def generate_random_number(max=2):
    return random.randint(1, max)


def generate_dangerous_number(val, luck=0):
    number = random.randint(-1 * val, val)

    if luck:
        number *= luck * .5

    if not number:
        return 1

    return number


def generate_stat(exclude: list = []):
    stats = {"attack", "defense", "luck", "health"}
    for ex in exclude:
        stats.remove(ex)
    return random.choice(list(stats))


def generate_weapon():
    return random.choice(["Sword", "Dagger", "Mace"])


def say(text, speed=0.5, cooldown=3):
    if text is not str:
        return

    for char in text:
        print(char)
        time.sleep(speed)
    time.sleep(cooldown)  #Time passed after dialogue has ended


def battle(player, enemy):

    def attack():
        enemy_choice = generate_stat(exclude=["health", "luck"])
        print(f"{enemy.name} has chosen to {enemy_choice}")
        if player.stats["attack"] > enemy.stats[enemy_choice]:
            damage = player.attack
            print("Enemy has taken " + str(damage) + " damage\n")
            enemy.stats["health"] -= damage
        if player.stats["attack"] < enemy.stats[enemy_choice]:
            damage = enemy.attack
            print("You have taken " + str(damage) + " damage\n")
            player.damage(damage)

    def defend():
        enemy_choice = generate_stat(exclude=["health", "luck"])
        print(f"{enemy.name} has chosen to {enemy_choice}")
        if enemy_choice == "attack":
            if player.defense > enemy.stats["attack"]:
                damage = player.defense - enemy.attack
                print("Enemy has taken " + str(damage) + " damage\n")
                enemy.stats["health"] -= damage
            if player.defense < enemy.stats["attack"]:
                damage = enemy.attack - player.defense
                print("You have taken " + str(damage) + " damage\n")
                player.damage(damage)

        else:
            print("   Stalemate   \n")

    while player.health and enemy.health:
        for item in player.inventory:
            player.selected = player.inventory[item]

        player.stats = update(player)
        print(f"{player.stats}\n")
        print(f"Your opponent is {enemy}\n")
        print(f"Player has {player.selected} equipped.\n")

        player_choice = input("What do you do?\n[A]ttack/[D]efend? : ")

        if player_choice[0] in "aA":
            attack()
        if player_choice[0] in "dD":
            defend()
        if player_choice == "quit":
            quit()


def update(player):
    return player.set_stats()


def sanitize_item_name(name):
    sanitized_name = ""
    for char in name:
        if char not in "+-1234567890":
            sanitized_name += char

    return sanitized_name[1:] + "s"


def assign_stat_point(player, val):
    stat = input("attack/defense/luck?: ")

    if "attack" in stat:
        player.attack += val

    if "defense" in stat:
        player.defense += val

    if "luck" in stat:
        player.luck += val

    else:
        assign_stat_point(player=player, val=val)


def give_exp(player, val):
    player.exp += val

    if can_level_up(player=player):
        player.level += 1


def can_level_up(player):
    if player.exp >= 10:
        return True
    return False
