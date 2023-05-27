FROM python:3.11
RUN apt-get update -qq
RUN pip install --upgrade pip
WORKDIR /scripts

COPY requirements.txt /scripts/requirements.txt
RUN pip install -r requirements.txt

COPY . /scripts
