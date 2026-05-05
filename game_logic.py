import random

from snowman import WORDS
from ascii_art import STAGES


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current game state for number of mistakes."""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_" + " "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """
    Main game loop.
    Game continues as long as stage 3 is not reached.
    :return: None
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < len(STAGES) - 1:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' was already guessed! Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("You saved the snowman from melting! The word was:", secret_word)
                return
        else:
            print("Wrong!")
            mistakes += 1

        display_game_state(mistakes, secret_word, guessed_letters)

    print("Game over! The snowman has melted. The word was:", secret_word)


def play_another_round():
    while True:
        rerun = input("Would you like to play again? (y/n): ").lower()
        if rerun == 'y':
            play_game()
        else:
            print("Thanks for playing!")
            break
