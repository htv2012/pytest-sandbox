#!/usr/bin/env python3
import collections
import dataclasses

import pytest

Param = collections.namedtuple(
    "Param",
    ["tid", "ingress", "egress"],
)


@dataclasses.dataclass
class Param2:
    tid: str
    ingress: str
    egress: str
    wild: bool = False


def get_test_id(test_data):
    return test_data.tid


@pytest.mark.parametrize(
    "test_data",
    [
        Param(tid="tcp-tcp", ingress="tcp", egress="tcp"),
        Param(tid="udp-udp", ingress="udp", egress="udp"),
    ],
    ids=get_test_id,
)
def test1(test_data):
    assert test_data.ingress in {"udp", "tcp", "tcp+tls"}


@pytest.mark.parametrize(
    "test_data",
    [
        Param2("tcp-tcp", ingress="tcp", egress="tcp"),
        Param2("udp-udp", ingress="udp", egress="udp", wild=True),
    ],
    ids=get_test_id,
)
def test2(test_data):
    assert test_data.ingress in {"udp", "tcp", "tcp+tls"}
