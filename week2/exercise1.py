"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# assign strings in a list to the variable some_words 
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # assign strings in a list to the variable some_words 

# loops through some_words and prints each string
for word in some_words:
    print(word) # loops through some_words and prints each string
# loops through some_words and prints each string
for x in some_words:
    print(x) # loops through some_words and prints each string

# Print results
print(some_words) # Print for loops above

# If length of vairable is greater than 3, print all strings with more than 3 characters
if len(some_words) > 3:
    print('some_words contains more than 3 words') # Print 'some_words contains more than 3 words' if length of some words are greater than 3

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
