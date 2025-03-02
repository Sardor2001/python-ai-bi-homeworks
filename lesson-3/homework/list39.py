def nested_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nested_list(numbers, 3))
