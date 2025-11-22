"""Problem:
- Take a list of strings
- Within each string, count the number of adjacent consonants
- Sort the list based on the number of adjacent consonants
- Return the sorted string

Rules/Restrictions
- If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other.
- Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.
- If there is punctuation in between consonants, it does not count
- Case is irrelevant
- Strings could have more than one word
- Based on examples, sort by most consonants to least
- Strings will not be empty
- Single consonants in a string do not affect sort order in comparison to strings with no consonants. Only adjacent consonants affect sort order.
- New list or sort original list?
  
Input/Output
- I: List of strings
- O: List of sorted strings

Examples:
my_list = ['aa', 'baa', 'ccaa', 'dddaa'] print(sort_by_consonant_count(my_list)) # ['dddaa', 'ccaa', 'aa', 'baa'] my_list = ['can can', 'toucan', 'batman', 'salt pan'] print(sort_by_consonant_count(my_list)) # ['salt pan', 'can can', 'batman', 'toucan'] my_list = ['bar', 'car', 'far', 'jar'] print(sort_by_consonant_count(my_list)) # ['bar', 'car', 'far', 'jar'] my_list = ['day', 'week', 'month', 'year'] print(sort_by_consonant_count(my_list)) # ['month', 'day', 'week', 'year'] my_list = ['xxxa', 'xxxx', 'xxxb'] print(sort_by_consonant_count(my_list)) # ['xxxx', 'xxxb', 'xxxa']

Data Structures:
string: we'll be evaluating lits of strings
lists: the input and output will be a list
int: we'll need to count the number of consonants in a row
Boolean: We'll need to compare the counts of consonants throughout the word to find the longest one

Algorithm:
- Intialize variable count to zero 
- Initialize empty adjacent consonants string 
- Loop through list of strings
- Loop through individual string elements by index position
- Remove the spaces from the string
- if the char in the index position is a vowel, skip
- if the char is not a vowel
		- add the char to the empty consonants string
		- loop through the remaining elements
		- add each non-consonant to the adjeacent consonants string
		-When you get to a vowel, save the ad. cons. string and its length somewhere
		- reset the adjacent consonanat string


Algorithm:
- Loop through the list of strings
- Loop through each string
- Find the max consonant count


I need to compare the consonant counts from each word and then 
- Dictionary of dictionaries? {word: {consonant string: length}}

"""

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

def count_max_adjacent_consonants(s):
    s_nospaces = s.replace(' ', '')
    adj_cons_string = ''
    max_cons_count = 0
    for char in s_nospaces:
        if char not in {'a', 'e', 'i', 'o', 'u'}:
            adj_cons_string += char
        else:
            if len(adj_cons_string) > max_cons_count:
                if len(adj_cons_string) > 1:
                     max_cons_count = len(adj_cons_string)
            adj_cons_string = ''

    if len(adj_cons_string) > max_cons_count:
        max_cons_string = adj_cons_string
        max_cons_count = len(max_cons_string)

    return max_cons_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# Expected: ['dddaa', 'ccaa', 'aa', 'baa']
# Actual:   ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# Expected: ['salt pan', 'can can', 'batman', 'toucan']
# Actual:   ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# Expected: ['bar', 'car', 'far', 'jar']
# Actual:   ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# Expected: ['month', 'day', 'week', 'year']
# Actual:   ['day', 'week', 'month', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))