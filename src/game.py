from .village import Village
from . import variables as v
from .attackers import Attackers
import copy


class Game:
    def __init__(self, time):
        # intialise village
        self._village = Village(v.N, v.M)
        # initalse attackers
        self._attackers = Attackers()
        # intialise game over
        self._game_over = False
        self._starttime = time

        self._replay = []
        return

    def get_replay(self):
        return self._replay

    def get_starttime(self):
        return self._starttime

    def get_village(self):
        return self._village

    def get_attackers(self):
        return self._attackers

    def game_screen_print(self):
        self._village.update_village()
        self._village.update_people(self._attackers.get_king())
        for barb in self._attackers.get_barbarians():
            self._village.update_people(barb)
        self._village.print_village()
        scene = copy.deepcopy(self)
        self._replay.append(scene)
        print(self._attackers.get_king().health_bar())
        print("Press R for Rage Spell")
        print("Press H for Heal Spell")
        print("Press Q to quit")

    def check_vic(self):
        return 1

    def check_defeat(self):
        return 1
