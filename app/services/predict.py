import pandas as pd
from ..models.base_model import BaseModel
from ..utils.monitoring import log_prediction


class PredictionService:
    """Service to handle ML predictions"""

    def __init__(self, model: BaseModel):
        """
        Initialize the service with a concrete model.

        Args:
            model (BaseModel): Any concrete ML model.
        """
        self.model = model
        self.model.load()

    def predict(self, input_data):
        """
        Make predictions using the ML model.

        Args:
            input_data (dict): Input features for prediction.

        Returns:
            prediction_value (float): Predicted value.
        """
        X = pd.DataFrame([input_data])
        y_pred = self.model.predict(X)
        prediction_value = float(y_pred[0])

        log_prediction(input_data, prediction_value, self.model.name)

        return prediction_value
