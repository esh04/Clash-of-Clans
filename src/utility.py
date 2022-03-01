from .game_over import game_over
from .king import *
from .village import *
from .input import *
import signal


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
    if char:
        # move king up
        if char == 'd':
            if(game.get_king().movement(0, 1, game.get_village())):
                return 1
        # move king left
        elif char == 'w':
            if(game.get_king().movement(-1, 0, game.get_village())):
                return 1
        # move king down
        elif char == 'a':
            if(game.get_king().movement(0, -1, game.get_village())):
                return 1
        # move king right
        elif char == 's':
            if(game.get_king().movement(1, 0,  game.get_village())):
                return 1
        # attack
        elif char == ' ':
            game.get_king().attack(game.get_village())
            return 1
        # spawning point 1
        elif char == 'z':
            return 1
        # spawning point 2
        elif char == 'x':
            return 1
        # spawning point 3
        elif char == 'c':
            return 1
        # quit
        elif char == 'q':
            game_over()
    return 0
