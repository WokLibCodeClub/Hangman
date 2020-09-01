from random import choice
from os import system
from string import join


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

for p in pictures:
  system('cls')
  print(p)
  a = input()

    
