dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'b': 5, 'e': 6}

# Check if there are any common keys
common_keys = set(dict1.keys()) & set(dict2.keys())

if common_keys:
    print("Common keys found:", common_keys)
else:
    print("No common keys.")
