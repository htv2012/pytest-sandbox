#!/usr/bin/env python3
import os

import pytest


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--test-servers", help="Servers list")
    parser.addoption("--test-ports", help="Ports to test")


def _get_test_data(config, name, default):
    value = config.getoption(name)
    value = value or os.getenv(name.upper(), default)
    return value.split(",")


def pytest_generate_tests(metafunc: pytest.Metafunc):
    TEST_SERVERS = "default1.com,default2.com"
    TEST_PORTS = "8001,8002"

    if "server" in metafunc.fixturenames:
        servers = _get_test_data(metafunc.config, "test_servers", TEST_SERVERS)
        metafunc.parametrize("server", servers, scope="session")

    if "port" in metafunc.fixturenames:
        ports = _get_test_data(metafunc.config, "test_ports", TEST_PORTS)
        ports = [int(port) for port in ports]
        metafunc.parametrize("port", ports, scope="session")
