import random

# Legend
# Miss = -
# Hit = X
# Game Spaces = O


def crete_random_ship():
    return random.randint(0, 5), random.randint(0, 5)


def play_again():
    try_again = input("Wanna play again <Y>es or <N>o :").lower()
    if try_again == "y":
        play_game()
    else:
        print("Suit Yourself!")
        return


print("""Welcome to Battleships!!
\n Your objective is simple. Find and destroy all three ships!\n""")

print("""How it works:
You have 15 bullets. There are three ships hidden on the map.
You need to destroy them all.
To shoot, select a row and a collumn between 1 and 5.
If you hit a ship, you will know about it!!"
For each ship you destroy you will be awarded 1 new bullet
Good Luck and have fun""")


def play_game():
    game_board = [["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"]]

    for i in game_board:
        print(*i)

    ship1 = crete_random_ship()
    ship2 = crete_random_ship()
    ship3 = crete_random_ship()
    ships_left = 3
    bullets = 15
    while bullets:
        try:
            row = int(input("Choose a row between 1 and 5: "))
            column = int(input("Choose a column between 1 and 5: "))
        except ValueError:
            print("Numbers only please: ")
            continue

        if row not in range(1, 6) or column not in range(1, 6):
            print("That's not between 1 and 5, Try again!: ")
            continue

        row = row - 1
        column = column - 1

        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("You already shot there!: ")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3:
            print("Boom! You hit a ship. Here is one extra bullet!")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("You Won. Woo Hoo!!!!")
                play_again()
        else:
            print("Missed")
            game_board[row][column] = "-"
            bullets -= 1

        for i in game_board:
            print(*i)

        print(f"Bullets left: {bullets} | Ships left: {ships_left}")
    play_again()


if __name__ == "__main__":
    play_game()
