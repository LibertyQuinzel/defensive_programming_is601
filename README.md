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


