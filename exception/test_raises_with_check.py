import pytest


def check_func(exc):
    return str(exc) == "Out of Milk"

def test_raises_with_check():
    with pytest.raises(ValueError, check=check_func):
        raise ValueError("Out of Milk")
