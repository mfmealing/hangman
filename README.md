# Hangman

## Project description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. 
This is an implementation of the hangman game, where the computer thinks of a word and the user tries to guess it.  
  
The user is asked to input a letter, this letter is checked to be alphabetical and length 1. It is also checked against any other previously guessed letters, so the same letter isn't guessed twice.
If the input is valid, it is then compared to a random word generated from a list of possible words.
If the letter is in the word, the letter will be added to an array which will spell out the word, with _ to indicate letters that have not yet been guessed.
If the letter is not in the word, a life will be lost. The user will be told whether the answer is correct or not and how many lives remain.
The user starts with 5 lives, if all 5 are lost, they lose the game. If all letters are guessed before they run out of lives, they win the game

## Installation and usage
All files are Python files and so can simply be downloaded to run. All modules used are from those pre-installed within Python.

## File structure
All Python files are found within the folder "hangman".  
  
milestone_2.py asks a user to input a single letter and this is checked to be length one and alphabetical.  
  
milestone_3.py expands upon this, and takes this checked letter (once changed to lowercase) and compares it to a randomly generated word to see if the letter is in it, telling the user the outcome.  
  
milestone_4.py once again expands on this, creating a class to house the functions. Lives are now included, and a life is lost when a letter that isn't in the word is entered. Correct inputs are now added to an array that will spell the word when all letters are entered, and letters are checked to make sure the same letter isn't input twice.  
  
milestone_5.py uses the class defined in milestone4, and adds a function in order to play the game. This function keeps track of lives and unguessed letters remaining. If the number of lives reaches 0, the player loses and if the number of unguessed letters reaches 0, the player wins.

## License information
Copyright (c) <2023>, <mfmealing>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
