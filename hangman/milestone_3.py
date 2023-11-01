import random

fruit_list = ["apple", "banana", "pear", "grape", "strawberry"]
fruit_word = random.choice(fruit_list)

def check_guess(guess):
    guess_lower = guess.lower()
    if guess_lower in fruit_word:
        print("Good guess! ", guess_lower, " is in the word.")
    else:
        print("Sorry, ", guess_lower, " is not in the word. Try again.")

def ask_for_input():
    while True:
        letter_guess = input("Please enter a single letter: ")
        if len(letter_guess) == 1 and letter_guess.isalpha() == True:
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(letter_guess)

ask_for_input()