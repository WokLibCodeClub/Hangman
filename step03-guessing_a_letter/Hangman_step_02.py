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
  |/    |
  |
  |
  |
  |
__|__
""",
"""
  _______
  |/    |
  |     O
  |
  |
  |
__|__
""",
"""
  _______
  |/    |
  |     O
  |     |
  |     |
  |
__|__
""",
"""
  _______
  |/    |
  |     O
  |   --|
  |     |
  |
__|__
""",
"""
  _______
  |/    |
  |     O
  |   --|--
  |     |
  |
__|__
""",
"""
  _______
  |/    |
  |     O
  |   --|--
  |     |
  |    /
__|__
""",
"""
  _______
  |/    |
  |     O
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

#############################################
# MAIN CODE
#############################################

# This next line clears the display area so you can draw the new
# picture in the same place as the previous one without the
# display scrolling. It works in Trinket but doesn't work in all Python settings.
system('cls')

# Display the first picture (just the gallows and no body parts)
print(pictures[0])

# Print the mystery word with underscores and spaces instead of letters
print(' '.join(word_with_guesses))


