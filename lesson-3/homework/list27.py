lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def max_in_sublist(lst, start, end):
    sublist = lst[start:end+1]
    return max(sublist) if sublist else None


print(max_in_sublist(lst1, 1, 3))
