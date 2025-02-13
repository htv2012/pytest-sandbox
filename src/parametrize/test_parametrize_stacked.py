#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize("second", ["abc", "def"])
@pytest.mark.parametrize("first", [1, 2, 3])
def test_add(first, second):
    pass


@pytest.mark.parametrize(
    "port", [pytest.param("80", id="http"), pytest.param("443", id="https")]
)
@pytest.mark.parametrize("method", "get put post delete".split())
def test_add_using_id(method, port):
    pass
