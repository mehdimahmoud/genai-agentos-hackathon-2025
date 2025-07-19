#!/bin/bash
# Safely remove the Docker image built from mcp_servers/google_drive/Dockerfile
set -euo pipefail

IMAGE_NAME="google_drive-google-drive-mcp-server"

get_image_id() {
  docker images --format '{{.Repository}}:{{.Tag}} {{.ID}}' | awk -v name="$IMAGE_NAME" '$1 ~ name {print $2}'
}

main() {
  local image_id
  image_id=$(get_image_id)
  if [[ -n "$image_id" ]]; then
    docker rmi -f "$image_id"
    echo "Image $IMAGE_NAME ($image_id) removed."
  else
    echo "No image found for $IMAGE_NAME."
  fi

  # Double check
  local image_id_check
  image_id_check=$(get_image_id)
  if [[ -z "$image_id_check" ]]; then
    echo "Double check: Image $IMAGE_NAME successfully removed."
  else
    echo "Double check: Image $IMAGE_NAME still exists (ID: $image_id_check). Please check manually."
  fi
}

main 