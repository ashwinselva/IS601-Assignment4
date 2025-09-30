# Simple Calculator (IS601 assignment)

Small teaching project: a tiny interactive calculator implemented in Python with a few unit tests and integration tests.

Contents

- `src/` — application source code (`calculator.py`, `main.py`).
- `tests/` — unit and integration tests (pytest).
- `pyproject.toml` — minimal pytest configuration.

Prerequisites

- Python 3.8+ installed (recommended: 3.10+). Use `python3 --version` to check.
- A POSIX shell (examples below use zsh on macOS).

Quick start (recommended)

1. Open a terminal and change into the project directory:

```bash
cd /path/to/is601-assignment2
```

2. Create and activate a virtual environment (venv):

```bash
python3 -m venv .venv
source .venv/bin/activate
# On Windows (PowerShell): .venv\Scripts\Activate.ps1
```

3. Install test tools (the project itself has no external runtime deps):

```bash
pip install --upgrade pip
pip install pytest
```

Run the program

```bash
python src/main.py
```

Behavior

- The program shows a prompt. Press Enter to run a calculation or type `q` to quit.
- You will be asked for two numbers and then to choose an operation:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide

Example session

```
Simple calculator. Enter calculations or type 'q' at the main prompt to quit.

Press Enter to perform a calculation or type 'q' to quit:
First number: 2
Second number: 3

1. Add
2. Subtract
3. Multiply
4. Divide
Choose operation (1/2/3/4): 1

Result: 2.0 + 3.0 = 5.0
```

Run the test suite

From the project root (virtualenv activated if used):

```bash
pytest -q
```

This project contains both unit tests (for `Calculator`) and integration tests that run the interactive `main.py` using the same Python interpreter.

Project notes / best practices

- Add a `.gitignore` that excludes environment folders (e.g. `.venv/` or `venv/`) and `__pycache__/` before committing.
- Keep tests fast and isolated. The integration tests here use subprocess to exercise the real script; if you need faster runs you can convert them to use `pytest`'s `monkeypatch` to stub `input()`.
- Pin test dependencies in real projects using a `requirements-dev.txt` or use Poetry/Poetry lock files for reproducible environments.

Troubleshooting

- If `python` points to a system Python without `venv` support, use your package manager to install a newer Python, or use pyenv to manage versions.
- If `pytest` reports missing `src` imports, ensure `pythonpath` is configured (this project uses `pyproject.toml` to set `pythonpath = ["src"]`).

Contact / Author

- Student: ashwin (IS601 assignment)
