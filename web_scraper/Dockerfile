FROM python:3.11

RUN apt-get update -qq \
    && apt-get install -y \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    libpq-dev \
    && apt-get clean

RUN pip install --upgrade pip setuptools wheel

WORKDIR /web_scraper

COPY requirements.txt /web_scraper/

RUN pip install -r requirements.txt

COPY . /web_scraper

CMD ["/bin/bash", "-c", "python3 main.py"]
