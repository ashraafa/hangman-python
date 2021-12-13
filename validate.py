import helpers

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
        print(f" {helpers.colors.RED}{e}{helpers.colors.RESET}\n") 

def input_validation(player_guess, game_word,letters_guessed, words_guessed):
    """
    Function to validate the input received from the user
    """
    try:
        if len(player_guess) < len(game_word) and len(player_guess) > 1 and player_guess.isalpha():
            raise ValueError(
                f" {player_guess} IS SHORTER THAN THE HIDDEN WORD AND NOT A SINGLE LETTER"
            )

        elif len(player_guess) > len(game_word) and len(player_guess) > 1 and player_guess.isalpha():
            raise ValueError(
                f" {player_guess} IS LONGER THAN THE HIDDEN WORD AND NOT A SINGLE LETTER"
            )

        elif not player_guess.isalpha() or player_guess == 1:
            raise ValueError(
                f" YOU CAN ONLY ENTER LETTERS. YOU ENTERED {player_guess}"
            )
        
        elif player_guess in letters_guessed:
            raise ValueError(
                f" YOU ALREADY GUESSED {player_guess}"
            )
        
        elif player_guess in words_guessed:
            raise ValueError(
                f" YOU ALREADY GUESSED {player_guess}"
            )

    except ValueError as e:
        print(f" {helpers.colors.RED}{e}{helpers.colors.RESET}\n") 