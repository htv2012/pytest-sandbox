"""
Some tests are expected to raise and while others don't
"""

import contextlib

import pytest


def expected_error(klass):
    if klass is None:
        return contextlib.nullcontext()
    return pytest.raises(klass)


@pytest.mark.parametrize(
    ["x", "y", "expected", "error"],
    [
        pytest.param(5, 2, 2.5, None, id="happy path"),
        pytest.param(5, 2, 2, None, id="expected fail", marks=pytest.mark.xfail),
        pytest.param(5, 0, None, ZeroDivisionError, id="div by zero"),
        pytest.param(5, "a", None, TypeError, id="int div by str"),
    ],
)
def test_division(x, y, expected, error):
    with expected_error(error):
        assert x / y == expected
