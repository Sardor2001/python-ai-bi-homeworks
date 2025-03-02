import random

num_elements = 5
start_range = 1
end_range = 10

random_set = set(random.sample(range(start_range, end_range), num_elements))

print("Random set:", random_set)
