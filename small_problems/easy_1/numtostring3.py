
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def signed_integer_to_string(number):
    result = ''
    sign = sign_finder(number)
    number = abs(number)

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    result = sign + result
    
    return result or '0'


def sign_finder(number):
    sign = ''
    if number > 0:
        return '+'
    elif number < 0:
        return '-'
    else:
        return ''

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True