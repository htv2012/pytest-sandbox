import os


def test_user(monkeypatch):
    with monkeypatch.context() as m:
        m.setenv("USER", "rootie")
        assert os.getenv("USER") == "rootie"
    assert os.getenv("USER") != "rootie"
