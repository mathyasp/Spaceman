'''Spaceman Assignment for ACS-1100'''
import random
import os


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
        string: The secret word to be used in the spaceman guessing game
    '''
    with open("words.txt", encoding="utf-8") as open_file:
        words_list = open_file.readlines()
    open_file.close()

    words_list = words_list[0].split(' ')
    secret = random.choice(words_list)
    return secret


def is_word_guessed(random_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TO DO: Loop through the letters in the secret_word
    # and check if a letter is not in lettersGuessed
    for letter in random_word:
        if letter not in letters_guessed:
            return False
        else:
            return True


def get_guessed_word(answer, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the 
    secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed 
        correctly, the string should contain the letter at the correct position.  
        For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # TO DO: Loop through the letters in secret word and build a string that
    # shows the letters that have been guessed correctly so far that are saved
    # in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_letters = ''
    for letter in answer:
        if letter in letters_guessed:
            guessed_letters += letter
        else:
            guessed_letters += '_'
    return guessed_letters


def is_guess_in_word(guess, correct_answer):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    # TO DO: check if the letter guess is in the secret word
    if guess in correct_answer:
        return True
    else:
        return False


def spaceman(random_secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    # TO DO: show the player information about the game according to the project spec
    print(
        "This is a game of Spaceman. See if you can guess the word.\n"
        "\nGuess a letter correctly, and you move on to the next round."
        "\nIf you guess incorrectly 7 times, you lose!\nIf you guess all the letters you win!\n"
        "\nEnter '1' at any time to quit.\n"
        )
    print(f"The secret word contains {len(random_secret_word)} letters")
    letters_guessed = ''

    guess_count = 0
    current_guess = ""
    guess = ""

    # TO DO: check if the game has been won or lost
    while current_guess != random_secret_word:
        guess = input('\nGuess a letter:\n')
        os.system('clear')

        if guess == "1":
            os.system('clear')
            print("Thanks for playing, please play again soon!")
            exit()

    # TO DO: Ask the player to guess one letter per round and check that it is only one letter
        if len(guess) > 1:
            print("Invalid guess, only one letter per guess.")
        else:

    # TO DO: Check if the guessed letter is in the secret or not and give the player feedback
            if is_guess_in_word(guess, random_secret_word) is True:
                print(f"\nCorrect, {guess} is in the secret word")
                letters_guessed += guess
            else:
                print(
                    f"\nIncorrect, {guess} is not in the secret word\n"
                    f"You have {6 - guess_count} guesses remaining."
                    )
                guess_count += 1
            if guess_count == 7:
                print("That's 7 guesses! Sorry, you lose")
                return

    # TO DO: show the guessed word so far
        current_guess = get_guessed_word(random_secret_word, letters_guessed)
        print(current_guess)
    print("Congrats, you win! You guessed the word correctly.")


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
