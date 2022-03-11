import os
import time
from src.utility import cannon_shoot, check_cannon, movement
from src.input import Get, AlarmException, input_to
from src.game import Game


# Start time of the game
start_time = time.time()

game = Game(start_time)
game.game_update()
game.game_screen_print()

while (not game.check_end()):
    if movement(game):
        os.system('clear')
        game.game_update()
        game.game_screen_print()
        cannon_shoot(game)
    # check_cannon(game)
