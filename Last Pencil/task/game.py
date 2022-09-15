from random import randint

name1 = "John"
name2 = "Jack"


def pencils_total():
    messages = ("The number of pencils should be numeric",
                "The number of pencils should be positive")
    while True:
        try:
            pencils = int(input("How many pencils would you like to use: "))
        except ValueError:
            print(messages[0])
            continue
        else:
            if pencils == 0:
                print(messages[1])
            elif pencils < 0:
                print(messages[0])
            else:
                return pencils


def active_player():
    while True:
        player = input(f"Who will be the first ({name1}, {name2}): ")
        if player not in (name1, name2):
            print(f"Choose between {name1} and {name2}")
        else:
            return player


def take_pencils(pens_on_table):
    messages = ("Possible values: '1', '2' or '3'",
                "Too many pencils were taken")
    while True:
        try:
            pens_taken = int(input())
            if pens_taken not in (1, 2, 3):
                print(messages[0])
            elif pens_taken > pens_on_table:
                print(messages[1])
            else:
                return pens_taken
        except ValueError:
            print(messages[0])


def change_player(p1, p2, active_p):
    if active_p == p1:
        return p2
    else:
        return p1


def bot_turn(pens_on_table):
    pens_taken = (pens_on_table - 1) % 4
    if pens_on_table == 1:
        return 1
    elif pens_taken == 0:
        return randint(1,3)
    else:
        return pens_taken


pencils_on_table = pencils_total()
active_player = active_player()

while pencils_on_table > 0:
    print("|" * pencils_on_table)
    print(f"{active_player}'s turn:")

    if active_player == name1:
        pencils_taken = take_pencils(pencils_on_table)
    else:
        pencils_taken = bot_turn(pencils_on_table)
        print(pencils_taken)

    pencils_on_table -= pencils_taken
    active_player = change_player(name1, name2, active_player)

print(f"{active_player} won!")
