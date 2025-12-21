import pathlib

import pytest
import yaml


def create_param(argnames, test_id, param):
    args = [param[name] for name in argnames]
    return pytest.param(*args, id=test_id)


def parametrize_from_file(path: pathlib.Path, test_name: str, argnames: list[str]):
    path = pathlib.Path(path)
    with open(path, "rb") as stream:
        content = yaml.safe_load(stream)

    test_params = content[test_name]
    argvalues = [
        create_param(argnames, test_id, params)
        for test_id, params in test_params.items()
    ]
    return pytest.mark.parametrize(argnames, argvalues)
