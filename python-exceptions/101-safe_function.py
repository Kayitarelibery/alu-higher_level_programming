#!/usr/bin/python3
"""Defines a function that executes another function safely."""
import sys


def safe_function(fct, *args):
    """Execute fct with the given args, catching any exception.

    Args:
        fct: a pointer to the function to execute.
        *args: the arguments to pass to fct.

    Returns:
        The result of fct(*args), or None if an exception occurred.
        On exception, prints the error to stderr, preceded by "Exception:".
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
