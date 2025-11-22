"""
Problem:
Write a function that takes a string of digits and returns the 
appropriate number as an integer. You may not use any of the 
standard conversion functions available in Python, such as int. 
Your function should calculate the result by using the characters in the string.


Example:
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

Algorithm:
- Get the string
- initialize a blank int_string variable
- Get length of the string in a variable
- Initialize index position variable to 0
- Initialize sum variable to 0

- While the length of the loop number is > 0:
    - Get the number in the index position
    - Compare that against a match/case table that returns ints
    - Multiply the int by 10 ^ length variable -1
    - Add that number to the sum variable
    - Length variable minus 1
    - index position variable plus 1

"""

def string_to_integer(s):
    s_length = len(s)
    loops = s_length
    ten_power = len(s) - 1
    idx = 0
    result = 0

    while loops > 0:
        num = ord(s[idx]) - ord('0')
        num = num * (10 ** ten_power)
        result += num
        idx += 1
        ten_power -= 1
        loops -= 1
    
    return result

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

