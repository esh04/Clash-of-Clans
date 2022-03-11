import pickle
import os
import sys
import time
from src.game import Game

counter = 0

for name in os.listdir('./replays/{}'.format(sys.argv[1])):
    with open('./replays/{}/{}.pkl'.format(sys.argv[1], counter), 'rb') as f:
        replay = pickle.load(f)
        os.system('clear')
        replay.get_village().print_village()
        time.sleep(0.5)
        counter += 1
