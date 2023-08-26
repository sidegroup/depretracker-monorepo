FROM python:3.11

RUN apt-get update -qq  \
    && apt-get install -y \
    && apt-get clean
RUN pip install --upgrade pip

WORKDIR /web_scraper

COPY requirements.txt /web_scraper
RUN pip install -r requirements.txt

COPY . /web_scraper
