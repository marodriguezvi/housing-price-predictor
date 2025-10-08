from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression

from ml.ml_workflow import (
    load_and_prepare_data,
    train_and_save_model,
    evaluate_model,
)
from ml.utils.io import load_json


def test_load_and_prepare_data(tmp_path):
    """Ensure CSV is loaded, cleaned, and split correctly."""
    df = pd.DataFrame(
        {
            "feature1": [1, 2, 3, 4, 5],
            "feature2": [5, 4, 3, 2, 1],
            "price": [10, 12, 13, 15, 18],
        }
    )

    csv_path = tmp_path / "data.csv"
    df.to_csv(csv_path, index=False)

    X_train, X_test, y_train, y_test = load_and_prepare_data(
        str(csv_path), "price"
    )

    assert hasattr(X_train, "shape")
    assert hasattr(X_test, "shape")
    assert hasattr(y_train, "shape")
    assert hasattr(y_test, "shape")

    assert X_train.shape[0] + X_test.shape[0] == df.shape[0]
    assert y_train.shape[0] + y_test.shape[0] == df.shape[0]


def test_train_and_save_model(tmp_path, monkeypatch):
    """Train a model and ensure the artifact is saved with the expected version."""
    monkeypatch.chdir(tmp_path)

    models_dir = tmp_path / "ml" / "models"
    models_dir.mkdir(parents=True)
    (models_dir / "model_v1.pkl").write_text("dummy")

    X_train = pd.DataFrame({"a": [1.0, 2.0, 3.0, 4.0]})
    y_train = pd.Series([2.0, 4.0, 6.0, 8.0])

    model, model_name = train_and_save_model(X_train, y_train)

    assert model is not None
    assert model_name.startswith("model_v")

    saved_path = Path("ml/models") / f"{model_name}.pkl"
    assert saved_path.exists()


def test_evaluate_model(tmp_path, monkeypatch):
    """Evaluate a trained model and assert metrics JSON have been created."""
    monkeypatch.chdir(tmp_path)

    X = pd.DataFrame({"x": [1, 2, 3, 4, 5]})
    y = pd.Series([2, 4, 6, 8, 10])

    model = LinearRegression()
    model.fit(X, y)

    X_test = X.iloc[-2:]
    y_test = y.iloc[-2:]

    model_name = "model_vtest"

    evaluate_model(model, X_test, y_test, model_name)

    results_path = Path("ml/metadata") / f"{model_name}.json"
    assert results_path.exists()

    results = load_json(results_path)

    assert "r2_score" in results
    assert "root_mean_squared_error" in results
    assert isinstance(results["r2_score"], float)
    assert results["root_mean_squared_error"] >= 0.0
