#!/usr/bin/python3
"""Module that defines a function to return the dictionary
description of a simple data structure for JSON serialization
of an object.
"""


def class_to_json(obj):
    """Return the dictionary description of a simple object.

    Args:
        obj: An instance of a Class with only serializable
            attributes (list, dictionary, string, integer, boolean).

    Returns:
        dict: The dictionary description of obj.
    """
    return obj.__dict__
