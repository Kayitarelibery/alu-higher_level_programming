#!/usr/bin/python3
"""Module that defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class.

    Args:
        obj: the object to check.
        a_class: the class to check against.

    Returns:
        True if obj is an instance of a subclass of a_class (but not
        a_class itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
