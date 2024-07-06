target := app
ra := run --no-deps --rm $(target)
dc := docker compose
run := ${dc} ${ra}
exec := ${dc} exec $(target)

up:
	${dc} up --build

upd:
	${dc} up -d

down:
	${dc} down

app-build:
	${dc} build $(target)

app-bundle: upd
	${exec} bundle

app-bash: upd
	${dc} exec $(target) bash

app-console: upd
	${dc} exec $(target) rails c

app-rspec: upd
	${dc} exec $(target) rspec

app-migrate: upd
	${dc} exec $(target) rails db:migrate

app-seed: upd
	${dc} exec $(target) rails db:seed

app-create-db: upd
	${dc} exec $(target) rails db:create