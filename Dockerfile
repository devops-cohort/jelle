FROM ubuntu:16.04

WORKDIR /app

RUN apt-get update -y && apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "/usr/bin/python3", "app.py" ] 
