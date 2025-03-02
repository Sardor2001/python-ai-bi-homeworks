def find_indices(lst, target):
    return [i for i, val in enumerate(lst) if val == target]


numbers = [1, 2, 3, 2, 4, 2, 5]
print(find_indices(numbers, 2))
