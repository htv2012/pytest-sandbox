import subprocess
import tempfile


def has_no_exception(notebook_path: str):
    with tempfile.TemporaryDirectory() as tmp_path:
        process = subprocess.run(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "markdown",
                "--execute",
                "--output-dir",
                tmp_path,
                str(notebook_path),
            ],
            check=False,
            capture_output=True,
        )
    return process.returncode == 0
