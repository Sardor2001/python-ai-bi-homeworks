tup = (1, 4, 9, 8)


def is_tuple_sorted_ascending(tpl):
    return tpl == tuple(sorted(tpl))


print(is_tuple_sorted_ascending(tup))
