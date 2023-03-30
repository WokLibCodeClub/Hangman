# How does the player guess a letter?

Next we need to write the code so that the player can try to guess one of the letters in the mystery word. This will happen over and over again as the game progresses, so the code for guessing will be contained in a Python ***loop***.

## What happens when the player guesses a letter

This is the overall sequence of our loop:

1. the computer asks the player to guess a letter

2. the computer checks if that letter is in the mystery word

3. *if it isn't* the computer increases the number of wrong guesses by one; *if it is* then the computer updates the ```word_with_guesses``` list and replaces underscores with the correct guessed letter

4. the computer clears the screen and draws the right picture, depending on how many wrong guesses the player has already had

5. the computer prints the updated ```word_with_guesses``` list

6. to help the player, the computer also prints a list of any letters the player has guessed wrongly so far

7. back to step 1: the computer asks the player to guess a letter ...

The loop continues running until either the player has correctly guessed the word, or the player has run out of guesses and is hanged. So we also need to keep track of whether the player has won or lost.

Firstly, we will write the code for the player to make a single guess at a letter. Then, in Step 4 of these instructions, we will make this code into a loop.

## We need some new variables

We're going to need two new variables - put these in the *VARIABLES* block of code after the line which makes the variable ```word_with_guesses```.

1. Make a variable for the number of wrong guesses and set it equal to 0. I called mine ```num_wrong_guesses``` but you can choose your own name. Do you remember how to make a variable and set its value to 0?

2. Make a variable which will hold a *list* of all the player's wrongly guessed letters (see step 6 in the list above) and set it to be an empty list. I called mine ```wrong_guesses_list```. To set a variable to an empty list make its value equal to ```[]```.

---

We'll now build up the code for the player to make a single guess. The next lines will go in the *MAIN CODE* block of code just before the line where we give away the mystery word.

## Using ```input()``` to get the player to choose a letter

The Python ```input()``` function is used to ask the user to type in something. Inside the brackets you can put some text (inside quotes) to tell the player what is wanted (a *prompt* string). This might be to ask the player to guess a letter, for example. The result - what the player types - will go into a variable. The Python code looks like this:

```python
a = input(?)
```

where you need to put your own prompt string in place of the question mark. ```a``` is my variable name for the answer.

>### Recommendation
>
>Put a **comment** line above the ```input()``` line to mark that this is where the code for the player's guess begins. You will need to find this place later. (A comment line begins with the ```#``` character.)

### Upper case or lower case?

The words in the ```Hangman_words.txt``` file are all in upper case (capital) letters, but the player might type in a lower case ```'a'```. Python is very fussy about upper case and lower case letters. If the player guesses the letter 'a', and the word is 'HANGMAN', Python will say there is no 'a' in 'HANGMAN'.

We can insist that the player only types capital letters when making guesses, but another way is to *convert* any letter the player types into upper case, which avoids the problem. The Python function ```upper()``` is used to convert text to upper case letters.

Add the Python line

```python
a = a.upper()
```

which will convert anything the player types into upper case.

---

>#### Experimenting with ```upper()```
>
>You can experiment with ```upper()``` in the [trinket Interactive Python Console](https://trinket.io/console). Open the console and type
>
>```python
>"Hello".upper()
>```
>
>The console will print ```HELLO``` because Python has taken every character in the string ```"Hello"``` and converted it to an upper case letter. The "H", which was already upper case, is not changed. If you have a variable which contains text you can put the name of the variable in place of "Hello" in this function.
>
>(As you might guess there is also a Python function ```lower()```. Experiment with it to find out what it does.)

---

### Unfair to the player

When the player guessed a letter was it a good guess or a bad guess? We keep track of this by making another variable which is of the type ***boolean***, which means it must be equal to either ```True``` or ```False```. We'll call this variable ```good_guess```.

We'll be a bit unfair to the player by assuming that the player had made a bad guess. To do this in Python code we'll set the boolean variable to ```False```. You'll see how this works in a litte bit.

Add this line of code after the last line to make the boolean variable equal to ```False```:

```python
good_guess = False
```

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

[Go back to previous page](../step02-choose_word_and_display/STEP2.md)
