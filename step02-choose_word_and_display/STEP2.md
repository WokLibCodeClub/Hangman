# Choosing the word to guess

In old-fashioned Hangman (before computers) one player would choose a mystery word - which has to be a normal dictionary word, not anyone's or anything's name and not slang - and the other player would try to guess it.

In the computer version the computer chooses the word and the player has to try and guess it.

In the starter project, on the left side, you will see two tabs, one labelled ```main.py```, and the other labelled ```Hangman_words.txt```. This second tab refers to a computer *file* which has been uploaded to the Trinket project. If you click on this tab you will see a list of 400 words, all in capital letters, which are from six to 10 letters long and fit the rules. We will have the computer select a word at random from this list as the mystery word to guess.

To do this we need to write code to

1. open the ```Hangman_words.txt``` file
2. read all 400 words from the file into a Python list
3. select a word at random from this list as the mystery word

Each of these operations needs a single line of Python code. Put these lines in the *VARIABLES* block of code after the end of the ```pictures``` list.

## 1. Opening the file

In Python we often write code where we need to access some information from another file on the computer, or even a file on the worldwide web. If the file just contains text characters we use the Python function ```open()```, and inside the brackets we put the name of the file, (which must be inside single or double quotes), then a comma,  then the *"mode"* of opening, which means whether we tell Python if we want to read data from the file (mode ```'r'```), or  start writing in a completely new file (mode ```'w'```), or add more data on to the end of an existing file (mode ```'a'```).

We usually link the opened file to a variable which is a *file* type of variable. Because we only want to read from and not write to the file we will use the ```r``` mode. Here is the code for opening the file with a file variable called ```wordfile```. Put this line after the end of the ```pictures``` list in the *VARIABLES* block of the project:

```python
wordfile = open('Hangman_words.txt', 'r')
```

## 2. Reading the words from the file into a Python list

We need to make a **list** variable to hold the list of words. In this example the list variable is called ```wordlist``` but you can choose your own name if you like.

The code for reading the list of words from the file into the list variable looks a bit complicated! It is

```python
wordlist = wordfile.read().splitlines()
```

Put this line after the previous line.

The middle part of this line is ```wordfile.read()``` which *reads* all the words from the file into Python storage, and the bit at the end ```.splitlines()``` means Python puts each line in the file into a different list item.

The beginning of this line ```wordlist =``` simply creates a list variable called ```wordlist``` which will hold all the words as a list. You could add a line of code to *print* this list if you want to see what it looks like.

## 3. Choosing a word at random from the list

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

---

## A variable to display the partially guessed word

As the player makes guesses for letters which might be in the mystery word we want the computer to display the mystery word as a mixture of underscores (for letters which haven't been guessed yet), and the letters which have been correctly guessed in their right places.

We will make a variable to hold this mixture of letters and underscores. I've called my variable ```word_with_guesses```. (You are free to choose a different name.)

### Set up the variable for the start of the game

At the start of the game none of the letters have been guessed, so the variable will consist of just underscores, one for each letter in the mystery word.

How can we find out how many underscores we need? We need to know how many letters there are in the mystery word. Luckily text variables in Python are a lot like lists, and you probably know that the function for counting the number of items in a list is ```len()```. We can use the same function for counting the number of letters in a text string. If the mystery word is in a variable called ```word_to_guess```, we would use ```len(word_to_guess)``` to get the number of letters.

If we want a text variable with, say,  eight underscores we can use multiplication! Yes, you can multiply bits of text. The code ```'_' * 8``` would produce a text string with eight underscores. But we want to use the number of letters in the mystery word.

Use the previous two paragraphs to help you write a line of Python code which sets a new text variable (I called mine ```word_with_guesses```) equal to the number of underscores in the text variable ```word_to_guess```. Put this line *after* the ```choice()``` line in the *VARIABLES* block. Do have a go at this before looking at the answer.

<details><summary>Click here to see one way to do it</summary>

```python
word_with_guesses = '_' * len(word_to_guess)
```
  
</details>

<p>

### Turning the word with guesses into a list

When we display our mixture of underscores and letters it would be nice to do this with a space between each character, otherwise the underscores would all run together and we wouldn't know how many letters there were in the mystery word. To do this we need to turn our ```word_with_guesses``` text variable into a **list** variable. There is a function to do this called ```list()```.

Here is a line of code to go *after* the previous line, which will turn the text string consisting of underscores into a *list* consisting of underscores:

```python
word_with_guesses = list(word_with_guesses)
```

#### Revision added on 2 February 2025

There is actually a slightly easier way of achieving a list of underscores for the variable ```word_with_guesses```. You can actually use multiplication with *lists*, so if you want to make a list consisting of, say, 5 zeros you could use ```[0] * 5``` which would produce the result ```[0, 0, 0, 0, 0]```. So to make a variable consisting of a list of underscore characters you would simply use

```python
word_with_guesses = ['_'] * len(word_to_guess)
```

This line of code would go ***instead of*** the two lines

```python
word_with_guesses = '_' * len(word_to_guess)
word_with_guesses = list(word_with_guesses)
```

## Displaying the word with guesses with spaces

Now we have our "word with guesses" as a list we can use a special string function for printing the list with a space between each item in the list. That function is the ```join()``` function, and the code we need looks like this:

```python
print(' '.join(word_with_guesses))
```

The ```join()``` function is used to output the items in a list with a *separator* character between each item. The *separator* character goes inside the quote marks just before ```.join()``` (in this example the separator is just a space), and the list you want to print goes in the brackets. (People often use this function to print a list with commas between each item, and the code for that would be ```','.join(name of list)``` where you can now see a *comma* inside the quote marks.)

We will want to use this line of code many times in the game, so we don't want it as part of the set up code, we want it in the *MAIN CODE* section of the project. So, make sure you put this line at the very end of the project code, just after the line where we print ```pictures[0]```.

## Giving away the mystery word

Now we do something which seems a bit silly: we get the computer to display the mystery word. Add this line in the *MAIN CODE* block of the project *after* the line which prints ```pictures[0]``` and before the line with the ```join()``` command:

```python
print('Mystery word: ', word_to_guess, '\n')
```

This is obviously silly, as the object of the game to guess this word, and we've just given it away. However, when we are writing and testing the code it will be very useful to know what the word is, to check if our code works properly. And when the code is all working we will delete this line.

Note the text ```\n``` in the line above - this will print a blank line after displaying the word to guess.

Run your code. Your display should look something like this:

![Step 2 display](step2.png "Display so far")

(except, of course, your mystery word will probably be something else, and the number of underscores may also be different).

[Go to Step 3 - Guessing a letter](../step03-guessing_a_letter/STEP3.md)

[Go back to previous page](../step01-list_of_pictures/STEP1.md)
