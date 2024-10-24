def remove_duplicates(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    return result

lst = input("Enter elements of the list separated by spaces: ").split()

print(remove_duplicates(lst))
