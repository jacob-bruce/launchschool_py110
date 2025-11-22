"""
Given the following string, create a dictionary that represents 
the frequency with which each letter occurs. 
The frequency count should be case-sensitive:

statement = "The Flintstones Rock"

Example:
# Pretty printed for clarity
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}

"""
from pprint import pprint

statement = "The Flintstones Rock"

def char_counter(your_string: dict):
    result = {}
    for char in your_string:
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result

pprint(char_counter(statement))

