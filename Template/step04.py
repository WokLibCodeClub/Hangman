#!/bin/python3

from random import choice
from os import system

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

file = open('Hangman words.txt', 'r')
words = file.read().splitlines()
word_to_guess = choice(words)
#word_to_guess = "HANGMAN"

word_with_guesses = "_" * len(word_to_guess)
word_with_guesses = list(word_with_guesses)

winner = False
wrong_guesses = []
num_wrong_guesses = 0

print(pictures[num_wrong_guesses])
print("Word to guess:   " + ' '.join(word_with_guesses))

while True:
    
  a = input("\nGuess a letter: ")
  guess = a.upper()
  
  good_guess = False
  for i in range(len(word_to_guess)):
    if guess == word_to_guess[i]:
      word_with_guesses[i] = guess
      good_guess = True
  if "_" not in word_with_guesses:
    winner = True
  if good_guess == False:
    wrong_guesses.append(guess)
    num_wrong_guesses += 1

  system('cls')
  print(pictures[num_wrong_guesses])
  print("Word to guess:   " + ' '.join(word_with_guesses))
  if len(wrong_guesses) > 0:
    print("\nWrong guesses: " + ' '.join(wrong_guesses))
  
  if winner or num_wrong_guesses == 6:
    break

if winner:
  print("\nCONGRATULATIONS - you won!")
else:
  print("\nYou lost - the word was " + ' '.join(word_to_guess))

