# Feature Specification: Remove Skills, Focus Python on Local API

**Feature Branch**: `001-remove-skills-python-api`

**Created**: 2026-11-22

**Status**: Draft

**Input**: User description: "i want to refactor this project removing all about skills in the master branch and focus on the python code to work when you connect it to the local api which is a local model i've installed"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Python code works against the local API (Priority: P1)

A user runs the project's Python code connected to their local API (the local model they installed) and receives a response from the local model for their query.

**Why this priority**: The Python code is the project's user-facing path; connecting it to the local model gives the user a working tool.

**Independent Test**: With the local API running, run the Python code and submit a query; confirm that a response from the local model is returned.

**Acceptance Scenarios**:

1. **Given** the local API is running and reachable, **When** the user runs the Python code and submits a query, **Then** the code returns a response from the local model.
2. **Given** the local API is not running, **When** the user runs the Python code, **Then** the user sees a clear error that the API is unreachable.

### User Story 2 - No skills remain in the project (Priority: P2)

A user looking at or interacting with the project finds no skills-related components or documentation; the project focuses on the Python code.

**Why this priority**: The user asked to remove all skills-related things; a focused, skills-free project matches the ask.

**Independent Test**: Search the project for skills-related components and documentation; none exist.

**Acceptance Scenarios**:

1. **Given** the project files and documentation, **When** a user searches for skills-related content, **Then** no skills components or documentation sections exist.

### Edge Cases

- What happens when the user asks for a report or skills-like output? The Python code path handles it; no skills component remains.
- What happens when the local API is not running when the user runs the Python code? The user gets a clear message that the API is unreachable.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST accept a user query when run against the local API and return a response produced by the local model.
- **FR-002**: The project MUST contain no skills-related components or documentation after the refactor; skills-related files are removed.
- **FR-003**: The project documentation MUST focus on the Python code and the local API connection, with no skills-related mentions.

### Key Entities *(include if feature involves data)*

- **Python code**: The project's interactive session — user query in, local-model response out — plus its supporting research tools.
- **Local API**: The user's installed local model endpoint; the Python code connects to it and returns its responses.
- **Skills component (report-generation)**: The skills-related component removed by this refactor.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: When the local API is running and reachable, running the Python code and submitting a query returns a response from the local model.
- **SC-002**: The project documentation and code contain no skills-related functionality or descriptions; the skills component is fully removed.

## Assumptions

- The refactor targets the master branch (the user's branch).
- "All about skills" refers to the skills component (the reusable report-generation skills component and its documentation); other project capabilities are out of scope for this refactor.
- The Python code is the user-facing path to focus on; the local API is the user's installed local model endpoint, available in the user's environment when they run the code.
- When the user asks for a report or similar output, the Python code path is the handling path (no skills component remains).
- The rest of the project (e.g., the GitHub Actions PR review workflow) is not part of this refactor.
