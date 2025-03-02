my_dict = {'b': 2, 'a': 1, 'c': 3, 'e': 5, 'd': 4}

sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}

print(sorted_dict)
