import logging
import pathlib
import time

import paramiko
import pytest


@pytest.fixture(scope="module")
def test_config():
    config_path = pathlib.Path("~/.ssh/config").expanduser()
    if not config_path.exists():
        pytest.skip("~/.ssh/config does not exist")

    config = paramiko.SSHConfig.from_path(config_path)
    if "test1" not in config.get_hostnames():
        pytest.skip("Test host 'test1' is not configured")

    return config.lookup("test1")


@pytest.fixture(scope="module")
def ssh_client(test_config):
    """
    Create a ssh client and perform some prep works remotely.
    """
    logging.info("First connection...")
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=test_config["hostname"], username=test_config["user"])
    logging.info("Connected")

    logging.info("Prep the remote host")
    # Perform prep works here

    logging.info("Reboot the remote host")
    client.exec_command("sudo shutdown -r now")

    logging.info("Second connection...")
    while True:
        try:
            client.connect(
                hostname=test_config["hostname"], username=test_config["user"]
            )
            logging.info("Connected again")
            break
        except (
            paramiko.SSHException,
            paramiko.ssh_exception.NoValidConnectionsError,
        ):
            logging.info("Waiting for host...")
            time.sleep(3)

    yield client

    logging.info("Clean up remote host")
    # Do something here to clean up
