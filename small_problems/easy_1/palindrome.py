"""
Write a function that returns True if the string passed as an argument 
is a palindrome, False otherwise. A palindrome reads the same forwards 
and backwards. For this problem, the case matters and all characters matter.

Problem:
- Given a string, return True if its a palindrome, False otherwise.

"""

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)