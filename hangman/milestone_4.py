import random
fruit_list = ["apple", "banana", "pear", "grape", "strawberry"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess_lower = guess.lower()
        if guess_lower in self.word:
            print("Good guess! ", guess_lower, " is in the word.")
            for position, letter in enumerate(self.word):
                if letter == guess_lower:
                    self.word_guessed[position] = guess_lower
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print("Sorry, ", guess_lower, " is not in the word.")
            print("You have ", self.num_lives, " lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            guess_lower = guess.lower()
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess_lower in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess_lower)

fruits = Hangman(word_list=fruit_list)
fruits.ask_for_input()