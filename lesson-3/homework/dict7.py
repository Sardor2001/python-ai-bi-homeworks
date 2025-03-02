my_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'b'

if key in my_dict:
    del my_dict[key]
    print(f"Key '{key}' removed.")
else:
    print(f"Key '{key}' not found.")

print("Updated Dictionary:", my_dict)
