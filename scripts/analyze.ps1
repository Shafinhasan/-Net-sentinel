$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

Write-Host "Cleaning previous Suricata output..." -ForegroundColor Cyan
Get-ChildItem ".\data\logs" -File |
    Where-Object { $_.Name -ne ".gitkeep" } |
    Remove-Item -Force

Write-Host "Analyzing the safe sample PCAP..." -ForegroundColor Cyan
docker compose --profile tools run --rm suricata

if (Test-Path ".\data\logs\eve.json") {
    Write-Host "Success: data\logs\eve.json was created." -ForegroundColor Green
} else {
    throw "Suricata finished but eve.json was not created."
}
