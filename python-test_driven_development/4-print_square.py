#!/usr/bin/python3
"""Module that prints a square with the character #."""


def print_square(size):
    """Print a square of '#' of the given size.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
