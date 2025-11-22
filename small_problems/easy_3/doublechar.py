"""
PROBLEM:
Write a function that takes a string, doubles every character 
in the string, then returns the result as a new string.

EXAMPLE:
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

DATA:
Input: string
Output: String

Algorithm:
- Loop through each character
- Add char * 2 to string
"""

def repeater(s):
    double_s = ''
    
    for char in s:
        double_s += 2 * char
    
    return double_s

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True