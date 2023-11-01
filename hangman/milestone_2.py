import random

fruit_list = ["apple", "banana", "pear", "grape", "strawberry"]
fruit_word = random.choice(fruit_list)

letter_guess = input("Please enter a single letter: ")
if len(letter_guess) == 1 and letter_guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
