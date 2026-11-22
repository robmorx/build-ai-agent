# Research: Remove Skills, Focus Python on Local API

**Date**: 2026-11-22

## Context

Refactor target: `specs/001-remove-skills-python-api/spec.md`.

- Remove the reusable report-generation skills component (`.github/skills/report-generation/` and the README sections describing it).
- Keep the Python code as the user-facing path — the user requested "keep using python".
- The Python session works against the user's local API (local model installed by the user).

## Research Tasks

No NEEDS CLARIFICATION items remained in the Technical Context (see plan.md) — no unknowns were dispatched to research agents. Findings below come from the spec, the project files, and this analysis.

## Findings and Decisions

### Decision: Language — Python 3.14.10

- **Decision**: Python remains the implementation language (user request: "keep using python"); the project's Python is 3.14.10.
- **Rationale**: The user explicitly asked to keep using Python; the spec's Assumptions designate the Python code as the user-facing path.
- **Alternatives considered**: Switching to another language for new code — rejected per the user's request.

### Decision: Dependencies — reuse `requirement.txt`

- **Decision**: Keep the existing dependencies (langchain, ddgs, wikipedia, python-dotenv, pydantic, requests); no changes.
- **Rationale**: None of them are skills components (the skills component was a Markdown doc); the Python session path uses the same stack.
- **Alternatives considered**: Replacing or pruning dependencies — rejected; nothing needs removal.

### Decision: Integration — the user's Local API (local model)

- **Decision**: The Python code connects to the user's local API endpoint (the local model they installed) and returns its responses.
- **Rationale**: The spec requires the Python code to work when connected to the local API; the user's installed local model is the integration target.
- **Alternatives considered**: Bundling a different model or endpoint — rejected; the user's local model is the target.

### Decision: Testing — end-to-end against the local API

- **Decision**: Validate by running `python3 main.py` with the local API running and confirming the local-model response (SC-001).
- **Rationale**: The spec's measurable outcome is a returned local-model response.
- **Alternatives considered**: Unit-level or static checks — deferred to the `/speckit.tasks` phase; not part of this plan.

### Decision: No new components or storage

- **Decision**: No new storage or components; the session stays stateless (spec assumption: the rest of the project is out of scope).
- **Rationale**: The refactor scope is skills removal + the Python/local-API focus.
- **Alternatives considered**: Adding persistence or other components — rejected; not requested.
