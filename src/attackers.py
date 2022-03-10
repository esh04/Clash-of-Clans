from .barbarian import Barbarian
from .king import King
from . import variables as v
import random


class Attackers():
    def __init__(self):
        # intialise king
        self._king = King((v.N)-2, 2)
        # intialise barbarians
        self._barbarians = []
        return

    def get_king(self):
        return self._king

    def get_barbarians(self):
        return self._barbarians

    def set_barbarians(self, x, y):
        new_barb = Barbarian(x, y)
        self._barbarians.append(new_barb)
        return

    def barb_coord(self, coord, dim):
        return random.randint(coord - (dim//2),
                              coord + (dim//2))
