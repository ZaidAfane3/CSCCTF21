#!/bin/bash 

docker rm -f carmicheal 
docker build -t carmicheal:latest . 
docker run -d --name carmicheal  -p 10453:1234 -it carmicheal:latest
docker exec -d -it carmicheal bash -c "/usr/bin/socat TCP-LISTEN:1234,fork,reuseaddr EXEC:'/bin/bash /app/script.sh'"