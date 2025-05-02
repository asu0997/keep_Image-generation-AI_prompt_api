#!/bin/bash

MYSQL_CONTAINER_NAME="mysql-container"
FASTAPI_CONTAINER_NAME="fastapi-container"

# MySQL コンテナが存在するか
MYSQL_EXISTS=$(docker ps -a -q -f name=$MYSQL_CONTAINER_NAME)

# FastAPI コンテナが存在するか
FASTAPI_EXISTS=$(docker ps -a -q -f name=$FASTAPI_CONTAINER_NAME)

if [ "$MYSQL_EXISTS" ] && [ "$FASTAPI_EXISTS" ]; then
    echo "Starting existing containers..."
    docker start $MYSQL_CONTAINER_NAME
    docker start $FASTAPI_CONTAINER_NAME
else
    echo "Creating and starting containers with docker-compose..."
    docker-compose up -d
fi
