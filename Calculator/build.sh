#!/bin/bash 

docker rm -f calculator 
docker build -t calculator:latest . 
docker run -d --name calculator  -p 10451:1234 -it calculator:latest
docker exec -d -it calculator bash -c "/usr/bin/socat TCP-LISTEN:1234,fork,reuseaddr EXEC:'/bin/bash /app/script.sh'"