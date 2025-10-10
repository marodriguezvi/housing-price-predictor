import argparse

from common.logger import get_logger
from ml.ml_workflow import (
    load_and_prepare_data,
    train_and_save_model,
    evaluate_model,
)

logger = get_logger("training")


def main(data_path: str, target: str, version: str | None):
    logger.info("Starting pipeline execution...")

    X_train, X_test, y_train, y_test = load_and_prepare_data(data_path, target)
    model, model_name = train_and_save_model(X_train, y_train, version)
    evaluate_model(model, X_test, y_test, model_name)

    logger.info("Pipeline completed successfully")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run ML training pipeline")
    parser.add_argument(
        "--data-path",
        type=str,
        default="data/HousingData.csv",
        help="Path to the CSV dataset",
    )
    parser.add_argument(
        "--target",
        type=str,
        default="MEDV",
        help="Name of the target column in the dataset",
    )
    parser.add_argument(
        "--version",
        type=str,
        default=None,
        help="Optional model version label (e.g. v2). If omitted, auto-increment will be used.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.data_path, args.target, args.version)
