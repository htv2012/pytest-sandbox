# content of conftest.py

from typing import Dict, Tuple

import pytest

# store history of failures per test class name and per index in parametrize (if parametrize used)
_test_failed_incremental: Dict[str, Dict[Tuple[int, ...], str]] = {}


def pytest_runtest_makereport(item, call):
    if "incremental" not in item.keywords:
        return

    if call.excinfo is None:
        return

    cls_name = str(item.cls)
    # retrieve the index of the test (if parametrize is used in combination with incremental)
    parametrize_index = (
        tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
    )

    # retrieve the name of the test function
    test_name = item.originalname or item.name
    # store in _test_failed_incremental the original name of the failed test
    _test_failed_incremental.setdefault(cls_name, {}).setdefault(
        parametrize_index, test_name
    )


def pytest_runtest_setup(item):
    if "incremental" not in item.keywords:
        return

    # retrieve the class name of the test
    cls_name = str(item.cls)
    # check if a previous test has failed for this class
    if cls_name not in _test_failed_incremental:
        return

    # retrieve the index of the test (if parametrize is used in combination with incremental)
    parametrize_index = (
        tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
    )
    # retrieve the name of the first test function to fail for this class name and index
    test_name = _test_failed_incremental[cls_name].get(parametrize_index, None)
    # if name found, test has failed for the combination of class name & test name
    if test_name is not None:
        pytest.xfail("previous test failed: {}".format(test_name))
