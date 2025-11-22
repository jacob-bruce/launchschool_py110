"""
Write a function that combines two lists passed as arguments and 
returns a new list that contains all elements from both list arguments, 
with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.
"""

def interleave(lst1, lst2):
    result = []
    length = len(lst1)
    print(length)
    for idx in range(0, length):
        result.append(lst1[idx])
        result.append(lst2[idx])
    
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True