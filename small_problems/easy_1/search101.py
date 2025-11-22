"""
Write a program that solicits six (6) numbers from the user 
and prints a message that describes whether the sixth number 
appears among the first five.

P:
- Take input from the user six times for a number
- store to a list
- search the list to see if the sixth number is among the first 5
- print the sixth number followed by a statement

Assumptions:
- Assume all inputs are numbers

E:
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

D:
- input: ints from user
- output: string

A:
- Take input from user. Append to empty list
- after sixth, search first 5 to see if the sixth number is in list
- Use if branches to write different results

"""


def number_finder():
    num_lst = []
    num1 = (input('Enter the 1st number: '))
    num2 = (input('Enter the 2nd number: '))
    num3 = (input('Enter the 3rd number: '))
    num4 = (input('Enter the 4th number: '))
    num5 = (input('Enter the 5th number: '))
    num6 = (input('Enter the 6th number: '))

    num_lst.append(num1)
    num_lst.append(num2)
    num_lst.append(num3)
    num_lst.append(num3)
    num_lst.append(num4)
    num_lst.append(num5)

    if num6 in num_lst[0:6]:
        print(f'{num6} is in {num1}, {num2}, {num3}, {num4}, {num5}')
    else:
        print(f"{num6} isn't in {num1}, {num2}, {num3}, {num4}, {num5}")

number_finder()