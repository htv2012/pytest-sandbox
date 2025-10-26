import pytest
from objectlib import create_object, get_object


@pytest.fixture(scope="module")
def object_under_test():
    return create_object()


@pytest.mark.incremental
def test_create(object_under_test):
    assert object_under_test.status == "created"


@pytest.mark.incremental
def test_get(object_under_test):
    assert get_object(object_under_test.id) is object_under_test


@pytest.mark.incremental
def test_delete(object_under_test):
    object_under_test.delete()
    assert object_under_test.status == "deleted"
