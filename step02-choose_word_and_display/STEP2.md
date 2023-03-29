# Choosing the word to guess

In old-fashioned Hangman one player would choose a mystery word - which has to be a normal dictionary word, not anyone or anything's name and not slang - and the other player would try to guess it.

In the computer version the computer chooses the word and the player has to try and guess it.

In the starter project you will see a tab titled ```main.py```, and next to it another tab titled ```Hangman_words.txt```. This tab refers to a computer *file* which has been uploaded to the Trinket project. If you click on this tab you will see a list of 400 words, all in capital letters, which are from six to 10 letters long and fit the rules. We will have the computer select a word at random from this list as the mystery word to guess.

To do this we need to write code to

* open the ```Hangman_words.txt``` file
* read all 400 words from the file into a Python list
* select a word at random from this list as the mystery word

Each of these operations needs a single line of Python code.

## Opening the file

In Python we often write code where we need to access some information from another file on the computer, or even a file on the worldwide web. If the file just contains text characters we use the Python function ```open()```, and inside the brackets we put the name of the file, (which must be inside single or double quotes), then a comma,  then the *"mode"* of opening, which means whether we tell Python if we want to read data from the file (mode ```'r'```), or  start writing in a completely new file (mode ```'w'```), or add more data on to the end of an existing file (mode ```'a'```).

We usually link the opened file to a variable which is a *file* type of variable. Because we only want to read the data from the word list we will use the ```r``` mode. Here is the code for opening the file with a file variable called ```wordfile```. Put this line after the end of the ```pictures``` list:

```python
wordfile = open('Hangman_words.txt', 'r')
```

## Reading the words from the file into a Python list

We need to make a **list** variable to hold the list of words. In this example the list variable is called ```wordlist``` but you can choose your own name if you like.

The code for reading the list of words from the file into the list variable looks a bit complicated! It is

```python
wordlist = wordfile.read().splitlines()
```

Put this line after the previous line.

The middle part of this line is ```wordfile.read()``` which *reads* all the words from the file into Python storage, and the bit at the end ```.splitlines()``` means Python puts each line in the file into a different list item.

The beginning of this line ```wordlist =``` simply creates a list variable called ```wordlist``` which will hold all the words as a list. You could add a line of code to *print* this list if you want to see what it looks like.

## Choosing a word at random from the list

Python has a ready-made function for choosing an item at random from a list. The Python function is ```choice()``` where you put the name of the list variable inside the brackets. ```choice()``` is one of the functions contained in the ```random``` library, so if you want to use ```choice()``` in your code you have to ***import*** this library, which means at the top of your code you need to include the line

```python
from random import choice
```

(this should already be in the starter project). 

We will make a variable to hold the random choice, called ```word_to_guess``` in this example. You can choose a different name if you want. Here is the code:

```python
word_to_guess = choice(wordlist)
```

Put this after the lines to open the file and read the words into a list.

## Giving away the mystery word

Now we do something which seems a bit silly: we get the computer to display the mystery word. Add this line *as the last line in the project*:

```python
print("\nMystery word: ", word_to_guess)
```

This is obviously silly, as the game is to try and guess this word. However, when we are writing and testing the code it will be very useful to know what the word is, to check if our code works properly. And when the code is all working we will delete this line.

Note the text ```\n``` in the line above - this will print a blank line before displaying the word to guess.

## Displaying the mystery word during the game

As the player guesses letters which might be in the word the computer will display the mystery word with any correctly guessed letters in their correct places, and underscores for letters which haven't been guessed. We need to find a way to write code to do this. 

### Displaying the mystery word at the start of the game

At the start of the game none of the letters have been guessed, so we need to display the word with underscore characters for each letter.

How many underscores? Well, this will be the number of letters in the mystery word. We can easily find this out because text strings in Python are a lot like lists, and you probably know that the function for counting the number of items in a list is ```len()```. We can use the same function for counting the number of letters in a text string.

We will make a text variable to hold all the underscores, (and we will change the text in this variable as the player correctly guesses letters). If we want a text variable with, say,  eight underscores we can use multiplication! Yes, you can multiply text strings. The code ```'_' * 8``` would produce a text string with eight underscores. But we want to use the number of letters in the mystery word.

Add this line of code after the line which chooses the mystery word:

```python
word_with_guesses = '_' * len(word_to_guess)
```

which makes a text variable with one underscore for each letter in the mystery word.

### Turning the word with guesses into a list

It would be nice to display the underscores with a space between each, otherwise they would all run together and you wouldn't know how many letters there were. To do this we need to turn our text variable ```word_with_guesses``` into a **list** variable. There is a function to do this called ```list()```.

Put this line of code after the previous line:

```python
word_with_guesses = list(word_with_guesses)
```

### Displaying the word with guesses with spaces

Once we have our word with guesses as a list we can use a special list command for printing a list with spaces between each item. That command is ```' '.join()```. Now we can print our mystery word with underscores and spaces. Add this line at the end of the project just *before* the line where we give away the mystery word:

print(' '.join(word_with_guesses))

Run your code. Your display should look like this:



### How many letters are there in the word to guess?

First let's count how many letters there are in the word we have to guess. We can do this easily because text strings in Python are a lot like lists, and you probably know that the function for counting the number of items in a list is ```len()```. We can use the same function for counting the number of letters in a text string.

### Multiplication with text strings

**_What!!!!???_** Why would you want to do multiplication with text strings?

In fact you can use multiplication to create copies of a text string. If I had a text string ```"abc"``` and I multiplied it by three ```"abc" * 3``` the result would be a text string ```"abcabcabc"```. Here's how we can use this: we need a variable to contain the display with underscores; we need to count how many letters in the original word; then we make the word display variable equal to ```"_"``` (underscore character) multiplied by the number of letters in the original word.

### Turning a text string into a list

Our display text string now contains an underscore instead of each letter in the original word, and as the player makes successful guesses we would like to update this text string, replacing the underscores with the correctly guessed letters.

Unfortunately you can't easily just replace one character in a text string in Python. What you *can* do is convert the text string to a list, where each letter becomes a new item in the list, then you can change individual items as you like. If I have a string variable ```textstring``` and I want to convert it into a list variable ```textlist``` then I would use the code ```textlist = list(textstring)```.

### Printing a list with a space between each item

There is a special Python function called ```join()``` which lets you print a list with a text character between each item. If I want to print my list ```textlist``` with a *space* between each item I would use the code ```print(' '.join(textlist))```. Note the item in quotes before the word ```join``` - this shows the character we want to use to put in between each item in the list, which is a space in this example. If I wanted an asterisk between each item I could use ```print('*'.join(textlist))```

# Challenge

Put all the ideas in the previous paragraphs together to write three lines of code. The first two lines go at the end of the VARIABLES section, after the code to choose the word to guess. The third line goes at the end of the code, after the line ```print(pictures[0])```. Your lines of code should

* make a text variable which consists of the same number of underscores as there are letters in the original word. You will need the ```len()``` function and multiplication
* turn the text variable from a text string into a list (you can use the same variable name for both if you want)
* print the variable with a space between each character

Save your code and test it. Did it work?

[Here](./STEP2A.md) is one way to do it.


[Go to Step 3 - Guessing a letter](../step03-guessing_a_letter/STEP3.md)

[Go back to previous page](../step01-list_of_pictures/STEP1.md)
