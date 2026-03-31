
# FastAPI Server + UI 

This project runs a FastAPI with a simple UI.

---

## 📁 Project Structure

```
project/
│
├── setup.py                 # Sets up project (creates venv + installs dependencies)
├── requirements.txt         # List of Python dependencies
│
├── start_Win.bat                 # Run project on Windows
├── start_Linux.sh                # Run project on Linux
├── start_Mac.command             # Run project on macOS
│
├── server/                 
│   ├── __init__.py
│   └── main.py             # FastAPI entry point
│
├── routers/                # API route modules
│   ├── __init__.py
│   ├── compiler_router.py
│   ├── dag_router.py
│   ├── documents_router.py
│   ├── spreadsheet_router.py
│   └── sot_router.py
│
├── static/                 # Frontend (UI pages)
│   ├── index.html
│   ├── compiler.html
│   ├── dag_viewer.html
│   └── sot_dashboard.html
│
└── .venv/                  # Virtual environment (auto-created)
```



## Setup (First Time Only)

Run this once to install everything:

### Windows / Linux / macOS

```bash
python setup.py
````

---

## Run the Server

### Windows

Double click:

```bash
start_Win.bat
```

---

###  Linux

```bash
chmod +x start.sh
./start_Linux.sh
```

---

###  macOS

```bash
chmod +x start.command
```

Then double click:

```bash
start_Mac.command
```

---

##  Access the App

After starting the server, open:

```
http://127.0.0.1:8080
```

---

## Notes

* `.venv` is created automatically by `setup.py`
* Do NOT delete `.venv` after setup
* If `.venv` is missing, run setup again:

```bash
python setup.py
```

---

## Tech Used

* FastAPI
* Uvicorn
* Pydantic
* HTML / CSS / JavaScript

---

## Summary

1. Run setup → `python setup.py`
2. Start server → `double click start_W.py file`
3. Open browser → `http://127.0.0.1:8080`


