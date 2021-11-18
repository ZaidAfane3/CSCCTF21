#!/bin/bash 

docker rm -f odds 
docker build -t odds:latest . 
docker run -d --name odds  -p 10454:1234 -it odds:latest
docker exec -d -it odds bash -c "/usr/bin/socat TCP-LISTEN:1234,fork,reuseaddr EXEC:'/bin/bash /app/script.sh'"