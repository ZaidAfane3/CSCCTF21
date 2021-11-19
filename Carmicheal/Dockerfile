FROM ubuntu:latest

#Setup enviroment variables
ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezon
ENV DEBIAN_FRONTEND noninteractive 
ENV TERM xterm

#Install Dependecies 
RUN apt -y update && \
apt install -y socat && \ 
apt install -y python3-pip

RUN mkdir -p /app

WORKDIR /app
COPY Challenge .

RUN pip install pycrypto

RUN chmod +x /app/script.sh

EXPOSE 1234