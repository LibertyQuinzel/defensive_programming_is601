"""Starter for Assignment 04: Decorators

Tiny example: a decorator that prints when a function runs.
"""

def announce(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}...")
        return fn(*args, **kwargs)

    return wrapper


@announce
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(2, 3))
