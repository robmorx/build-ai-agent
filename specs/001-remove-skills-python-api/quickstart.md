# Quickstart: Validate the Python-Local-API Flow

## Prerequisites

- Python installed (the project uses Python — user request: "keep using python"); the repo provides a `.venv` (Python 3.14.10) and `requirement.txt`
- Python dependencies: `pip install -r requirement.txt` (or use the existing `.venv`)
- A local API running and reachable — the local model the user installed

## Scenario 1 — Happy path: the Python code returns a local-model response

1. Start the local API and confirm it is reachable.
2. Run `python3 main.py`.
3. When prompted (`What can I help you research?`), submit a query (e.g., `What is the capital of France?`).
4. **Expected**: the code returns a response produced by the local model.

## Scenario 2 — Local API unreachable

1. Stop the local API.
2. Run `python3 main.py` and submit a query.
3. **Expected**: the code prints a clear error that the API is unreachable.

## Scenario 3 — No skills remain

1. Search the project for skills-related components and documentation.
2. **Expected**: none exist (spec FR-002 / SC-002).
