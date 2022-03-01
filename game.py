import os
import time
from src.utility import movement
from src.input import Get, AlarmException, input_to
from src.game import Game


# Start time of the game
start_time = time.time()

game = Game()
game.game_screen_print()

while True:
    if movement(game):
        # print(game.get_king().getx(), game.get_king().gety())
        os.system('clear')
        game.game_screen_print()

    # for barbarian movement
new_time = time.time() - start_time
if(new_time % 1 == 0):
    print(new_time)
