# Giving the player more than one guess

As said in the last section we are going to put all the code for the player's guess inside a loop so the player can keep on guessing letters.

This will be a forever loop, which means it will keep going forever, except we will add in a bit of code to see if the player has won or lost and if either of these is true then we will jump out of the forever loop using the Python command ```break```.

## Making a forever loop

A Python forever loop begins with the code
```python
while True:
```
then all the lines of code which we want to be *inside* the forever loop have to be indented.

If you followed the suggestion to put a comment in your code at the start of the section dealing with the player's guess then you will quickly be able to find this point. Put the ```while True:``` line above the comment, then select all the code from here to the end and press the TAB key - you should see *all* these lines get indented together. (And if some lines were already indented they should now be indented twice.)

If you didn't put a comment in your code you will have to go back to the previous step and find where this would go.

Save your code and test it. You should be able to keep guessing letters, and the display should update correctly as you make a right guess or a wrong guess, but you will find that it keeps asking you to guess a letter even after the gallows is complete, or you have completely guessed the word, and when you make another guess it might give an error ```IndexError: list index out of range```. This means that you are trying to print a picture from the pictures list that doesn't exist. This happens because we haven't yet coded the end of the game, and it is stuck in the forever loop.

## Breaking out of the forever loop

We need to write code which will work out if the player has won or lost, to know when to break out of the forever loop. We will put this code at the end of the forever loop (*inside* the loop).

If the player has *lost* then the body hanging on the gallows is complete. How many wrong guesses does this take? We could test the variable which holds the number of wrong guesses to find out if the player has lost using:
```python
if wrong_guesses_variable == losing number:
  break
```
This code will break out of the forever loop when the player has lost (you will have to put the name of your number of wrong guesses variable, and the right number to make your code work).

If the player has *won* then all the letters have been guessed. In this case there will be no more underscore characters in the list variable we were using to display the mystery word. Python has a very neat way of checking if a particular item is present in a list. To check if the text "_" is present in the list we could use
```python
if "_" in name_of_list_variable:
  break
```
(substitute the name of your list variable). This code will break out of the loop if there is a "\_" character anywhere in the list, **but that's not what we want!** We actually want to test if the "_" character is *absent* from the list, so in Python we can do this by adding in the word ```not```:
```python
if "_" not in name_of_list_variable:
  break
```
and this will now jump out of the loop if the player has won.

We have two ```if``` blocks to add to the end of the ```while True``` loop, but Python actually gives a way to test **_both_** conditions with the one ```if``` block using the key word ```or```:
```python
if wrong_guesses_variable == losing number or "_" not in name_of_list_variable:
  break
```
(you will have to adapt this line for your own variable names). The ```if``` line needs to be on a single line of code from the ```if``` to the ```:``` but in your browser you might find this rather long line has been split into two. Make sure you put it all on one line in your code.

Save your code and test it. You should find the code will stop after you have won or lost, because in both cases we have now jumped out of the forever loop. What do we want to happen now?

## Coding a win or a loss

We're nearly there.

At the end of the code, *outside* the ```while True:``` loop (so not indented), we put code either to congratulate the player for being clever, or tell them they've lost, and let them know what the mystery word was.

Our code will only ever get to these lines after the game has been won or lost but which is it? We can use the same tests we used inside the forever loop.
```python
if wrong_guesses_variable == losing number: # this means the player has lost
  [WRITE CODE TO SAY THE PLAYER HAS LOST AND TO TELL THEM WHAT THE MYSTERY WORD WAS]
else: # this means the player has won
  [WRITE CODE TO GIVE A MESSAGE OF CONGRATULATIONS]
```
Test your code again. If it's all working the programme will let you know if you've won or lost. For the last step you should now locate the line of code you added for debugging (which displayed the mystery word at the beginning of the game) and add a ```#``` character at the beginning to turn it into a comment. Python will now ignore this line and not print the mystery word before it's been guessed.

You have now coded Hangman! Well done. See if you can beat your own game.

# Challenges

There are some extras you could put in to your game:

1. This code doesn't check if the player accidentally types more than one letter during a guess, so one improvement would be to test this and warn the player if they type more than one character

2. If you play your game many times you might wonder if you are winning more than the computer. You could add code to keep the score and display it at the end of each game

3. If you play so often that you start to see the same mystery words coming up over and over again you might want to find a longer list of words. You can search for lists of English words on the internet. If you find a good list you will have to convert all the words to capital letters (you could write Python code to do this) then upload your improved word list to your trinket project.

Have fun.

[Go back to main page](../README.md)
