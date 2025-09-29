"""Skeleton for Assignment 01 - Guard Clauses."""

def divide(a, b):
    """Divide two numbers with defensive checks.

    TODOs:
    - raise TypeError if a or b aren't int/float
    - raise ValueError if b is zero
    """
    # Defensive type checks
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an int or float")

    # Defensive value checks
    if b == 0:
        raise ValueError("division by zero is not allowed")

    return a / b
