list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2, 3, 4, 5, 6, 7]


def middle(lst):
    mid = len(lst) // 2
    return lst[mid - 1:mid + 1] if len(lst) % 2 else [lst[mid]]


print(middle(list1))
print(middle(list2))
