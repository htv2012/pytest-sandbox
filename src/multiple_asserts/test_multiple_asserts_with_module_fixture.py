"""
Use a fixture to perform the prepare- and action phrase. Then each test
will assert just once.
"""

import pytest


@pytest.fixture(scope="module")
def actual():
    """Perform the action and return the actual data."""
    return {
        "name": "env1",
        "description": "My Environment",
        "tags": ["sandbox", "experimental"],
    }


def test_name(actual):
    assert actual["name"] == "env1"


def test_tag_sandbox(actual):
    assert "sandbox" in actual["tags"]


def test_tag_experimental(actual):
    assert "experimental" in actual["tags"]


def test_description(actual):
    assert actual["description"] == "My Environment"
