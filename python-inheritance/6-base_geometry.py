#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Compute the area of the geometry object."""
        raise Exception("area() is not implemented")
