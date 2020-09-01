# Creating the set of pictures in a list variable

In this version of Hangman the player has six guesses at letters in the mystery word. Each time the player guesses a letter which is **_not_** in the word the picture changes and adds an extra bit of body to the figure of the person being hanged.

This means that the picture which is displayed is linked to the number of wrong guesses so far: if there are no wrong guesses the picture shows just the gallows and no parts of the person; if there has been one wrong guess so far the picture shows the gallows and the person's head, two wrong guesses and we show the gallows, head and body, and so on up to a maximum of six wrong guesses.

In Python the smartest way to achieve this is to make a numeric variable to hold the number of wrong guesses, and put all the different pictures in a **_list_** variable. The programme chooses which picture to display by using the number of wrong guesses as the **_index_** number for the list.

Example - we'll put all the pictures in a list variable called ```pictures``` and if there have been four wrong guesses the variable with the number of wrong guesses will be set to 4 and the Python code to show the right picture will be
```
print(pictures[number of wrong guesses variable])
```
which will print the **_5th_** item in the list. (Do you remember why it will print the 5th item although the index number is 4?)

In the starter project we have already started a list variable called ```pictures``` and put the first two items in the list, separated by a comma, which are the pictures to use when there have been no wrong guesses, and one wrong guess.

These pictures are really text characters arranged cleverly so they seem to draw a picture. The symbols used so far are ```_ | O /```. By choosing different text characters you should be able to work out how to draw the person's body, arms and legs.
 
## Your first task

Your first task is to add five more pictures to this list for the situations where there have been 2, 3, 4, 5 and 6 wrong guesses. 

The smart way is to copy the last item in the list, paste it onto the end of the list (**don't forget to put in a comma**) then add another part of the figure to the pasted version. Then copy the new last item, paste it on the end of the list and edit it, and so on.


## Triple quotes as a way of making a Python string

Each of the items in a list is a text string, but you might have noticed that these text strings don't begin and end with `"` or `'`, they begin and end with `"""` - a triple double-quote mark. What is the meaning of a triple quote mark?

You can see an explanation of this near the end of the introductory [video](https://youtu.be/FOJO9RdFEF8) for this project, but the simple explanation is that a text string which is inside *triple* quotes can spread across several lines, so if you want your string to 


The starter project has already 

We need to create a set of pictures for each stage of the game, and we will put the set of these pictures in a list.

In the starter project there is a list called ```pictures``` which already has the empty gallows picture, and the picture showing the head of the man. Notice how 

## Check your handiwork

You should check that your sequence of pictures looks all right and the pictures a

[Go to Step 2 - Choosing and displaying the mystery word](../step02-choose_word_and_display/STEP2.md)
