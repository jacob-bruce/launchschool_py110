"""
Write a function that takes a list of numbers and returns a list 
with the same number of elements, but with each element's value 
being the running total from the original list.

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

Problem:
- Take a list
- Return a new list with same number of elements as first list
- But now the elements should be a running total 

[a, b, c, d, e]. ---> [a, a+b, a+b+c, a+b+c+d+e]

Algorithm:
- Create new empty list
- We'll probably need to track index positions
- Loop is something like, for each number, add all the numbers behind it
- I think we can just add the first one, so loop would start at second number

Better we use a sum variable

initialize sum
- loop through the list of numbers
- add each value to sum
- append sum to the new list 
-start loop over
"""

def running_total(lst):
    total = 0
    result = []

    for num in lst:
        total += num
        result.append(total)

    return result

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True