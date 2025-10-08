import json
from pathlib import Path
from logging import Logger


def save_json(data: dict, output_path: str) -> None:
    """Save any dictionary as a JSON file.

    Args:
        data (dict): Dictionary to be saved.
        output_path (str): Full path (including filename) where will be written.

    Returns:
        None
    """
    try:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Unable to save JSON - path not found: {output_path}"
        ) from e
    except Exception as e:
        raise Exception(f"Error saving JSON to {output_path}: {e}") from e


def load_json(input_path: str) -> dict:
    """Load a JSON file and return its contents as a dict."""
    input_path = Path(input_path)
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"JSON file not found at path: {input_path}"
        ) from e
