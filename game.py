import os
from tabnanny import check
import time
from src.utility import troop_move, check_shoot, movement
from src.game import Game

# take input of choice of character

# default values
while(True):
    print("Choose your character:\nPress q for Archer Queen and k for King")
    choice = input()
    if choice == 'q':
        queen = True
        break
    elif choice == 'k':
        queen = False
        break
    print("Please give a valid input")

# while(True):
#     print("Choose the level of the game you want to play.\nPress 1 for easy, 2 for medium and 3 for hard")
#     level = input()
#     if level in ['1', '2', '3']:
#         break
#     print("Please give a valid input")

for level in range(1, 4):
    # Start time of the game
    start_time = time.time()
    board_time = time.time()
    game = Game(start_time, queen, level)
    game.game_update()
    game.game_screen_print()

    check_end = game.check_end()

    while (not check_end):
        printvillage = False
        if movement(game):
            printvillage = True

        if(time.time() - board_time > 2):
            board_time = time.time()
            if troop_move(game):
                printvillage = True
            if check_shoot(game):
                printvillage = True
        if printvillage:
            game.game_update()
            game.game_screen_print()
        check_end = game.check_end()

    if (check_end == -1):
        os.system('clear')
        print("You Lose:( All your people are dead.")
        quit()
    elif (check_end == 1):
        os.system('clear')
        print("You Win! All buildings are destroyed.")
        print("Press any key to move to the next level")
        temp = input()

os.system('clear')
print("All Levels Complete.")
