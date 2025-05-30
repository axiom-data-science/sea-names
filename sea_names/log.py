# -*- coding: utf-8 -*-
"""Logging configuration."""
import importlib.resources
import logging
import logging.config


logger = logging.getLogger("sea-names")


def setup_logging():
    """Initializes the project logging."""
    ref = importlib.resources.files("sea_names") / "logging.conf"
    with importlib.resources.as_file(ref) as path:
        logging.config.fileConfig(path)
