import numpy as np


def faranheit_to_celcius(f):
    return (f - 32) * 5 / 9


vectorized_conversion = np.vectorize(faranheit_to_celcius)

temperature_f = np.array([32, 68, 100, 212, 77])
temperature_c = vectorized_conversion(temperature_f)

print(temperature_c)

