"""

Example:
print(swap_name('Karl Oskar Henriksson Ragvals') == "Ragvals, Karl Oskar Henriksson")  # True

Algorithm:
- Save names to a list
- Print out the last indexed item
- Print out the other items
"""
def swap_name(fml_name):
    name_str = ''
    name_lst = fml_name.split()

    result = name_lst[-1] + ', '

    for name in name_lst:
        name_str += name
    
    return result

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True