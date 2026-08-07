.PHONY: analyze up down logs test clean

analyze:
	docker compose --profile tools run --rm suricata

up:
	docker compose up --build -d api

down:
	docker compose down

logs:
	docker compose logs -f api

test:
	docker compose run --rm api pytest -q

clean:
	docker compose down
	rm -f data/logs/*.json data/logs/*.log data/logs/*.stats
