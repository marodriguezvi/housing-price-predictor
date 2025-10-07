from utils.logger import get_logger
from .ml_workflow import (
    load_and_prepare_data,
    train_and_save_model,
    evaluate_model,
)

logger = get_logger(__name__, log_file="logs/training.log")


def main():
    logger.info("Starting pipeline execution...")

    X_train, X_test, y_train, y_test = load_and_prepare_data(
        "data/HousingData.csv", "MEDV"
    )
    model, version = train_and_save_model(X_train, y_train, "v1")
    evaluate_model(model, X_test, y_test, version)

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()
