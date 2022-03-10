from .village import Village
from . import variables as v
from .attackers import Attackers


class Game:
    def __init__(self):
        # intialise village
        self._village = Village(v.N, v.M)
        # initalse attackers
        self._attackers = Attackers()
        # intialise game over
        self._game_over = False
        return

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
