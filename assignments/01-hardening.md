# Assignment 1: Harden the Operations Module

## Goal
Harden the `examples.operations` module by adding clear contracts, guard clauses, and custom exceptions. Add tests for error paths.

## Tasks
1. Read `defensive_programming/examples/operations.py`.
2. Add at least 2 tests that cover:
   - Passing a non-number (e.g., `None` or a string) to `add`/`multiply` should raise `InvalidOperandError`.
   - Dividing by zero should raise `DivisionByZeroError` with a helpful message.
3. Ensure there are no `except:` (bare except) patterns in the module.
4. Run `pytest defensive_programming/tests` and ensure tests pass.

## Acceptance
- 2+ tests covering error paths
- Custom exceptions used and documented
- Clear guard clauses present in the implementation
