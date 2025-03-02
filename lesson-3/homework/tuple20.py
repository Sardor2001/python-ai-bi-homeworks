tup = (1, 2, 3, 4, 5)
size = 3

nested_tuple = tuple(tup[i:i + size] for i in range(0, len(tup), size))

print(nested_tuple)
