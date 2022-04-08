from .person import Person
from colorama import init, Fore, Back, Style
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


class ArcherQueen(Person):
    def __init__(self, x_cood, y_cood):
        damage = 8
        health = 200
        speed = 2
        self._body = Fore.YELLOW + 'Q' + Fore.RESET
        Person.__init__(self, x_cood, y_cood, damage, health, speed)

    def get_object(self):
        return self._body

    def health_bar(self):

        char = "+"
        health = (self.get_health_percentage()/100)*15
        health_bar = char * int(health) + (15-int(health))*" "
        return "Health of Archer Queen: |" + health_bar + '|'
