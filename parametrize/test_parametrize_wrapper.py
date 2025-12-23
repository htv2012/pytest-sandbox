from typing import Any, List, Union

import pytest


def parametrize_wrapper(argnames: Union[List, str], argvalues: List[Any]):
    def _param(**kwargs):
        nonlocal names

        test_id = kwargs.pop("id", None)
        values = [kwargs[name] for name in names]
        return pytest.param(*values, id=test_id)

    if isinstance(argnames, str):
        names = [name.strip() for name in argnames.split(",")]
    else:
        names = list(argnames)

    return pytest.mark.parametrize(names, [_param(**values) for values in argvalues])


@parametrize_wrapper(
    "in_contact, is_unified",
    [
        dict(in_contact=False, is_unified=False, id="out of contact, legacy names"),
        dict(in_contact=False, is_unified=True, id="out of contact, unified names"),
        dict(in_contact=True, is_unified=False, id="in contact, legacy names"),
        dict(in_contact=True, is_unified=True, id="in contact, unified names"),
    ],
)
def test_get_faults(in_contact, is_unified):
    pass
