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

  SVC_ID=$(grep -A2 "\"$MODEL\"" render-services.json | grep service_id | cut -d'"' -f4)
  IMAGE=$(grep -A3 "\"$MODEL\"" render-services.json | grep image | cut -d'"' -f4)

  echo "  Image: $IMAGE"
  echo "  Service ID: $SVC_ID"

  docker build -t "$IMAGE:$BUILD_NUM" -t "$IMAGE:latest" "models/$MODEL/"
  docker push "$IMAGE:$BUILD_NUM"
  docker push "$IMAGE:latest"

  curl -s -X POST \
    "https://api.render.com/v1/services/$SVC_ID/deploys" \
    -H "Authorization: Bearer $RENDER_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{}"

  echo "  ✅ $MODEL deployed (build #$BUILD_NUM)"
done

echo "=== All done! ==="