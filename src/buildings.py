from .person import Person
from colorama import init, Fore, Back, Style
import numpy as np
init()


class Building():

    def __init__(self, x_cood, y_cood, health, xdim, ydim, body):
        # Protected variables to be inherited
        self._x = x_cood
        self._y = y_cood
        self._display = True
        self._health = health
        self._max_health = health
        self._xdim = xdim
        self._ydim = ydim
        self._object_char = str(body)

    def get_health_percentage(self):
        return (self._health/self._max_health) * 100

    def getx(self):
        return self._x

    def setx(self, x):
        self._x = x

    def gety(self):
        return self._y

    def sety(self, y):
        self._y = y

    def get_max_health(self):
        return self._max_health

    def get_health(self):
        return self._health

    def get_xdim(self):
        return self._xdim

    def get_ydim(self):
        return self._ydim

    def get_display(self):
        return self._display

    def get_object(self):
        if self.get_health_percentage() <= 0:
            self._display = False
            return ' '

        if self.get_health_percentage() > 50:
            return Fore.GREEN + self._object_char + Fore.RESET
        elif self.get_health_percentage() > 25:
            return Fore.LIGHTYELLOW_EX + self._object_char + Fore.RESET
        else:
            return Fore.RED + self._object_char + Fore.RESET

    def attacked(self, damage):
        # decrease health by damage
        self._health -= damage

    # def set_object(self, village):
    #     village.get_matrix()[self._x_cood - (self._xdim//2):self._x_cood + (self._xdim//2), self._y_cood - (self._ydim//2):self._y_cood + (self._ydim//2)
    #                          ] = self._object


# colour change based on health, setting the objects in the given matrix of the game


class TownHall(Building):

    def __init__(self, x_cood, y_cood):
        health = 150
        body = "T"
        xdim = 4
        ydim = 3
        Building.__init__(self, x_cood, y_cood, health, xdim, ydim, body)


class Huts(Building):

    def __init__(self, x_cood, y_cood):
        health = 120
        body = "H"
        xdim = 1
        ydim = 1
        Building.__init__(self, x_cood, y_cood, health, xdim, ydim, body)


class Wall(Building):

    def __init__(self, x_cood, y_cood):
        health = 50
        body = "W"
        Building.__init__(self, x_cood, y_cood, health, 1, 1, body)


class Cannon(Building):

    def __init__(self, x_cood, y_cood):
        self._damage = 2
        self._range = 6
        health = 50
        body = "C"
        xdim = 1
        ydim = 1
        Building.__init__(self, x_cood, y_cood, health, xdim, ydim, body)

    def shoot(self, game):
        for i in range(-self._range, self._range + 1):
            for j in range(-self._range, self._range + 1):
                matrix = game.get_village().get_matrix()
                # king = game.get_attackers().get_king()
                # print(self._y + i, self._x + j, king.getx(),
                #       king.gety(), matrix[self._y + i][self._x + j])

                if isinstance(matrix[self._y + i][self._x + j], Person):
                    matrix[
                        self._y + i][self._x + j].attacked(self._damage)
                    return True

        return False
