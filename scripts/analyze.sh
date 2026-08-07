#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."

find ./data/logs -maxdepth 1 -type f ! -name '.gitkeep' -delete
docker compose --profile tools run --rm suricata
test -f ./data/logs/eve.json
echo "Success: data/logs/eve.json was created."
