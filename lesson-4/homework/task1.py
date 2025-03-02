list1 = [1, 2, 3, 4]
list2 = [4, 3, 5, 8]

uncommon_elements = list(set(list1) ^ set(list2))

print("Uncommon elements: ", uncommon_elements)
