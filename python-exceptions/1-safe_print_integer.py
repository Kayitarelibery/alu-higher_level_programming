#!/usr/bin/python3
"""Module that safely prints an integer."""


def safe_print_integer(value):
    """Print an integer using "{:d}".format().

    Args:
        value: the value to print, can be any type.

    Returns:
        bool: True if value has been correctly printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
