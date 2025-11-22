
"""
Write a function that takes a string, doubles every consonant in the string, 
and returns the result as a new string. The function should not double vowels 
('a','e','i','o','u'), digits, punctuation, or whitespace.

Algorithm:

"""
def double_consonants(s):
    result = []
    
    for char in s:
        if char.lower() not in {'a', 'e', 'i', 'o', 'u'} and char.isalpha():
            result.append(char * 2)
        else:
            result.append(char)
    return ''.join(result)
    
    #return ''.join([char * 2 for char in s]) if s not in {'a', 'e', 'i', 'o', 'u'} else ''.join([char for char in s])

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")