#!/bin/bash

# Тег образа, который вы хотите запустить
IMAGE="kirillermolaev/test_geno:latest"

# Порт на котором будет работать контейнер (например, 8080 на хосте)
HOST_PORT=8080
CONTAINER_PORT=80

# Скачиваем образ (если его нет локально)
docker pull $IMAGE

# Запускаем контейнер с пробросом портов
docker run -d -p $HOST_PORT:$CONTAINER_PORT $IMAGE
