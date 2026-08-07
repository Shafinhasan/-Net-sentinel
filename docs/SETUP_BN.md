# NetSentinel Part 1 — বাংলা Setup Guide

## ZIP কোথায় বসাবে

তোমার GitHub Desktop দিয়ে clone করা folder:

```text
Documents\GitHub\netsentinel
```

Download করা ZIP extract করলে `netsentinel-part1` নামে folder পাবে।
সেই folder-এর **ভেতরের সব file এবং folder** copy করে এখানে paste করবে:

```text
Documents\GitHub\netsentinel
```

শেষে এমন দেখাবে:

```text
netsentinel/
├── backend/
├── data/
├── docs/
├── rules/
├── scripts/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── LICENSE
├── Makefile
└── README.md
```

`netsentinel-part1` folder-টি `netsentinel`-এর ভিতরে রেখে দেবে না।
তার ভেতরের content copy করবে।

## Run করার সবচেয়ে সহজ পদ্ধতি

1. Docker Desktop চালু করো।
2. `Documents\GitHub\netsentinel` folder খোলো।
3. উপরের address bar-এ `powershell` লিখে Enter দাও।
4. নিচের command একবার করে চালাও:

```powershell
Copy-Item .env.example .env
```

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\analyze.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start.ps1
```

5. Browser-এ খোলো:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

## Expected result

Dashboard-এ এই alert দেখবে:

```text
NETSENTINEL Safe Test HTTP Request
```

## GitHub-এ upload

GitHub Desktop খোলো। Changed files দেখা গেলে Summary-তে লেখো:

```text
feat: build NetSentinel Part 1 IDS foundation
```

তারপর:

1. `Commit to main`
2. `Push origin`

`.env` এবং `data/logs`-এর generated files upload হবে না, কারণ `.gitignore`
সেগুলো block করে।
