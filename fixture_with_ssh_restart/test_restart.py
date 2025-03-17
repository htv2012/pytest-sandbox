import paramiko
import pytest


@pytest.mark.skip(reason="Need add config file")
def test_user_is_not_root(ssh_client: paramiko.SSHClient):
    _, stdout, _ = ssh_client.exec_command("whoami")
    user = stdout.read().decode().strip()
    assert user != "root"


@pytest.mark.skip(reason="Need add config file")
def test_os_release_exists(ssh_client: paramiko.SSHClient):
    with ssh_client.open_sftp() as sftp:
        sftp.stat("/etc/os-release")  # Will raise if not exist
