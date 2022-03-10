import pickle
import os
import sys
import time
from src.game import Game

with open('./replays/%s.pkl' % sys.argv[1], 'rb') as f:
    replay = pickle.load(f)
    for i in range(len(replay)):
        os.system('clear')
        replay[i].get_village().print_village()
        time.sleep(0.5)
