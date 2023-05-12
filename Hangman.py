import random
import string

from Words import words

def get_valid_word (words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in thew word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters)) # the letters used

        word_list = [letter if letter in used_letters else '-' for letter in word] # showing user the current words they have guessed
        print("Current Word: ", ' '.join(word_list))
        # getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes away a life if wrong
                print("Letter not in the word")

        elif user_letter in used_letters:
            print("You have already used that letter. Please try again")

        else:
            print("Invalid letter, try again")

    if lives == 0:
        print("You Died, sorry the word was", word)

    else:
        print("You guessed the word", word, "!!!")

hangman()