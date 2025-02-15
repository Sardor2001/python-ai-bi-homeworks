from decimal import Decimal

number = Decimal(input("Enter a number: "))

if number>0 and number%2 == 0:
    print("It is positive and even")
else:
    print("It is not both positive and even")