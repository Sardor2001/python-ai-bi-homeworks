my_dict = {'a': 5, 'b': 10, 'c': 3, 'd': 8, 'e': 1}

filtered_dict = {key: value for key, value in my_dict.items() if value > 5}

print(filtered_dict)
