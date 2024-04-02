#!/bin/bash

# kill all running containers
sudo docker-compose down --remove-orphans

# rebuild all
sudo docker-compose build

# start all docker services
sudo docker-compose up