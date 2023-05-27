dc := docker-compose

scripts-bash:
	$(dc) run --rm scripts bash

scripts-translate-csv:
	$(dc) run --rm scripts python3 translate_csv.py $(FILE) $(COLUMN) $(LANG)