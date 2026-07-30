#!/usr/bin/python3
"""Module that defines a Student class with serialization and
deserialization support.
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of attribute names to
                include. If not a list, all attributes are
                returned.

        Returns:
            dict: The dictionary representation of the instance,
                filtered by attrs if provided.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary of attribute names and values
                to set on the instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
