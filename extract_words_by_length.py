if __name__ == "__main__":
    print("This short program reads from a dictionary file and output a new dictionary file")
    print("where each word have only a particular number of letters")
    num_letters_input = input("Enter number of letters a word in the new dictionary should have: ")
    num_letters = int(num_letters_input)
    if (num_letters <= 0):
        print("number of letteers is negative or zero. Please input a positive number.")
        exit()

    file_name = input("Enter file name to read in the dictionary: ")
    dict_file = open(file_name)
    new_dict_file = open("dictionary_" + str(num_letters) + "_letters.txt", "w")

    for line in dict_file:
        word = line.strip()
        if (len(word) == num_letters):
            new_dict_file.write(word + "\n")

    dict_file.close()
    new_dict_file.close()
   