import random
fruit_list = ["apple", "banana", "pear", "grape", "strawberry"]

class Hangman:
    '''
    This class plays a game of hangman with the user. A random word is selected and the user will input letters until either the word is guessed or all lives are lost

    Attributes:
    word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
    word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int - The number of lives the player has at the start of the game.
    word_list: list - A list of words
    list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        '''
        This function checks if the letter input by the user is in the randomly generated word after making it lowercase.
        If it is, its added to an array which displays _ for unguesed letters and all of the currently guessed letters.
        If it isn't, a life is lost.
        The user is told if they are correct or not.

        Args:
            guess (str): the single letter input by the user to be compared with the word
        '''
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
        '''
        This function checks if the user input letter is a single alphabetical value.
        It also checks if the letter has already been guessed before, as all letters that pass the initial check are added to a blank array of guessed letters.
        This will repeat until a correct input is given.
        '''
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