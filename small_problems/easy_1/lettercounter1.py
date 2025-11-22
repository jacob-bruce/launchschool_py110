"""
Write a function that takes a string consisting of zero or 
more space-separated words and returns a dictionary that 
shows the number of words of different sizes.

Problem: 
- Take a string that could have zero or more words separated by spaces
- Return a dictionary. The keys are word lengths, the values are number of 
words that are that length

Rules:
- Non-alpha seems to be part of the string e.g. this. = 5 characters

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

Data:
- Input: string
- Output: dictionary

Algorithm:
- Create blank dictionary result
- Put the words in a list using split since all words sep by space
- Loop through words and get count
- Then we use get +1 

"""

def word_sizes(s):
    result = {}
    word_lst = s.split(' ')
    
    if not s:
        return result
    else:
        for word in word_lst:
            result[len(word)] = result.get(len(word), 0) + 1
    return result

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})