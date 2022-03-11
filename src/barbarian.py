from .buildings import Building
from .validation import isvalid
from .person import Person
from colorama import init, Fore, Back, Style


class Barbarian(Person):
    def __init__(self, x_cood, y_cood):
        damage = 5
        health = 100
        speed = 1
        self._body = Fore.MAGENTA + 'B' + Fore.RESET
        Person.__init__(self, x_cood, y_cood, damage, health, speed)

    def get_object(self):
        if self.get_health_percentage() <= 0:
            self._dead = True
            return ' '
        if self.get_health_percentage() > 50:
            return Fore.MAGENTA + Style.BRIGHT + self._body + Fore.RESET + Style.RESET_ALL
        elif self.get_health_percentage() > 25:
            return Fore.MAGENTA + Style.NORMAL + self._body + Fore.RESET + Style.RESET_ALL
        else:
            return Fore.MAGENTA + Style.DIM + self._body + Fore.RESET + Style.RESET_ALL

    def auto_move(self, game):
        nearest_building = self.find_nearerst(game.get_village())
        # move towards the nearest building
        x = nearest_building.gety() - self.getx()
        y = nearest_building.getx() - self.gety()

        # print(nearest_building.getx(), nearest_building.gety(),
        #       nearest_building.get_object())
        # print(self.getx(), self.gety())

        if x > 0:
            movex = 1
        elif x < 0:
            movex = -1
        else:
            movex = 0
        if y > 0:
            movey = 1
        elif y < 0:
            movey = -1
        else:
            movey = 0
        # print(movex, movey)
        if isvalid(self.getx() + movex, self.gety() + movey):
            if isinstance(game.get_village().get_matrix()[self.getx() + movex][self.gety() + movey], Building):
                game.get_village().get_matrix()[
                    self.getx() + movex][self.gety() + movey].attacked(self._attack)
                return 1
            elif(self.movement(movex, movey, game.get_village())):
                return 1
        return 0

    def distance(self, building):
        x = building.gety() - self.getx()
        y = building.getx() - self.gety()
        return (x**2 + y**2)**0.5

    def find_nearerst(self, village):
        nearest_dist = 1000000
        nearest_building = None
        for building in village.get_all():
            dist = self.distance(building)
            if dist < nearest_dist:
                nearest_building = building
                nearest_dist = dist
            # print(building.get_object(), dist,
            #       building.getx(), building.gety())
        return nearest_building
