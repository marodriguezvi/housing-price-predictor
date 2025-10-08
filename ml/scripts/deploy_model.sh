#!/bin/bash
set -e

# Paths
MODEL_DIR="artifacts/models"
APP_ENV_FILE=".env"
APP_MODEL_PATH="app/models/current_model.pkl"

# Get latest model by modification date
LATEST_MODEL=$(ls -t $MODEL_DIR/model_*.pkl | head -n 1)

echo "🚀 Deploying latest model: $LATEST_MODEL"

# Copy latest model to app models directory
cp "$LATEST_MODEL" "$APP_MODEL_PATH"

# Extract version number from filename
MODEL_VERSION=$(basename "$LATEST_MODEL" | sed 's/model_\(.*\)\.pkl/\1/')

# Update environment variable in .env file
if grep -q "^MODEL_VERSION=" "$APP_ENV_FILE"; then
    sed -i "s/^MODEL_VERSION=.*/MODEL_VERSION=$MODEL_VERSION/" "$APP_ENV_FILE"
else
    echo "MODEL_VERSION=$MODEL_VERSION" >> "$APP_ENV_FILE"
fi

echo "✅ Model version updated to: $MODEL_VERSION"

# Restart app service (assuming using gunicorn or flask in background)
if pgrep -f "gunicorn" > /dev/null; then
    echo "🔁 Restarting Gunicorn..."
    pkill -HUP -f "gunicorn"
elif pgrep -f "flask run" > /dev/null; then
    echo "🔁 Restarting Flask app..."
    pkill -f "flask run"
    nohup flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &
else
    echo "⚠️ No running app detected — skipping restart."
fi

echo "✅ Deployment completed successfully!"
