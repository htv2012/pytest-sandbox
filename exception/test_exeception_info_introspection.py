"""
Show relevant members inside an ExceptionInfo and what we can do with them.
"""

import pytest


def test_exception_info_introspection():
    with pytest.raises(ValueError) as exc_info:
        int("foo")

    # These are the same.
    # exconly() returns a string presentation of the exception
    exc_info.match("invalid literal")
    assert "invalid literal" in exc_info.exconly()

    # However, match() can take a regular expression
    exc_info.match("invalid literal .* 'foo'")

    assert exc_info.typename == "ValueError"
    assert exc_info.type is ValueError

    # These are the same
    assert isinstance(exc_info.value, ValueError)  # .value is the exception itself
    assert exc_info.errisinstance(ValueError)
