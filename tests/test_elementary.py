from pytest import raises
from simple_math.arithmetic import add, subtract, multiply, divide, integer_divide


class Test_Add:

    def test_ints(self):
        assert add(1, 2) == 3

    def test_floats(self):
        assert add(4.5, 3.0) == (4.5 + 3.0)

    def test_strings(self):
        with raises(TypeError):
            add("1", "2")


class Test_Subtract:

    def test_ints(self):
        assert subtract(1, 2) == -1

    def test_floats(self):
        assert subtract(4.5, 3.0) == (4.5 - 3.0)

    def test_strings(self):
        with raises(TypeError):
            subtract("1", "2")


class Test_Multiply:

    def test_ints(self):
        assert multiply(1, 2) == 2

    def test_floats(self):
        assert multiply(4.5, 3.0) == (4.5 * 3.0)

    def test_strings(self):
        with raises(TypeError):
            multiply("1", "2")


class Test_Divide:

    def test_ints(self):
        assert divide(1, 2) == 0.5

    def test_floats(self):
        assert divide(4.5, 3.0) == (4.5 / 3.0)

    def test_strings(self):
        with raises(TypeError):
            divide("1", "2")

    def test_divide_by_zero(self):
        with raises(ValueError):
            divide(1, 0)


class Test_Integer_Divide:

    def test_ints(self):
        assert integer_divide(1, 2) == 0

    def test_floats(self):
        assert integer_divide(4.5, 3.0) == (4.5 // 3.0)

    def test_strings(self):
        with raises(TypeError):
            integer_divide("1", "2")

    def test_divide_by_zero(self):
        with raises(ValueError):
            integer_divide(1, 0)
