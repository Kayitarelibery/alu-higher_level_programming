#!/usr/bin/python3
"""Module that divides element by element two lists."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element two lists.

    Args:
        my_list_1 (list): the list of numerators.
        my_list_2 (list): the list of denominators.
        list_length (int): the length of the resulting list.

    Returns:
        list: a new list with the results of each division.
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
