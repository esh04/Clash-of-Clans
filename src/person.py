# barbarian, king -> person
# movement, attack, damage, health, speed, dead

from pymysql import NULL

from .barbarian import Spawning
from .validation import isvalid


class Person():

    def __init__(self, x_cood, y_cood,  damage, health, speed):
        # Protected variables to be inherited
        self._x_cood = x_cood
        self._y_cood = y_cood
        self._dead = False
        self._health = health
        self._speed = speed
        self._attack = damage

    def getx(self):
        return self._x_cood

    def setx(self, x):
        self._x_cood = x

    def gety(self):
        return self._y_cood

    def sety(self, y):
        self._y_cood = y

    # move the person
    # x,y can be +1,-1,0

    def movement(self, x, y, village):
        # print(self._x_cood + x, self._y_cood + y)
        if isvalid(self._x_cood + x, self._y_cood + y):
            if not village.get_matrix()[self._x_cood + x][self._y_cood + y]:
                village.delete_people(self)
                self._x_cood += x
                self._y_cood += y
                return 1
            elif isinstance(village.get_matrix()[self._x_cood + x][self._y_cood + y], Spawning):
                village.delete_people(self)
                self._x_cood += x
                self._y_cood += y
            return 1
        return 0

    def attack(self, village):
        if isvalid(self._x_cood - 1, self._y_cood):
            if village.get_matrix()[self._x_cood - 1][self._y_cood]:
                village.get_matrix()[self._x_cood -
                                     1][self._y_cood].attacked(self._attack)
                return 1
        return 0

    def get_health(self):
        return self._health

    def attacked(self, damage):
        # decrease health by damage
        self._health -= damage

    def is_dead(self):
        if self._health <= 0:
            self._dead = 1
            return True
        else:
            return False
