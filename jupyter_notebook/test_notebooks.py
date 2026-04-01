import pathlib

import jupyterlib
import pytest


@pytest.mark.parametrize(
    ["filename", "expected"],
    [
        pytest.param("good.ipynb", True, id="good"),
        pytest.param("bad.ipynb", False, id="bad"),
    ],
)
def test_notebook(filename, expected, tmp_path):
    notebook_path = str(pathlib.Path(__file__).parent / "notebooks" / filename)
    assert jupyterlib.is_valid_notebook(notebook_path) is expected
