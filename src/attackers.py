from .barbarian import Archer, Balloon, Barbarian
from .king import King
from . import variables as v
import random


class Attackers():
    def __init__(self):
        # intialise king
        self._king = King((v.N)-2, 2)
        # intialise barbarians
        self._barbarians = []
        self._balloons = []
        self._archers = []
        return

    def get_king(self):
        return self._king

    def get_barbarians(self):
        return self._barbarians

    def get_archers(self):
        return self._archers

    def get_balloons(self):
        return self._balloons

    def set_barbarians(self, x, y):
        new_barb = Barbarian(x, y)
        self._barbarians.append(new_barb)
        return

    def set_balloons(self, x, y):
        new_balloon = Balloon(x, y)
        self._balloons.append(new_balloon)
        return

    def set_archers(self, x, y):
        new_archer = Archer(x, y)
        self._archers.append(new_archer)
        return

    def rand_coord(self, coord, dim):
        return random.randint(coord - (dim//2),
                              coord + (dim//2))

    def all_dead(self):
        for barb in self._barbarians:
            if not barb.is_dead():
                return False
        for archer in self._archers:
            if not archer.is_dead():
                return False
        for balloon in self._balloons:
            if not balloon.is_dead():
                return False
        if not self._king.is_dead():
            return False
        return True
