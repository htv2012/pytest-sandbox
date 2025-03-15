import pathlib
import tomllib

import pytest


def _load_data():
    data_path = pathlib.Path(__file__).with_name("cases.toml")
    assert data_path.exists()

    with open(data_path, "rb") as stream:
        raw = tomllib.load(stream)

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
