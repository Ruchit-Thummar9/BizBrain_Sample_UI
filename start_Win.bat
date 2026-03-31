@echo off
REM Launch FastAPI Server (Windows)

cd /d "%~dp0"

if not exist ".venv" (
echo Virtual environment not found. Run setup first:
echo   python setup.py
echo.
pause
exit /b 1
)

echo Starting server on http://127.0.0.1:8080 ...

start http://127.0.0.1:8080

.venv\Scripts\python.exe -m uvicorn server.main:app --host 127.0.0.1 --port 8080

pause
