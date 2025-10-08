import json
from pathlib import Path


def test_model_performance_threshold():
    """Ensure the model meets minimum performance requirements."""
    metadata_dir = Path("ml/metadata")
    assert metadata_dir.exists()

    files = sorted(metadata_dir.glob("model_*.json"))
    assert files
    results_path = files[-1]

    with open(results_path, "r") as f:
        results = json.load(f)

    assert results["r2_score"] > 0.60
    assert results["root_mean_squared_error"] < 6.0
