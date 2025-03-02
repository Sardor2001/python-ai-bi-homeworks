nested_dict = {
    'person': {
        'name': 'Alice',
        'age': 30,
        'address': {
            'city': 'New York',
            'state': 'NY'
        }
    }
}

# Accessing the value of the 'city' key inside the 'address' dictionary
city = nested_dict['person']['address']['city']
print(city)
