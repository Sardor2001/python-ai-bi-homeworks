def check_sorted(lst):
    if lst == sorted(lst):
        return True
    return False


lst1 = [1, 2, 3, 4, 11, 6, 7, 8, 9, 10]
print(check_sorted(lst1))
