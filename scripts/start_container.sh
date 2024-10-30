#!/bin/bash
set -e

# Define the port
HOST_PORT=8000
CONTAINER_PORT=5000
IMAGE_NAME="alifa666/simple-python-flask-app"

# Pull the Docker image from Docker Hub
docker pull $IMAGE_NAME

# Check if a container is already running on the host port
EXISTING_CONTAINER=$(docker ps -q --filter "publish=$HOST_PORT")

if [ -n "$EXISTING_CONTAINER" ]; then
    echo "Stopping existing container using port $HOST_PORT..."
    docker stop $EXISTING_CONTAINER
    echo "Removing existing container..."
    docker rm $EXISTING_CONTAINER
fi

# Run the Docker image as a container
echo "Starting a new container..."
docker run -d -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME
echo "Container started on port $HOST_PORT."
