"""
PROBLEM:
Create a function that takes two integers as arguments. 
- The first argument is a count. The function should return a list containing 
the same number of elements as the count argument. 
- the second is the starting number of a sequence that your function will create. 

- The value of each element should be a multiple of the starting number.

You may assume that count will always be an integer greater than or 
equal to 0. The starting number can be any integer. If the count is 0, 
the function should return an empty list.

Example:
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

Algorithm:
- Add the start element to result
- Start a loop that goes while the length of result is less than desired_length
- During the loop, take the first element and multiply it by the count number



"""

def sequence(desired_length, start):
    result = []
    count = 1

    while count <= desired_length:
        result.append(start * count)
        count += 1

    return result

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
        
    
    
    
    
    
    #return [num for num in range(start, count * start + 1, start)]