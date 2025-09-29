"""Skeleton for Assignment 02 - Sentinels."""

_SENTINEL = object()

def choose_value(value=_SENTINEL, fallback=None):
    """Return provided value or fallback if omitted.

    TODO: ensure behavior distinguishes between explicit None and omitted value.
    """
    if value is _SENTINEL:
        return fallback
    return value
