#!/usr/bin/env python3
import os

import pytest

DEFAULT_SERVERS = [
    "default1.com",
    "default2.com",
]


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--test-server",
        action="append",
        default=[],
        help="Servers list",
    )


def pytest_generate_tests(metafunc: pytest.Metafunc):
    global DEFAULT_SERVERS

    if "server" in metafunc.fixturenames:
        # Command-line options will take precedence
        servers = metafunc.config.getoption("test_server")

        # If no command-line option, look for environment variable
        if not servers:
            servers = os.getenv("TEST_SERVERS")
            if servers is not None:
                servers = servers.split(",")

        # No command-line option, no environment variable, use default
        if not servers:
            servers = DEFAULT_SERVERS

        # Use pytest.param to control tests' names
        servers = [
            pytest.param(server, id=f"test server: {server}") for server in servers
        ]

        # Finally, parametrize it
        metafunc.parametrize("server", servers, scope="session")
