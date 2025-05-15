"""Show inside a request object."""

import logging

import pytest

from pytest_sandbox import introspect


@pytest.fixture
def custom_fixture(request):
    introspect.explore(request.node, "node")


def test_explore_node(request, custom_fixture):
    pass
