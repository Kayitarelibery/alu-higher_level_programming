#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list.

    Args:
        my_list: the list
        idx: the index to delete

    Returns:
        The modified list, or the same list unchanged if idx is
        negative or out of range.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    return my_list[:idx] + my_list[idx + 1:]
