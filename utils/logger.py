import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler


def get_logger(name: str, log_file: str = "logs/app.log") -> logging.Logger:
    """
    Get a configured logger instance.

    Args:
        name (str): The name of the logger.
        log_file (str, optional): Path where log messages will be written.

    Returns:
        logging.Logger: A configured logger instance.
    """
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler = TimedRotatingFileHandler(
            log_file,
            when="midnight",
            interval=1,
            backupCount=7,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
