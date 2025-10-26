# conftest.py
import pytest

# store history of failures per test class name and per index in parametrize (if parametrize used)
_failed = {}


def pytest_runtest_makereport(item: pytest.Function, call: pytest.CallInfo):
    if "incremental" not in item.keywords:
        return

    if call.excinfo is None:
        return

    cls_name = str(item.cls)

    # retrieve the index of the test (if parametrize is used in combination with incremental)
    parametrize_index = (
        tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
    )

    # retrieve the name of the test itemtion
    test_name = item.originalname or item.name
    # store in _failed the original name of the failed test
    # _failed[cls_name][parametrize_index] = test_name
    _failed.setdefault(cls_name, {}).setdefault(parametrize_index, test_name)


def pytest_runtest_setup(item):
    if "incremental" not in item.keywords:
        return

    # retrieve the class name of the test
    cls_name = str(item.cls)
    # check if a previous test has failed for this class
    if cls_name not in _failed:
        return

    # retrieve the index of the test (if parametrize is used in combination with incremental)
    parametrize_index = (
        tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
    )
    # retrieve the name of the first test itemtion to fail for this class name and index
    # test_name = _failed[cls_name].get(parametrize_index, None)
    test_name = _failed.get(cls_name, {}).get(parametrize_index, None)
    # if name found, test has failed for the combination of class name & test name
    if test_name is not None:
        pytest.skip("previous test failed: {}".format(test_name))
