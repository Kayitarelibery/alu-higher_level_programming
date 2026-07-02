#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position.

    Args:
        my_list: the list
        idx: the index to replace
        element: the new element

    Returns:
        The modified list, or the original list unchanged if idx is
        negative or out of range.
    """
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
