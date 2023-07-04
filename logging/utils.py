import logging
import sys


def get_logger(logger_name: str, level: int = logging.INFO, format: str = "%(message)s"):
    """
    Create a logger with a StreamHandler attached that outputs to stdout.
    Propagation of messages to parent logger is turned off.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(format))
    logger.addHandler(handler)
    logger.propagate = False
    return logger

