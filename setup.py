"""
setup.py — One-click setup for FastAPI + UI project

Usage:
    python setup.py
"""

import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_PATH = ROOT / ".venv"
REQUIREMENTS = ROOT / "requirements.txt"


def get_python():
    if sys.platform == "win32":
        return VENV_PATH / "Scripts" / "python.exe"
    return VENV_PATH / "bin" / "python"


def run(cmd):
    print(f"> {' '.join(str(c) for c in cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Error occurred. Stopping setup.")
        sys.exit(1)



def main():
    print("===== Project Setup Started =====\n")

    # 1. Create virtual environment
    if not VENV_PATH.exists():
        print("Creating virtual environment...")
        venv.create(VENV_PATH, with_pip=True)
    else:
        print("Virtual environment already exists.")

    py = get_python()

    # 2. Install requirements
    print("\nInstalling dependencies...")
    run([str(py), "-m", "pip", "install", "-r", str(REQUIREMENTS)])

    print("\nSetup completed successfully.\n")

    # 3. Run server option
    print("To start server run:")
    if sys.platform == "win32":
        print("  .venv\\Scripts\\python.exe -m uvicorn server.main:app --reload")
    else:
        print("  .venv/bin/python -m uvicorn server.main:app --reload")



if __name__ == "__main__":
    main()