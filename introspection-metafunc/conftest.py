import pytest
from pytest_sandbox import introspect


def pytest_generate_tests(metafunc: pytest.Metafunc):
    introspect.explore(metafunc, "Metafunc")
