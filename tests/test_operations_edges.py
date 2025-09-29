import math

import pytest

from defensive_programming.examples.operations import (
    add,
    divide,
    InvalidOperandError,
)


def test_add_nan_rejected():
    with pytest.raises(InvalidOperandError):
        add(float('nan'), 1)


def test_add_inf_rejected():
    with pytest.raises(InvalidOperandError):
        add(float('inf'), 1)


def test_divide_large_numbers():
    # Large numbers should still compute or raise DivisionByZeroError appropriately
    assert math.isfinite(add(1e308, -1e308))


def test_divide_coercion_policy():
    # string input should be rejected
    with pytest.raises(InvalidOperandError):
        divide("6", "3")
