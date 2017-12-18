"""
Contains all methods for configuring any applicable loggers using built-in logging module
"""
import logging
import sys


def configure_stdout_logger():
    """
    Configures a logger, which prints cleanly to stdout

    If this logger has already been configured, this skips the configuration step and simply returns the logger.
    :return: returns the configured logger
    """
    logger = logging.getLogger("STDOUT")
    if len(logger.handlers) == 0:
        logger.setLevel(logging.INFO)
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.INFO)
        stdout_fmt = logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s', datefmt='%H:%M:%S')
        stdout_handler.setFormatter(stdout_fmt)
        logger.addHandler(stdout_handler)
        logger.info("Standard Output logger configured")

    return logger