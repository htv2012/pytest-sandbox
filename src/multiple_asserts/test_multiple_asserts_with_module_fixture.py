"""
Use a fixture to perform the prepare- and action phrase. Then each test
will assert just once.
"""

import pytest


@pytest.fixture(scope="module")
def actual():
    """Perform the action and return the actual data."""
    return {
        "metadata": {
            "name": "My Environment",
            "tags": ["sandbox", "experimental"],
        }
    }


def test_name(actual):
    assert actual["metadata"]["name"] == "My Environment"


def test_tag_sandbox(actual):
    assert "sandbox" in actual["metadata"]["tags"]


def test_tag_experimental(actual):
    assert "experimental" in actual["metadata"]["tags"]
