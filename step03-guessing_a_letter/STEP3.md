# How does the player guess a letter?

Next we need to write the code so that the player can try to guess one of the letters in the mystery word.

## What happens when the player guesses a letter

A lot of things have to happen at the time when the player guesses a letter. We will build the code up gradually for each of these items and eventually put them all inside a loop which runs until the player guesses the word or is hanged. This is the overall picture:

1. the computer asks the player to guess a letter

2. the computer checks if that letter is in the mystery word

3. *if it isn't* the computer increases the number of wrong guesses by one, but *if it is* then the computer updates the list which contains guessed letters and underscores, and replaces underscores with the correct guessed letter

4. the computer clears the screen and draws the gallows with the right picture, depending on how many wrong guesses the player has already had

5. the computer prints the mystery word using underscores where the letters have not been guessed, and letters where the player has made correct guesses

6. the computer prints the list of all the wrong guesses so far, if any

7. the computer asks the player to guess a letter ... back to item 1.

## We need some new variables

We've mentioned a variable to hold the number of wrong guesses a couple of times, but, so far, we haven't made one. In the VARIABLES section of your code make a variable for the number of wrong guesses and set it to 0. (Choose your own name.)

In item 6 of the list above we get the computer to print out all the previous wrong guesses - we'll keep track of these in a *list*, which starts out as an empty list, and gets added to each time the player makes a wrong guess. Make a list variable and set it to ```[]```, which means it's an empty list.

## Your code so far

Here's a sketch of what your code should look like:

In the VARIABLES section you should have

* a list variable containing a series of pictures for the gallows
* code to open the word list file, select a word at random and put this in a variable
* code to make a list variable to contain the partially guessed mystery word  - at the moment this will consist entirely of underscores
* a variable to hold the number of wrong guesses, initially set to 0
* an empty list variable to hold all the wrong guessed letters

In the MAIN CODE section you should have

* a line to print the first picture in the list of pictures
* a line to print the list containing the partially guessed mystery word, using the function ```join()``` to put a space between each character.

### Useful extra step for debugging

*Debugging* is the rather odd computer name for finding all the "bugs" in your code - these are bits of your code that stop it from running properly - they might be simply typos (which are usually easy to find) or more tricky bugs where a programme might run but not be doing exactly what you want.

When we're running our finished version of Hangman the computer will not reveal the mystery word until the very end. But while we're writing the code and making sure it's working properly it would be very useful if we know what the mystery word is. So, a good suggestion is to add a line of code at the bottom to print the mystery word. You should be able to work out this line for yourself.

When our code is all written and running properly we will put the comment sign ```#``` in front of this line so the computer will not display the word.

## Asking the player to choose a letter

You probably know the Python function ```input()``` to ask the user to type in something. We will use this to ask the player to guess a letter. You will need to put a *prompt* string inside the brackets (some text which Python will print when asking for input - don't forget to put the prompt in quotes) and you will also need a variable to put the guess in.

Put the input line at the very bottom of the code for now. (Later we will put this line, and other lines which deal with the player's guess, inside a loop.)

You could try putting in a **comment** line above the ```input()``` line, to remind you that this is where the code for the player's guess begins. You will need to find this place later.

### Upper case or lower case?

All the words in the word list are all in upper case (capital) letters, and Python is very fussy about upper case or lower case letters. If the player guesses the letter "a", and the word is "HANGMAN", Python will say there is no "a" in "HANGMAN". We can insists that the player only types capital letters when guessing, but another way is to *convert* any letter the player types into capitals, which avoids the problem. The Python function ```upper()``` is used to convert text to upper case letters.

You can try this out in the [trinket Interactive Python Console](https://trinket.io/console). Open the console and type
```python
"Hello".upper()
```
The console will print ```HELLO``` because Python has taken every character in the string ```"Hello"``` and converted it to an upper case letter. The "H", which was already upper case, is not changed. If you have a variable which contains text you can put the name of the variable in place of "Hello" in this function.

(As you might guess there is also a Python function ```lower()``` which you can experiment with to find out what it does.)

In the Hangman code if your input function has put the player's guess into a variable called ```a``` then add, after the input line,
```python
a = a.upper()
```
which will take the text in variable ```a```, convert it to upper case and put the result back in ```a```. (Use your own variable name in place of ```a```.) So, whether the player typed a capital or a lower case letter we can write the code as if it was a capital letter.

### Unfair to the player!

Next, we're going to be a bit unfair to the player - and assume that the player's guess is *wrong*. We'll make a **_Boolean_** variable (one which can be ```True``` or ```False```) and add it to the bottom of the code, like this:
```
good_guess = False
```
You'll see how we use this in a minute.

## Is the player's guessed letter in the mystery word?

Once the player has made a guess we need to loop through every letter in the mystery word to see if the guess is matched in the word, so we need to code a ```for``` loop, and it needs to repeat exactly once for each letter in the mystery word.

### ```for``` loop to cycle through the mystery word

Here is the structure of the ```for``` loop:

```python
for loop_variable in range(number_of_times_to_run_the_loop):
```
Choose your loop_variable name for the loop.

What Python function can you use to get the number_of_times_to_run_the_loop? *Clue*: this needs to be the number of letters in the mystery word - look back to [Step 2](../step02-choose_word_and_display/STEP2.md).

Inside the loop we want to check each letter in the mystery word against the player's guess. We can use the fact that in Python a piece of text, for example a word, behaves a lot like a list: if I have a text variable ```myword = "GENIUS"``` then I can check what the 3rd letter is with the code ```myword[2]```, just as if the letters were items in a list.

As we go through the ```for``` loop the value of loop_variable increases, starting from 0, and we can look at the letters in the mystery word in turn, using this variable as the **index**, and seeing if that letter is equal to the player's guess.

If the variable for the loop is called ```l``` and the player's guess variable is ```a``` and the mystery word is in a variable called ```word_to_guess``` then the code I need is an ```if``` statement (which must be indented as it is inside the ```for``` loop) like this:
```python
  if word_to_guess[l] == a:
```
This is comparing the player's guess with a letter in the mystery word. *If they are equal* we need to do two things

- first, change the Boolean variable ```good_guess``` to be True (this line has to be indented *twice* as it is in the ```for``` loop *and* the ```if``` block),

- second, change the **list** where we are keeping the updated word with guesses. Remember, this list contains a mixture of underscores and letters. If the loop variable now has the value 3, and we have found that the player's guess matches the letter of the mystery word with index 3, then in the list we need to replace the underscore item index 3 of the list with the guessed letter. So if my list variable is called ```word_with_guesses``` I could do this with the code

```python
    word_with_guesses[loop_variable] = a
```
Use your own variable names in place of mine.

*If the player's guess and the letter in the mystery word are not equal* then we just go on to check the next letter, so we don't need to write any code for an ```else``` option in this ```if``` block.

### Was it a good guess?

Once the ```for``` loop has finished it means we have checked the player's guess against *every* letter in the mystery word. Before we started we set the variable ```good_guess``` to ```False```. What is it set to now?

Well, if the player's guess matched a letter in the word our ```if``` block will have set this variable to ```True```, meaning it was a good guess. But if there were no matches in the mystery word, then this variable will still be set to ```False```, and that tells us it was a wrong guess. If it's a wrong guess we do two things - add one to the number of wrong guesses, and add the player's guess to the list of wrong guesses.

So after the ```for``` loop we can put in an ```if``` block to check the setting of ```good_guess```:
```python
if good_guess == False:
  number_of_wrong_guesses += 1
  wrong_guesses_list.append(a)
```
You should put your own variable names in place of the one's I've used.

**Be careful** with the indentation - this ```if``` block is *not* part of the ```for``` loop.

We are nearly done with coding the player's guess!

### Reset the screen after the player's guess

These lines of code need to be added to the end, after the last ```if``` block, but they are not indented, because they are not part of the if test.

First, clear the screen using
```python
system('cls')
```
Second, ```print``` the item from the list of pictures which matches the number of wrong guesses the player has made. (The number of wrong guesses will go inside square brackets after the name of the list of pictures.)

Third, ```print``` the partially guessed word, using the ```join()``` function to put a space between each character (this is the same code you have used already to print the partially guessed word). You could add a bit of text inside the brackets before ```' '.join``` to explain what this line means.

Fourth, ```print``` the list of wrong guesses using the ```join()``` function to put a space between each item. We don't need this line if there aren't any wrong guesses, so we should put this line in an ```if``` block:
```python
if len(wrong_guesses_list) > 0:
  print("\nWrong guesses so far: " + ' '.join(wrong_guesses_list))
```
Here we are counting the items in the list of wrong guesses and only printing the list if it is not empty. Notice, I have added a bit of extra text to the beginning of the print function just to explain to the player what this list is. The ```\n``` forces Python to print a blank line to space out the display better.

### Testing, testing...

That's the end of the code for the player's guess. Now we have to save the code and TEST it! 

Run your code. 

If you followed the suggestion above about debugging to print out the mystery word then you will be able to "guess" a letter which you **_know_** is in the word. What happened? Did the guessed letter appear in place of underscores in the word?

Run the code again. This time "guess" a letter which you know is **_not_** in the word. What happened? Did the gallows display change to show the person's head? Did your chosen letter appear in a list of wrong guesses?

If your code didn't work exactly as you want you will have to try and find the problem. If a line of code in trinket appears with a pink background that is a good place to start. Work through your code one line at a time, thinking what might be happening to the variables.

We have only coded one guess by the player, then the code gets to the end and stops. In the next step we will put this section of code inside a loop which will continue until the player either wins or is hanged.

[Go to Step 4 - More guesses, and ending the game](../step04-ending_the_game/STEP4.md)

