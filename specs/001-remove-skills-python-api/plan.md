# Implementation Plan: Remove Skills, Focus Python on Local API

**Branch**: `001-remove-skills-python-api` | **Date**: 2026-11-22 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/001-remove-skills-python-api/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command; its definition describes the execution workflow.

## Summary

Refactor of the project: the reusable report-generation skills component (`.github/skills/report-generation/` and the README sections describing it) is removed, and the Python code becomes the single user-facing path — the interactive Python session works against the user's local API (the local model they installed), returning the local model's responses to user queries (SC-001) and printing a clear error when the API is unreachable (SC-002, Edge Cases).

## Technical Context

**Language/Version**: Python 3.14.10 — user request: "keep using python"; the existing code uses Python type hints.

**Primary Dependencies**: langchain, ddgs, wikipedia, python-dotenv, pydantic, requests (requirement.txt). None are related to the skills component; none are needed by the Python path, so no new dependencies are introduced.

**Storage**: N/A — the Python session is stateless; no persistent storage involved.

**Testing**: End-to-end against the local API — run `python3 main.py` with the local API running and confirm the local model response (SC-001). The unreachable-API path is covered by the error behavior documented in the contract and quickstart.

**Target Platform**: Local machine / terminal (interactive session).

**Project Type**: cli

**Performance Goals**: None specified — the local model response time is the observed bound for this single-user interactive session (per spec assumptions).

**Constraints**: The user asked to keep using Python; the refactor targets the master branch (spec assumption).

**Scale/Scope**: Single-user interactive session; the refactor scope is limited to skills removal and the Python/local-API focus (out of scope per spec: the rest of the project, e.g., the GitHub Actions PR review workflow).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The project constitution (`.specify/memory/constitution.md`) currently contains only unfilled template placeholders — no substantive principles, governance rules, or version are defined. The standard gates therefore pass:

- ERROR: Plan violates any constitution principle — none exist.
- ERROR: Complexity tracking — no violations requiring justification.
- ERROR: Unresolved NEEDS CLARIFICATION in Technical Context — none (all filled above).

All gates pass. When the constitution is completed, this section must be re-evaluated against the final plan.

## Project Structure

### Documentation (this feature)

```text
specs/001-remove-skills-python-api/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
│   └── interactive-session.md
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

The project keeps its flat root layout — the Python code is the user-facing path; the skills component is removed:

```text
main.py                # Interactive research session entry point (Python)
tools.py               # Research tools used by the session (Python)
requirement.txt        # Dependencies for the Python code
README.md              # Project documentation (updated: no skills sections)

# Removed by the refactor (FR-002):
.github/skills/report-generation/
```

**Structure Decision**: Keep the existing flat, Python-based layout. No new packages or directories are introduced; the interactive CLI session remains the user-facing surface, and the Local API remains the external dependency.
