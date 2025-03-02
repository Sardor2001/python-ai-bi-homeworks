my_tuple = (1, 2, 3, 4, 5, 2)
el = 2

lst = list(my_tuple)
if el in lst:
    lst.remove(el)
print(tuple(lst))
