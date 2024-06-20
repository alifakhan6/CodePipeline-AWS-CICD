#!/bin/bash
set -e

# Stop and remove the running container (if any)
containerID=$(docker ps -q --filter "name=simple-python-flask-app")
if [ -n "$containerID" ]; then
  echo "Stopping and removing container $containerID"
  docker stop "$containerID"
  docker rm "$containerID"
else
  echo "No running container found with the name simple-python-flask-app"
fi


