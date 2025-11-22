"""
Problem: 
Write a function that takes a list as an argument and returns 
a list that contains two elements, both of which are lists. 
Put the first half of the original list elements in the first element 
of the return value and put the second half in the second element. 
If the original list contains an odd number of elements, place the middle 
element in the first half list.

Example:
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

Data:
Input: List
Outout: Two lists

Algorithm:
- Initialize an empty variable -- lst_length
- initialize empty result lst
- Set lst_length to the length of the list passed in

- If its even
    - half_lst length = lst_length // 2

- If it's odd
    - first_lst_length = lenth - (length // 2)
    - second_lst_length = length // 2

"""
def half_lst_maker(lst, length):
    result1 =[]
    result2 = []
    length_lst_1 = ''
    length_lst_2 = ''

    if length % 2 == 0:
        length_lst_1 = length_lst_2 = length // 2
    else:
        length_lst_1 = length - (length // 2)
        length_lst_2 = length // 2

    for idx in range(length_lst_1):
        result1.append(lst[idx])

    for idx in range(length_lst_2 + 1, length):
        result2.append(lst[idx])
    
    return result1, result2

def halvsies(lst):
    result = []
    full_lst = lst.copy()
    lst_length = len(full_lst)

    half_lst1, half_lst2 = half_lst_maker(full_lst, lst_length)

    result.append(half_lst1)
    result.append(half_lst2)

    return result

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([1, 5, 2, 4, 3]))
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])