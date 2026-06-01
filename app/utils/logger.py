"""Centralized logging configuration."""

import logging
import sys
from pathlib import Path

from app.config import settings


def setup_logger(name: str = __name__) -> logging.Logger:
    """Configure and return a logger instance.

    Args:
        name: Logger name, typically __name__

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(settings.LOG_LEVEL)

    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(settings.LOG_LEVEL)

    # File handler
    file_handler = logging.FileHandler(logs_dir / "app.log")
    file_handler.setLevel(settings.LOG_LEVEL)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


# Module logger
logger = setup_logger(__name__)
