#!/usr/bin/python3
"""Module that defines an is_same_class function."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: the object to check.
        a_class: the class to check against.

    Returns:
        True if obj's type is exactly a_class, otherwise False.
    """
    return type(obj) == a_class
