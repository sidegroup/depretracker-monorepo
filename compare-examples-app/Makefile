target := app
ra := run --no-deps --rm $(target)
dc := docker compose
run := ${dc} ${ra}
exec := ${dc} exec $(target)

upd:
	${dc} up -d

down:
	${dc} down

build:
	${dc} up --build

app-bundle: upd
	${exec}

app-bash: upd
	${dc} exec $(target) bash

app-console: upd
	${dc} exec $(target) rails c

app-rspec: upd
	${dc} exec $(target) rspec

app-migrate: upd
	${dc} exec $(target) rails db:migrate