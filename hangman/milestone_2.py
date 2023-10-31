import random

word_list = ["apple", "banana", "pear", "grape", "strawberry"]
word = random.choice(word_list)

guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")

#print(word)