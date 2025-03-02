my_dict = {
    'name': 'Alice',
    'age': 30,
    'address': {'city': 'New York', 'state': 'NY'}
}

result = any(isinstance(value, dict) for value in my_dict.values())

print(result)
