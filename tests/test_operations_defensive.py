import pytest

from defensive_programming.examples.operations import (
    add,
    divide,
    multiply,
    InvalidOperandError,
    DivisionByZeroError,
)


def test_add_invalid_operand():
    with pytest.raises(InvalidOperandError):
        add(None, 1)
    with pytest.raises(InvalidOperandError):
        add(1, "two")


def test_multiply_invalid_operand():
    with pytest.raises(InvalidOperandError):
        multiply(True, 2)  # booleans are rejected here


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        divide(5, 0)


def test_divide_and_add_happy_path():
    assert add(2, 3) == 5.0
    assert divide(6, 3) == 2.0
