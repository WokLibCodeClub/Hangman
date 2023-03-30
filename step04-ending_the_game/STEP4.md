# Making more than one guess

We're now going to put all the code for the player's guess inside a loop so the player can keep on guessing letters.

We will use a Python ***forever*** loop, except it won't go on forever because we will add in a bit of clever code which lets us ***jump out*** of the loop. This will happen if the player has either won or lost the game.

As you will see, the key Python word to jump out of a loop is ```break```.

## Making a forever loop

A Python forever loop begins with the code

```python
while True:
```

then all the lines of code which we want to be *inside* the forever loop have to be **indented**.

Insert the ```while True:``` line of code just before the line which includes the ```input()``` function.

If you followed the suggestion to put a comment in your code at the start of the section dealing with the player's guess then you will quickly be able to find this place.

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

>#### Try this in the trinket console:
>
>Copy this line and paste it into the console
>
>```python
>'a' in ['a', 'p', 'p', 'l', 'e']
>```
>
>You should find the console types ```True```. This is because (obviously) ```'a'``` is one of the items in the list. If you tried
>
>```python
>'b' in ['a', 'p', 'p', 'l', 'e']
>```
>
>it would print ```False``` because ```'b'``` is not in the list.
>
>Now set up a list variable like we might have in Hangman if some, but not all, of the letters had been guessed:
>
>```python
>word_with_guesses = ['a', '_', '_', 'l', '_']
>```
>
>Now type
>
>```python
>'_' in word_with_guesses
>```
>
>and it should print ```True```, because the list contains the ```'_'``` character. This gives a way of testing if the player has won.
>
>Actually, for our test for whether the player has won the game we want to check if the character ```'_'``` is ***NOT*** in the list, and Python lets us do that simply by adding the word ```not``` into the code. In this example the word has been fully guessed and there are no underscores left in the list:
>
>```python
>word_with_guesses = ['a', 'p', 'p', 'l', 'e']
>'_' not in word_with_guesses
>```
>
> This will print ```True``` telling us that there are no underscores in the list.

Our code to break out of the forever loop if the player has won will use a Python ```if``` statement, and be something like

```python
  if "_" not in word_with_guesses:
    break
```

(substitute the name of your list variable if it is different).

Save your code and test it. You should find the code will stop after you have won or lost, because in both cases we have now jumped out of the forever loop. The code won't ask you for any more guesses, but it won't tell you if you won or lost. What do we want to happen now?

## Coding a win or a loss

We're nearly there.

At the end of the code, *outside* the ```while True:``` loop (so not indented), we put code either to congratulate the player for being clever, or tell them they've lost, and let them know what the mystery word was.

Our code will only ever get to these lines after the game has been won or lost but which is it? We can use the same test for the player losing (with an ```if``` statement) that we used inside the forever loop, but now we can also add an ```else:``` statement, because we know if the player didn't lose they must have won! Here is a sketch of the code to put at the very end of the project (not indented):

```python
if num_wrong_guesses == ?: # this means the player has lost
  print(?) # WRITE SOME TEXT HERE TO SAY THE PLAYER HAS LOST AND TO TELL THEM WHAT THE MYSTERY WORD WAS]
else: # this means the player has won
  print(?) # WRITE CODE TO GIVE A MESSAGE OF CONGRATULATIONS
```

You need to fill in the question marks. The first line will be the same as the line you coded inside the forever loop to ```break``` if the player lost.

Test your code again. If it's all working the programme will now let you know if you've won or lost.

## Get rid of the line that gives away the mystery word

Finally, before you let your friends have a go at your new game, you should locate the *two* places where there is a line of code which displays the mystery word. Either delete these lines, or add a ```#``` character at the beginning of each to turn them into comments so that Python will ignore these lines and not print the mystery word and spoil the game.

You have now coded Hangman! Well done. See if you can beat the computer in your own game.

## Challenges

There are some modifications you could put in to your game:

1. This code doesn't check if the player accidentally types more than one letter during a guess, so one modification would be to test this and warn the player if they type more than one character. How could you do that?

2. You could adapt your game so that at the end it asked if you wanted to play again, and then restarted the game without you having to click on the Run arrow.

3. If made the modification in number 2 above, and played Hangman many times you might wonder whether you were winning more or less often than the computer. You could add code to keep the score and display it at the end of each game.

4. If you play so often that you start to see the same mystery words coming up over and over again you might want to find a longer list of words. You can search for lists of English words on the internet. If you find a good list you will have to convert all the words to capital letters (you could write Python code to do this) then upload your improved word list to your trinket project.

Have fun.

[Return to main page](../README.md)

[Go back to previous page](../step03-guessing_a_letter/STEP3.md)
