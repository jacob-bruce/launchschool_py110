"""
Modify the word_sizes function from the previous exercise 
to exclude non-letters when determining word size. 
For instance, the word size of "it's" is 3, not 4.

Algorithm:
- Split sentence into list of words
- Loop through the list
- Loop through each word
- Delete non 
"""

def alpha_lst(words: list):
    alpha_word_lst = []
    alpha_word = ''

    for word in words:
        for char in word:
            if char.isalpha():
                alpha_word += char
        alpha_word_lst.append(alpha_word)
        alpha_word = ''
    
    return alpha_word_lst

def word_splitter(words: list):
    non_alpha_word_lst = words.split(' ')
    return non_alpha_word_lst    

def word_sizes(s):
    result = {}
    word_lst = (alpha_lst(word_splitter(s)))

    if not s:
        return result
    else:
        for word in word_lst:
            result[len(word)] = result.get(len(word), 0) + 1
    return result


string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
