FROM python:3

RUN apt-get update 
RUN apt-get install socat -y

RUN mkdir -p /app

WORKDIR /app
COPY Challenge .

RUN chmod +x /app/script.sh

EXPOSE 1234