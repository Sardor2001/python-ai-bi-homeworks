from decimal import Decimal

num = Decimal(input("Enter a number: "))

if num%3 == 0 and num%5 == 0:
    print("It is divisible by both 3 and 5")
else:
    print("It is NOT divisible by both 3 and 5")
