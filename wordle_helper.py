import re


def print_info():
    print("Welcome to Wordle Helper, a program that can help users find appropriate words to")
    print("answer on Wordle and provide insights into the possible words there are based on")
    print("the user input.")
    print()
    print("When prompted to enter the information about a word, please enter the following symbols:")
    print("O indicate that the corresponding letter is in a word and in the right spot.")
    print("I indicate that the corresponding letter is in a word but not in the right spot.")
    print("X indicate that the corresponding letter is not in the word in any spot.")
    print()


# Get a list of 5-letter words to be used in Wordle
def get_word_list():
    word_file = open("dictionary_5_letters.txt")
    word_list = set()

    for line in word_file:
        word = line.strip()
        word_list.add(word)

    word_file.close()
    return word_list


def get_user_word():
    user_word = input("Enter the word you want to try: ")

    while (len(user_word) != 5 and (not user_word.isalpha())):
        print("Please enter a five-letter word with valid alphabetical characters.")
        user_word = input("Enter the word you want to try: ")

    return user_word.lower()


def get_word_info():
    word_info = input("Enter the information about above word in I, O, X format: ")

    while (len(word_info) != 5 and re.match("[IOX]{5}") == None):
        print("Please enter information with I, O, and X as characters (e.g. IOXXX)")
        word_info = input("Enter the information about above word in I, O, X format: ")

    return word_info


def check_match_condition(curr_word, user_word, word_info):
    for i in range(len(user_word)):
        if word_info[i] == "X" and curr_word.find(user_word[i]) != -1:
            return False
        elif word_info[i] == "I":
            if (curr_word[i] == user_word[i] or curr_word.find(user_word[i]) == -1):
                return False
        elif (curr_word[i] == "O" and curr_word[i] != user_word[i]):
            return False

    return True


def find_possible_word_list(word_list):
    user_word = get_user_word()
    word_info = get_word_info()

    new_word_list = []

    for word in word_list:
        if (check_match_condition(word, user_word, word_info)):
            new_word_list.append(word)
    return new_word_list


if __name__ == "__main__":
    WORDS_SHOWN_CUTOFF = 20

    print_info()
    base_word_list = get_word_list()
    curr_word_list = list(base_word_list)
    print("Number of possible words:", len(curr_word_list))
    print()

    while (len(curr_word_list) > 1):
        curr_word_list = find_possible_word_list(curr_word_list)
        print("Number of possible words:", len(curr_word_list))

        if (len(curr_word_list) < WORDS_SHOWN_CUTOFF):
            print(curr_word_list)
        print()

    if len(curr_word_list) == 1:
        print(curr_word_list)


