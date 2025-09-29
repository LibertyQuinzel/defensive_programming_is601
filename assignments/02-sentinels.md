# Assignment 2: Sentinel Values vs Exceptions

## Goal
Explore when to use sentinel values and when to raise exceptions. Implement a small API that uses a sentinel for "not found" and another API that raises an exception — justify your choice.

## Tasks
1. Read `examples/sentinel_examples.py`.
2. Implement `find_in_list(seq, predicate, default=SENTINEL)` which returns `default` if not found.
3. Implement `get_required(seq, index)` which raises `NotFoundError` if index missing.
4. Add tests that assert sentinel behavior vs exception behavior.

## Autograder hints
- The sentinel must be a unique sentinel object exported as `SENTINEL`.
- `get_required` must raise `NotFoundError` (a custom exception).
- Tests should cover empty sequences, out-of-range indices, and large sequences.
