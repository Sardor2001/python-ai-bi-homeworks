def check_palindrome(lst):
    return lst == lst[::-1]


lst1 = [1, 2, 3, 2, 1]
print(check_palindrome(lst1))
