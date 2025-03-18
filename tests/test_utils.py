from pytest import raises
from simple_math.common import validate_numeric_type


def test_validate_numeric_type():
    with raises(TypeError):
        validate_numeric_type("1")

    assert validate_numeric_type(1) == 1
    assert validate_numeric_type(5.2) == 5.2
