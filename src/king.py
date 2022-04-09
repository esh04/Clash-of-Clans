from .buildings import Building
from .person import Person
from colorama import init, Fore, Back, Style
from .validation import isvalid
import os

init()


class King(Person):
    def __init__(self, x_cood, y_cood):
        damage = 10
        health = 200
        speed = 1
        self._body = Fore.CYAN + 'K' + Fore.RESET
        Person.__init__(self, x_cood, y_cood, damage, health, speed)

    def get_object(self):
        return self._body

    def health_bar(self):

        char = "+"
        health = (self.get_health_percentage()/100)*15
        health_bar = char * int(health) + (15-int(health))*" "
        return "Health of King: |" + health_bar + '|'

    def attack(self, village):
        if isvalid(self._x_cood - 1, self._y_cood):
            if village.get_matrix()[self._x_cood - 1][self._y_cood]:
                village.get_matrix()[self._x_cood -
                                     1][self._y_cood].attacked(self._attack)
                return 1
        return 0


class ArcherQueen(Person):
    def __init__(self, x_cood, y_cood):
        damage = 8
        health = 200
        speed = 2
        self._body = Fore.YELLOW + 'Q' + Fore.RESET
        self._lastmoved = 'w'
        Person.__init__(self, x_cood, y_cood, damage, health, speed)

    def get_object(self):
        return self._body

    def health_bar(self):

        char = "+"
        health = (self.get_health_percentage()/100)*15
        health_bar = char * int(health) + (15-int(health))*" "
        return "Health of Archer Queen: |" + health_bar + '|'

    def get_last_moved(self):
        return self._lastmoved

    def set_last_moved(self, char):
        self._lastmoved = char

    def attack(self, village):
        matrix = village.get_matrix()
        attacked = False
        keys = {
            'w': (-1, 0),
            'a': (0, -1),
            's': (1, 0),
            'd': (0, 1)

        }
        dx, dy = keys[self._lastmoved]
        y = self._y_cood + (8*dy)
        x = self._x_cood + (8*dx)

        # aoe 5x5
        for m in range(-2, 3):
            for n in range(-2, 3):
                if isvalid(x+m, y+m):
                    matrix[x + m][y + n] == '+'
                    if isinstance(matrix[x + m][y + n], Building):
                        matrix[x + m][y + n].attacked(self._attack)
                        attacked = True
        return attacked
