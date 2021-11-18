#!/bin/bash 

docker rm -f hilo 
docker build -t hilo:latest . 
docker run -d --name hilo  -p 10455:1234 -it hilo:latest
docker exec -d -it hilo bash -c "/usr/bin/socat TCP-LISTEN:1234,fork,reuseaddr EXEC:'/bin/bash /app/script.sh'"