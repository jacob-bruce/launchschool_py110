"""
Given a string of words separated by spaces, write a function 
that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and 
that the string will always contain at least one word. You may 
also assume that each string contains nothing but words and spaces, 
and that there are no leading, trailing, or repeated spaces.


Examples:
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

Algorithm:
- Get string into a list
- Loop through that list word by word
- Loop through each word by index position
    - For a given index position, 
        - Index position + 1 becomes index position
        - Index position becomes index position + 1


[t, h, a, t]
[s, t, r, i, n, g] .pop(0)
[t, r, i, n, g]
        


t moves to 1 
h moves to 0 #htat

t moves to 2
a moves to 1 #hatt

last t moves to 3 
t moves to 2 #hatt

-Loop through the string by index
- if length is 

"""

def swap(s):
    word_lst = s.split(' ')
    swapped_lst = []
    swapped_word = ''

    for word in word_lst:
        if len(word) == 1:
            swapped_lst.append(word)
        else:
            char_lst = list(word)
            for i in range(len(char_lst) - 1):
                next_letter = char_lst[i]
                char_lst[i] = char_lst[i + 1]
                char_lst[i + 1] = next_letter
            print(char_lst)

    
    print(swapped_lst)


swap('Oh what a wonderful day it is')


