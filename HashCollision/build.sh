#!/bin/bash 

docker rm -f collisions 
docker build -t collisions:latest . 
docker run -d --name collisions  -p 4000:1234 -it collisions:latest
docker exec -d -it collisions bash -c "/usr/bin/socat TCP-LISTEN:1234,fork,reuseaddr EXEC:/app/hashcol.py"