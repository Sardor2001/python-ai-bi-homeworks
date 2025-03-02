lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def min_in_sublist(lst, start, end):
    sublist = lst[start:end + 1]
    return min(sublist) if sublist else None


print(min_in_sublist(lst1, 1, 3))
