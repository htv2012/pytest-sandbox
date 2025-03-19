"""
The `request` fixture has an attribute `path` which is the path of the
test script. We can use that in order to locate the `data` dir
"""
import pathlib

import pytest
import yaml


@pytest.fixture
def data_path(request):
    script_dir: pathlib.Path = request.path.parent
    return script_dir / "data"


def test_data(data_path):
    with open(data_path / "data.yaml") as stream:
        data = yaml.safe_load(stream)
    assert data == {"uid": 501, "shell": "zsh"}
