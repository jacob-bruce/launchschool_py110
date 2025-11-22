"""
PROBLEM:
Write a function that takes a string argument consisting of a 
first name, a space, and a last name. The function should return 
a new string consisting of the last name, a comma, a space, and the first name.

EXAMPLE:
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

ALGORITHM:
- Convert into list using name.split(' ')
- Use iterable unpacking to assign to name, last name
- Return f'{last_name}, {name}'
"""
def swap_name(firstlast_name):
    first_name, last_name = firstlast_name.split(' ')
    return f'{last_name}, {first_name}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
