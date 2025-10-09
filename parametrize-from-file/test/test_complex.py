"""
Sometimes, each test case consists of many parameters, we should
use a dictionary to simplify the test signature
"""

import pathlib

import pytest
import yaml


def _load_cases():
    here = pathlib.Path(__file__).parent
    data_path = here / "data" / "complex.yaml"
    assert data_path.exists()

    with open(data_path) as stream:
        cases = yaml.safe_load(stream)

    for test_id, test_data in cases.items():
        yield pytest.param(test_data, id=test_id)


@pytest.mark.parametrize("data", _load_cases())
def test_it(data):
    assert data["uid"] < 1000
