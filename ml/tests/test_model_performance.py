from pathlib import Path
from ml.utils.io import load_json
from common.files import get_latest_version_file


def test_model_meets_minimum_performance_threshold():
    """Ensure the model meets minimum performance requirements."""
    metadata_dir = Path("ml/metadata")
    assert metadata_dir.exists()

    results_path = get_latest_version_file(
        str(metadata_dir), base_name="model", extension="json"
    )

    results = load_json(results_path)

    assert results["r2_score"] > 0.60
    assert results["root_mean_squared_error"] < 6.0
