# Assignment 3: Design by Contract

## Goal
Implement and use pre- and post-condition checks for small functions.

## Tasks
1. Read `examples/contracts.py`.
2. Write at least two functions with explicit `@pre` / `@post` checks (decorators provided in `examples/decorators.py`).
3. Add tests that trigger precondition failures and postcondition failures.

## Autograder hints
- Use the provided decorator `@pre` and `@post`.
- Pre/post checks should raise `ContractError` with informative messages.
- Tests should use `pytest.raises(ContractError)` to assert failures.

### Beginner walkthrough (step-by-step)

This walkthrough shows concrete, copy/paste commands for learners who are new to Python and the command line.

1) Set up a virtual environment (recommended) and install the course requirements:

```bash
# from repository root
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r defensive_programming/requirements.txt
```

2) Open the starter code for this assignment:

```
defensive_programming/starter/03-design-by-contract/starter.py
```

Run it to see expected behavior:

```bash
python defensive_programming/starter/03-design-by-contract/starter.py
```

3) Read `examples/contracts.py` to see how `@pre` and `@post` are used. Try making a small change in the starter and re-run to observe what breaks.

4) Run the tests that target this assignment to see failures you should fix. Replace `test_file.py` with the test name used in this repo (look under `defensive_programming/tests`):

```bash
PYTHONPATH=. pytest -q defensive_programming/tests/test_contracts.py
```

5) Edit your functions to satisfy the contracts. After each small change, re-run the test above. Tests will show clear assertion or `ContractError` messages which guide your next edits.

Troubleshooting tips
- If you see `ImportError: cannot import name` make sure you run tests from the repository root and use `PYTHONPATH=.` when running `pytest` or `python`.
- If you get `TypeError` or `ValueError`, read the message: it's usually the defensive check telling you what's wrong.
- Use small changes and re-run tests often — that makes debugging easier.

Where to get help
- Instructor notes: `defensive_programming/instructor_notes.md`
- Example implementations: `defensive_programming/examples/`
- Starter code for this assignment: `defensive_programming/starter/03-design-by-contract/starter.py`
