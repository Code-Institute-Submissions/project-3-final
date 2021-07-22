import random

# Legend
# Miss = -
# Hit = X
# Game Spaces = O


def crete_random_ship():
    return random.randint(0, 5), random.randint(0, 5)


print("""Welcome to Battleships!!
\n Your objective is simple. Find and destroy all three ships!\n""")

print("""How it works:
You have 15 bullets. There are three ships hidden on the map.
You need to destroy them all.
To shoot, select a row and a collumn between 1 and 5.
If you hit a ship, you will know about it!!"
For each ship you destroy you will be awarded 1 new bullet
Good Luck and have fun""")


def game():
    game_board = [["O", "O", "O", "O", "O"],  ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"]]
    for i in game_board:
        print(*i)
