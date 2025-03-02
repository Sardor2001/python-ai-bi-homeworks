tuple1 = (1, 2, 1, 4, 5, 1, 7, 1)
el = 1


def find_all_indices(tpl, elem):
    return [i for i, x in enumerate(tpl) if x == elem]


print(find_all_indices(tuple1, el))
