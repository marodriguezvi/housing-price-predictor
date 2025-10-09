import json
from datetime import datetime

from common.logger import get_logger

logger = get_logger("app")


def log_prediction(input_data: dict, prediction: float, model: str) -> None:
    """
    Log prediction usage for monitoring.

    Args:
        input_data (dict): Input features used in the prediction.
        prediction (float): Model prediction result.
        model (str): Model name.
    """
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "input_sample": input_data,
        "prediction": prediction,
    }
    logger.info(f"Prediction log: {json.dumps(log_entry)}")
