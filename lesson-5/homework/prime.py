import math


def is_prime(n):
    if n < 2:
        return False

    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):  # Check divisibility from 2 to √n
        if n % i == 0:
            return False
    return True


n = int(input("Enter a number: "))
print(is_prime(n))
