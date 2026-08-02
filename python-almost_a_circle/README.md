# python-almost_a_circle

## Description

This project is part of the ALU Higher-Level Programming curriculum. It focuses on Object-Oriented Programming in Python: building a class hierarchy (Base, Rectangle, Square), private attributes with getters/setters, input validation, magic methods, serialization (JSON, CSV), and full unit testing with PEP 8 compliance.

## Learning Objectives

- How to write unittests and PEP 8-compliant code
- How to use private/protected attributes with getters and setters
- How to use *args and **kwargs
- How Python's inheritance works, and how it applies to __init__ and super()
- How to serialize and deserialize a class using JSON
- How to manage id attributes across a class hierarchy

## Requirements

- Ubuntu 20.04 LTS
- Python 3 (python3 interpreter)
- Scripts must pass pycodestyle (version 2.x)
- All files must end with a new line
- The first line of all files must be exactly #!/usr/bin/python3
- All files must be executable
- Every module, class, and function must have a docstring
- All classes and methods must be unit tested (folder tests/)
- models/__init__.py and tests/__init__.py must exist and be empty
- README.md at the root of the project folder is mandatory

## File Structure

python-almost_a_circle/
- README.md
- models/
  - __init__.py
  - base.py
  - rectangle.py
  - square.py
- tests/
  - __init__.py
  - test_base.py
  - test_rectangle.py
  - test_square.py

## Files

| File | Description |
| --- | --- |
| models/base.py | Base class, manages id, plus to_json_string, save_to_file, from_json_string, create, load_from_file |
| models/rectangle.py | Rectangle class (inherits Base), private attributes with getters/setters, area, display, __str__, update, to_dictionary |
| models/square.py | Square class (inherits Rectangle), size property, __str__, update, to_dictionary |
| tests/test_base.py | Unittests for Base |
| tests/test_rectangle.py | Unittests for Rectangle |
| tests/test_square.py | Unittests for Square |

## Usage

Run all unittests:

python3 -m unittest discover tests

Run a single test file:

python3 -m unittest tests.test_rectangle

## Author

Libery
