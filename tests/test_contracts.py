import math

import pytest

from defensive_programming.examples.contracts import reciprocal, ContractError


def test_reciprocal_happy_path():
    assert math.isclose(reciprocal(2), 0.5)


def test_reciprocal_precondition():
    with pytest.raises(ContractError):
        reciprocal(True)  # boolean is rejected


def test_reciprocal_postcondition_nan():
    with pytest.raises(ContractError):
        reciprocal(0.0)  # division by zero -> inf -> postcondition fails
