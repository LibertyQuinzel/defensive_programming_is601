# Examples — Defensive Programming (quick index)

This folder contains short, focused example modules that illustrate defensive
programming patterns used throughout the course. Open this file first and then
click the links below to inspect and run each example. Use the checkboxes to
mark your progress — they are interactive on GitHub and many editors.

---

## How to use this page

1. Click a file link below to open and read the example's docstring and code.
2. Run the quick example command (copy/paste shown under each file) to see the
   function in action.
3. Complete the short practice task and tick the checkbox when done.

Note: run commands from the repository root so `PYTHONPATH` covers the package.

---

## Examples index

- [ ] [__init__.py](./__init__.py) — package initializer for the examples module. Open
  the file to see how the examples package is organized.

- [ ] [contracts.py](./contracts.py) — Design-by-contract helpers and a sample
  `reciprocal(x)` function.
  - Quick read: inspect the `pre` and `post` decorator factories and the
    `ContractError` class.
  - Try it:

    ```bash
    PYTHONPATH=. python -c "from defensive_programming.examples import contracts; print('reciprocal(2)=', contracts.reciprocal(2))"
    ```
  - Practice: call `reciprocal(0)` and observe the raised `ContractError`.

- [ ] [decorators.py](./decorators.py) — Decorator helpers that preserve
  metadata (`functools.wraps`) and validate `args/kwargs`.
  - Quick read: see the `pre` and `post` factories and how they wrap target
    functions.
  - Try it:

    ```bash
    PYTHONPATH=. python - <<'PY'
    from defensive_programming.examples import decorators

    @decorators.pre(lambda x: isinstance(x, int) and x > 0, 'x must be positive int')
    def square(x):
        return x * x

    print('square(3)=', square(3))
    try:
        square(0)
    except Exception as e:
        print('expected error:', type(e).__name__, e)
    PY
    ```
  - Practice: write a small function wrapped with `@decorators.post(...)` to
    ensure output is a non-negative number.

- [ ] [operations.py](./operations.py) — Small arithmetic helpers demonstrating
  guard clauses, a small exception hierarchy, and input validation.
  - Quick read: look for `_is_number`, `InvalidOperandError`, and
    `DivisionByZeroError`.
  - Try it:

    ```bash
    PYTHONPATH=. python - <<'PY'
    from defensive_programming.examples import operations
    print('1+2=', operations.add(1, 2))
    print('10/2=', operations.divide(10, 2))
    try:
        operations.divide(1, 0)
    except Exception as e:
        print('expected error:', type(e).__name__, e)
    PY
    ```
  - Practice: pass a boolean (True/False) to `add` and confirm it is rejected.

- [ ] [sentinel_examples.py](./sentinel_examples.py) — Contrast sentinel return
  values vs explicit exceptions (`NotFoundError`).
  - Quick read: see `SENTINEL`, `find_in_list` (returns sentinel), and
    `get_required` (raises `NotFoundError`).
  - Try it:

    ```bash
    PYTHONPATH=. python - <<'PY'
    from defensive_programming.examples import sentinel_examples as s
    print('find 3 =>', s.find_in_list([1,2,3,4], lambda x: x==3))
    print('find 10 (returns sentinel) =>', s.find_in_list([1,2,3], lambda x: x==10) is s.SENTINEL)
    try:
        s.get_required([1,2], 5)
    except Exception as e:
        print('expected error:', type(e).__name__, e)
    PY
    ```
  - Practice: change `default` to `None` in a call to `find_in_list` and decide
    whether a sentinel or None better fits your use case.

---

## Learning checklist (suggested order)

- [ ] Read `contracts.py` and run the `reciprocal` examples.
- [ ] Read `decorators.py` and create a small pre/post decorated function.
- [ ] Read `operations.py` and write 2–3 unit tests for `add`/`divide`.
- [ ] Read `sentinel_examples.py` and decide when you'd prefer sentinel vs
      exception in your code.

When you finish an item above, tick the corresponding checkbox.


