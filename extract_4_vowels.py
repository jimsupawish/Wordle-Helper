from wordle_helper import get_word_set

def has_4_distinct_vowels(word):
    vowel_set = set()
    for letter in word:
        if letter in "aeiou":
            vowel_set.add(letter)
      
    return len(vowel_set) >= 4
            

if __name__ == "__main__":
    word_set = get_word_set()
    words_file = open("words_5_letters_4_vowels.txt", "w")

    for word in word_set:
        if has_4_distinct_vowels(word):
            words_file.write(f"{word}\n")

    words_file.close()