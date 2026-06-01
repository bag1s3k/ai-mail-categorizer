import logging


def setup_logging():
    """Setup global logging settings"""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt="{levelname:8} {asctime} {name} - {message}",
        datefmt="%d.%m.%Y %H:%M:%S",
        style="{",
    )

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
