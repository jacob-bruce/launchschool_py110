def find_dup(lst):
    seen = set()

    for element in lst:
        if element in seen:
            return element
        
        seen.add(element)