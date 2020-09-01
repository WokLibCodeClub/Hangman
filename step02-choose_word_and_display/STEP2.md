# Choosing the word to guess

In the rules of Hangman one player selects a mystery word - which has to be a normal dictionary word, not anyone or anything's name and not slang.

For the Python version we need a way for the computer to select a mystery word which fits the rules. The simplest way is to provide the code with a list of valid words, and have the computer select one at random.

In the starter project you will see, next to the tab titled ```main.py```, another tab titled ```Hangman words.txt```. This refers to a computer *file* which has been uploaded to the Trinket project. If you click on this tab you will see a list of 400 words, all in capital letters, which are from six to 10 letters long and fit the rules. We will have the computer select a word at random from this list.

There are three stages to this

* open the file
* read the file into a list variable
* select at random an item from the list variable

(If you have done the Raspberry Pi/Code Club project called [Team Chooser](https://projects.raspberrypi.org/en/projects/team-chooser) you will already have seen this process in action.)

### Opening the file

In Python we often write code where we need to access some information from another file on the computer, or even a file on the worldwide web. If the file just contains text characters the Python command to open a file looks like this ```open('name of the file to be opened', 'method for opening file')```. We put the name of the file, inside single or double quotes, first inside the brackets, then the *"mode"* of opening, which means whether we just want to read data from the file ```'r'```, or add more data on to the end of the file ```'a'``` or write data to a completely new file ```'w'```.

In Trinket projects we can add files to the project, like the ```Hangman words.txt``` file, but if we weren't using Trinket we would have to indicate to the Python code which folder the file was located in.

For our code we need this line:
```
open('Hangman words.txt', 'r')
```
which opens the project file called ```Hangman words.txt```, and tells Python we just want to read data from the file.

The computer needs to select a mystery word for the player to guess.

# Displaying the word to guess

We need to display an underscore character for each letter in the mystery word. But how do we know how many letters it has?

[Go to Step 3 - Guessing a letter](../step03-guessing_a_letter/STEP3.md)

