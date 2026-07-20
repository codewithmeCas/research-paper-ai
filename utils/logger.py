"""
Sets up logging for the project so every module can print messages with
timestamps instead of using plain print() statements.
"""

import logging
import sys


def get_logger(module_name: str) -> logging.Logger:
    """
    Create (or reuse) a logger for a given module.

    Args:
        module_name: Pass in __name__ from the calling file so log
            messages show which file they came from.

    Returns:
        A configured Logger instance.
    """
    logger = logging.getLogger(module_name)

    # Skip setup if this logger already has a handler, otherwise messages
    # get duplicated (happens when Streamlit reruns the script).
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    log_format = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    formatter = logging.Formatter(log_format, datefmt="%H:%M:%S")
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger