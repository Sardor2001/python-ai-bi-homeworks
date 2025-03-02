my_dict = {'name': 'Alice', 'age': 30, 'city': 'Alice', 'job': 'Engineer'}
target_value = 'Alice'

keys_with_value = [key for key, value in my_dict.items() if value == target_value]

print(keys_with_value)
