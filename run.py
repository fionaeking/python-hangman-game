import docx2txt
import os
import random

from constants import DOC_FILE, TEXT_FILE
from hangman import Hangman


def run():
    """
    Top-level method to run hangman game
    :return: None
    """
    create_text_file_if_reqd()
    chosen_word = select_random_word()
    h = Hangman(chosen_word)
    lives = h.play_hangman()
    if lives > 0:
        print("Congratulations, you win!")
    else:
        print(f"Sorry, you lost. The correct word was {chosen_word}")


def create_text_file_if_reqd():
    """
    If text file has not been supplied, creates txt file from docx
    file. Raises exception if neither a txt or docx file is supplied
    :return: None
    """
    if not os.path.isfile(TEXT_FILE):
        if os.path.isfile(DOC_FILE):
            with open(TEXT_FILE, "w+") as f:
                print(docx2txt.process(DOC_FILE), file=f)
        else:
            raise Exception("Missing word list text file")


def parse_text_file_as_list():
    """
    Reads in text file and writes to list, removing blank lines
    :return: List of words in text file
    """
    with open(TEXT_FILE, "r") as f:
        all_lines = (line.rstrip() for line in f)
        non_empty_lines = list(line for line in all_lines if line)
    f.close()
    return non_empty_lines


def select_random_word():
    """
    Reads input text file and returns random word from file
    :return: Random word from input file
    """
    input_words = parse_text_file_as_list()
    return str(random.choice(input_words))


if __name__ == '__main__':
    run()
