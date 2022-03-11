from colorama import init, Fore, Back, Style
import os
from . import variables as v
import pickle
init()


def game_over(game):

    os.system('tput reset')
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "                                                     ".center(v.SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "  _____                         ____                 ".center(v.SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          " / ____|                       / __ \                ".center(v.SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ".center(v.SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|".center(v.SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ".center(v.SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          " \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ".center(v.SCREEN))
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "                                                     ".center(v.SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "                                                     ".center(v.SCREEN)+Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
          "                                                     ".center(v.SCREEN)+Style.RESET_ALL)
    quit()
