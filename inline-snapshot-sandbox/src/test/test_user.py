from inline_snapshot import snapshot
from inline_snapshot_sandbox import create_user


def test_create_user():
    user = create_user("anna")
    assert user == snapshot({})
