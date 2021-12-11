import gspread
from google.oauth2.service_account import Credentials
import random
import string

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
    game_word = random.choice(category)
    return game_word

game_word = get_random_word(animals)
play_game = "Y"
player_guess = ""
letters_guessed = []
words_guessed = []

def input_validation(player_guess):
    """
    Function to validate the input received from the user
    """
    try:
        if len(player_guess) < len(game_word) and len(player_guess) > 1 and player_guess.isalpha():
            raise ValueError(
                f" {player_guess} is shorter than the hidden word and not a single letter"
                )

        if len(player_guess) > len(game_word) and len(player_guess) > 1 and player_guess.isalpha():
            raise ValueError(
                f" {player_guess} is longer than the hidden word and not a single letter"
                )

        elif not player_guess.isalpha() or player_guess == 1:
            raise ValueError(
                f" You can only enter letters. You entered {player_guess}"
                )
        
        elif player_guess in letters_guessed or words_guessed:
            raise ValueError(
                f" You already guessed {player_guess}"
            )

    except ValueError as e:
            print({e})


def play_hangman():
    """
    Function to play game using the random word generated from 
    get_random_word. 
    """
    attempts = 0
    display_word = "_" * len(game_word)

    
    print(f" Attempts: {attempts}\n")
    print(f" Word to guess: {game_word}\n")
    print(f" Words Guessed: {words_guessed}\n")
    print(f" Letters Guessed: {letters_guessed}\n")
    print(f" Your secret: "+" ".join(display_word) + "\n")


    while play_game == "Y":
        player_guess = input("Please guess a single letter or take a chance with the complete word\n")

        input_validation(player_guess)
        
        if len(player_guess) == len(game_word) and player_guess != game_word and player_guess.isalpha() and player_guess in words_guessed:
            words_guessed.append(player_guess)
            print(f" {player_guess} is not the hidden word")
        
        elif len(player_guess) == len(game_word) and player_guess != game_word and player_guess.isalpha() and player_guess not in words_guessed:
            words_guessed.append(player_guess)
            attempts += 1
            print(f" Words Guessed: {words_guessed}")
            print(f" Your attempts: {attempts}\n")
            
            
        elif len(player_guess) == len(game_word) and player_guess == game_word:
                words_guessed.append(player_guess)
                print("Congrats you chose the correct word")
                print(words_guessed)
         
        elif len(player_guess) == 1 and player_guess.isalpha():
            for letter in player_guess:
                letters_guessed.append(player_guess)
                if letter in game_word:
                    index = [i for i, l in enumerate(game_word) if l == player_guess]
                    for i in index:
                        display_word = display_word[:i] + player_guess + display_word[i+1:]
                    print("Congrats you chose a correct letter")
                    print(f" Word: "+" ".join(display_word) + "\n")
                elif letter not in game_word or letters_guessed:
                    attempts += 1
                    print("Letter not in word")
                    print(attempts)
                    print(f" Guessed Letters: {letters_guessed}\n")


        else:
            print(str("Incorrect letter"))
            print(letters_guessed)

play_hangman()


            