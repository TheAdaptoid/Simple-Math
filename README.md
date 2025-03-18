# Simple Math

Simple Math is a collection of functions for performing basic mathematical operations.

## Arithmetic

### Elementary

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