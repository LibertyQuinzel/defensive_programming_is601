"""Starter for Assignment 03: Design by Contract

This starter shows a precondition and postcondition example.
Edit the function to make tests pass and obey the contract.
"""

def reciprocal(x):
    # Precondition: x must be non-zero number
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    if x == 0:
        raise ValueError("x must not be zero")

    result = 1 / x

    # Postcondition: result times x should be approximately 1
    if not abs(result * x - 1) < 1e-9:
        raise AssertionError("postcondition failed")
    return result


if __name__ == "__main__":
    print(reciprocal(2))
