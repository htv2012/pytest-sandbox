import fabric


def test_host_is_linux(conn: fabric.Connection):
    result: fabric.runners.Result = conn.run("uname", hide=True)
    assert result.stdout == "Linux\n"


def test_bash_is_install(conn: fabric.Connection):
    result: fabric.runners.Result = conn.run("which bash", hide=True)
    assert result.return_code == 0
