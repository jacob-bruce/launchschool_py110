def swap_name(name):
    return ', '.join(name.split()[::-1])

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
