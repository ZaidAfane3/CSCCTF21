#!/bin/bash 

docker rm -f sonic 
docker build -t sonic:latest . 
docker run -d --name sonic  -p 10457:1234 -it sonic:latest
docker exec -d -it sonic bash -c "/usr/bin/socat TCP-LISTEN:1234,fork,reuseaddr EXEC:'/bin/bash /app/script.sh'"