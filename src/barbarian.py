from .buildings import Building, Wall
from .validation import isvalid
from .person import Person
from colorama import init, Fore, Back, Style
from . import variables as v


class Troops(Person):
    def __init__(self, x_cood, y_cood, damage, health, speed, body):
        self._body = body
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
                # attack if not the troop is not archer
                if (isinstance(self, Archer) == False):
                    if game.get_village().get_matrix()[self.getx() + movex][self.gety() + movey].get_display():
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
            if building.get_display():
                dist = self.distance(building)
                if dist < nearest_dist:
                    nearest_building = building
                    nearest_dist = dist
                # print(building.get_object(), dist,
                #       building.getx(), building.gety())
        return nearest_building

    def find_nearest_defensive(self, village):
        nearest_dist = 1000000
        nearest_building = None
        for building in village.get_defensive():
            if building.get_display():
                dist = self.distance(building)
                if dist < nearest_dist:
                    nearest_building = building
                    nearest_dist = dist
                # print(building.get_object(), dist,
                #       building.getx(), building.gety())
        return nearest_building


class Barbarian(Troops):
    def __init__(self, x_cood, y_cood):
        damage = v.BARB_DAMAGE
        health = v.BARB_HEALTH
        speed = v.BARB_MOVT
        body = Fore.MAGENTA + 'B' + Fore.RESET
        Troops.__init__(self, x_cood, y_cood, damage, health, speed, body)


class Balloon(Troops):
    def __init__(self, x_cood, y_cood):
        damage = v.BARB_DAMAGE*2
        health = v.BARB_HEALTH
        speed = v.BARB_MOVT*2
        body = Fore.MAGENTA + 'X' + Fore.RESET
        Troops.__init__(self, x_cood, y_cood, damage, health, speed, body)

    def auto_move(self, game):
        nearest_building = self.find_nearest_defensive(game.get_village())
        if nearest_building is None:
            nearest_building = self.find_nearerst(game.get_village())
        # move towards the nearest building
        x = nearest_building.gety() - self.getx()
        y = nearest_building.getx() - self.gety()

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

        if isvalid(self.getx() + movex, self.gety() + movey):
            if isinstance(game.get_village().get_matrix()[self.getx() + movex][self.gety() + movey], Building):
                if (isinstance(game.get_village().get_matrix()[self.getx() + movex][self.gety() + movey], Wall)):
                    # fly over wall
                    self.movement(2*movex, 2*movey, game.get_village())
                    return 1
                else:
                    if game.get_village().get_matrix()[self.getx() + movex][self.gety() + movey].get_display():
                        game.get_village().get_matrix()[
                            self.getx() + movex][self.gety() + movey].attacked(self._attack)
                        return 1
            elif(self.movement(movex, movey, game.get_village())):
                return 1
        return 0


class Archer(Troops):
    def __init__(self, x_cood, y_cood):
        damage = v.BARB_DAMAGE*0.5
        health = v.BARB_HEALTH*0.5
        speed = v.BARB_MOVT*2
        body = Fore.MAGENTA + 'A' + Fore.RESET
        self._range = 6
        Troops.__init__(self, x_cood, y_cood, damage, health, speed, body)

    def shoot(self, game):
        for i in range(-self._range, self._range + 1):
            for j in range(-self._range, self._range + 1):
                matrix = game.get_village().get_matrix()
                # king = game.get_attackers().get_king()
                if isinstance(matrix[self._x_cood + i][self._y_cood + j], Building):
                    matrix[
                        self._x_cood + i][self._y_cood + j].attacked(self._attack)
                    self._body = Fore.MAGENTA + 'A' + Fore.RESET
                    return True
        self._body = Fore.MAGENTA + 'A' + Fore.RESET
        return False
