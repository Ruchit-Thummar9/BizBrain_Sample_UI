#!/bin/bash

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
echo "Virtual environment not found. Run setup first:"
echo "  python3 run.py"
exit 1
fi

echo "Starting server on http://127.0.0.1:8080 ..."

.venv/bin/python -m uvicorn server.main:app --host 127.0.0.1 --port 8080 &
sleep 2
open http://127.0.0.1:8080
    