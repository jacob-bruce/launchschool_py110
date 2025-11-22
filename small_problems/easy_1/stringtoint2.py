"""
Problem:
Take a number formatted as a string. If the first character of the number is a minus sign,
the number is negative.

Input: String
Output: Int

Rules/Restrictions:
- If there is no sign, return a positive number.
- You may assume the string will always contain a valid number.
- You may not use any of the standard conversion functions available in Python, such as int. 
- You may, however, use the string_to_integer function from the previous exercise.

Ex:
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

Algorithm:
- Take the string number
- Pass it to a helper function "sign checker
    - If first character is -, return '-'
    - Else return '+'
    - Save return value in a variable
- Pass it to another helper function "number maker"
    - If first character is '+' or '-'
        return s[1:]
    - Else return s
    - Save return value in a variable 
- Now we have sign and number without sign,
    - We use string to int helper function to return int values
- Finally we assign sign using + minus from above
    - return s * -1 if 

    

"""
def sign_checker(s):
    return '-' if s[0] == '-' else '+'

def remove_sign(s):
    return s[1:] if s[0] == '-' or s[0] == '+' else s

def string_to_integer(s):
    string_to_int_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    result = 0
    for digit in s:
        result = (10 * result) + string_to_int_dict[digit]
    
    return result

def string_to_signed_integer(s):
    sign = sign_checker(s)
    sign_removed_string = remove_sign(s)
    int_string = string_to_integer(sign_removed_string)

    return int_string * -1 if sign == '-' else int_string

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True




