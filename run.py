import random
import validate
import helpers
import api

"""
Variables that need to be declared for more than one function
"""
play_game = ""
player_guess = ""
letters_guessed = []
words_guessed = []

CATEGORY_MAPPER = {
    '1': api.animals,
    '2': api.cars,
    '3': api.movies,
    '4': api.sports,
    '5': api.hard,
}


def get_random_word(category):
    """
    Function to retrieve a random word based on the category
    selected by the player
    """
    game_word = random.choice(category).upper()
    return game_word


def welcome():
    """
    Function to display a welcome screen with the game rules
    """
    print(
        helpers.COLORS.YELLOW +
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
        helpers.COLORS.BLUE + helpers.COLORS.UNDERLINE + helpers.COLORS.BOLD +
        "HANGMAN RULES\n" + helpers.COLORS.RESET +
        """
      1. The computer randomly generates a word from the category selected.
      2. You have 6 attempts to guess the correct word using either a single
         letter or the complete word.
      3. The hidden word has "_" as a placeholder to represent the number of
         letters.
      4. The computer will not penalize if you enter a letter or word that has
         been previously used.
    """
    )

    input(helpers.COLORS.GREEN + "Press ENTER to continue..." +
          helpers.COLORS.RESET)
    helpers.clear_terminal()
    get_user()


def get_user():
    """
    Function to call user_validation() and return a validated
    username.
    Parse username to game_category()
    """
    while True:
        player_name = input(helpers.COLORS.GREEN +
                            "Please enter a username with a maximum of 10 "
                            "characters from the alphabet only.\n" +
                            helpers.COLORS.RESET).upper()
        helpers.clear_terminal()
        validate.user_validation(player_name)
        if not player_name.isalpha() or len(player_name) > 10:
            player_name = ""
        else:
            helpers.clear_terminal()
            game_category(player_name)
            return player_name


def game_category(player_name):
    """
    Function to present player with game category options.
    Parse player_name, play_game and category value to play_hangman()
    """
    print(f"{helpers.COLORS.BLUE}{helpers.COLORS.BOLD}{player_name}, "
          f"please select 1 of 5 options below. If you're feeling lucky, "
          f"choose the Hard option.{helpers.COLORS.RESET}\n")
    print("Enter " + helpers.COLORS.BLUE + helpers.COLORS.BOLD +
          "1 " + helpers.COLORS.RESET + "for " + helpers.COLORS.BLUE +
          helpers.COLORS.BOLD + "ANIMALS" + helpers.COLORS.RESET)
    print("Enter " + helpers.COLORS.BLUE + helpers.COLORS.BOLD +
          "2 " + helpers.COLORS.RESET + "for " + helpers.COLORS.BLUE +
          helpers.COLORS.BOLD + "CARS" + helpers.COLORS.RESET)
    print("Enter " + helpers.COLORS.BLUE + helpers.COLORS.BOLD +
          "3 " + helpers.COLORS.RESET + "for " + helpers.COLORS.BLUE +
          helpers.COLORS.BOLD + "MOVIES" + helpers.COLORS.RESET)
    print("Enter " + helpers.COLORS.BLUE + helpers.COLORS.BOLD +
          "4 " + helpers.COLORS.RESET + "for " + helpers.COLORS.BLUE +
          helpers.COLORS.BOLD + "SPORTS" + helpers.COLORS.RESET)
    print("Enter " + helpers.COLORS.BLUE + helpers.COLORS.BOLD +
          "5 " + helpers.COLORS.RESET + "for " + helpers.COLORS.BLUE +
          helpers.COLORS.BOLD + "HARD\n" + helpers.COLORS.RESET)

    input_category = False

    while not input_category:
        category_choice = input(helpers.COLORS.GREEN + "Enter your category"
                                " selection below:\n" + helpers.COLORS.RESET)
        if category_choice in CATEGORY_MAPPER:
            category = CATEGORY_MAPPER[category_choice]
            input_category = True
            play_game = "Y"
            helpers.clear_terminal()
            play_hangman(player_name, play_game, category)    
        else:
            print(f"{helpers.COLORS.RED}{helpers.COLORS.BOLD}You entered "
                  f"{category_choice}. Only numbers 1 to 5 are allowed\n")
    return category


def player_won(player_name, game_word):
    """
    Function to display message when a game is won
    and present user with option to continue or quit
    Parse player_name to game_category() function
    """
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
    print("Would you like to continue: Y/N\n")

    input_continue = False

    while not input_continue:
        continue_choice = input("Enter your selection below\n").upper()

        if continue_choice == "Y":
            input_continue = True
            helpers.clear_terminal()
            game_category(player_name)
        elif continue_choice == "N":
            input_continue = True

            helpers.clear_terminal()
            welcome()
        else:
            print(f"You entered {continue_choice}."
                  f"Only letters Y or N are allowed\n")
    return continue_choice


def player_lost(player_name, game_word):
    """
    Function to display message when a game is won
    and present user with option to continue or quit.
    Parse player_name to game_category() function.
    """
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
    print("Would you like to try again: Y/N\n")

    input_continue = False

    while not input_continue:
        continue_choice = input("Enter your selection below\n").upper()

        if continue_choice == "Y":
            input_continue = True
            helpers.clear_terminal()
            game_category(player_name)
        elif continue_choice == "N":
            input_continue = True
            helpers.clear_terminal()
            welcome()
        else:
            print(f"You entered {continue_choice}. Only letters \
                  Y or N is allowed\n")
    return continue_choice


def play_hangman(player_name, play_game, category):
    """
    Function to play game using the random word generated from
    get_random_word.
    Call the validate_input() function from validate.py
    Call the hangman_pic list in helpers.py for each increase in attempts made
    Populate declared variable list with words_guessed and letters_guessed
    by the player
    """
    attempts = 0
    game_word = get_random_word(category)
    display_word = "_" * len(game_word)

    print(f" Word to guess: {game_word}\n")
    print(helpers.COLORS.YELLOW + helpers.display_hangman(attempts) +
          helpers.COLORS.RESET)

    while play_game == "Y" and attempts <= 5:
        player_guess = input(helpers.COLORS.GREEN + "Please guess a single "
                             "letter or take a chance entering the complete "
                             "word\n" + helpers.COLORS.RESET).upper()
        helpers.clear_terminal()
        validate.input_validation(player_guess, game_word, letters_guessed,
                                  words_guessed)
        if len(player_guess) == len(game_word) and player_guess != game_word \
                and player_guess.isalpha() and player_guess not in \
                words_guessed:
            words_guessed.append(player_guess)
            attempts += 1
            print(f"{helpers.COLORS.BLUE}{helpers.COLORS.BOLD}{player_guess} "
                  f"is not the hidden word {player_name}. You have depleted "
                  f"{attempts} of 6 attempts!{helpers.COLORS.RESET}")
        elif len(player_guess) == len(game_word) and player_guess == game_word:
            letters_guessed.clear()
            words_guessed.clear()
            helpers.clear_terminal()
            player_won(player_name, game_word)
        elif len(player_guess) == 1 and player_guess.isalpha() \
                and player_guess not in letters_guessed:
            for letter in player_guess:
                letters_guessed.append(player_guess)
                if letter not in game_word:
                    attempts += 1
                    print(f"{helpers.COLORS.BLUE}{helpers.COLORS.BOLD}"
                          f"{player_guess} is not a letter in the hidden word "
                          f"{player_name}. You have depleted {attempts} of "
                          f"6 attempts!{helpers.COLORS.RESET}")
                elif letter in game_word:
                    index = [i for i, let in enumerate(game_word) if
                             let == player_guess]
                    for i in index:
                        display_word = display_word[:i] + player_guess \
                                       + display_word[i+1:]
                    print(f"{helpers.COLORS.BLUE}{helpers.COLORS.BOLD}Nice "
                          f" one {player_name}! You have depleted {attempts} "
                          f" of 6 attempts.{helpers.COLORS.RESET}")
                    if "_" not in display_word:
                        letters_guessed.clear()
                        words_guessed.clear()
                        helpers.clear_terminal()
                        player_won(player_name, game_word)

        print(helpers.COLORS.YELLOW + helpers.display_hangman(attempts) +
              helpers.COLORS.RESET)
        print(f"Hidden Word: {helpers.COLORS.CYAN} "+" "
              "".join(display_word) + "\n")
        print(f"{helpers.COLORS.RESET}Words Guessed: "
              f"{helpers.COLORS.CYAN} "+" ".join(words_guessed) + "\n")
        print(f"{helpers.COLORS.RESET}Letters Guessed: "
              f"{helpers.COLORS.CYAN} "+" ".join(sorted(letters_guessed)) +
              "\n" + helpers.COLORS.RESET)
    else:
        letters_guessed.clear()
        words_guessed.clear()
        helpers.clear_terminal()
        player_lost(player_name, game_word)


welcome()