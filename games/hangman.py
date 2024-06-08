import random

word_list = ["mustard", "beat", "rats", "option", "hangman", "school", "young", "minor", "chord", "choir", "discipline",
             "bagel", "raft", "disintegrate", "explode", "police", "shinji", "short", "access", "ballerina", "batman",
             "spiderman", "quicksilver", "aquaman", "michaelangelo", "grunge", "stork", "trident", "chemical"]


def print_board(incorrect):
    if incorrect == 0:
        print('''
              |------|
              |      |
              |
              |
              |
              |
        ______|_________
        ''')
    if incorrect == 1:
        print('''
                  |------|
                  |      |
                  |      0
                  |
                  |
                  |
            ______|_________
        ''')
    if incorrect == 2:
        print('''
                          |------|
                          |      |
                          |      0
                          |      |
                          |
                          |
                    ______|_________
        ''')
    if incorrect == 3:
        print('''
                          |------|
                          |      |
                          |      0
                          |     /|
                          |
                          |
                    ______|_________
        ''')
    if incorrect == 4:
        print('''
                          |------|
                          |      |
                          |      0
                          |     /|\
                          |
                          |
                    ______|_________
        ''')
    if incorrect == 5:
        print('''
                          |------|
                          |      |
                          |      0
                          |     /|\
                          |      |
                          |
                    ______|_________
        ''')
    if incorrect == 6:
        print('''
                          |------|
                          |      |
                          |      0
                          |     /|\
                          |      |
                          |     /
                    ______|_________
        ''')
    if incorrect == 7:
        print('''
                                  |------|
                                  |      |
                                  |      0
                                  |     /|\
                                  |      |
                                  |     / \
                            ______|_________
                ''')

def start_hangman():
    bad_guesses = 0
    print("Welcome to the Hangman")
    print(" ")
    hang_word = word_list[random.randint(0, len(word_list) - 1)]
    print(f"\033[1;31;40mCHEATER VISION: {hang_word} \033[0m")
    print("A word has been picked")
    while True:
        print_board(bad_guesses)
