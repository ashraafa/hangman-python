import gspread
from google.oauth2.service_account import Credentials
import random
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
"""
Constants for declaring API credentials and accessing the
the Google workbook
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_python')

"""
Constants for accessing worksheets in the Google workbook
"""
ANIMALS = SHEET.worksheet('animals').get_all_values()
CARS = SHEET.worksheet('cars').get_all_values()
MOVIES = SHEET.worksheet('movies').get_all_values()
SPORTS = SHEET.worksheet('sports').get_all_values()
HARD = SHEET.worksheet('hard').get_all_values()
LEADERBOARD = SHEET.worksheet('leaderboard').get_all_values()

"""
Variables to declare a new list from the default nested list
retrieved by the API
"""
animals = [x for list in ANIMALS for x in list]
cars = [x for list in CARS for x in list]
movies = [x for list in MOVIES for x in list]
sports = [x for list in SPORTS for x in list]
hard = [x for list in HARD for x in list]

def get_random_word(category):
    """
    Function to retrieve a random word based on the category 
    selected by the player
    """
    game_word = random.choice(category).upper()
    return game_word


def clear_terminal():
    """
    Function to clear terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

play_game = ""
player_guess = ""
letters_guessed = []
words_guessed = []

def welcome():
    """
    Welcome screen for user to enter name
    """
    print(
    """
     _   _      _      _   _     ____    __  __      _      _   _     
    |'| |'| U  /"\  u | \ |"| U /"___|uU|' \/ '|uU  /"\  u | \ |"|    
 /| |_| |\ \/ _ \/ <|  \| |>\| |  _ /\| |\/| |/ \/ _ \/ <|  \| |>   
   U|  _  |u / ___ \ U| |\  |u | |_| |  | |  | |  / ___ \ U| |\  |u   
    |_| |_| /_/   \_\ |_| \_|   \____|  |_|  |_| /_/   \_\ |_| \_|    
    //   \\  \\    >> ||   \\,-._)(|_  <<,-,,-.   \\    >> ||   \\,-. 
   (_") ("_)(__)  (__)(_")  (_/(__)__)  (./  \.) (__)  (__)(_")  (_/ 

    """
    )
    print(
    """
                         HANGMAN RULES
    1. The computer randomly generates a word from the category selected.
    2. You have 6 attempts to quess the correct word using either a single 
       letter or the complete word.
    3. The secret word has "_" as a placeholder to represent thes number of 
       letters.
    4. The computer will not penalize if you enter a letter or word that has
       been previously used.
    """
    )

    input("Press any key to continue...")
    clear_terminal()
    get_user()
    

def get_user():
    """
    Function to validate and return a username
    """

    while True:
        player_name = input("Please enter a username with less than 10 characters from the alphabet only...\n").upper()
        user_validation(player_name)
        
        if not player_name.isalpha() and len(player_name) < 10:
            player_name = ""
        else:
            clear_terminal()
            game_category(player_name)
            return player_name
"""
def player_options(player_name):

    Function to present player with options
    
    print(f"Welcome {player_name}\n")
    print("Enter 1 to Play Game")
    print("Enter 2 to View Leaderboard\n")

    input_choice = False

    while not input_choice:
        user_choice = input("Enter your selection below\n")

        if user_choice == "1":
            input_choice = True
            clear_terminal()
            game_category(player_name)
        elif user_choice == "2":
            input_choice = True
            clear_terminal()
            get_leaderboard()
        else:
            print(f"You entered {user_choice}. Only numbers 1 or 2 is allowed\n")
    return user_choice
"""  


def game_category(player_name):
    """
    Function to present player with player game category options
    """
    print(f"{player_name}, please select 1 of 5 options below. If you're feeling lucky, choose the Hard option\n")
    print("Enter 1 for Animals")
    print("Enter 2 for Cars")
    print("Enter 3 for Movies")
    print("Enter 4 for Sports")
    print("Enter 5 for Hard\n")

    input_category = False

    while not input_category:
        category_choice = input("Enter your category selection below\n")
        
        if category_choice == "1":
            category = animals
            input_category = True
            play_game = "Y"
            clear_terminal()
            play_hangman(player_name, play_game, category)
        elif category_choice == "2":
            category = cars
            input_category = True
            play_game = "Y"
            clear_terminal()
            play_hangman(player_name, play_game, category)
        elif category_choice == "3":
            category = movies
            input_category = True
            play_game = "Y"
            clear_terminal()
            play_hangman(player_name, play_game, category)
        elif category_choice == "4":
            category = sports
            input_category = True
            play_game = "Y"
            clear_terminal()
            play_hangman(player_name, play_game, category)
        elif category_choice == "5":
            category = hard
            input_category = True
            play_game = "Y"
            clear_terminal()
            play_hangman(player_name, play_game, category)
        else:
            print(f"You entered {category_choice}. Only numbers 1 to 5 is allowed\n")
 
    return category
    
def user_validation(player_name):
    """
    Function to validate the input received from the user
    """
    try:
        if not player_name.isalpha():
            raise ValueError(
                f" You can only enter letters. You entered {player_name}"
            )
        elif len(player_name) > 10:
            raise ValueError(
                f" You are only allowed 10 letters. You entered: {len(player_name)}"
            )

    except ValueError as e:
        print(f"{e}\n")

def input_validation(player_guess, game_word):
    """
    Function to validate the input received from the user
    """
    try:
        if len(player_guess) < len(game_word) and len(player_guess) > 1 and player_guess.isalpha():
            raise ValueError(
                f" {player_guess} is shorter than the hidden word and not a single letter"
            )

        elif len(player_guess) > len(game_word) and len(player_guess) > 1 and player_guess.isalpha():
            raise ValueError(
                f" {player_guess} is longer than the hidden word and not a single letter"
            )

        elif not player_guess.isalpha() or player_guess == 1:
            raise ValueError(
                f" You can only enter letters. You entered {player_guess}"
            )
        
        elif player_guess in letters_guessed:
            raise ValueError(
                f" You already guessed {player_guess}"
            )
        
        elif player_guess in words_guessed:
            raise ValueError(
                f" You already guessed {player_guess}"
            )

    except ValueError as e:
            print(f"{e}\n")

def player_won(player_name, game_word):
    print(
        """
          __   __   U  ___ u   _   _                     U  ___ u  _   _     
          \ \ / /    \/"_ \/U |"|u| |     __        __    \/"_ \/ | \ |"|    
           \ V /     | | | | \| |\| |     \"\      /"/    | | | |<|  \| |>   
          U_|"|_u.-,_| |_| |  | |_| |     /\ \ /\ / /\.-,_| |_| |U| |\  |u   
            |_|   \_)-\___/  <<\___/     U  \ V  V /  U\_)-\___/  |_| \_|    
        .-,//|(_       \\   (__) )(      .-,_\ /\ /_,-.     \\    ||   \\,-. 
         \_) (__)     (__)      (__)      \_)-'  '-(_/     (__)   (_")  (_/  
        """
    )

    print(f" Well done {player_name}! The correct word was {game_word}\n")
    print(f" Would you like to continue: Y/N\n")

    input_continue = False

    while not input_continue:
        continue_choice = input("Enter your selection below\n").upper()

        if continue_choice == "Y":
            continue_choice = True
            clear_terminal()
            game_category(player_name)
        elif continue_choice == "N":
            input_choice = True

            clear_terminal()
            welcome()
        else:
            print(f"You entered {continue_choice}. Only letters Y or N is allowed\n")
    return continue_choice

    

def player_lost(player_name, game_word):
    print(
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """
    )

    print(f" You lost {player_name}! The correct word was {game_word}\n")
    print(f" Would you like to try again: Y/N\n")

    input_continue = False

    while not input_continue:
        continue_choice = input("Enter your selection below\n").upper()

        if continue_choice == "Y":
            continue_choice = True
            clear_terminal()
            game_category(player_name)
        elif continue_choice == "N":
            input_choice = True
            clear_terminal()
            welcome()
        else:
            print(f"You entered {continue_choice}. Only letters Y or N is allowed\n")

    return continue_choice

def play_hangman(player_name, play_game, category):
    """
    Function to play game using the random word generated from 
    get_random_word. 
    """
    attempts = 0
    game_word = get_random_word(category)
    display_word = "_" * len(game_word)

    print(f" Word to guess: {game_word}\n")
    print(display_hangman(attempts))

    while play_game == "Y" and attempts <= 5:
        player_guess = input("Please guess a single letter or take a chance trying the complete word\n").upper()
        clear_terminal()
        input_validation(player_guess, game_word)
     
        if len(player_guess) == len(game_word) and player_guess != game_word and player_guess.isalpha() and player_guess not in words_guessed:
            words_guessed.append(player_guess)
            attempts += 1
            print(f" {player_guess} is not the hidden word {player_name}. You have depleted {attempts} of 6 attempts!")
        
        elif len(player_guess) == len(game_word) and player_guess == game_word:
            letters_guessed.clear()
            words_guessed.clear()
            player_won(player_name, game_word)
        
        elif len(player_guess) == 1 and player_guess.isalpha() and player_guess not in letters_guessed:
            for letter in player_guess:
                letters_guessed.append(player_guess)
                if letter not in game_word:
                    attempts += 1
                    print(f" {player_guess} is not a letter in the hidden word {player_name}. You have depleted {attempts} of 6 attempts!")
                elif letter in game_word:
                    index = [i for i, l in enumerate(game_word) if l == player_guess]
                    for i in index:
                        display_word = display_word[:i] + player_guess + display_word[i+1:]
                    print(f" Nice one {player_name}! You have depleted {attempts} of 6 attempts.")
                    if "_" not in display_word:
                         letters_guessed.clear()
                         words_guessed.clear()
                         player_won(player_name, game_word)

        print(display_hangman(attempts))
        print(f" Hidden Word: "+" ".join(display_word) + "\n")
        print(f" Words Guessed: "+" ".join(words_guessed) + "\n")
        print(f" Letters Guessed: "+" ".join(sorted(letters_guessed)) + "\n")  
      
    else:
        letters_guessed.clear()
        words_guessed.clear()
        clear_terminal()
        player_lost(player_name, game_word)

def end_game(play_game):
    """
    Function to disaply end of game screen
    """

    if play_game == "N":
            print(" Thank you for playing!")
    else:
        print("Would you like to continue")

def display_hangman(attempts):
    """
    Function to display hangman picture in ascending order
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



welcome()


            