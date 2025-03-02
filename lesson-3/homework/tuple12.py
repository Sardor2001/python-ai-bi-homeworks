def second_largest(tpl):
    first, second = float('-inf'), float('-inf')
    for num in tpl:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second if second != float('inf') else None


numbers = (1, 8, 8, 7, 5, 5)
print(second_largest(numbers))
