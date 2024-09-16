#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <username> <password>"
    exit 1
fi

# Assign the arguments to variables
DOCKER_USERNAME=$1
DOCKER_PASSWORD=$2

# Login to Docker Hub
echo "Logging in to Docker Hub..."
echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin

if [ $? -eq 0 ]; then
    echo "Login successful!"
    # build and push docker image
    docker build -t $DOCKER_USERNAME/custom_workload .
    if [ $? -ne 0 ]; then
        echo "Docker build failed."
        exit 1
    fi
    echo "Push Docker image"
    docker push $DOCKER_USERNAME/custom_workload:latest
else
    echo "Login failed. Please check your credentials."
    exit 1
fi
