"""
Some tests are expected to raise and while others don't
"""

import contextlib

import pytest

NO_ERROR = contextlib.nullcontext()


@pytest.mark.parametrize(
    ["x", "y", "expected", "expected_error"],
    [
        pytest.param(5, 2, 2.5, NO_ERROR, id="happy path"),
        pytest.param(5, 0, None, pytest.raises(ZeroDivisionError), id="div by zero"),
    ],
)
def test_division(x, y, expected, expected_error):
    with expected_error:
        assert x / y == expected
