#!/bin/bash 

docker rm -f rsa 
docker build -t rsa:latest . 
docker run -d --name rsa  -p 10456:1234 -it rsa:latest
docker exec -d -it rsa bash -c "/usr/bin/socat TCP-LISTEN:1234,fork,reuseaddr EXEC:/app/rsa.py"