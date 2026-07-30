#!/usr/bin/python3
"""Module that prints the first x integers of a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, only if they are integers.

    Args:
        my_list (list): the list to print elements from.
        x (int): the number of elements to access in my_list.

    Returns:
        int: the real number of integers printed.
    """
    count = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return count
