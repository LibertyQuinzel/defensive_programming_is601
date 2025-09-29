"""Smoke tests for starter code to help beginners verify local changes quickly."""

from starter._import_paths import add_starter_path, import_starter


def test_starter_00_greet():
    module_globals = import_starter("00-intro")
    assert module_globals["greet"]("Student") == "Hello, Student"


def test_starter_01_divide():
    module_globals = import_starter("01-guard-clauses")
    assert module_globals["divide"](10, 2) == 5


def test_starter_02_choose_value():
    module_globals = import_starter("02-sentinels")
    assert module_globals["choose_value"]() is None
    assert module_globals["choose_value"](None, fallback=123) is None


def test_starter_03_reciprocal():
    module_globals = import_starter("03-design-by-contract")
    assert abs(module_globals["reciprocal"](2) - 0.5) < 1e-9


def test_starter_04_add():
    module_globals = import_starter("04-decorators")
    assert module_globals["add"](2, 3) == 5
