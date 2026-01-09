import pathlib

import pytest
import yaml


def parametrize_from_file(path: pathlib.Path, section: str, argnames: list[str]):
    path = pathlib.Path(path)
    with open(path, "rb") as stream:
        content = yaml.safe_load(stream)

    test_params = content[section]
    return pytest.mark.parametrize(
        argnames,
        [
            pytest.param(*[params[name] for name in argnames], id=test_id)
            for test_id, params in test_params.items()
        ],
    )
