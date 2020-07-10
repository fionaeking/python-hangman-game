from constants import NUM_LIVES


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
        hangman = self.print_hangman(correct_letters)
        lives = NUM_LIVES
        while "*" in hangman and lives > 0:
            # save list of letters guessed correctly
            guess = input("Please enter your next guess: ")
            if guess.isalpha() and guess in self.word_to_guess:
                correct_letters.append(guess)
            else:
                lives -= 1
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
