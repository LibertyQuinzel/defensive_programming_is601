# Intro: Defensive Programming (Quick)

This mini-course teaches practical defensive programming patterns for day-to-day engineering: choosing EAFP vs LBYL, guard clauses, pre/post-conditions, custom exceptions, and safe logging.

Learning objectives:
- Explain EAFP and LBYL and when to use each
- Add guard clauses and precondition checks to small functions
- Replace ambiguous return codes with explicit exceptions
- Write tests that cover error paths and assertions

Estimated time: 30–60 minutes

Tasks:
- Read the example in `../examples/operations.py`
- Write two tests that exercise invalid inputs and division-by-zero
- Propose a small API contract and implement a guard clause to enforce it
