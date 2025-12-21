import pathlib

import pytestlib

TEST_DATA_PATH = pathlib.Path(__file__).with_name("test_data.yaml")


@pytestlib.parametrize_from_file(TEST_DATA_PATH, "test_user", ["uid", "shell"])
def test_basic(uid, shell):
    assert uid >= 500 or uid == 0
    assert shell in {"sh", "bash", "zsh"}


@pytestlib.parametrize_from_file(TEST_DATA_PATH, "test_complex", ["uid", "permissions"])
def test_complex(uid, permissions):
    if uid == 0:
        assert permissions["sudo"] is True
    elif uid > 1000:
        assert permissions["sudo"] is False
    assert permissions["print"] is True
