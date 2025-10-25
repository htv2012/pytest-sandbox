import pytest
from objectlib import create_object, get_object


@pytest.fixture(scope="module")
def test_object():
    return create_object()


def test_id(test_object):
    assert test_object.id > 1000


@pytest.mark.incremental
def test_create(test_object):
    assert test_object.status == "created"
    assert test_object.id == 123


@pytest.mark.incremental
def test_get(test_object):
    assert get_object(test_object.id) is test_object


@pytest.mark.incremental
def test_delete(test_object):
    test_object.delete()
    assert test_object.status == "deleted"
