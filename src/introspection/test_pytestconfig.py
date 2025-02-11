"""Show inside a request object."""

from pytest_sandbox import introspect


def test_pytestconfig(pytestconfig):
    introspect.explore(pytestconfig, "pytestconfig")
