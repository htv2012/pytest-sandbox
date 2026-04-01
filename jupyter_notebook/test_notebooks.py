import pathlib

import notebook
import pytest


@pytest.mark.parametrize(
    ["filename", "expected"],
    [
        pytest.param("without_exception.ipynb", True, id="without exception"),
        pytest.param("with_exception.ipynb", False, id="with exception"),
    ],
)
def test_notebook(filename, expected, tmp_path):
    notebook_path = str(pathlib.Path(__file__).parent / "data" / filename)
    assert notebook.has_no_exception(notebook_path) is expected
