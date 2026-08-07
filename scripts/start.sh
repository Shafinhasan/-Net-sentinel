#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
docker compose up --build -d api
echo "NetSentinel: http://localhost:8000"
echo "Swagger docs: http://localhost:8000/docs"
