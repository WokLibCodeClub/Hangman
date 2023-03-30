# Making more than one guess

We're now going to put all the code for the player's guess inside a loop so the player can keep on guessing letters.

We will use a Python forever loop, except it won't go on forever because we will add in a bit of clever code which lets us ***jump out*** of the loop. This will happen if the player has either won or lost the game.

As you will see, the key Python word to jump out of a loop is ```break```.

## Making a forever loop

A Python forever loop begins with the code

```python
while True:
```

then all the lines of code which we want to be *inside* the forever loop have to be indented.

Insert this line of code just before the line which includes the ```input()``` function.

If you followed the suggestion to put a comment in your code at the start of the section dealing with the player's guess then you will quickly be able to find this point. 

Everything from here to the end of the code needs to be **indented**. Note, some lines are already indented - for these lines we need to add a further indentation.

The quick way to do this in *trinket* is to select all the lines of code you want to indent and press the TAB key once. That should indent all the selected lines by two spaces.

Save your code and run it. You should be able to keep guessing letters, and the display should update correctly as you make a right guess or a wrong guess, but you will find that it keeps asking you to guess a letter even after the gallows is complete, or you have completely guessed the word, and when you make another guess it might give an error ```IndexError: list index out of range```. This means that you are trying to print a picture from the pictures list that doesn't exist. This happens because we haven't yet coded the end of the game, and it is stuck in the forever loop.

## Jumping out of the forever loop

We need to write code which will work out if the player has won or lost, to know when to jump out of the forever loop. We will put this code at the end of the forever loop (but *inside* the loop, so the next lines still need to be indented).

### Working out if the player has lost

If the player has *lost* then the body hanging on the gallows is complete. How many wrong guesses does this take? We could test the variable which holds the number of wrong guesses to find out if the player has lost:

```python
  if num_wrong_guesses == ?:
    break
```

In place of the question mark put the number of wrong guesses for when the player has lost. (Also, if you used a different variable name then use your name in place of mine.)

This line will cause the code to break out of the forever loop and go on to any code which comes after the loop. (At the moment, there isn't any, but we'll fix that soon.)

### Working out if the player has won

If the player has *won* then all the letters in the mystery word have been guessed. In this case there will be no more underscore characters in the list variable we were using to hold the mixture of underscores and letters. 

How can Python tell if a particular item is present in a list?



To check if the text "_" is present in the list we could use

```python
  if "_" in ?:
    break
```

(substitute the name of your list variable). This code will break out of the loop if there is a "\_" character anywhere in the list, **but that's not what we want!** We actually want to test if the "_" character is *absent* from the list, so in Python we can do this by adding in the word ```not```:

```python
if ? not in ?:
  break
```

and this will now jump out of the loop if the player has won.

We have two ```if``` blocks to add to the end of the ```while True``` loop, but Python actually gives a way to test **_both_** conditions with the one ```if``` block using the key word ```or```:
```python
if wrong_guesses_variable == losing number or "_" not in name_of_list_variable:
  break
```
(you will have to adapt this line for your own variable names). The ```if``` line needs to be on a single line of code from the ```if``` to the ```:``` but in your browser you might find this rather long line has been split into two. Make sure you put it all on one line in your code.

Save your code and test it. You should find the code will stop after you have won or lost, because in both cases we have now jumped out of the forever loop. The code won't ask you for any more guesses, but it won't tell you if you won or lost. What do we want to happen now?

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

Test your code again. If it's all working the programme will let you know if you've won or lost. 

## Get rid of the line that gives away the mystery word

Finally, before you let your friends have a go at your new game, you should locate the line of code which displays the mystery word. Either delete this line, or add a ```#``` character at the beginning to turn it into a comment so that Python will ignore this line and not print the mystery word before it's been guessed.

You have now coded Hangman! Well done. See if you can beat the computer in your own game.

## Challenges

There are some modifications you could put in to your game:

1. This code doesn't check if the player accidentally types more than one letter during a guess, so one modification would be to test this and warn the player if they type more than one character. How could you do that?

2. If you play your game many times you might wonder whether you are winning more or less often than the computer. You could add code to keep the score and display it at the end of each game.

3. If you play so often that you start to see the same mystery words coming up over and over again you might want to find a longer list of words. You can search for lists of English words on the internet. If you find a good list you will have to convert all the words to capital letters (you could write Python code to do this) then upload your improved word list to your trinket project.

Have fun.

[Return to main page](../README.md)

[Go back to previous page](../step03-guessing_a_letter/STEP3.md)
