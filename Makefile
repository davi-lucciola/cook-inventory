run:
	cd src && uv run flask --app main run --debug

revision:
	cd src && uv run flask --app main db migrate -m "${name}"

migrate:
	cd src && uv run flask --app main db upgrade