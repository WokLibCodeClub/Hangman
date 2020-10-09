In this example the variable to hold the original word has been named ```word_to_guess``` and the variable to hold the display text has been named ```word_with_guesses```.

These two lines go at the end of the VARIABLES section:

```python
word_with_guesses = "_" * len(word_to_guess)
word_with_guesses = list(word_with_guesses)
```
and this line goes at the very end of the code

```python
print(' '.join(word_with_guesses)) 
```


[Go back to Step 2 - Choosing and displaying the mystery word](./STEP2.md)

[Go to Step 3 - Guessing a letter](../step03-guessing_a_letter/STEP3.md)

