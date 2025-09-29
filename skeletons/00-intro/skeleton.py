"""Skeleton for Assignment 00 - Intro.

Fill in the TODOs and run the starter to verify.
"""

def greet(name: str) -> str:
    # TODO: implement a friendly greeting
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if name == "":
        return "Hello, stranger"
    return f"Hello, {name}"
