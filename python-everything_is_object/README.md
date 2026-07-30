# python-everything_is_object

## Description

This project is part of the Higher Level Programming curriculum. It covers
a foundational Python concept: everything is an object. It explores
`id()`, `type()`, mutable vs immutable objects, references vs copies,
and how arguments are passed to functions.

## Learning Objectives

- Why Python programming is awesome
- Everything is an object in Python
- What's an id
- What's a reference
- What's an assignment
- What's an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- What's mutable and immutable objects
- What's the difference between a list and a tuple
- How does Python pass variables to functions

## Requirements

- Editors allowed: vi, vim, emacs
- All files are interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.5)
  where applicable
- All `.txt` answer files contain a single line with no trailing new line,
  unless otherwise specified
- Where a `.py` file is required, the first line is exactly
  `#!/usr/bin/python3`
- Code follows the `pycodestyle` style (version 2.7.*)
- No modules may be imported unless a task explicitly allows it

## Tasks

| File | Description |
| --- | --- |
| `0-answer.txt` | Function used to print an object's type |
| `1-answer.txt` | Function used to get an object's identifier |
| `2-answer.txt` | Whether `a = 89` and `b = 100` share an object |
| `3-answer.txt` | Whether `a = 89` and `b = 89` share an object |
| `4-answer.txt` | Whether `a = 89` and `b = a` share an object |
| `5-answer.txt` | Whether `a = 89` and `b = a + 1` share an object |
| `6-answer.txt` | Output of `s1 == s2` when `s2 = s1` (strings) |
| `7-answer.txt` | Output of `s1 is s2` when `s2 = s1` (strings) |
| `8-answer.txt` | Output of `s1 == s2` for two equal string literals |
| `9-answer.txt` | Output of `s1 is s2` for two equal string literals |
| `10-answer.txt` | Output of `l1 == l2` for two equal list literals |
| `11-answer.txt` | Output of `l1 is l2` for two equal list literals |
| `12-answer.txt` | Output of `l1 == l2` when `l2 = l1` (lists) |
| `13-answer.txt` | Output of `l1 is l2` when `l2 = l1` (lists) |
| `14-answer.txt` | Output after appending to a list via an alias |
| `15-answer.txt` | Output after reassigning a list via `+` |
| `16-answer.txt` | Output after incrementing an int inside a function |
| `17-answer.txt` | Output after appending to a list inside a function |
| `18-answer.txt` | Output after reassigning a list inside a function |
| `19-copy_list.py` | Returns a copy of a list |
| `20-answer.txt` | Whether `()` is a tuple |
| `21-answer.txt` | Whether `(1, 2)` is a tuple |
| `22-answer.txt` | Whether `(1)` is a tuple |
| `23-answer.txt` | Whether `(1, )` is a tuple |
| `24-answer.txt` | Output of `a is b` for `a = (1)`, `b = (1)` |
| `25-answer.txt` | Output of `a is b` for `a = (1, 2)`, `b = (1, 2)` |
| `26-answer.txt` | Output of `a is b` for `a = ()`, `b = ()` |
| `27-answer.txt` | Whether `id(a)` stays the same after `a = a + [5]` |
| `28-answer.txt` | Whether `id(a)` stays the same after `a += [4]` |
| `29-*.txt` | Blog post URLs on mutable/immutable objects in Python |

## Author

Created as part of the ALU Higher Level Programming curriculum.
