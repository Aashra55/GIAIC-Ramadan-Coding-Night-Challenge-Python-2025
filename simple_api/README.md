# Simple API

## Overview
This is a simple **FastAPI** project that provides two GET endpoints:

1. **/side_hustles** - Returns a random side hustle idea.
2. **/money_quotes** - Returns a random inspirational quote related to wealth, success, and finance.

To access these endpoints, an **API key** is required.

---

## Features
✅ Random side hustle ideas for entrepreneurs & freelancers.  
✅ Motivational money quotes from famous personalities.  
✅ API key authentication for secure access.  
✅ Built using **FastAPI** for fast and efficient performance.  

---

## Installation & Setup

### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Install UV (If not already installed)
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Initialize the project
uv init simple-api
cd simple-api

### Install Fast API (Dependency)
```sh
uv add fastapi[standard]
```

### Activate UV Virtual Environment
For Windows:
```sh
.venve\Scripts\activate
```
For MacOS/Linux:
```sh
source .venv/bin/activate
```

### Run API
```sh
fastapi dev main.py
```

### Test the API
Paste the following in your browser:
```sh
http://127.0.0.1:8000/side_hustles
http://127.0.0.1:8000/money_quotes
```
or via Swagger UI:
```sh
http://127.0.0.1:8000/docs
```
**API_Key** = "1234567890"

