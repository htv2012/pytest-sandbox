"""Show inside a request object."""

from . import introspect


def test_pytestconfig(pytestconfig):
    introspect.explore(pytestconfig, "pytestconfig")
