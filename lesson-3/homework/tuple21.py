tup = (1, 2, 3, 4, 5)
num = 2
new_tup = tuple(elem for elem in tup for _ in range(num))
print(new_tup)
