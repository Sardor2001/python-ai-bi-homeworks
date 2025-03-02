tup = (1, 9, 9, 8, 2, 5)


def second_smallest(tpl):
    sorted_list = sorted(list(set(tpl)))
    return sorted_list[-2]


print(second_smallest(tup))
