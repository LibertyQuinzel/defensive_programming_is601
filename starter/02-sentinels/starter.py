"""Starter for Assignment 02: Sentinels

This starter demonstrates a simple sentinel default value and safe handling.
"""

_SENTINEL = object()

def choose_value(value=_SENTINEL, fallback=None):
    """Return value if provided; otherwise use fallback.

    This demonstrates detecting when callers intentionally passed None vs omitted.
    """
    if value is _SENTINEL:
        return fallback
    return value


if __name__ == "__main__":
    print(choose_value())
    print(choose_value(None, fallback=123))
