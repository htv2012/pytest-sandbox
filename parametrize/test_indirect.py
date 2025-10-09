#!/usr/bin/env python3
"""
Parametrize with indirect
"""

import logging
import pytest
logger = logging.getLogger()


@pytest.fixture
def ggma(request):
    return f"ggma{request.param}"


@pytest.fixture
def sgw(request):
    return f"sgw{request.param}"


@pytest.mark.parametrize(
    "ggma, sgw",
    [
        pytest.param(1, 2, id="ggm1 and sgw2"),
        pytest.param(3, 4, id="ggm3 and sgw4"),
    ],
    indirect=True,
)
def test_it(ggma, sgw):
    logger.debug(f"{ggma=}")
    logger.debug(f"{sgw=}")
    assert ggma in {"ggma1", "ggma2", "ggma3"}
    assert sgw in {"sgw1", "sgw2", "sgw3", "sgw4"}
