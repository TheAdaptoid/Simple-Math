"""
This module contains the implementation of the simplest arithmetic operations.

The functions in this module are used to add, subtract, multiply and divide two numbers.

The functions are:

- `add(a, b)`: Adds two numbers.
- `subtract(a, b)`: Subtracts two numbers.
- `multiply(a, b)`: Multiplies two numbers.
- `divide(a, b)`: Divides two numbers.
- `integer_divide(a, b)`: Divides two numbers using integer division.

The functions take two arguments, which must be of type `int` or `float`.
The return value is of the same type as the arguments.

The functions will raise a `TypeError` if the arguments are not of type `int` or `float`.

The functions will raise a `ValueError` if the arguments are zero
when using the `divide` or `integer_divide` functions.
"""

from simple_math.common import validate_numeric_type


def add(a: int | float, b: int | float) -> int | float:
    """
    Adds two numbers.

    Args:
        a (int | float): A value of type int or float.
        b (int | float): A value of type int or float.

    Returns:
        int | float: The sum of a and b.
    """
    validate_numeric_type(a)
    validate_numeric_type(b)

    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """
    Subtracts two numbers.

    Args:
        a (int | float): A value of type int or float.
        b (int | float): A value of type int or float.

    Returns:
        int | float: The difference of a and b.
    """
    validate_numeric_type(a)
    validate_numeric_type(b)

    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiplies two numbers.

    Args:
        a (int | float): A value of type int or float.
        b (int | float): A value of type int or float.

    Returns:
        int | float: The product of a and b.
    """
    validate_numeric_type(a)
    validate_numeric_type(b)

    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    """
    Divides two numbers.

    Args:
        a (int | float): The dividend. A value of type int or float.
        b (int | float): The divisor. A value of type int or float. Cannot be zero.

    Raises:
        ValueError: Rased if b is zero.

    Returns:
        int | float: The quotient of a and b.
    """
    validate_numeric_type(a)
    validate_numeric_type(b)

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def integer_divide(a: int | float, b: int | float) -> int:
    """
    Divides two numbers using integer division.

    Args:
        a (int | float): The dividend. A value of type int or float.
        b (int | float): The divisor. A value of type int or float. Cannot be zero.

    Raises:
        ValueError: Rased if b is zero.

    Returns:
        int | float: The quotient of a and b.
    """
    validate_numeric_type(a)
    validate_numeric_type(b)

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return int(a // b)
