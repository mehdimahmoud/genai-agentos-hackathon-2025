#!/bin/bash

# Remove the latest Docker image for the text-analysis-agent service
echo "Looking for image: a2a-server-text-analysis-agent:latest"
IMAGE_ID=$(docker images --format '{{.Repository}}:{{.Tag}} {{.ID}}' | grep '^a2a-server-text-analysis-agent:latest' | awk '{print $2}')

if [ -z "$IMAGE_ID" ]; then
  echo "No image found for a2a-server-text-analysis-agent:latest."
  exit 0
fi

echo "Removing image ID: $IMAGE_ID"
docker rmi -f "$IMAGE_ID" 