#!/usr/bin/python3
"""Defines a function that reproduces the given bytecode behavior."""


def magic_calculation(a, b):
    """Perform a calculation equivalent to the provided bytecode.

    Args:
        a: an integer or float.
        b: an integer or float.

    Returns:
        The computed result.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result = result + a ** b / i
        except Exception:
            result = b + a
            break
    return result
