"""
Use a fixture to perform the prepare- and action phrase. Then each test
will assert just once.
"""

import pytest

# ======================================================================


@pytest.fixture(scope="module")
def payload():
    return {"id": 1, "userId": 501}


# ======================================================================


def test_userid(payload):
    assert payload["userId"] == 501


def test_id(payload):
    assert payload["id"] == 1
