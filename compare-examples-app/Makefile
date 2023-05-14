target := app
ra := run --no-deps --rm $(target)
run := ${dc} ${ra}
dc := docker-compose

upd:
	${dc} up -d

down:
	${dc} down

build:
	${dc} up --build

app-bundle:
	${run} bundle install
	${dc} up --build

app-bash: upd
	${dc} exec $(target) bash

app-console: upd
	${dc} exec $(target) rails c

app-rspec: upd
	${dc} exec $(target) rspec

app-migrate: upd
	${dc} exec $(target) rails db:migrate