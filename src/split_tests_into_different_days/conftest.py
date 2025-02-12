import datetime

import pytest

DOW = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
DOW_SET = set(DOW)


def pytest_runtest_setup(item: pytest.Item):
    """
    We have so many tests, we need to split them up, some run on Monday,
    some run on Tuesday, ...
    """
    # Get markers which contains Monday, Tuesday, ... Sunday
    days = DOW_SET.intersection(mark.name for mark in item.iter_markers())

    # If there is no *day marker, this test should be run all the times
    if not days:
        return

    # Get today's day of the week
    today = datetime.date.today()
    today_dow = DOW[today.weekday()]

    # Skip if not meant to run today
    if today_dow not in days:
        pytest.skip(reason="Test not meant for today")
