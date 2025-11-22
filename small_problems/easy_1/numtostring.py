"""
Write a function that converts a non-negative 
integer value (e.g., 0, 1, 2, 3, and so on) to 
the string representation of that integer.


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

Problem:
Convert integer number to string version without built in methods

Algorithm:
- Create blank string num_string = ''
- Create dictionary with int, string key value pairs


Get Digit
- Can't loop or make list: not iterable
- Loop (helper function)
    - Integer ivide by powers of ten until you get to 0
    - Each time have a counter go up --> this gives us the length of the int
    - May need zerodivision try except here

- Loop through
    - Divide by 1 * 10 ** lenth above
    - Add the number to a list
    - subtract 1 from the length
    - subtract from the whole

ivide by powers of ten 
- while loop
    num // 

"""

def integer_length(num):
    int_length = 0
    result = 1

    try:
        1 / num
    except ZeroDivisionError:
        return 0 
    
    while num != 0:
        num = num // (10)
        result += 1
    print(result)
    return result - 1

def digit_lst_maker(num, int_length):
    result = []
    count = int_length - 1
    
    while count >= 0:
        digit = num // (10 ** count)
        result.append(digit)
        num = num - (digit * 10 ** count)
        count -= 1

    return result

def digit_str_maker(lst):
    digit_str = ''

    int_str_dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9'
    }

    for digit in lst:
        digit_str += int_str_dict[digit]
    
    return digit_str

def integer_to_string(num):
    int_length = integer_length(num)
    
    if not digit_lst_maker(num, int_length):
        return '0'
    else:
        digit_lst = digit_lst_maker(num, int_length)
        return digit_str_maker(digit_lst)

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True