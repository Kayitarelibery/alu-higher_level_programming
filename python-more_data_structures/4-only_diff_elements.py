#!/usr/bin/python3
"""Module that returns elements present in only one of two sets."""


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set.

    Args:
        set_1 (set): the first set.
        set_2 (set): the second set.

    Returns:
        set: the symmetric difference of the two sets.
    """
    return set_1 ^ set_2
