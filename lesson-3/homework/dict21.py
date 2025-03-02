def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

print(sort_dict_by_value(my_dict))

print(sort_dict_by_value(my_dict, reverse=True))
