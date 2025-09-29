"""Starter for Assignment 00: Hello and basic guard clauses.

This file is deliberately tiny. Run it with:

    python starter.py

Then edit the value of `x` and re-run.
"""

def greet(name):
    if not isinstance(name, str):
        # Defensive check: prefer a clear error early
        raise TypeError("name must be a string")
    if name == "":
        return "Hello, stranger"
    return f"Hello, {name}"


if __name__ == "__main__":
    x = "Student"
    print(greet(x))
