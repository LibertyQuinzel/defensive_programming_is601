"""Skeleton for Assignment 04 - Decorators."""

import functools
import os


def announce(fn):
    """A minimal decorator that prints when function runs.

    If the environment variable `QUIET` is set (non-empty), the decorator will not print.
    """

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if not os.environ.get("QUIET"):
            print(f"Calling {fn.__name__}...")
        return fn(*args, **kwargs)

    return wrapper
