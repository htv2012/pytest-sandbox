#!/usr/bin/env python3
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger()


def function_under_test():
    logger.info("Out of Milk")


def test_log(caplog):
    with caplog.at_level(logging.INFO):
        function_under_test()

    assert "Out of Milk" in caplog.text
