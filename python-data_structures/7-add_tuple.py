#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples of integers, element-wise, for the first 2 elements.

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        A tuple with the addition of the first two elements of each
        argument, using 0 for any missing element.
    """
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1 + b1, a2 + b2)
