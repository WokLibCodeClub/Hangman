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

#############################################
# MAIN CODE
#############################################

# This next line clears the display area so you can draw the new
# picture in the same place as the previous one without the
# display scrolling. It works in Trinket but doesn't work in all Python settings.
system('cls')

# This loop will print each of the pictures in the list pictures
# Click once in the Result window, then press any key to show the next picture
for p in pictures:
  system('cls')
  print(p)
  input()
  
