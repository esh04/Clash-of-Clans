from numpy import False_
from .game_over import game_over
from .input import *
import signal
import time
from .spells import heal, rage
from . import variables as v


def input():
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
    return user_input()


def movement(game):
    # moves the player

    char = input()
    if game.isQueen():
        king = game.get_attackers().get_queen()
    else:
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
        elif char == '1' or char == '2' or char == "3":
            if(len(game.get_attackers().get_barbarians()) < v.MAX_BARB):
                spawning_point = game.get_village().get_spawning()[
                    int(char) - 1]
                x = game.get_attackers().rand_coord(
                    spawning_point.getx(), spawning_point.get_xdim())
                y = game.get_attackers().rand_coord(
                    spawning_point.gety(), spawning_point.get_ydim())
                game.get_attackers().set_barbarians(y, x)
                return 1
            else:
                return 0
        elif char == '6' or char == '4' or char == "5":
            if(len(game.get_attackers().get_archers()) < v.MAX_ARCH):
                spawning_point = game.get_village().get_spawning()[
                    int(char) - 1]
                x = game.get_attackers().rand_coord(
                    spawning_point.getx(), spawning_point.get_xdim())
                y = game.get_attackers().rand_coord(
                    spawning_point.gety(), spawning_point.get_ydim())
                game.get_attackers().set_archers(y, x)
                return 1
            else:
                return 0

        elif char == '9' or char == '7' or char == "8":
            if(len(game.get_attackers().get_balloons()) < v.MAX_BALLOON):
                spawning_point = game.get_village().get_spawning()[
                    int(char) - 1]
                x = game.get_attackers().rand_coord(
                    spawning_point.getx(), spawning_point.get_xdim())
                y = game.get_attackers().rand_coord(
                    spawning_point.gety(), spawning_point.get_ydim())
                game.get_attackers().set_balloons(y, x)
                return 1
            else:
                return 0

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


def troop_move(game):
    barbarians = game.get_attackers().get_barbarians()
    archers = game.get_attackers().get_archers()
    balloons = game.get_attackers().get_balloons()
    move = False_
    for barb in barbarians:
        if not barb.is_dead():
            barb.auto_move(game)
            move = True
    for archer in archers:
        if not archer.is_dead():
            archer.auto_move(game)
            move = True
    for balloon in balloons:
        if not balloon.is_dead():
            balloon.auto_move(game)
            move = True
    return move


def check_shoot(game):
    shoot = False
    for cannon in game.get_village().get_cannons():
        # bool to check if shot is fired
        shoot = shoot or cannon.shoot(game)
    for archer in game.get_attackers().get_archers():
        shoot = shoot or archer.shoot(game)
    return shoot
