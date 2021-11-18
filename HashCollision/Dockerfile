FROM python:3

RUN apt-get update 
RUN apt-get install socat -y

RUN mkdir -p /app

WORKDIR /app
COPY Challenge .

RUN pip install pycrypto

RUN chmod +x /app/hashcol.py

EXPOSE 1234

CMD = ["/usr/bin/socat", "TCP-LISTEN:1234,fork,reuseaddr", "EXEC:/app/hashcol.py"]