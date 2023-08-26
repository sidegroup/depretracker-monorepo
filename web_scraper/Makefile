dc := docker-compose


upd:
	$(dc) up -d

build:
	$(dc) build

web-scraper-bash:
	$(dc) run --rm web_scraper bash

down:
	$(dc) down

run:
	$(dc) run --rm web_scraper python3 main.py