"""
PROBLEM:
Write a function named join_or that allows you to specify a 
form of punctuation with which to connect a list of items.
The function should also allow you to specify a word to go before 
the last item in the list.

EXAMPLE:
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"

ALGORITHM:
- Print each element of a list followed by punc, except for the last element

"""
def join_or(lst = [], punc = ',', and_or = 'or'):
    result = ''
    punc = punc.strip()
    and_or = and_or.strip()
    
    if not lst:
        return ''
    elif len(lst) == 1:
        return f'{lst[0]}'
    elif len(lst) == 2:
        return f'{lst[0]} {and_or} {lst[1]}'
    else:
        for idx, item in enumerate(lst):
            if idx == len(lst) - 1:
                result += f'{and_or} {item}'
            else:
                result += f'{item}{punc} '
    
    return result