from defensive_programming.examples.sentinel_examples import (
    SENTINEL,
    find_in_list,
    get_required,
    NotFoundError,
)


def test_find_returns_sentinel_when_missing():
    seq = [1, 2, 3]
    res = find_in_list(seq, lambda x: x == 10)
    assert res is SENTINEL


def test_get_required_raises():
    with __import__("pytest").raises(NotFoundError):
        get_required([], 0)


def test_find_large_sequence_performance():
    seq = range(100000)
    res = find_in_list(seq, lambda x: x == 99999)
    assert res == 99999
