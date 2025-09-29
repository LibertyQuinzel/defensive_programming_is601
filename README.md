# Defensive Programming Course (Beginner Friendly)

This mini-course teaches defensive programming for learners who are new to professional Python development. It uses small, guided steps and starter code so students can try things locally and learn by doing.

What you'll find here
- `assignments/` — step-by-step exercises with beginner walkthroughs
- `starter/` — skeleton code you can copy or work from (one folder per assignment)
- `examples/` — instructor examples showing defensive patterns
- `tests/` — pytest tests used for validation and autograding
- `autograder.py` — minimal autograder that runs tests and writes a JSON result
- `requirements.txt` — development dependencies (pytest, flake8)

Quick start (explicit, copy/paste)

1) Create and activate a virtual environment (recommended)

```bash
# from repo root
python3 -m venv .venv
source .venv/bin/activate
```

2) Install the course dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r defensive_programming/requirements.txt
```

3) Run the tests to confirm everything is working

```bash
# Run only the defensive programming tests
PYTHONPATH=. pytest -q defensive_programming/tests

# Or run the autograder to produce a JSON report
PYTHONPATH=. python defensive_programming/autograder.py
cat defensive_programming/autograder_result.json
```

If you are new to Python or the command line, follow the `starter/` folders for each assignment — they contain minimal skeletons and explicit instructions.


Student checklist (copy this to work from):

1. Set up your environment
	- `python3 -m venv .venv`
	- `source .venv/bin/activate`
	- `python -m pip install -r defensive_programming/requirements.txt`

2. Read the assignment spec
	- Open `defensive_programming/assignments/0X-<topic>.md` for the assignment you're working on.

3. Learn with the starter material
	- Read and run `defensive_programming/starter/0X-<topic>/starter.py` or open the notebook in the same folder.

4. Quick starter smoke test
	- `pytest -q defensive_programming/starter/tests/test_starters.py`

5. Implement the skeleton
	- Edit `defensive_programming/skeletons/0X-<topic>/skeleton.py` to satisfy the spec and tests.

6. Quick skeleton sanity test (fast)
	- `pytest -q defensive_programming/skeletons/tests/test_quick_skeletons.py`

7. Run assignment tests (detailed)
	- Example: `pytest -q defensive_programming/tests/test_operations_defensive.py`

8. (Optional) Run autograder locally
	- `python defensive_programming/autograder.py`
	- `cat defensive_programming/autograder_result.json`

9. Style check before pushing
	- `flake8 defensive_programming --max-line-length=100`

10. Push and open a PR — CI runs flake8, pytest, and the autograder on push/PR.


Per-topic step-by-step workflow (follow in order for each assignment)

Assignment 00 — Intro
- Read: `defensive_programming/assignments/00-intro.md`
- Starter script: `defensive_programming/starter/00-intro/starter.py`
- Starter notebook: `defensive_programming/starter/00-intro/intro.ipynb`
- Skeleton (student file, if present): `defensive_programming/skeletons/00-intro/skeleton.py`
- Starter smoke test: `defensive_programming/starter/tests/test_starters.py::test_starter_00_greet`

Commands (example):
```bash
# Run the starter smoke test for the intro
PYTHONPATH=. pytest -q defensive_programming/starter/tests/test_starters.py::test_starter_00_greet
```

Assignment 01 — Guard Clauses / Hardening
- Read: `defensive_programming/assignments/01-hardening.md`
- Starter script: `defensive_programming/starter/01-guard-clauses/starter.py`
- Starter notebook: `defensive_programming/starter/01-guard-clauses/guard_clauses.ipynb`
- Skeleton (student file): `defensive_programming/skeletons/01-guard-clauses/skeleton.py`
- Quick skeleton sanity tests: `defensive_programming/skeletons/tests/test_quick_skeletons.py::test_skeleton_divide_importable`
- Assignment tests: `defensive_programming/tests/test_operations_defensive.py`

Commands (example):
```bash
# Run the starter smoke test for divide
PYTHONPATH=. pytest -q defensive_programming/starter/tests/test_starters.py::test_starter_01_divide

# Quick skeleton sanity check
PYTHONPATH=. pytest -q defensive_programming/skeletons/tests/test_quick_skeletons.py::test_skeleton_divide_importable

# Run the assignment tests
PYTHONPATH=. pytest -q defensive_programming/tests/test_operations_defensive.py
```

Assignment 02 — Sentinels
- Read: `defensive_programming/assignments/02-sentinels.md`
- Starter script: `defensive_programming/starter/02-sentinels/starter.py`
- Starter notebook: `defensive_programming/starter/02-sentinels/sentinels.ipynb`
- Skeleton (student file): `defensive_programming/skeletons/02-sentinels/skeleton.py`
- Quick skeleton sanity tests: `defensive_programming/skeletons/tests/test_quick_skeletons.py::test_skeleton_choose_value_exists`
- Assignment tests: `defensive_programming/tests/test_sentinel.py`

Commands (example):
```bash
# Starter smoke test
PYTHONPATH=. pytest -q defensive_programming/starter/tests/test_starters.py::test_starter_02_choose_value

# Quick skeleton sanity check
PYTHONPATH=. pytest -q defensive_programming/skeletons/tests/test_quick_skeletons.py::test_skeleton_choose_value_exists

# Run the sentinel tests
PYTHONPATH=. pytest -q defensive_programming/tests/test_sentinel.py
```

Assignment 03 — Design by Contract
- Read: `defensive_programming/assignments/03-design-by-contract.md`
- Starter script: `defensive_programming/starter/03-design-by-contract/starter.py`
- Starter notebook: `defensive_programming/starter/03-design-by-contract/design_by_contract.ipynb`
- Skeleton (student file): `defensive_programming/skeletons/03-design-by-contract/skeleton.py`
- Quick skeleton sanity tests: `defensive_programming/skeletons/tests/test_quick_skeletons.py::test_skeleton_reciprocal_exists`
- Assignment tests: `defensive_programming/tests/test_contracts.py`

Commands (example):
```bash
# Starter smoke test for reciprocal
PYTHONPATH=. pytest -q defensive_programming/starter/tests/test_starters.py::test_starter_03_reciprocal

# Quick skeleton sanity check
PYTHONPATH=. pytest -q defensive_programming/skeletons/tests/test_quick_skeletons.py::test_skeleton_reciprocal_exists

# Run the contract tests
PYTHONPATH=. pytest -q defensive_programming/tests/test_contracts.py
```

Assignment 04 — Decorators
- Read: `defensive_programming/assignments/04-decorators.md`
- Starter script: `defensive_programming/starter/04-decorators/starter.py`
- Starter notebook: `defensive_programming/starter/04-decorators/decorators_intro.ipynb`
- Skeleton (student file): `defensive_programming/skeletons/04-decorators/skeleton.py`
- Assignment tests: `defensive_programming/tests/test_decorators.py`

Commands (example):
```bash
# Starter smoke test for decorators
PYTHONPATH=. pytest -q defensive_programming/starter/tests/test_starters.py::test_starter_04_add

# Run decorator tests
PYTHONPATH=. pytest -q defensive_programming/tests/test_decorators.py
```

Final checks before submitting
- Run the autograder to produce the JSON result used by CI: `python defensive_programming/autograder.py` (then inspect `defensive_programming/autograder_result.json`)
- Run style checks: `flake8 defensive_programming --max-line-length=100`



