from pathlib import Path
from typing import Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from ml.utils.io import save_json
from commont.logger import get_logger
from ml.utils.time import measure_time


logger = get_logger("training")


@measure_time
def load_and_prepare_data(
    filepath: str, target_column: str
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Load dataset from CSV and split into train and test sets.

    Args:
        filepath (str): Path to the CSV file.
        target_column (str): Name of the target variable column.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]: X_train, X_test, y_train, y_test
    """
    logger.info(f"Loading data from {filepath}")
    try:
        df = pd.read_csv(filepath)

        # df.head()
        # df.info()
        # df.describe()
        # df.isnull().sum()
        # df.duplicated().sum()

        df.dropna(inplace=True)
        X = df.drop(columns=[target_column])
        y = df[target_column]

        return train_test_split(X, y, test_size=0.2)

    except FileNotFoundError as e:
        logger.error(f"File not found: {filepath}")
        raise e
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise e


@measure_time
def train_and_save_model(
    X_train: pd.DataFrame, y_train: pd.Series, version: str = None
) -> None:
    """Train a simple regression model and save it as an artifact.

    Args:
        csv_path (str): Path to the CSV file containing the dataset.
        version (str): Version label for the model artifact.

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
    """
    try:
        model = LinearRegression()
        model.fit(X_train, y_train)

        version = version or get_next_version()
        model_name = f"model_{version}"
        output_path = Path(f"ml/models/{model_name}.pkl")
        joblib.dump(model, output_path)

        logger.info(f"Model saved at {output_path}")

        return model, model_name
    except Exception as e:
        logger.error(f"Error training or saving model: {e}")
        raise e


def get_next_version() -> str:
    """Get the next version number for the model artifact.

    Returns:
        str: Next version label (e.g., "v2" if "model_v1.pkl" exists).
    """
    models_dir = Path("ml/models")
    models_dir.mkdir(parents=True, exist_ok=True)
    versions = [
        int(p.stem.split("_v")[-1]) for p in models_dir.glob("model_v*.pkl")
    ]
    return f"v{max(versions) + 1}" if versions else "v1"


@measure_time
def evaluate_model(
    model: LinearRegression,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    model_name: str,
) -> None:
    """
    Evaluate a trained regression model and save the metrics as a JSON file.

    Args:
        model (LinearRegression): Trained regression model.
        X_test (pd.DataFrame): Test features.
        y_test (pd.Series): True target values for the test set.
        model_name (str): name.

    Returns:
        None
    """
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    results_path = f"ml/metadata/{model_name}.json"
    results = {
        "model_version": model_name.split("_v")[-1],
        "mean_absolute_error": mae,
        "mean_squared_error": mse,
        "root_mean_squared_error": rmse,
        "r2_score": r2,
    }
    save_json(results, results_path)

    logger.info(f"Evaluation saved at {results_path}")
