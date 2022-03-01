from .king import *
from .village import *
from . import variables as v


class Game:
    def __init__(self):
        # intialise village
        self._village = Village(v.N, v.M)
        # intialise king
        self._king = King(N-2, 2)
        # intialise barbarians
        self._barbarians = []
        # intialise game over
        self._game_over = False
        return

    def get_village(self):
        return self._village

    def get_king(self):
        return self._king

    def get_barbarians(self):
        return self._barbarians

    def game_screen_print(self):
        self._village.update_village()
        self._village.update_people(self._king)
        self._village.print_village()
        # for barbarian in self._barbarians:
        #     barbarian.print_barbarian()
