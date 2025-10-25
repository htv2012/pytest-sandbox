import fabric
import paramiko
import pytest


def get_test_hostnames():
    config: paramiko.config.Config = fabric.Config().base_ssh_config
    names = [name for name in config.get_hostnames() if name.startswith("ssh-sandbox")]
    return names


@pytest.fixture(params=get_test_hostnames())
def conn(request: pytest.FixtureRequest):
    """A fabric.Connection"""
    try:
        connection = fabric.Connection(host=request.param, connect_timeout=2)
        connection.run("whoami", hide=True)
        return connection
    except (paramiko.ssh_exception.NoValidConnectionsError, TimeoutError):
        pytest.skip(f"Host {request.param} is not online.")
