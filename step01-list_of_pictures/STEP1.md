# Creating the set of pictures in a list variable

In this version of Hangman the player has six guesses at letters in the mystery word. Each time the player guesses a letter which is *not* in the word the picture changes and adds an extra bit of body to the figure of the person being hanged.

This means that the picture which is displayed is linked to the number of wrong guesses so far: if there are no wrong guesses the picture shows just the gallows and no parts of the person; if there has been one wrong guess so far the picture shows the gallows and the person's head, two wrong guesses and we show the gallows, head and body, and so on up to a maximum of six wrong guesses.

In Python the smartest way to achieve this is to make a numeric variable to hold the number of wrong guesses, and put all the different pictures in a _*list*_ variable. The programme chooses which picture to display by using the number of wrong guesses as the _*index*_ number for the list.

Example - we'll put all the pictures in a list variable called ```pictures``` and if there have been four wrong guesses the variable with the number of wrong guesses will be set to 4 and the Python code to show the right picture will be
```
print(pictures[number of wrong guesses variable])
```



## Triple quotes as a way of making a Python string




The starter project has already 

We need to create a set of pictures for each stage of the game, and we will put the set of these pictures in a list.

In the starter project there is a list called ```pictures``` which already has the empty gallows picture, and the picture showing the head of the man. Notice how 



[Go to Step 2 - Choosing and displaying the mystery word](../step02-choose_word_and_display/STEP2.md)
