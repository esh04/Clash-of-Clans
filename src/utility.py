from .game_over import game_over
from .input import *
import signal
import time
from .spells import heal, rage


def movement(game):
    # moves the player
    def alarmhandler(signum, frame):
        # ''' input method '''
        raise AlarmException

    def user_input(timeout=0.1):
        # ''' input method '''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = Get()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    INPUT_CHAR = user_input()
    char = INPUT_CHAR
    king = game.get_attackers().get_king()
    if char:
        # move king up
        if char == 'd':
            if(king.movement(0, 1, game.get_village())):
                return 1
        # move king left
        elif char == 'w':
            if(king.movement(-1, 0, game.get_village())):
                return 1
        # move king down
        elif char == 'a':
            if(king.movement(0, -1, game.get_village())):
                return 1
        # move king right
        elif char == 's':
            if(king.movement(1, 0,  game.get_village())):
                return 1
        # attack
        elif char == ' ':
            king.attack(game.get_village())
            return 1
        # spawning points
        elif char == '1' or char == '2' or char == "3" or char == "4":
            spawning_point = game.get_village().get_spawning()[int(char) - 1]
            x = game.get_attackers().barb_coord(
                spawning_point.getx(), spawning_point.get_xdim())
            y = game.get_attackers().barb_coord(
                spawning_point.gety(), spawning_point.get_ydim())
            game.get_attackers().set_barbarians(y, x)
            # print(x, y)
            return 1
        # quit
        elif char == 'q':
            game_over(game)
        elif char == 'h':
            heal(game)
            return 1
        elif char == 'r':
            rage(game)
            return 1

    return 0


# check if person is in cannon range, if yes then shoot

def cannon_shoot(game):
    shoot = False
    for cannon in game.get_village().get_cannons():
        # bool to check if shot is fired
        shoot = shoot or cannon.shoot(game)
    return shoot


def check_cannon(game):
    new_time = time.time() - game.get_starttime()
    if(new_time % 1 == 0):
        game.get_village().update_village()
        game.get_village().update_people(game.get_attackers().get_king())
        for barb in game.get_attackers().get_barbarians():
            game.get_village().update_people(barb)
        if (cannon_shoot(game)):
            return 1
