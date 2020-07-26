TODO: Reflect on what you learned this week and what is still unclear.
Quite stumped on getting the wordy_pyramid final test to pass. Tried to change the main function, but not sure if that should be needed.

The questions on triangles were quite fun to do. Found out there are a few ways to use a square root.
>pow(x,0.5)

>x**(1/2)

>import math
>math.sqrt(x)

Formatting the dictionary proved to be quite challenging in the sense that repetitive use of the word "dictionary" gets quite confusing and causes silly mistake. Will need to think more careful about to name variables in the future.

Used knowledge from week4 to import random word generator and convert to python readable text for the word pyramid. However, as mentioned above, the last part of the wordy_pyramid doesn't pass the test due to:
>unsupported operand type(s) for +: 'range' and 'range'
As range doesn't return a list on python 3, I have place a list bracket over the range functions, but it is to no avail.

Update:
> lengths = list(range(3,21,2) + range(20,3,-2))
was changed to 
> lengths=[3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4]
with a new error saying: "wordy_pyramid is broken can't concat str to bytes"... still unsure of a way to fix this

Update 2:
message was fixed by changing 
> r.content 
to 
>r.text
.content outputs in bytes while .text outputs in unicode

Also, in list_of_words_with_lengths
    # noPyr = []
    # for i in list_of_lengths:
    #     noPyr.append(get_a_word_of_length_n(i))
    #     return noPyr

was replace with the map
    # pyrMap =map(get_a_word_of_length_n, list_of_lengths)
    # return pyrMap

The tests for exercise 2, do not seem to update unless I fix everything in exercise 1 first, which is quite inconvenient.