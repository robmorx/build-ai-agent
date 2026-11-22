# Data Model: Remove Skills, Focus Python on Local API

## Overview

Entities for the refactored project state (`specs/001-remove-skills-python-api/`): the Python interactive session and its Local API dependency. The skills component (report-generation) is removed per FR-002 and has no entry in the final data model.

## Entities

### Python Code (Interactive Session)

- **Type**: Entry point — interactive terminal session (CLI)
- **Fields**:
  - `user_query` — string input from the user (the query they type)
  - `model_response` — string output produced by the Local API
- **Validation rules**: a non-empty query is accepted; the response is returned to the user; on Local API unreachability, a clear error message is shown (see contracts/interactive-session.md and quickstart.md)
- **Relationships**: consumes responses from the Local API; supports the research tools defined in `tools.py`
- **State transitions**: none persistent — single-user session flow

### Local API

- **Type**: External endpoint — the user's installed local model
- **Fields**:
  - `host` — the host the local model listens on (local endpoint the user's model is installed on)
  - `port` — the port of the local endpoint
  - `path prefix` — the base path of the model endpoint as used by the Python code
- **Validation rules**: must be reachable when the Python code runs; its response is returned as the model response
- **Relationships**: the Python session is the consumer; a failure surfaces as the user-facing error in the contract

### Skills component (report-generation) — REMOVED

- **Status**: Removed (FR-002). Not part of the final state; no data model is retained for it.

## Relationships

```text
User → [Python Code (Interactive Session)] → Local API (local model) → Model Response → User
```

## Notes

- No persistent storage or database is involved — the session is stateless.
- `requirement.txt` dependencies are unchanged: langchain, ddgs, wikipedia, python-dotenv, pydantic, requests.
