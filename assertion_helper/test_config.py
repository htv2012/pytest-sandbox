import json
import pathlib

import pytest


def verify_config(config_file: str | pathlib.Path):
    """
    Help assert the configuration file is a valid one.

    Note the use of pytest's builtin `__tracebackhide__` variable. When
    set to `True`, the assertion failure will not show this
    function. Instead, it will show its caller.
    """
    global __tracebackhide__
    __tracebackhide__ = True
    config_file = pathlib.Path(config_file)

    # File must exist
    assert config_file.exists(), f"File {config_file} does not exist"

    # and parsable
    try:
        with open(config_file) as stream:
            json.load(stream)
        return
    except json.decoder.JSONDecodeError:
        pass
    pytest.fail(f"Not a valid JSON file: {config_file}")


def test_valid():
    verify_config("valid.json")


def test_invalid():
    verify_config("invalid.json")
