from app import create_app
import app.routes.predict as predict_module


def test_predict_route_happy_path(monkeypatch):
    """Verify that the endpoint returns a valid prediction."""
    valid_input = {
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

    class DummyPredictionService:
        def predict(self, input_data):
            return 29.557198852056562

    monkeypatch.setattr(
        predict_module, "prediction_service", DummyPredictionService()
    )

    app = create_app({"TESTING": True})
    client = app.test_client()

    resp = client.post("/predict", json=valid_input)
    assert resp.status_code == 200
    data = resp.get_json()
    assert "prediction" in data
    assert data["prediction"] == 29.557198852056562


def test_predict_route_validation_error():
    """Verify that the endpoint returns a bad request response."""
    invalid_input = {"CRIM": -1}

    app = create_app({"TESTING": True})
    client = app.test_client()

    resp = client.post("/predict", json=invalid_input)
    assert resp.status_code == 400
    data = resp.get_json()
    assert "error" in data
