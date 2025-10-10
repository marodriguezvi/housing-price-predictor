#!/bin/bash
# ===============================================
# Training Pipeline Script
# This script activates the virtual environment,
# sets the PYTHONPATH, and runs the ML training
# pipeline defined in ml/pipeline.py.
# ===============================================
set -e

PROJECT_DIR="$(pwd)"

# Usage: ./scripts/train_model.sh [DATA_PATH] [TARGET] [VERSION]
# Examples:
#   ./scripts/train_model.sh                # use defaults
#   ./scripts/train_model.sh data/my.csv PRICE v3

# Activate virtual environment
source "$PROJECT_DIR/venv/bin/activate"

export PYTHONPATH="$PROJECT_DIR"

# Read optional positional args and convert to CLI flags
DATA_PATH_ARG=${1:-}
TARGET_ARG=${2:-}
VERSION_ARG=${3:-}

CMD_ARGS=()
if [ -n "$DATA_PATH_ARG" ]; then
	CMD_ARGS+=("--data-path" "$DATA_PATH_ARG")
fi
if [ -n "$TARGET_ARG" ]; then
	CMD_ARGS+=("--target" "$TARGET_ARG")
fi
if [ -n "$VERSION_ARG" ]; then
	CMD_ARGS+=("--version" "$VERSION_ARG")
fi

python -m ml.pipeline "${CMD_ARGS[@]}"

echo "✅ Pipeline successfully completed from: $PROJECT_DIR"
