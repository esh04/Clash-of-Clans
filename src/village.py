import numpy as np
from .variables import N, M
from .buildings import TownHall, Huts,  Wall
from .defenseBuildings import WizardTower, Cannon
from .spawning import Spawning


class Village:
    def __init__(self, rows, cols):
        '''Initialise the village'''
        self._rows = rows
        self._cols = cols
        self._matrix = np.empty(
            (self._rows, self._cols), dtype=object)

        # create spawning points
        self._spawning = [Spawning(M//2 + M//10, 50, 1), Spawning(
            M//4, 40, 2), Spawning((3*M)//4, 40, 3), Spawning(M//2, 40, 4), Spawning(M//10, 50, 5), Spawning((9*M)//10, 50, 6), Spawning(
            M//4, 50, 7), Spawning((3*M)//4, 50, 8), Spawning((2*M)//5, 50, 9)]

        # create huts
        self._huts = [Huts((3*M)//4, N//6), Huts(M//4, N//6), Huts(
            ((M//2) - (M//8)), N//4), Huts(((M//2) + (M//8)), N//4), Huts(M//2, N//2)]

        # create town hall
        self._townhall = TownHall(M//2, N//4)

        # cannons
        self._cannons = [Cannon(((M//2) - (M//8)), N//2 - N//10),
                         Cannon(((M//2) + (M//8)), N//2 - N//10)]
        self._walls = []
        # create walls
        for i in range(6):
            self._walls.extend([Wall(M//2 + i+1, N//3), Wall(((M//2) - (M//8) + i+1), N // 2), Wall(((M//2) + (M//8) + i+1), N//2), Wall(M//2 + i+1, (N//2) - (N//3)), Wall(
                (3*M)//4 + i+1, N//6 + 5), Wall(M//4 + i+1, N//6 + 5), Wall(((M//2) - (M//8) + i+1), N//4 + 5), Wall(((M//2) + (M//8) + i+1), N//4 + 5), Wall(M//2 + i+1, N//2 + 5)])
            self._walls.extend([Wall(M//2 - i, N//3), Wall(((M//2) - (M//8) - i), N // 2), Wall(((M//2) + (M//8) - i), N//2), Wall(M//2 - i, (N//2) - (N//3)), Wall(
                (3*M)//4 - i, N//6 + 5), Wall(M//4 - i, N//6 + 5), Wall(((M//2) - (M//8) - i), N//4 + 5), Wall(((M//2) + (M//8) - i), N//4 + 5), Wall(M//2 - i, N//2 + 5)])

        for i in range(4):
            self._walls.extend(
                [Wall(M//2 - 7, N//4 + i), Wall(M//2 + 7, N//4 + i)])
            self._walls.extend(
                [Wall(M//2 - 7, N//4 - i - 1), Wall(M//2 + 7, N//4 - i - 1)])

        self._wizardTowers = [WizardTower(
            (3*M)//4, N//2 - N//10), WizardTower(M//4, N//2 - N//10)]

        return

    def get_spawning(self):
        return self._spawning

    def get_matrix(self):
        return self._matrix

    def get_cannons(self):
        return self._cannons

    def print_village(self):
        '''Print the village'''
        for row in range(self._rows):
            for col in range(self._cols):
                # print(type(self._matrix[row, col]), end="")
                if (self._matrix[row, col]):
                    # if(self._matrix[row, col] and self._matrix[row, col].get_display()):
                    print(self._matrix[row, col].get_object(), end="")
                else:
                    print(' ', end="")
            print()
        return

    def update_matrix(self, building):
        # self._matrix = building.set_object(self)
        if building.get_display():
            self._matrix[building.gety() - (building.get_ydim()//2): building.gety() + (building.get_ydim()//2) + 1,
                         building.getx() - (building.get_xdim()//2): building.getx() + (building.get_xdim()//2) + 1] = building
        else:
            self.delete_building(building)
        # print(building.getx() - (building.get_xdim()//2), building.getx() + (building.get_xdim()//2), building.gety() -
        #       (building.get_ydim()//2), building.gety() + (building.get_ydim()//2), building.get_object())
        return

    def update_village(self):
        for spawning in self._spawning:
            self.update_matrix(spawning)
        for hut in self._huts:
            self.update_matrix(hut)
        self.update_matrix(self._townhall)
        for cannon in self._cannons:
            self.update_matrix(cannon)
        for wall in self._walls:
            self.update_matrix(wall)
        for tower in self._wizardTowers:
            self.update_matrix(tower)
        return

    def update_people(self, person):
        if person.is_dead():
            self.delete_people(person)
        else:
            self._matrix[person.getx(), person.gety()] = person
        return

    def delete_people(self, person):
        self._matrix[person.getx(), person.gety()] = np.empty(0, dtype=object)
        return

    def delete_building(self, building):
        self._matrix[building.gety() - (building.get_ydim()//2): building.gety() + (building.get_ydim()//2) + 1, building.getx() - (
            building.get_xdim()//2): building.getx() + (building.get_xdim()//2) + 1] = np.empty((), dtype=object)
        return

    def all_dead(self):
        for hut in self._huts:
            if hut.get_display():
                return False
        if self._townhall.get_display():
            return False
        for cannon in self._cannons:
            if cannon.get_display():
                return False
        for tower in self._wizardTowers:
            if tower.get_display():
                return False
        return True

    def get_all(self):
        buildings = []
        buildings.extend(self._huts)
        buildings.append(self._townhall)
        buildings.extend(self._cannons)
        buildings.extend(self._wizardTowers)
        return buildings

    def get_defensive(self):
        buildings = []
        buildings.extend(self._cannons)
        buildings.extend(self._wizardTowers)
        return buildings

    def get_towers(self):
        return self._wizardTowers
