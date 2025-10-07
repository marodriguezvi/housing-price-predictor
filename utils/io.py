import json
from pathlib import Path
from logging import Logger


def save_json(data: dict, output_path: str, logger: Logger) -> None:
    """Save any dictionary as a JSON file.

    Args:
        data (dict): Dictionary to be saved.
        output_path (str): Full path (including filename) where will be written.
        logger (logging.Logger): Logger instance for logging messages.

    Returns:
        None
    """
    try:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logger.error(f"Error saving JSON to {output_path}: {e}")
        raise e
