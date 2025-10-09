#!/bin/bash
# ===============================================
# Training Pipeline Script
# This script activates the virtual environment,
# sets the PYTHONPATH, and runs the ML training
# pipeline defined in ml/pipeline.py.
# ===============================================
set -e

PROJECT_DIR="$(pwd)"

# Activate virtual environment
source "$PROJECT_DIR/venv/bin/activate"

export PYTHONPATH="$PROJECT_DIR"

python -m ml.pipeline

echo "✅ Pipeline successfully completed from: $PROJECT_DIR"
