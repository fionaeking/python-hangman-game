from constants import NUM_LIVES


def ask_user_for_guess():
    """
    Ask user to guess a letter. Only returns a valid
    alphabetical character
    :return: Valid letter guessed by user
    """
    guess = input("Please enter your next guess: ")
    while not guess.isalpha():
        guess = input("Please enter a valid letter: ")
    return guess.lower()  # convert to lower case


def print_lives(number_lives):
    """
    Print number of lives user has remaining
    :param number_lives: Integer
    """
    print(f"Number of lives remaining: {number_lives}")


class Hangman:
    """
    Class used to represent a game of hangman
    """

    def __init__(self, chosen_word):
        self.word_to_guess = chosen_word

    def play_hangman(self):
        """
        Ask user for guesses. User has NUM_LIVES "lives" initially. Game ends when
        word has been guessed correctly or if user guesses incorrectly NUM_LIVES times
        :return: Number of lives left at end of game
        """
        guessed_letters = []
        hangman = self.print_hangman(guessed_letters)
        lives = NUM_LIVES
        while "*" in hangman and lives > 0:
            print_lives(lives)
            guess = ask_user_for_guess()
            # if guess has already been guessed
            if guess in guessed_letters:
                print("You've already guessed that letter!")
            else:
                # save list of letters guessed
                guessed_letters.append(guess)
                if guess not in self.word_to_guess:
                    lives -= 1
            hangman = self.print_hangman(guessed_letters)
        return lives

    def print_hangman(self, letters_guessed):
        """
        Prints out current state of guessed word
        :param letters_guessed: Guessed characters
        :return: List of characters representing current state of guessed word
        """
        word_to_write = []
        for character in self.word_to_guess:
            if character in letters_guessed:
                word_to_write.append(character)
            else:
                word_to_write.append("*")
        print("".join(val for val in word_to_write))
        return word_to_write
