# Creating the set of pictures in a list variable

In this version of Hangman the player has six guesses at letters in the mystery word. Each time the player makes a *wrong* guess (guesses a letter which is **_not_** in the word) the picture adds an extra bit of body to the figure of the person being hanged.

This means which picture we display is controlled by the number of wrong guesses: if there are no wrong guesses so far we show the picture with just the gallows; if there has been one wrong guess so far we show the gallows and the person's head, two wrong guesses and we show the gallows, head and body, and so on up to a maximum of six wrong guesses.

We can do this in Python by making a variable to hold the number of wrong guesses, and putting all the pictures in a Python **list**. Then we can use the number of wrong guesses as the **_index_** for the picture in the pictures list that we want to show.

In the starter project we have already started a list variable called ```pictures``` and put the first two items (pictures) in the list, separated by a comma.

These pictures are really just combinations of text symbols arranged cleverly so they seem to draw a picture. The symbols used so far are ```_ | O /```. By adding these and other text symbols you should be able to draw the person's body, arms and legs.

## Your first task

Your first task is to add five more pictures to the pictures list: first add the body, then the left arm, then the right arm, then the left leg, then the right leg. We will use these pictures for 2, 3, 4, 5 and 6 wrong guesses.

One smart way to add a new picture is to copy the previous picture in the list, paste it onto the end of the list (**don't forget to put in a comma**) then add a new body part to the pasted version.

## Triple quotes as a way of making a Python string which goes over several lines

Each of the items in a list in the starter project is a *text string*, but you might have noticed that these text strings don't begin and end with `'` or `"` like normal text strings, they begin and end with `"""` - a triple quote mark. What is the meaning of a triple quote mark?

You can see an explanation of this near the end of the introductory video [(link to video)](https://youtu.be/FOJO9RdFEF8) for this project, but the simple explanation is that a text string which is inside *triple* quotes can spread across several lines, so any time you want your string start a new line you type ENTER inside the triple quotes, and this will be shown as a new line when Python prints the text.

You can use either triple single quotes ```'''``` or triple double-quotes ```"""``` to get this effect.

## Special feature of the ```\``` character

You might decide to use the backslash ```\``` character for one of the figure's legs - unfortunately this creates a small problem. 

In Python strings sometimes people wanted to include types of formatting which wouldn't be available from the normal keyboard, so it was decided that if you put a backslash character in the string you could follow that with some other character which would tell the string to include formatting. One example is if you put ```\n``` inside a string and print it Python won't print the backslash or the ```n```, it will start a new line. 

If we want a string where we actually **_do_** want to print a backslash (for example for one of the figure's legs) we simply put two backslashes ```\\```, and Python will ignore the first, and print the second.

## Check your handiwork

Once you've finished making your list you should check that your sequence of pictures looks all right and the pictures are in the right order. At the end of the starter project, in the MAIN CODE section, there is a line of code
```python
print(pictures[0])
```
which will print the first item from the list. Change the number in square brackets to see the other items in your list.

# Challenge

How would you make a Python **_loop_** to show the pictures one after another without having to keep typing a different number in the square brackets?

You will want your loop to start with ```for```, then a list variable, then ```in```, then your pictures list, then a ```:```. On the next lines, (which need to be indented) you should put the code which will 

* clear the screen so the next picture is drawn in the same place - that line is already in the starter project, it is ```system('cls')```, 
* print the item from the list
* pause before going on to the next picture

The code for clearing the screen is ```system('cls')``` and you should find this in the starter project.
To pause the code use

```python
input()
```

which means the programme will wait until you press the Enter key

Don't forget about **_indenting_** the lines of code inside the loop.

### Note about typing in the right hand panel

When you're writing code in Trinket it always assumes you're in the *edit* panel so anything you type on the keyboard will appear in the code. This is no good if you want to type the response to a question in the **Result** panel on the right. The way to do this is the click the mouse once inside the right panel before you type anything, and this switches the **_focus_** to the right panel, so what you type will appear there and not inside your code.

Be warned: it's **terribly** easy to forget to do this, and accidentally make edits to your code!

Did you manage to make a loop which worked? Go to [this link](./STEP1A.md) to see one way to do it.

We don't need the loop for the game. Instead, remove your loop, and at the end of the code add the code
```python
print(pictures[0])
```

[Go to Step 2 - Choosing and displaying the mystery word](../step02-choose_word_and_display/STEP2.md)
