lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    else:
        print("Index out of range")


remove_by_index(lst1, 3)
print(lst1)

