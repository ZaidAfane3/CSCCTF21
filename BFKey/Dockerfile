FROM python:3

RUN apt-get update 
RUN apt-get install socat -y

RUN mkdir -p /app

WORKDIR /app
COPY Challenge .

RUN pip install pycrypto

RUN chmod +x /app/main.py

EXPOSE 1234