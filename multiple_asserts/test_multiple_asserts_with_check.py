import pytest
from pytest_check import check, equal


@pytest.fixture
def actual():
    return {"id": 1, "userId": 501}


def test_example(actual):
    equal(actual["id"], 1)
    equal(actual["userId"], 501)


def test_example2(actual):
    with check:
        assert actual["id"] == 1
    with check:
        assert actual["userId"] == 501
