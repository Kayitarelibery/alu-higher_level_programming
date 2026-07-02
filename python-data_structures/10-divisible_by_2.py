#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Args:
        my_list: list of integers

    Returns:
        A new list of the same size, with True or False depending on
        whether the integer at the same position is a multiple of 2.
    """
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
