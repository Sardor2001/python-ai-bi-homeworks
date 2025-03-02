def convert_cel_to_far(celsius):
    return celsius * 9 / 5 + 32


def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


fahrenheit = float(input("Enter a temperature in degrees Fahrenheit: "))
celsius = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit}°F is equal to {round(celsius, 2)}°C")

celsius = float(input("Enter a temperature in degrees Celsius: "))
fahrenheit = convert_cel_to_far(celsius)
print(f"{celsius}°C is equal to {round(fahrenheit, 2)}°F")
