#!/bin/bash
# ===============================================
# Model Deployment Script
# Copies a trained model (.pkl) from ml/artifacts to app/artifacts.
# You can provide a specific filename as an argument,
# or let the script automatically pick the latest version.
# ===============================================

set -euo pipefail

# Directories
PROJECT_DIR="$(pwd)"
MODEL_SOURCE_DIR="$PROJECT_DIR/ml/artifacts"
MODEL_DEST_DIR="$PROJECT_DIR/app/artifacts"

# Help message
show_help() {
    echo "Usage: $(basename "$0") [MODEL_FILENAME]"
    echo
    echo "If MODEL_FILENAME is omitted, the script will copy the latest"
    echo "file matching model_v*.pkl from:"
    echo "  $MODEL_SOURCE_DIR"
    echo "to:"
    echo "  $MODEL_DEST_DIR"
}

# Handle help flag
if [[ "${1-}" =~ ^(-h|--help)$ ]]; then
    show_help
    exit 0
fi

# Validate source directory
if [[ ! -d "$MODEL_SOURCE_DIR" ]]; then
    echo "Source directory not found: $MODEL_SOURCE_DIR"
    exit 1
fi

# Determine which model to copy
if [[ $# -ge 1 ]]; then
    MODEL_NAME="$1"

    if [[ -f "$MODEL_NAME" ]]; then
        SELECTED_MODEL="$MODEL_NAME"
    elif [[ -f "$MODEL_SOURCE_DIR/$MODEL_NAME" ]]; then
        SELECTED_MODEL="$MODEL_SOURCE_DIR/$MODEL_NAME"
    else
        echo "Model file not found: $MODEL_NAME"
        echo "Checked: $MODEL_NAME and $MODEL_SOURCE_DIR/$MODEL_NAME"
        exit 1
    fi
else
    SELECTED_MODEL=$(ls "$MODEL_SOURCE_DIR"/model_v*.pkl 2>/dev/null | sort -V | tail -n 1 || true)
    if [[ -z "$SELECTED_MODEL" ]]; then
        echo "No model found in $MODEL_SOURCE_DIR"
        exit 1
    fi
fi

# Copy the model
echo "Selected model: $(basename "$SELECTED_MODEL")"

mkdir -p "$MODEL_DEST_DIR"
cp "$SELECTED_MODEL" "$MODEL_DEST_DIR/"

echo "Model copied to: $MODEL_DEST_DIR"
echo "Deployment completed successfully!"
