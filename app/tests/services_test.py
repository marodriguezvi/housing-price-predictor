import pandas as pd

from app.services.predict import PredictionService


class DummyModel:
    name = "model_vtest"

    def __init__(self):
        self.loaded = False

    def load(self):
        self.loaded = True

    def predict(self, X):
        return [float(X.iloc[0].sum())]


def test_prediction_service_returns_float_prediction(monkeypatch):
    """Test that PredictionService returns a float prediction."""
    dummy = DummyModel()
    service = PredictionService(dummy)

    input_data = {
        "CRIM": 0.00632,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.09,
        "RAD": 1,
        "TAX": 296.0,
        "PTRATIO": 15.3,
        "B": 396.9,
        "LSTAT": 4.98,
    }

    pred = service.predict(input_data)
    assert isinstance(pred, float)

    expected = float(pd.DataFrame([input_data]).iloc[0].sum())
    assert pred == expected
