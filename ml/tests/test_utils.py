import pytest
from pathlib import Path
from ml.utils.io import save_json, load_json


def test_save_and_load_json(tmp_path):
    """Ensure JSON is saved and loaded correctly."""

    data = {"r2_score": 0.8, "version": "v1"}
    file_path = tmp_path / "test.json"

    save_json(data, file_path)
    assert file_path.exists()

    loaded = load_json(file_path)
    assert loaded == data


def test_save_json_invalid_path():
    """Ensure save_json raises an exception for invalid paths."""
    with pytest.raises(Exception):
        save_json({"data": 1}, Path("/invalid/path/test.json"))
