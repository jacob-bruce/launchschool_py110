"""

Calculate the total age given the following dictionary:

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

Problem:
- Calculate the sum of all the ages in the dictionary

Input: N/A
Output: Sum of ages

Algorithm:
- If I didn't know about the sum function, I would use a count variable
with a loop

"""

def dictionary_summer(your_dict):
    count = 0
    for number in your_dict.values():
        count += number
    return count

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print(dictionary_summer(ages))
print(sum(ages.values()))