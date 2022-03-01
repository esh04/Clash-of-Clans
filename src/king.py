from .person import Person
from colorama import init, Fore, Back, Style
init()


class King(Person):
    def __init__(self, x_cood, y_cood):
        damage = 10
        health = 100
        speed = 1
        self._body = Fore.CYAN + 'K' + Fore.RESET
        Person.__init__(self, x_cood, y_cood, damage, health, speed)

    def get_object(self):
        return self._body
