import collections
import graphlib

import pytest

# {nodeid: passed/failed/skipped/error}
OUTCOME = {}


def get_dependencies(item: pytest.Function) -> set[str]:
    marker = next(item.iter_markers(name="depends_on"), None)
    if not marker:
        return set()
    return set(marker.args)


def pytest_collection_modifyitems(
    session: pytest.Session, config: pytest.Config, items: list[pytest.Function]
):
    """Order the tests based on dependencies resolution."""
    dependency = collections.defaultdict(set)  # {test: set of tests}
    for it in items:
        dependency[it.function.__name__].update(get_dependencies(it))

    # Resolve dependencies and establish the tests order
    sorter = graphlib.TopologicalSorter(dependency)
    test_order = list(sorter.static_order())

    # Order the tests
    items.sort(key=lambda it: test_order.index(it.function.__name__))


def pytest_runtest_setup(item: pytest.Function):
    """Skip a test if at least one dependencies not passed."""
    mark = next(item.iter_markers(name="depends_on"), None)
    if mark is None or not mark.args:
        return

    for dep_name in mark.args:
        dep_id = item.nodeid.replace(item.originalname, dep_name)
        result = OUTCOME[dep_id]
        if result != "passed":
            pytest.skip(f"because {dep_id} {result}")
            break


def pytest_runtest_logreport(report):
    """Called for each phase of each test (setup/call/teardown)."""
    # Normally, outcome is recorded at "call" time
    # When a test is skipped, outcome at setup is "skipped"
    if report.when == "setup" or report.when == "call":
        OUTCOME[report.nodeid] = report.outcome  # 'passed', 'failed', or 'skipped'
