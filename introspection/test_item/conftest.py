"""Show what inside an item."""

import logging

import pytest

from pytest_sandbox import introspect


def pytest_collection_modifyitems(
    session: pytest.Session, config: pytest.Config, items: list[pytest.Item]
):
    logging.info("Show what inside a pytest.Item")
    introspect.explore(items[0], "items[0]")
