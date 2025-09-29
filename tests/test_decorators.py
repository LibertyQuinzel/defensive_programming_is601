import math

import pytest

from examples.decorators import pre, post, ContractError


@pre(
    lambda a, b: isinstance(a, (int, float)) and isinstance(b, (int, float)),
    "args must be numeric",
)
@post(
    lambda r: isinstance(r, float) and math.isfinite(r),
    "result must be finite float",
)
def safe_divide(a, b):
    return float(a) / float(b)


def test_safe_divide_happy():
    assert safe_divide(6, 3) == 2.0


def test_safe_divide_pre():
    with pytest.raises(ContractError):
        safe_divide("x", 1)


def test_safe_divide_post_inf():
    with pytest.raises(ContractError):
        safe_divide(1e308, 1e-308)  # very large result -> may be inf on some platforms
