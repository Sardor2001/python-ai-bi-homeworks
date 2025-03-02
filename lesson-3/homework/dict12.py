my_dict = {'name': 'Alice', 'age': 30, 'city': 'Alice', 'country': 'USA'}
value_to_count = 'Alice'

count = sum(1 for v in my_dict.values() if v == value_to_count)
print(count)
