from .person import Person
from colorama import init, Fore, Back, Style


class Barbarian(Person):
    def __init__(self, x_cood, y_cood):
        damage = 5
        health = 80
        speed = 1
        self._body = Fore.MAGENTA + 'B' + Fore.RESET
        Person.__init__(self, x_cood, y_cood, damage, health, speed)

    def get_object(self):
        return self._body
