"""
PROBLEM:
Write a function that takes a string as an argument and returns True 
if all parentheses in the string are properly balanced, False otherwise. 
To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

EXAMPLE:
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

DATA:

ALGORITHM:
- Two counts: open and closed
- If closed count > then open FALSE

"""
def is_balanced(s):
    open_count = 0
    closed_count = 0
    start = 0
    s_length = len(s)

    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            closed_count += 1
        
        if closed_count > open_count:
            return False
        
    return open_count == closed_count
    
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True