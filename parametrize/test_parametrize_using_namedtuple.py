#!/usr/bin/env python3
"""
These are good candidates to represent test case data, but the test
IDs are not set.
"""

import dataclasses
import typing

import pytest


class Param(typing.NamedTuple):
    ingress: str = None
    egress: str = None
    wild: bool = False


@pytest.mark.parametrize(
    "test_data",
    [
        pytest.param(Param(ingress="tcp", egress="tcp"), id='tcp-tcp'),
        pytest.param(Param(ingress="udp", egress="udp", wild=True), id='udp-udp'),
    ],
)
def test1(test_data):
    assert test_data.ingress in {"udp", "tcp", "tcp+tls"}


@dataclasses.dataclass
class Param2:
    ingress: str
    egress: str
    wild: bool = False


@pytest.mark.parametrize(
    "test_data",
    [
        pytest.param(Param2(ingress="tcp", egress="tcp"), id='tcp-tcp'),
        pytest.param(Param2(ingress="udp", egress="udp", wild=True), id='udp-udp'),
    ],
)
def test2(test_data):
    assert test_data.ingress in {"udp", "tcp", "tcp+tls"}
