# python-test_driven_development

## Description

This project is part of the ALU Higher-Level Programming curriculum. It focuses on Test-Driven Development (TDD) in Python: writing functions alongside doctests and unittests, validating edge cases, and enforcing strict input checking before implementation.

## Learning Objectives

- What is Test-Driven Development
- How to use the `doctest` module to validate interactive documentation tests
- How to use the `unittest` module to write test cases
- How to write docstrings for every module and function
- How to handle type checking and raise appropriate exceptions

## Requirements

- Ubuntu 20.04 LTS
- Python 3 (`python3` interpreter)
- Scripts must pass `pycodestyle` (version 2.x)
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- All files must be executable
- Every module, class, and function must have a docstring
- All test files must be inside a `tests` folder
- README.md at the root of the project folder is mandatory

## Files

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds two integers or floats (casting floats to int), raises `TypeError` on invalid input |
| `tests/0-add_integer.txt` | Doctest file validating `add_integer` |
| `2-matrix_divided.py` | Divides all elements of a matrix by a given number, rounded to 2 decimal places |
| `tests/2-matrix_divided.txt` | Doctest file validating `matrix_divided` |
| `3-say_my_name.py` | Prints `My name is <first_name> <last_name>` |
| `tests/3-say_my_name.txt` | Doctest file validating `say_my_name` |
| `4-print_square.py` | Prints a square of `#` characters of a given size |
| `tests/4-print_square.txt` | Doctest file validating `print_square` |
| `5-text_indentation.py` | Prints text with 2 new lines after each `.`, `?`, and `:` |
| `tests/5-text_indentation.txt` | Doctest file validating `text_indentation` |
| `6-max_integer.py` | Returns the max integer in a list (or `None` if the list is empty) |
| `tests/6-max_integer_test.py` | Unittest file validating `max_integer` |

## Usage

Doctests are run like this:

```bash
python3 -m doctest -v tests/0-add_integer.txt
python3 -m doctest -v tests/2-matrix_divided.txt
python3 -m doctest -v tests/3-say_my_name.txt
python3 -m doctest -v tests/4-print_square.txt
python3 -m doctest -v tests/5-text_indentation.txt
```

Unittests are run like this:

```bash
python3 -m unittest tests.6-max_integer_test
```

Each module can also be run directly through its own `X-main.py` test script, for example:

```bash
./0-main.py
./2-main.py
./3-main.py
```

## Author

Libery
