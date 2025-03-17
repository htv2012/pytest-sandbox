import pathlib

import pytest
import yaml


def _load_data():
    here = pathlib.Path(__file__).parent
    data_path = here / "data" / "users.yaml"
    assert data_path.exists()

    with open(data_path, "rb") as stream:
        raw = yaml.safe_load(stream)

    for test_id, data in raw.items():
        yield pytest.param(
            data["uid"],
            data["shell"],
            id=test_id,
        )


@pytest.mark.parametrize(["uid", "shell"], _load_data())
def test_user(uid, shell):
    assert uid >= 0
    assert shell.endswith("sh")
