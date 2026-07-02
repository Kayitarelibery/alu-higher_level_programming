#!/usr/bin/python3
def multiple_returns(sentence):
    """Return the length of a string and its first character.

    Args:
        sentence: the string

    Returns:
        A tuple (length, first_character). first_character is None
        if the sentence is empty.
    """
    first_character = sentence[0] if len(sentence) > 0 else None
    return (len(sentence), first_character)
