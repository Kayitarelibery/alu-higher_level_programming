#!/usr/bin/python3
"""Module that defines a BaseGeometry class with a validator method."""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Compute the area of the geometry object."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): the name of the attribute being validated.
            value: the value to validate.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
