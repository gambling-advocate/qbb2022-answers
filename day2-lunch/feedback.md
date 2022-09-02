# Feedback day2-lunch

Overall this is a really good script. Your comments both convey your intent but also nicely break the code up into logical chunks. Your logic made sense and was nicely executed. Just a couple of notes.

- If this script encounters a value that can't be converted into the expected type, it will throw an error and exit. The easiest solution would be to wrap the type conversion in a `try` statement.
- There needs to be a check that itemRGB is exactly 3 items
- There is no splitting and converting of blockStarts and blockSizes
- You need to check that when split, blockStarts and blockSizes have lengths equal to the number in blockCount

You seem to be in a comfortable place with this level of python. Great job and keep it up!