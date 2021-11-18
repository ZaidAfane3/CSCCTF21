#!/bin/bash 

docker rm -f collisions 
docker build -t collisions:latest . 
docker run -d --name collisions  -p 4000:1234 -it collisions:latest