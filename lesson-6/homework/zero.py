# Decorator function to check for zero denominator
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)

    return wrapper


# Applying the decorator to the div function
@check
def div(a, b):
    return a / b


# Test cases
print(div(6, 2))  # Output: 3
print(div(6, 0))  # Output: "Denominator can't be zero"
