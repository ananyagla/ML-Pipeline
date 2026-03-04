#!/bin/bash
set -e

RENDER_API_KEY=$1
BUILD_NUM=$2

echo "=== Detecting changed models ==="
CHANGED=$(git diff --name-only HEAD~1 HEAD | grep '^models/' | cut -d/ -f2 | sort -u)

if [ -z "$CHANGED" ]; then
  echo "No model changes detected. Skipping deploy."
  exit 0
fi

echo "Changed models: $CHANGED"

for MODEL in $CHANGED; do
  echo ""
  echo ">>> Processing model: $MODEL"

  # Read config from render-services.json
  SVC_ID=$(python3 -c "import json; d=json.load(open('render-services.json')); print(d['$MODEL']['service_id'])")
  IMAGE=$(python3 -c "import json; d=json.load(open('render-services.json')); print(d['$MODEL']['image'])")

  echo "  Image: $IMAGE"
  echo "  Service ID: $SVC_ID"

  # Build Docker image
  echo "  Building Docker image..."
  docker build -t "$IMAGE:$BUILD_NUM" -t "$IMAGE:latest" "models/$MODEL/"

  # Push to DockerHub
  echo "  Pushing to DockerHub..."
  docker push "$IMAGE:$BUILD_NUM"
  docker push "$IMAGE:latest"

  # Trigger Render deploy
  echo "  Triggering Render deploy..."
  curl -s -X POST \
    "https://api.render.com/v1/services/$SVC_ID/deploys" \
    -H "Authorization: Bearer $RENDER_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{}"

  echo "   $MODEL deployed successfully (build #$BUILD_NUM)"
done

echo ""
echo "=== All done! ==="