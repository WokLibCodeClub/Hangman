# Creating the set of pictures in a list variable

In this version of Hangman the player has six guesses at letters in the mystery word. Each time the player makes a *wrong* guess (guesses a letter which is ***not*** in the word) the picture adds an extra bit of body to the figure of the person being hanged.

This means which picture we display is controlled by the number of wrong guesses: if there are no wrong guesses so far we show the picture with just the gallows; if there has been one wrong guess so far we show the gallows and the person's head, two wrong guesses and we show the gallows, head and body, and so on up to a maximum of six wrong guesses.

We can do this in Python by making a variable to hold the number of wrong guesses, and putting all the pictures in a Python **list**. Then we can use the number of wrong guesses as the ***index*** for the picture in the pictures list that we want to show.

In the starter project we have already started a list variable called ```pictures``` and put the first two items (pictures) in the list, separated by a comma.

These pictures are really just combinations of text symbols arranged cleverly so they seem to draw a picture. The symbols used so far are ```_ | O /```. By adding these and other text symbols you will be able to draw the person's body, arms and legs.

## Your first task

Your first task is to add five more pictures to the pictures list: first add the body, then the left arm, then the right arm, then the left leg, then the right leg. We will use these pictures for 2, 3, 4, 5 and 6 wrong guesses.

One smart way to add a new picture is to copy the previous picture in the list, paste it onto the end of the list (**don't forget to put in a comma first**) then edit in a new body part to the pasted version.

---

### Triple quotes as a way of making a Python string go over several lines

>Each of the items in a list in the starter project is a *text string*, but you might have noticed that these text strings don't begin and end with `'` or `"` like normal text strings, they begin and end with `"""` - a triple quote mark. What is the meaning of a triple quote mark?
>
>You can see an explanation of this near the end of the [introductory video](https://youtu.be/FOJO9RdFEF8) for this project, but the simple explanation is that a text string which is inside *triple* quotes can spread across several lines, so any time you want your string to start a new line you type ENTER inside the triple quotes, and this will be shown as a new line when Python prints the text.
>
>You can use either triple single quotes ```'''``` or triple double-quotes ```"""``` to get this effect.

---

## Special feature of the ```\``` character

You might decide to use the backslash ```\``` character in your list of pictures - unfortunately this creates a small problem.

In Python strings sometimes people wanted to include types of formatting which wouldn't be available from the normal keyboard, so it was decided that if you put a backslash character in the string you could follow that with some other character which would tell the string to include formatting. One example is if you put ```\n``` inside a string and print it Python won't print the backslash or the ```n```, it will start a new line.

If we make a string where we actually ***do*** want to print a backslash (for example for one of the figure's legs) we simply put two backslashes ```\\```, and Python will ignore the first, and print the second.

## Check your handiwork

Once you've finished making your list you should check that your sequence of pictures looks good and that the pictures are in the right order. At the end of the starter project, in the MAIN CODE section, there is a line of code

```python
print(pictures[0])
```

which will print the first item from the ```pictures``` list. Run your code - it should display the first picture in the list. Change the number in square brackets and run the code again to see the other items in your list.

## Challenge

How would you make a Python ***loop*** to show the pictures one after another without having to keep typing a different number in the square brackets?

You will want your loop to start with ```for```, then a loop variable (which you can name as you like), then ```in```, then the name of your pictures list, then a ```:```. On the next lines, (which need to be indented) you should put the code which will

* clear the screen
* print the item from the list
* pause before going on to the next picture

The code for clearing the screen is ```system('cls')``` and you should find this in the starter project already.

To pause the code use

```python
  input()
```

which means the programme will wait until you press the Enter key (but see the note below on typing in the Result panel). This gives you a chance to see each picture before the loop goes on to the next one.

---

### Typing in the Result (right hand) panel

>When your Python code includes an ```input()``` function the code will expect you to type something in the right hand **Result** panel of the trinket webpage.
>
>But while you're writing code Trinket assumes you are typing in the code **Editing** (left hand) panel - this panel "**has the focus**". When you want to type something in the Result panel you need to **switch the focus** to the Result panel, and the way to do this is to click the mouse once inside the right panel.
>
>If you don't do this you may find that anything you type, even just pressing *Enter*, will appear in your code window, and you will have to use Control-Z to undo your action.
>
>Be warned: it's **terribly** easy to forget to do this, and accidentally make edits to your code!

---

Don't forget about ***indenting*** the lines of code inside the loop.

Did you manage to make a loop which worked?

<details><summary>Click here to see one way to do it</summary>

```python
for p in pictures:
  system('cls')
  print(p)
  input()
```
  
</details>

<p>

### Check code

You can look [here](ex_step1.md) to see an example of how the code might look if you've followed the instructions so far.

We don't actually need this ```for``` loop for the game. It was just an excuse to see if you remembered how to make a ```for``` loop. So remove your loop, and go back to the original code which ends with this line *not indented*
  
```python
print(pictures[0])
```

which will print the first item in the pictures list, for when we are ready to start playing the game.
  
[Go to Step 2 - Choosing and displaying the mystery word](../step02-choose_word_and_display/STEP2.md)

[Go back to front page](../README.md)
