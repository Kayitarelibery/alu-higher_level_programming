#!/usr/bin/python3
"""Module that defines a function to write an Object to a text file
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to save.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
