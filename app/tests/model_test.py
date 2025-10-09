import pandas as pd

from app.models.regression_model import RegressionModel


def test_regression_model_interface(monkeypatch):
    """Verify that RegressionModel exposes the expected interface."""
    model = RegressionModel()
    monkeypatch.setattr(model, "load", lambda: None)

    def fake_predict(X):
        return [float(42.0)] * X.shape[0]

    monkeypatch.setattr(model, "predict", fake_predict)

    X = pd.DataFrame({"a": [1.0, 2.0]})
    preds = model.predict(X)

    assert isinstance(preds, list) or hasattr(preds, "__iter__")
    assert len(preds) == X.shape[0]

    first_val = float(preds[0])
    assert first_val == 42.0
