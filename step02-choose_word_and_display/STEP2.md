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

In Trinket projects we can add files to the project, like the ```Hangman words.txt``` file, but if we weren't using Trinket we would have to indicate to the Python code which folder on the computer's hard drive the file was located in.

For our game we need to add three lines of code after the end of the ```pictures``` list variable. The first line to add is:
```
wordfile = open('Hangman words.txt', 'r')
```
which opens the project file called ```Hangman words.txt```, tells Python we just want to read data from the file, and links the open file to a variable called ```wordfile```.

### Reading the list of words from the file

We need to make a **list** variable to hold the list of words. This example calls the variable ```wordlist``` but you can call yours whatever you like.

The code for reading the list of words from the file into the list variable is
```
wordlist = wordfile.read().splitlines()
```
The contents of the file are now added to the list variable ```wordlist```. The bit of code at the end of this line, ```.splitlines()```, tells Python that whenever the file has a new line (which is for every word) Python should make a new item in the list.

### Choosing a word at random from the list

This is the easiest of the three steps, because Python has a ready-made function for choosing an item at random from a list. The Python function is ```choice()``` where you put the name of the list variable inside the brackets. ```choice()``` is one of the functions contained in the ```random``` library, so if you want to use ```choice()``` in your code you have to **_import_** this library, which means at the top of your code you need to include the line
```
from random import choice
```
(this should already be in the starter project). 

We will put the random choice in another variable, which is called ```word_to_guess``` in this example. You can choose a different name if you want. Here is the line of code:
```
word_to_guess = choice(wordlist)
```

# Displaying the word to guess

We've now got the computer to choose a word for us to try and guess. Next we want the computer to display the word, but instead of each of the letters in the word we want the computer to print an underscore character. But if we just printed a number of underscore characters one after another they would run together to make a single line, and we wouldn't be able to see how many letters there are in the word to guess. So we need to display the word with an underscore instead of every letter, **_and_** a space between each underscore. How can we do that?



We need to display an underscore character for each letter in the mystery word. But how do we know how many letters it has?

[Go to Step 3 - Guessing a letter](../step03-guessing_a_letter/STEP3.md)

