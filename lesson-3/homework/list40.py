def unique_elements(lst):
    myset = set()
    return [x for x in lst if not (x in myset or myset.add(x))]


numbers = [4, 2, 2, 3, 1, 5, 3, 6, 1, 7]
print(unique_elements(numbers))
