# Housing Price Predictor

This repository contains a small Flask application and supporting ML code for training a housing price prediction model.

 

## Requirements

- Python 3.10+
- Flask 3.1.2

Please keep these versions in mind when setting up your development environment.

## Quick setup (local, virtual environment)

1. Clone this repository to your local machine.

2. Open a terminal in the project folder.

3. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run the Flask app locally:

```bash
python -m flask --app app run
```

By default Flask binds to 127.0.0.1:5000. Set `FLASK_RUN_HOST=0.0.0.0` if you need external access.

## Run the training pipeline

Train and build the model using the project's pipeline module:

```bash
python -m ml.pipeline
```

This will run the pipeline code defined in `ml/pipeline.py` and should produce model artifacts under `ml/artifacts/` and defines the model metrics in `ml/metadata/`.

## Run tests

Run the test suite with pytest:

```bash
pytest -v
```

There are tests located in `app/tests/` and `ml/tests/`.

## Run maintenance scripts

Two helper scripts are provided:

```bash
bash scripts/train_model.sh
bash scripts/deploy_model.sh
```

Use `train_model.sh` to run a scripted training flow. Use `deploy_model.sh` to copy artifacts to their deployment location.

## Docker

Development (with `docker-compose-dev.yml`):

```bash
docker compose -f docker-compose-dev.yml up --build
```

Production (with `docker-compose.yml`):

```bash
docker compose -f docker-compose.yml up -d --build
```

Adjust the compose files and any environment variables before running in a real environment.

## API documentation

A Postman collection documenting the API endpoints is available in the `documentation/` folder.

## Project layout (high level)

- A Flask app that exposes prediction endpoints (`app/`) — contains routes, schemas, services, and runtime model artifacts.
- ML training pipeline and helpers (`ml/`, `ml/pipeline.py`, `ml/ml_workflow.py`) — training code, workflows, and tests.
- Model artifacts (`ml/artifacts/` and `app/artifacts/`) — trained models and related artifacts used during inference.
- Tests for model, routes, schemas, and services (`app/tests/` and `ml/tests/`).
- Scripts to train and deploy the model (`scripts/`).
- Docker compose files for development and production (`docker-compose-dev.yml`, `docker-compose.yml`).
- Postman collection documenting the API (`documentation/Housing Price Predictor.postman_collection.json`).

## Possible improvements

Listed below are suggested improvements to make the project more robust and production-ready:

1. Model tracking and versioning with MLflow
   - Integrate MLflow (or a similar model registry) to track experiments, parameters, metrics, and artifacts.
   - This enables reproducible training runs and easy model rollbacks.

2. Batch training and datasource abstraction
   - Allow the pipeline to read the training datasource (CSV, database, object store) in configurable batches.
   - This helps training on larger datasets and enables streaming or incremental training strategies.

3. Split repositories for model and application (if models are trained separately)
   - If model training is performed independently (for example, by a data science team), consider splitting the repo into two:
     - `model-repo` for training pipelines, experiments, and model artifacts + CI that runs training and validation.
     - `app-repo` for the Flask service and deployment pipelines that only need to pick up packaged model artifacts.
   - This allows smaller CI runs focused on the relevant changes (faster builds and clearer ownership).
