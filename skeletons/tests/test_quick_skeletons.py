"""Very small, fast sanity checks for the skeletons.

These tests are intentionally tiny so students can run them quickly while
working on an assignment. They check that the expected functions exist and
have the basic behavior/signatures (happy-path only) without enforcing full
autograder-style edge cases.
"""

from importlib import import_module


def test_skeleton_divide_importable():
	mod = import_module("defensive_programming.skeletons.01-guard-clauses.skeleton")
	assert hasattr(mod, "divide")
	assert callable(mod.divide)
	# sanity check: a simple division
	assert mod.divide(6, 3) == 2


def test_skeleton_choose_value_exists():
	mod = import_module("defensive_programming.skeletons.02-sentinels.skeleton")
	assert hasattr(mod, "choose_value")
	# distinguish explicit None vs omitted value
	assert mod.choose_value() is None


def test_skeleton_reciprocal_exists():
	mod = import_module("defensive_programming.skeletons.03-design-by-contract.skeleton")
	assert hasattr(mod, "reciprocal")
	assert abs(mod.reciprocal(2) - 0.5) < 1e-9
