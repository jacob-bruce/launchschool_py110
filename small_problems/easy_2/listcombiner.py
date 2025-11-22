"""
Write a function that takes two lists as arguments and returns 
a set that contains the union of the values from the two lists. 
You may assume that both arguments will always be lists.

Problem:
- Take two lists
- Return one set with the union of the values
"""

#Solution 1
def union(lst1, lst2):
    result = set(lst1)

    for value in lst2:
        result.add(value)

    return result

#Solution 2
def union(lst1, lst2):
    result = set(lst1)
    result.update(lst2)
    return result

#Solution 3
def union(lst1, lst2):
    return set(lst1) | set(lst2)


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
