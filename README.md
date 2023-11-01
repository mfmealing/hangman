# Hangman

## Project description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. 
This is an implementation of the hangman game, where the computer thinks of a word and the user tries to guess it.
Currently the user is asked to input a letter, this letter is checked to be alphabetical and length 1, and then it is compared to a random word to see if the letter is within this. If the letter is correct, the letter is added to a blank array that will spell out the letter when complete. If incorrect, a life will be lost. The user will be told whther the answer is correct or not and how many lives remain.

## Installation and usage
All files are currently Python files and so can simply be downloaded to run. All modules used are from those pre-installed within Python.

## File structure
All Python files are found within the folder "hangman".  
milestone_2.py asks a user to input a single letter and this is checked to be length one and alphabetical.  
milestone_3.py expands upon this, and takes this checked letter (once chnaged to lowercase) and compares it to a randomly generated word to see if the letter is in it, telling the user the outcome.  
milestone_4.py once again expands on this, creating a class to house the functions. Lives are now included, and a life is lost when a letter that isn't in the word is entered. Correct inputs are now added to an array that will spell the word when all letters are entered, and letters are checked to make sure the same letter isn't input twice.  

## License information
