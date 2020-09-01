# Choosing the word to guess

In the rules of Hangman one player selects a mystery word - which has to be a normal dictionary word, not anyone or anything's name and not slang.

For the Python version we need a way for the computer to select a mystery word which fits the rules. The simplest way is to provide the code with a list of valid words, and have the computer select one at random.

In the starter project you will see, next to the tab titled ```main.py```, another tab titled ```Hangman words.txt```. If you click on this tab you will see a list of 400 words, all in capital letters, which are from six to 10 letters long and fit the rules. We will have the computer select a word at random from this list.

There are three stages to this

* open the file
* read the file into a list variable
* select at random an item from the list variable



The computer needs to select a mystery word for the player to guess.

# Displaying the word to guess

We need to display an underscore character for each letter in the mystery word. But how do we know how many letters it has?

[Go to Step 3 - Guessing a letter](../step03-guessing_a_letter/STEP3.md)

