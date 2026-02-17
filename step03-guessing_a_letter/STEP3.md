# How does the player guess a letter?

Next we need to write the code so that the player can try to guess one of the letters in the mystery word. This will happen over and over again as the game progresses, so the code for guessing will be contained in a Python ***loop***.

## What happens when the player guesses a letter

This is the overall sequence of our loop:

1. the computer asks the player to guess a letter

2. the computer checks if that letter is in the mystery word

3. - *if it isn't* the computer increases the number of wrong guesses by one; 

- - *if it is* then the computer updates the ```word_with_guesses``` list and replaces underscores with the correct guessed letter

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

We'll now build up the code for the player to make a single guess. The next lines will go in the *MAIN CODE* block of code at the very end of the project.

## Using ```input()``` to get the player to choose a letter

The Python ```input()``` function is used to ask the user to type in something. Inside the brackets you can put some text (inside quotes) to tell the player what is wanted (a *prompt* string). This might be to ask the player to guess a letter, for example. The result - what the player types - will go into a variable. The Python code looks like this:

```python
a = input(?)
```

where you need to put your own prompt string (inside quotes) in place of the question mark. ```a``` is my variable name for the answer.

**Suggestion**: to space your game out a bit one idea is to put the characters ```\n``` at the start of your prompt string. This will print a blank line before the text asking the player for a letter.

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

We'll be a bit unfair to the player by assuming that the player made a bad guess (the guessed letter *wasn't* in the mystery word). To do this in Python code we'll set the boolean variable to ```False```. You'll see how this works in a litte bit.

Add this line of code after the line with the ```upper()``` function to make the boolean variable equal to ```False```:

```python
good_guess = False
```

## Is the player's guessed letter in the mystery word?

Once the player has guessed a letter we need to go through every letter in the mystery word to see if the guessed letter is in the word. We'll do this with a Python ```for``` loop, and it needs to repeat exactly once for each letter in the mystery word.

### ```for``` loop to cycle through the mystery word

Here is the structure of the first line of the ```for``` loop (which goes after the line setting the boolean variable to ```False```):

```python
for ? in range(?):
```

You need to fill in the question marks. The first question mark is the name of a *loop variable* where you can choose any variable name which fits the Python rules for variable names. The second question mark needs to be the number of letters in the mystery word. *Clue*: look back to [Step 2: Set up the variable for the start of the game](../step02-choose_word_and_display/STEP2.md#set-up-the-variable-for-the-start-of-the-game) to see how to use the number of letters in the mystery word.

This line will take your loop variable and set it to 0 the first time the loop runs, 1 the second time the loop runs, 2 the third time etc up to one less than the number of letters in the mystery word.

---

>#### Try this in the trinket console:
>
>Let's say the mystery word is 'GENIUS' and this is in a text variable called ```word_to_guess```. Set this up by typing
>
>```python
>word_to_guess = 'GENIUS'
>```
>
>If I write in the console
>
>```python
>word_to_guess[0]
>```
>
>it will print ```G``` because this is the letter which has the index value 0 in the text string. (Text strings are just like lists.) Try putting different numbers in the square brackets to print out the other letters of GENIUS.

---

Inside the ```for``` loop, (which means any lines of code inside the loop *must* be indented) we compare the player's guess (which I have in a variable called ```a```) with the letter in the mystery word with the index which corresponds to the value of the loop variable. We do this using a Python ```if``` statement:

```python
  if word_to_guess[?] == a:
```

In place of the question mark put the name of your loop variable. In Python if we want to check if two things are equal we use a *double equals sign*: ```==```.

#### The player's guess is the same as the current letter

We have compared the player's guess with a letter in the mystery word. *If they are equal* we need to do two things

- first, add a line of code to change the Boolean variable ```good_guess``` to be True (this line has to be indented *twice* as it is inside the ```for``` loop *and* inside the ```if``` block)

<details><summary>Click here if you need to see how to do this</summary>

```python
    good_guess = True
```
  
</details>

<p>

- second, change the **list** where we are keeping the "word with guesses". Remember, at the start, this list contains just underscores. If the loop variable now has the value 3, and we have found that the player's guess matches the letter of the mystery word with index 3, then in the ```word_with_guesses``` list we need to replace the underscore at item index 3 of the list with the guessed letter, except we use the value of the loop variable instead of 3. The code to do this is

```python
    word_with_guesses[?] = a
```

Put your loop variable in place of the question mark.

#### The player's guess is not the same as the current letter

If the player's guess and the current letter in the mystery word are *not equal* then we don't have to do anything - we just go on to check the next letter in the word, so we don't need to write any code for this.

### Did the player make a good guess?

Once the ```for``` loop has finished it means we have checked the player's guess against *every* letter in the mystery word. Before we started we set the variable ```good_guess``` to ```False```. What is it set to now?

Well, if the player's guess matched a letter in the word our ```if``` block will have set this variable to ```True```, meaning it was a good guess. But if there were no matches in the mystery word, then this variable will still be set to ```False```, and that tells us it was a bad guess. If it's a bad guess we do two things:

1. add one to the number of wrong guesses, and
2. add the player's guessed letter to the list of wrong guesses.

So *after* the ```for``` loop we can put in another ```if``` block to check the setting of ```good_guess```. This block is *not* part of the ```for``` loop, so this line is *not* indented at all:

```python
if good_guess == False:
  num_wrong_guesses += 1
  wrong_guesses_list.append(a)
```

(These are *my* variable names. You should use your own variable names in place of mine if they are different.)

**Be careful** with the indentation - this ```if``` block is *not* part of the ```for``` loop.

We are nearly done with coding the player's guess!

### Redraw the screen after the player's guess

We just a few more lines of code to complete coding the player's guess, and these lines go after the last ```if``` block. They are *not* indented:

first, clear the screen using

```python
system('cls')
```

second, ```print``` the picture from the list of pictures which matches the number of wrong guesses the player has made. This will be almost the same as the line we used previously to print the first picture ```print(pictures[0])```, except you should **edit** it, so in place of the 0 you put the variable for the number of wrong guesses.

(Since the player has only made one guess so far the number of wrong guesses can only be 0 or 1.)

thirdly, we want to repeat the line which gives away the mystery word - copy this line from higher up in the code

fourthly, we want to copy the line which prints the mixture of underscores and letters and uses the ```join()``` command (again copy this from higher up in the code)

lastly, we want to print a list of any wrong guesses the player has made. (At this stage there will either be one or none.) If the player has only made good guesses we don't need to print this list, so we can use another ```if``` statement to decide whether to print it or not. We do this by testing the length of the list of wrong guesses - if the length is 0 then we don't need to print it. If the length is more than zero then we do print it. Notice we are using the ```join()``` command again, to insert spaces between each item in the list. Here is the code:

```python
if len(wrong_guesses_list) > 0:
  print("\nWrong guesses so far: " + ' '.join(wrong_guesses_list))
```

 The ```\n``` forces Python to print a blank line before the list, to space out the display better.

### Testing, testing...

That's the end of the code for the player's first guess. Now we can save the code and TEST it!

Run your code. When Python asks you to guess a letter try one that *is* in the mystery word (you can do this because the code is showing what the mystery word is).

**Don't forget to click the mouse once inside the Result panel to switch the focus before you type a letter!!**

You should see the display of the word with underscores change to show your chosen letter instead of underscores.

Now run the code again and choose a letter which is *not* in the mystery word. You should see the picture change, to show the head of the person, and the list of wrong guesses should be displayed showing your incorrect letter.

If your code didn't work exactly as you want you will have to try and find the problem. If a line of code in trinket appears with a pink background that is a good place to start. Work through your code one line at a time, thinking what might be happening to the variables.

We have only coded one guess by the player, then the code gets to the end and stops. In the next step we will put this section of code inside a loop which will continue until the player either wins or is hanged.

### Check code

You can look [here](ex_step3.md) to see an example of how the code might look if you've followed the instructions so far. (The list of pictures is not shown in this example.)

### Next step

[Go to Step 4 - More guesses, and ending the game](../step04-ending_the_game/STEP4.md)

[Go back to previous page](../step02-choose_word_and_display/STEP2.md)
