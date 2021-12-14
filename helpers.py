import os


class COLORS:
    # Class with color variables defined for applying to text in the console

    RESET = '\33[0m'
    UNDERLINE = '\033[04m'
    BOLD = '\033[01m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    CYAN = '\033[36m'


def clear_terminal():
    """
    Function to clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def display_hangman(attempts):
    """
    Function to display hangman picture in ascending order
    when called by play_hangman() function.
    """
    hangman_pic = [
        """
        --------
        |      |
        |
        |
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |      |
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """
    ]

    return hangman_pic[attempts]