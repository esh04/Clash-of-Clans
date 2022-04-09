from .buildings import *
from .attackers import Balloon


class WizardTower(Building):
    def __init__(self, x_cood, y_cood):
        self._damage = 20
        self._range = 4
        health = 50
        body = "Z"
        xdim = 1
        ydim = 1
        Building.__init__(self, x_cood, y_cood, health, xdim, ydim, body)

    def shoot(self, game):
        for i in range(-self._range, self._range + 1):
            for j in range(-self._range, self._range + 1):
                matrix = game.get_village().get_matrix()
                # king = game.get_attackers().get_king()
                if isinstance(matrix[self._y + i][self._x + j], Person):
                    matrix[
                        self._y + i][self._x + j].attacked(self._damage)
                    self._object_char = 'Z+'
                    # aoe 3x3 tiles around the troop
                    for m in range(-1, 2):
                        for n in range(-1, 2):
                            if isinstance(matrix[self._y + i + m][self._x + j + n], Person):
                                matrix[
                                    self._y + i + m][self._x + j + n].attacked(self._damage)
                    return True

        self._object_char = 'Z'
        return False


class Cannon(Building):

    def __init__(self, x_cood, y_cood):
        self._damage = 20
        self._range = 4
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
                if isinstance(matrix[self._y + i][self._x + j], Person):
                    # dont shoot areal troops
                    if isinstance(matrix[self._y + i][self._x + j], Balloon) == False:
                        matrix[
                            self._y + i][self._x + j].attacked(self._damage)
                        self._object_char = 'C+'
                        return True

        self._object_char = 'C'
        return False
