#!/usr/bin/python3
"""Defines a function that safely prints an integer, with error message."""
import sys


def safe_print_integer_err(value):
    """Print an integer, with error message printed to stderr on failure.

    Args:
        value: the value to attempt to print as an integer.

    Returns:
        True if value has been correctly printed (i.e. it's an integer),
        otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
