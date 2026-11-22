# Contract: Interactive Session

## Interface

- **Type**: CLI tool (interactive terminal session)
- **Invocation**: `python3 main.py`

## Flow

1. The code prompts the user: `What can I help you research?` and accepts a query string as input.
2. The code sends the query to the Local API (the user's local model).
3. The code returns the model response to the user (printed to standard output).
4. If the Local API is unreachable, the code prints a clear error message that the API is unreachable.

## Error Behavior

- Local API down → user-facing error message stating the API is unreachable (no silent failure, no crash).
- Model-side errors → surfaced as produced by the session.

## Out of Scope

- Skills-related behavior: none — the skills component was removed (FR-002).
