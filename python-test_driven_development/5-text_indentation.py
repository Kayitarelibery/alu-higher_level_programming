#!/usr/bin/python3
"""Module that prints a text with indentation after . ? and :"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    symbols = ".?:"
    printable = ""
    for char in text:
        if char in symbols:
            printable += char + "\n\n"
        else:
            printable += char
    lines = printable.split("\n")
    for line in lines:
        print(line.strip())
