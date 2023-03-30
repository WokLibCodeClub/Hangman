#!/bin/python3

from random import choice
from os import system

#############################################
# VARIABLES
#############################################

# The items in this list are pictures made up from text characters like
# _ and |. Each of the items in the list is enclosed in triple quote marks.
# This means any new line characters you type inside the triple quotes will
# be shown as new lines when Python prints the text.
pictures = [
"""
  _______
  | /   |
  |/
  |
  |
  |
__|__
""",
"""
  _______
  | /   |
  |/    O
  |
  |
  |
__|__
""",
"""
  _______
  | /   |
  |/    O
  |     |
  |     |
  |
__|__
""",
"""
  _______
  | /   |
  |/    O
  |   --|
  |     |
  |
__|__
""",
"""
  _______
  | /   |
  |/    O
  |   --|--
  |     |
  |
__|__
""",
"""
  _______
  | /   |
  |/    O
  |   --|--
  |     |
  |    /
__|__
""",
"""
  _______
  | /   |
  |/    O
  |   --|--
  |     |
  |    / \\
__|__
"""]

# Code to open file Hangman_words.txt and select a word at random
wordfile = open('Hangman_words.txt', 'r')
wordlist = wordfile.read().splitlines()
word_to_guess = choice(wordlist)

# Make a text variable called word_with_guesses which is the
# same length as word_to_guess but has an underscore instead of each letter.
word_with_guesses = "_" * len(word_to_guess)

# Turn the text variable word_with_guesses into a list
word_with_guesses = list(word_with_guesses)

num_wrong_guesses = 0
wrong_guesses_list = []

#############################################
# MAIN CODE
#############################################

# This next line clears the display area so you can draw the new
# picture in the same place as the previous one without the
# display scrolling. It works in Trinket but doesn't work in all Python settings.
system('cls')

# Display the first picture (just the gallows and no body parts)
print(pictures[0])

# Give away the mystery word
print('Mystery word:', word_to_guess, '\n')

# Print the mystery word with underscores and spaces instead of letters
print(' '.join(word_with_guesses))

# Beginning of code for player's guess
a = input("\nGuess a letter: ")
a = a.upper()
good_guess = False

# Loop to go through all the letters in mystery word
for letter in range(len(word_to_guess)):
  if word_to_guess[letter] == a:
    # if it's a good guess then change the value of the Boolean variable
    good_guess = True
    # update the list variable with the correctly guessed letter
    word_with_guesses[letter] = a

# If good_guess is still False then the player's guess wasn't in the mystery word
if good_guess == False:
  # increase the number of wrong guesses by 1
  num_wrong_guesses += 1
  # add the wrong guess to the end of the list of wrong guesses
  wrong_guesses_list.append(a)
  
# Clear the display
system('cls')

# Display the correct picture for the number of wrong guesses
print(pictures[num_wrong_guesses])

# Give away the mystery word
print('Mystery word:', word_to_guess, '\n')

# Print the mystery word with underscores and spaces instead of letters
print(' '.join(word_with_guesses))

if len(wrong_guesses_list) > 0:
  print("\nWrong guesses so far: " + ' '.join(wrong_guesses_list))
