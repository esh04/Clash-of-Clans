import os
import time
from src.utility import barb_move, cannon_shoot, movement
from src.input import Get, AlarmException, input_to
from src.game import Game


# Start time of the game
start_time = time.time()
board_time = time.time()
game = Game(start_time)
game.game_update()
game.game_screen_print()

while (not game.check_end()):
    if movement(game):
        os.system('clear')
        game.game_update()
        game.game_screen_print()
    if(time.time() - board_time > 0.8):
        board_time = time.time()
        if barb_move(game) or cannon_shoot(game):
            os.system('clear')
            game.game_update()
            game.game_screen_print()
