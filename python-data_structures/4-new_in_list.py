#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position, without
    modifying the original list.

    Args:
        my_list: the list
        idx: the index to replace
        element: the new element

    Returns:
        A new list with the element replaced, or a copy of the
        original list if idx is negative or out of range.
    """
    new_list = my_list[:]
    if idx < 0:
        return new_list
    if idx > len(new_list) - 1:
        return new_list
    new_list[idx] = element
    return new_list
