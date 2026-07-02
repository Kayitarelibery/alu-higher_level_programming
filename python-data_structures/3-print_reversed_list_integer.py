#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line.

    Args:
        my_list: list of integers
    """
    my_list.reverse()
    for number in my_list:
        print("{:d}".format(number))
