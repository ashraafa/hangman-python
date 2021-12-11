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

def play_hangman():
    """
    Function to play game using the random word generated from 
    get_random_word. 
    """
    game_word = get_random_word(animals)
    display_word = "_" *len(game_word)
    letters_guessed = []
    words_guessed =[]
    attempts = 0

    print(f" Attempts: {attempts}\n")
    print(f" Word to guess: {game_word}\n")
    print(f" Words Guessed: {words_guessed}\n")
    print(f" Letters Guessed: {letters_guessed}\n")
    print(f" Your secret: "+" ".join(display_word) + "\n")

play_hangman()


