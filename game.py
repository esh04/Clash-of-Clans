import os
import time
from src.utility import troop_move, check_shoot, movement
from src.game import Game


# Start time of the game
start_time = time.time()
board_time = time.time()
game = Game(start_time)
game.game_update()
game.game_screen_print()

while (not game.check_end()):
    print = False
    if movement(game):
        print = True

    if(time.time() - board_time > 2):
        board_time = time.time()
        if troop_move(game):
            print = True
        if check_shoot(game):
            print = True
    if print:
        game.game_update()
        game.game_screen_print()
