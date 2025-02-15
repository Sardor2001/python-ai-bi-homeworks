from decimal import Decimal

kilometers = Decimal(input("Enter in kilometers: "))
meters = kilometers*1000
centimetres = meters*100

print(f"{meters.normalize()} meters or {centimetres} centimeters")
