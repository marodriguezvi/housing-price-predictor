from pydantic import ValidationError
from flask import request, jsonify, Blueprint

from ..schemas.predict import HouseInput
from ..services.predict import PredictionService
from ..models.regression_model import RegressionModel

prediction_service = PredictionService(RegressionModel())

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        validated_input = HouseInput(**data)
        serialized_input = validated_input.model_dump()

        prediction_value = prediction_service.predict(serialized_input)

        return jsonify({"prediction": prediction_value})

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
