#!/usr/bin/python3
"""Module that returns the key with the biggest integer value."""


def best_score(a_dictionary):
    """Return a key with the biggest integer value.

    Args:
        a_dictionary (dict): the dictionary to check.

    Returns:
        The key with the highest value, or None if not found.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
