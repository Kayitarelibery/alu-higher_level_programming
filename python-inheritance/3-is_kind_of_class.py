#!/usr/bin/python3
"""Module that defines an is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherits from, a_class.

    Args:
        obj: the object to check.
        a_class: the class to check against.

    Returns:
        True if obj is an instance of a_class or a subclass, else False.
    """
    return isinstance(obj, a_class)
