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
- initialize empty list
- initialize empty string (swapped_string)
- create list of words from string
- loop through each word
- swapped string = word[-1] + word[1:-2] + word[0]
- add swapped string to word list
- combine word list into new string

"""

def swap(s):
    word_lst = s.split(' ')
    swapped_lst = []
    swapped_string = ''

    for word in word_lst:
        if len(word) == 1:
            swapped_string = word
            swapped_lst.append(swapped_string)
        else:
            swapped_string = word[-1] + word[1:-1] + word[0]
            swapped_lst.append(swapped_string)
    
    swapped_string = ' '.join(swapped_lst)

    return swapped_string


print(swap('Oh what a wonderful day it is'))
print(swap('Abcde'))
print(swap('a'))

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

