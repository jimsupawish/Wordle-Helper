import re

WORDS_SHOWN_CUTOFF = 50
WORDS_IN_ROW = 10

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


def print_possible_words(word_list):
    print("Number of possible words:", len(word_list))
    print("Possible words (only show the first", WORDS_SHOWN_CUTOFF, "words)")
    num_words_to_print = min(len(word_list), WORDS_SHOWN_CUTOFF)

    for i in range(num_words_to_print):
        if (i % WORDS_IN_ROW == (WORDS_IN_ROW - 1) or i == num_words_to_print - 1):
            print(word_list[i])
        else:
            print(word_list[i], end="     ")
    print()


# Get a list of 5-letter words to be used in Wordle
def get_word_set():
    word_file = open("dictionary_5_letters.txt")
    word_set = set()

    for line in word_file:
        word = line.strip()
        word_set.add(word)

    word_file.close()
    return word_set


def get_user_word(word_set):
    user_word = input("Enter the word you want to try: ")
    user_word = user_word.lower()
    wrong_format = re.match("[a-zA-Z]{5}", user_word) is None

    while (wrong_format or (user_word not in word_set)):
        if (wrong_format):
            print("Please enter a five-letter word with valid alphabetical characters.")
        else:
            print("The word", user_word, "is not a 5-letter word in the dictionary.")
        user_word = input("Enter the word you want to try: ")
        user_word = user_word.lower()
        wrong_format = re.match("[a-zA-Z]{5}", user_word) is None

    return user_word


def get_word_info():
    word_info = input("Enter the information about above word in I, O, X format: ")

    while (re.match("[IOX]{5}", word_info) is None):
        print("Please enter information with I, O, and X as characters (e.g. IOXXX)")
        word_info = input("Enter the information about above word in I, O, X format: ")

    return word_info.lower()


def check_match_condition(curr_word, user_word, word_info):
    for i in range(len(user_word)):
        if word_info[i] == "x" and curr_word.find(user_word[i]) != -1:
            return False
        elif word_info[i] == "i" and (curr_word[i] == user_word[i] or
                curr_word.find(user_word[i]) == -1):
            return False
        elif (word_info[i] == "o" and curr_word[i] != user_word[i]):
            return False

    return True


def find_possible_word_list(base_word_set, word_list):
    user_word = get_user_word(base_word_set)
    word_info = get_word_info()

    new_word_list = []

    for word in word_list:
        if (check_match_condition(word, user_word, word_info)):
            new_word_list.append(word)
    return new_word_list

def print_last_word(word_list):
    if len(word_list) == 1:
        print("Only possible word = " + word_list[0])
    else:
        print("No words found with the above plays.")
    print()

def get_play_again():
    play_again = input("Retry? Type ('Y' for yes and 'N' for no): ")
    while (play_again != "Y" and play_again != "N"):
        input("Retry? Type ('Y' for yes and 'N' for no): ")
    print()
    return play_again

if __name__ == "__main__":
    print_info()
    base_word_set = get_word_set()
    play_again = "Y"

    while (play_again != "N"):
        curr_word_list = list(base_word_set)
        print_possible_words(curr_word_list)

        while (len(curr_word_list) > 1):
            curr_word_list = find_possible_word_list(base_word_set, curr_word_list)
            print_possible_words(curr_word_list)

        print_last_word(curr_word_list)
        play_again = get_play_again()

    print("Thank you for using this program!")


