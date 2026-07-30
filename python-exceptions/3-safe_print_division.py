#!/usr/bin/python3
"""Module that safely divides two integers."""


def safe_print_division(a, b):
    """Divide 2 integers and print the result.

    Args:
        a (int): the dividend.
        b (int): the divisor.

    Returns:
        The result of the division, or None if it could not be computed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
