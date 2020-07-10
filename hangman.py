from constants import NUM_LIVES


def ask_user_for_guess():
    return input("Please enter your next guess: ")


def print_lives(number_lives):
    print(f"Number of lives remaining: {number_lives}")


class Hangman:

    def __init__(self, chosen_word):
        self.word_to_guess = chosen_word

    def play_hangman(self):
        """
        Ask user for guesses. User has NUM_LIVES "lives". Game ends when word has been
        guessed correctly or if user guesses incorrectly NUM_LIVES times
        :return: Number of lives left at end of game
        """
        correct_letters = []
        wrong_letters = []
        hangman = self.print_hangman(correct_letters)
        lives = NUM_LIVES
        while "*" in hangman and lives > 0:
            print_lives(lives)
            guess = ask_user_for_guess()
            if guess.isalpha():
                if guess in self.word_to_guess:
                    # save list of letters guessed correctly
                    correct_letters.append(guess)
                elif guess in wrong_letters:
                    print("You've already guessed that letter!")
                else:
                    # save list of letters guessed incorrectly
                    wrong_letters.append(guess)
                    lives -= 1
            else:
                print("Please enter a valid letter")
            hangman = self.print_hangman(correct_letters)
        return lives

    def print_hangman(self, correct_letters):
        """
        Prints out current state of guessed word
        :param correct_letters: Correctly guessed characters
        :return: List of characters representing current state of guessed word
        """
        word_to_write = []
        for character in self.word_to_guess:
            if character in correct_letters:
                word_to_write.append(character)
            else:
                word_to_write.append("*")
        print("".join(val for val in word_to_write))
        return word_to_write
