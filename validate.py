import helpers

def user_validation(player_name):
    """
    Function to validate the input received from the user
    """
    try:
        if not player_name.isalpha():
            raise ValueError(
                f"You can only enter letters. You entered {player_name}".upper()
            )

        elif len(player_name) > 10:
            raise ValueError(
                f"You are only allowed 10 letters. You entered: {len(player_name)}".upper()
            )

    except ValueError as e:
        print(f" {helpers.colors.RED}{helpers.colors.BOLD}{e}{helpers.colors.RESET}\n") 

def input_validation(player_guess, game_word,letters_guessed, words_guessed):
    """
    Function to validate the input received from the user
    """
    try:
        if len(player_guess) < len(game_word) and len(player_guess) > 1 and player_guess.isalpha():
            raise ValueError(
                f"{player_guess} is shorter than the hidden word and not a single letter".upper()
            )

        elif len(player_guess) > len(game_word) and len(player_guess) > 1 and player_guess.isalpha():
            raise ValueError(
                f"{player_guess} is longer than the hidden word and not a single letter".upper()
            )

        elif not player_guess.isalpha() or player_guess == 1:
            raise ValueError(
                f"You can only enter letters. You entered {player_guess}".upper()
            )
        
        elif player_guess in letters_guessed:
            raise ValueError(
                f"You already guessed {player_guess}".upper()
            )
        
        elif player_guess in words_guessed:
            raise ValueError(
                f"You already guessed {player_guess}".upper()
            )

    except ValueError as e:
        print(f"{helpers.colors.RED}{helpers.colors.BOLD}{e}{helpers.colors.RESET}\n") 