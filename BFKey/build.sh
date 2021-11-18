#!/bin/bash 

docker rm -f bfkey 
docker build -t bfkey:latest . 
docker run -d --name bfkey  -p 10452:1234 -it bfkey:latest
docker exec -d -it bfkey bash -c "/usr/bin/socat TCP-LISTEN:1234,fork,reuseaddr EXEC:'/bin/bash /app/script.sh'"