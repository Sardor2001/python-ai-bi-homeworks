from decimal import Decimal

num1 = Decimal(input('Enter first number: '))
num2 = Decimal(input('Enter second number: '))
num3 = Decimal(input('Enter third number: '))

if num1 == num2 == num3:
    print('They are equal')
else:
    print('They are not equal')
