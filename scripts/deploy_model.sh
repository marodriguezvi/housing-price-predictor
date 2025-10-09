#!/bin/bash
# ===============================================
# Model Deployment Script
# Copies the latest trained model from ml/artifacts
# to app/artifacts for application use.
# ===============================================

set -e

PROJECT_DIR="$(pwd)"
MODEL_SOURCE_DIR="$PROJECT_DIR/ml/artifacts"
MODEL_DEST_DIR="$PROJECT_DIR/app/artifacts"

# Verify source directory exists
if [ ! -d "$MODEL_SOURCE_DIR" ]; then
    echo "Model source directory does not exist: $MODEL_SOURCE_DIR"
    exit 1
fi

# Find the latest model by version number
LATEST_MODEL=$(ls "$MODEL_SOURCE_DIR"/model_v*.pkl 2>/dev/null | sort -V | tail -n 1)

if [ -z "$LATEST_MODEL" ]; then
    echo "No model found in $MODEL_SOURCE_DIR"
    exit 1
fi

echo "Latest model found: $(basename "$LATEST_MODEL")"

mkdir -p "$MODEL_DEST_DIR"

cp "$LATEST_MODEL" "$MODEL_DEST_DIR/"
echo "Model copied to $MODEL_DEST_DIR"

# Activate virtual environment if available
# if [ -d "$PROJECT_DIR/venv" ]; then
#     source "$PROJECT_DIR/venv/bin/activate"
# else
#     echo "Virtual environment not found in $PROJECT_DIR/venv"
# fi

# Optional: restart app server if needed
# pkill -f "flask run" || true
# nohup flask --app app run &

# systemctl restart housing_app.service

echo "Deployment completed successfully"
