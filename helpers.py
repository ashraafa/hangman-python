import os

class colors:
    RESET = '\33[0m'
    UNDERLINE = '\033[04m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    LIGHTBLUE = '\033[94m'
    GREEN ='\033[32m'
    LIGHTGREEN ='\033[92m'

def clear_terminal():
    """
    Function to clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')