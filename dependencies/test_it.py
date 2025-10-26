"""
Demo: Test dependencies

Tests sometimes depends on the passing of previous tests. When
previous tests failed, it does not make sense for the next test to
start.
"""

import pytest


# Order in the file does matter
@pytest.mark.dependency
def test_login():
    pass


@pytest.mark.dependency(depends=["test_login"])
def test_tokens():
    pass


@pytest.mark.dependency(depends=["test_login", "test_tokens"])
def test_access():
    assert False


@pytest.mark.dependency(depends=["test_login", "test_tokens", "test_access"])
def test_logout():
    pass
