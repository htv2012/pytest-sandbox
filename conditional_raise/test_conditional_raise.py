"""
Some tests are expected to raise and while others don't
"""

import contextlib

import pytest


@pytest.mark.parametrize(
    ["x", "y", "cond"],
    [
        pytest.param(5, 2, contextlib.nullcontext(), id="happy path"),
        pytest.param(5, 0, pytest.raises(ZeroDivisionError), id="div by zero"),
    ],
)
def test_division(x, y, cond):
    with cond:
        x / y
