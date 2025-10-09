import re
from pathlib import Path


def get_latest_version_file(
    directory: str, base_name: str, extension: str
) -> Path:
    """Get the latest versioned file in a directory.

    This function scans a directory for files that follow the naming convention:
    `{base_name}_v<version>.<extension>` and returns the one with the highest version number.

    Args:
        directory (str): Path to the directory containing the versioned files.
        base_name (str): Base name of the files (e.g., "model", "metrics").
        extension (str): File extension to filter by.

    Returns:
        Path: Path object pointing to the latest versioned file.

    Raises:
        FileNotFoundError: If no versioned files matching the pattern are found.
    """
    dir_path = Path(directory)
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    pattern = re.compile(rf"{base_name}_v(\d+)\.{extension}$")
    candidates = []

    for file in dir_path.glob(f"{base_name}_v*.{extension}"):
        match = pattern.search(file.name)
        if match:
            version = int(match.group(1))
            candidates.append((version, file))

    if not candidates:
        raise FileNotFoundError(
            f"No versioned {extension} files found for '{base_name}' in {directory}"
        )

    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]
