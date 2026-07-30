#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Args:
        matrix: list of lists of integers
    """
    for row in matrix:
        elements = []
        for number in row:
            elements.append("{:d}".format(number))
        print(" ".join(elements))
