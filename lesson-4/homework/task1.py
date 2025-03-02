list1 = [1, 2, 3, 4]
list2 = [4, 3, 5, 8]

uncommon_elements = []

for item in list1:
    if item not in list2:
        uncommon_elements.append(item)

for item in list2:
    if item not in list1:
        uncommon_elements.append(item)

print("Uncommon elements: ", uncommon_elements)