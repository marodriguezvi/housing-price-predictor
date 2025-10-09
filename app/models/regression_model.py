import joblib

from common.logger import get_logger
from common.time import measure_time
from .base_model import BaseModel

logger = get_logger("app")


class RegressionModel(BaseModel):
    """Concrete implementation of BaseModel for regression tasks."""

    @property
    def name(self) -> str:
        return "model"

    def load(self):
        """Load the regression model from the specified path."""
        path = self.get_latest_model_path()
        self.model = joblib.load(path)

    @measure_time(logger)
    def predict(self, X):
        """Make predictions using the loaded regression model.

        Args:
            X (pd.DataFrame): Input features for prediction.

        Returns:
            np.ndarray: Predicted values."""
        if self.model is None:
            raise ValueError("Model is not loaded. Call 'load' first.")

        return self.model.predict(X)
