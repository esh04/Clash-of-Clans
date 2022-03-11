from .village import Village
from . import variables as v
from .attackers import Attackers
import copy
import os
import pickle


class Game:
    def __init__(self, time):
        # intialise village
        self._village = Village(v.N, v.M)
        # initalse attackers
        self._attackers = Attackers()
        # intialise game over
        self._game_over = False
        self._starttime = time
        self._scenenum = 0
        return

    def get_replay(self):
        return self._replay

    def get_starttime(self):
        return self._starttime

    def get_village(self):
        return self._village

    def get_attackers(self):
        return self._attackers

    def game_update(self):
        self._village.update_village()
        self._village.update_people(self._attackers.get_king())
        for barb in self._attackers.get_barbarians():
            self._village.update_people(barb)

    def game_screen_print(self):
        os.system('clear')
        self._village.print_village()
        scene = copy.deepcopy(self)
        if self._scenenum == 0:
            os.mkdir('./replays/{}'.format(str(self._starttime)))

        with open('./replays/{}/{}.pkl'.format(self._starttime, self._scenenum), 'wb') as f:
            pickle.dump(scene, f)
            self._scenenum += 1

        # self._replay.append(scene)
        print(self._attackers.get_king().health_bar() + ' ' +
              str(self._attackers.get_king().get_health())+'/' + str(self._attackers.get_king().getmaxhealth()))
        print("Press R for Rage Spell")
        print("Press H for Heal Spell")
        print("Press Q to quit")

    def check_vic(self):
        if(self._village.all_dead()):
            self._game_over = True
            return 1
        return 0

    def check_defeat(self):
        if(self._attackers.all_dead()):
            self._game_over = True
            return 1
        return 0

    def check_end(self):
        if self.check_vic():
            os.system('clear')
            print("You Win! All buildings are destroyed.")
            return 1
        elif self.check_defeat():
            os.system('clear')
            print("You Lose:( All your people are dead.")
            return 1
        return 0
