from decimal import Decimal

num1 = Decimal(input("Enter a number1: "))
num2 = Decimal(input("Enter a number2: "))

if num1+num2>50.8:
    print("The sum is greater than 50.8")

if 10<=num1<=20:
    print("The number1 is between 10 and 20 (inclusive)")
