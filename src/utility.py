from .game_over import game_over
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

    # if barbarians are present then move them automatically
#     new_time = time.time() - start_time
# if(new_time % 1 == 0):
#     print(new_time)

    # check if person is in cannon range, if yes then shoot

    return 0
