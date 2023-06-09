#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    f = open(file_name, "r") #opening the file in read only mode
    l = f.readlines() #readlines() returns and array where each line is a value in an array
    f.close() #closing the file when I'm done
    return l


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    word = words[random.randint(0, len(words) -1)] #list index starts at 0 and so its max index is one lower than its size
    #selecting a random letter and replacing it with _, then printing
    letter = random.randint(0, len(word) -2)
    w = ""
    for i in range(len(word)):
        if i != letter:
            w += word[i]
        else:
            w += "_"
    print("Guess the word: " + w) 

    return word 


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    return input("Guess the missing letter: ")


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+ word )


if __name__ == "__main__":
    run_game('short_words.txt')

