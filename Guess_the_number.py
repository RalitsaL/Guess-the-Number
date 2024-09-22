import random

pc_num = random.randint(1, 100)
print("Guess the number :) hint for you: it is in the range from 1 to 100: ")

while True:

    player_input = input()

    if not player_input.isdigit():
        print("Wrong input. Please type a number.")
        continue

    player_input = int(player_input)
    if player_input == pc_num:
        print("Well done! You guess it!")
        break
    elif player_input > pc_num:
        print("Try again, this one is a little bit too high.")
    elif player_input < pc_num:
        print("Try again. This one is a little bit too low.")

