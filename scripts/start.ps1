$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

docker compose up --build -d api
Write-Host "NetSentinel is starting at http://localhost:8000" -ForegroundColor Green
Write-Host "Swagger API docs: http://localhost:8000/docs" -ForegroundColor Green
