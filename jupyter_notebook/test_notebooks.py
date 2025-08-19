import pathlib
import subprocess

import pytest


@pytest.fixture(scope="module")
def notebooks_dir():
    return pathlib.Path(__file__).parent / "notebooks"


@pytest.mark.parametrize(
    ["filename", "expected"],
    [
        pytest.param("good.ipynb", 0, id="good"),
        pytest.param("bad.ipynb", 1, id="bad"),
    ],
)
def test_notebook(filename, expected, notebooks_dir, tmp_path):
    notebook_path = notebooks_dir / filename
    process = subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "markdown",
            "--execute",
            "--output-dir",
            str(tmp_path),
            str(notebook_path),
        ],
        check=False,
        capture_output=True,
    )

    assert process.returncode == expected
