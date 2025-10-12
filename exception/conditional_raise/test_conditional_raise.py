"""
Some tests are expected to raise and while others don't
"""

from contextlib import nullcontext

import pytest


@pytest.mark.parametrize(
    "x, y, expected, context",
    [
        pytest.param(5, 2, 2, nullcontext(), id="happy path"),
        pytest.param(
            5, 2, 3, nullcontext(), marks=pytest.mark.xfail, id="expected fail"
        ),
        pytest.param(
            5, 0, nullcontext(), pytest.raises(ZeroDivisionError), id="div by zero"
        ),
        pytest.param(5, "a", None, pytest.raises(TypeError), id="int div by str"),
    ],
)
def test_division(x, y, expected, context):
    with context:
        assert x // y == expected
