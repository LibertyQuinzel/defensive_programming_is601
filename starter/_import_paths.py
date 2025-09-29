"""Helper functions for tests to import starter modules by path.

These helpers are intentionally tiny and only used by the smoke tests in
`defensive_programming/starter/tests/`.
"""
from pathlib import Path
import sys


def add_starter_path(folder_name: str) -> None:
    """Add the starter folder to sys.path so runpy or imports find it.

    Example: add_starter_path("00-intro")
    """
    repo_root = Path(__file__).resolve().parents[2]
    starter_root = repo_root / "defensive_programming" / "starter" / folder_name
    if str(starter_root) not in sys.path:
        sys.path.insert(0, str(starter_root))


def import_starter(folder_name: str):
    """Return a module object by running its starter.py file via runpy."""
    import runpy

    repo_root = Path(__file__).resolve().parents[2]
    starter_file = repo_root / "defensive_programming_is601" / "starter" / folder_name / "starter.py"
    return runpy.run_path(str(starter_file))
