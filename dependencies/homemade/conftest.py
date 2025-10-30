import pytest

# TODO: Re-order tests so that dependencies got to run first

# Test outcome: {node_id: result}
# where result in {'passed', 'failed', 'skip'}
# Sample node_id: 'dir/test_file::test_name[parametrize id]'
OUTCOME = {}


def pytest_runtest_logreport(report):
    """Called for each phase of each test (setup/call/teardown)."""
    if report.when != "call":  # only store final outcome of the test
        return
    OUTCOME[report.nodeid] = report.outcome  # 'passed', 'failed', or 'skipped'


def pytest_runtest_setup(item: pytest.Function):
    # Locate the `depends_on` mark
    depends_on_mark = next(
        (mark for mark in item.iter_markers(name="depends_on")), None
    )
    if depends_on_mark is None:
        return

    # For each dependency, ensure that it has been ran and passed
    # Otherwise, skip the test
    for dependency_name in depends_on_mark.args:
        dependency_node_id = item.nodeid.replace(item.originalname, dependency_name)
        result = OUTCOME.get(dependency_node_id, "has not been run")
        if result != "passed":
            pytest.skip(f"because {dependency_node_id} {result}")
            break
