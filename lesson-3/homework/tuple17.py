def max_in_subtuple(tup, start, end):
    """
    Find the maximum value in a subtuple
    :param tup: The original tuple
    :param start: Starting index of the subtuple (inclusive)
    :param end: Ending index of the subtuple (exclusive)
    :return: Maximum element in the subtuple
    """

    if start < 0 or end >= len(tup) or start >= end:
        return None
    return max(tup[start:end])


my_tuple = (1, 2, 3, 4, 5)
print(max_in_subtuple(my_tuple, 1, 3))
