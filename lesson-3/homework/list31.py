def repeat(lst, num):
    return [x for x in lst for _ in range(num)]


lst1 = [1, 2, 3, 4, 5]
print(repeat(lst1, 2))
