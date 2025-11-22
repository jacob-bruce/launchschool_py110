"""
How would you count the number of occurrences of "banana" in the tuple?

fruits = ("apple", "banana", "cherry", "date", "banana")

Problem: 
- Count the number of times a string occurs in a tuple
- Specifically, how many times the word banana occurs

E:
string_counter(fruits, 'banana') # 2

D:
Input: String
Output: Int (#times string occurs)

A:
- Initialize variable count and set to zero
- loop through the tuple
- if the item in the loop matches the string, count += 1
- return count
"""


def string_counter(lst, word):
    count = 0

    for item in lst:
        if item == word:
            count += 1
    return count

fruits = ["apple", "banana", "cherry", "date", "banana"]

print(string_counter(fruits, 'banana')) # 2
print(fruits.count("banana"))
