"""Skeleton for Assignment 03 - Design by Contract."""

def reciprocal(x):
    """Return reciprocal with pre/post conditions.

    TODO:
    - check x is a number
    - check x is not zero
    - ensure postcondition holds
    """
    # Precondition: type and non-zero
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    if x == 0:
        raise ValueError("x must not be zero")

    result = 1 / x

    # Postcondition: result * x is approximately 1
    if abs(result * x - 1) > 1e-9:
        raise AssertionError("postcondition failed: reciprocal inaccurate")

    return result
