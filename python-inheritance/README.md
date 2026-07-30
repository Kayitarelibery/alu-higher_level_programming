# python-inheritance

## Description

This project is part of the Higher Level Programming curriculum. It covers
Python inheritance: how classes can share and extend behavior, how to
inspect objects and classes at runtime, and how to build a small geometry
class hierarchy (`BaseGeometry` -> `Rectangle` -> `Square`) using inheritance,
private attributes, and custom validation.

## Learning Objectives

- What is a base class, subclass, superclass
- Why Python programming is awesome
- What is inheritance and its benefits
- How to list all attributes and methods of a class or instance
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by inheritance
- What is `object` and `isinstance`
- What is the difference between `isinstance` and `type`
- How to define a class that inherits from another class

## Files

| File | Description |
| --- | --- |
| `0-lookup.py` | Returns the list of available attributes/methods of an object |
| `1-my_list.py` | `MyList` class that inherits from `list` with a `print_sorted` method |
| `2-is_same_class.py` | Checks if an object is exactly an instance of a class |
| `3-is_kind_of_class.py` | Checks if an object is an instance of, or inherits from, a class |
| `4-inherits_from.py` | Checks if an object is an instance of a class that inherits from another |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with an `area` method that raises an exception |
| `7-base_geometry.py` | `BaseGeometry` with an `integer_validator` method |
| `8-rectangle.py` | `Rectangle` class with private `width`/`height` attributes |
| `9-rectangle.py` | `Rectangle` class with `area` and `__str__` |
| `10-square.py` | `Square` class that inherits from `Rectangle` |
| `11-square.py` | `Square` class with a custom `__str__` |

## Usage

Each file can be imported and used directly, e.g.:

```python
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)
print(r)        # [Rectangle] 3/5
print(r.area()) # 15
```

## Author

Kayitare Libery

_Last verified: 2026-07-16_
