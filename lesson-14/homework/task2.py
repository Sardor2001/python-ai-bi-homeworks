import numpy as np


def power_function(base, exponent):
    return base ** exponent


vectorized_power = np.vectorize(power_function)

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
results = vectorized_power(bases, exponents)

print(results)