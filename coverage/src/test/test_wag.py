import pytest
from my_package.wag import wag


@pytest.mark.parametrize(
    ["mood", "expected"],
    [
        ("happy", 10),
        ("sad", 1),
    ],
)
def test_wag(mood, expected):
    assert wag(mood) == expected
