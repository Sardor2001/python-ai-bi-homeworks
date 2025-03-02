tup = (1, 2, 2, 3, 4, 3, 5)
unique_tup = tuple(sorted(set(tup), key=tup.index))
print("Unique tuple:", unique_tup)
