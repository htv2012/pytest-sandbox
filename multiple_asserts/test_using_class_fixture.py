#!/usr/bin/env python3
"""
Multiple independent asserts using class-scope fixture
"""

import pytest


@pytest.fixture(scope="class")
def actual():
    return {"id": 1, "userId": 501}


class TestIt:
    def test_id(self, actual):
        assert actual["id"] == 1

    def test_user_id(self, actual):
        assert actual["userId"] == 501
