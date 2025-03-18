from typing import Any


def validate_numeric_type(value: Any) -> int | float:
    """
    Validates that a given value is of type int or float
    and returns the value if it is of type int or float.

    Args:
        value (Any): The value to validate

    Raises:
        TypeError: Raised if the value is not of type int or float

    Returns:
        int | float: The validated value
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{value} must be of type int or float")

    return value
