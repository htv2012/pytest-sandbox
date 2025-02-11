import pytest


@pytest.mark.skip(reason="Need to install ssh server")
def test_ssh(ssh_client):
    with ssh_client.open_sftp() as sftp:
        with sftp.open("/etc/os-release", "r") as stream:
            raw = stream.read()
    assert b"ID=" in raw
