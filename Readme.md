
# FastAPI Server + UI (BizBrain Style)

This project runs a FastAPI with a simple UI.

---

## Project Structure

project/
│
├── setup.py              # Setup file (creates venv + installs dependencies)
├── requirements.txt   # Python dependencies
├── start.bat          # Windows launcher
├── start.sh           # Linux launcher
├── start.command      # macOS launcher
│
├── .venv/             # Virtual environment (auto created)
│
├── server/
│   ├── __init__.py
│   └── main.py        # FastAPI app
│
├── static/
│   ├── index.html
│   ├── compiler.html
│   ├── dag_viewer.html
│   ├── sot_dashboard.html
│   │
├── routers/
│   │   ├── __init__.py
│   │   ├── compiler_router.py
│   │   ├── dag_router.py
│   │   ├── documents_router.py
│   │   ├── spreadsheet_router.py
│   │   └── sot_router.py
---

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
start_W.bat
```

---

###  Linux

```bash
chmod +x start.sh
./start_L.sh
```

---

###  macOS

```bash
chmod +x start.command
```

Then double click:

```bash
start_M.command
```

---

##  Access the App

After starting the server, open:

```
http://127.0.0.1:8000
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
3. Open browser → `http://127.0.0.1:8000`

---

Done.

```

