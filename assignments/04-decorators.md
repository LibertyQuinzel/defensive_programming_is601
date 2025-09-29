# Assignment 4: Pre/Post Condition Decorators

## Goal
Learn to write decorators that implement pre- and post-conditions and apply them to small APIs.

## Tasks
1. Study `examples/decorators.py` which provides `pre` and `post` helpers.
2. Write a function `safe_divide` that uses `@pre` to check inputs and `@post` to ensure result finite.
3. Add tests verifying behavior for zero, NaN, and extremely large inputs.

## Autograder hints
- Decorators must be tolerant of functions with positional and keyword args.
- Postcondition failures must raise `ContractError` and include the resulting value in the message.
