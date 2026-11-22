---

description: "Task list template for feature implementation"
---

# Tasks: Remove Skills, Focus Python on Local API

**Input**: Design documents from `specs/001-remove-skills-python-api/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested in the specification - no test tasks are included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 [P] Verify project structure per plan.md: `main.py`, `tools.py`, `requirement.txt` at repository root (structure decision: flat layout)
- [X] T002 [P] Create/refresh the Python virtual environment and install dependencies from `requirement.txt` (langchain, ddgs, wikipedia, python-dotenv, pydantic, requests)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 [P] Smoke-test the Python session against the Local API: run `python3 main.py` and confirm it starts and connects to the Local API (precondition before user story work begins)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Python code works against the local API (Priority: P1) 🎯 MVP

**Goal**: Users run the Python session connected to the Local API and get a response from the local model

**Independent Test**: With the Local API running, run `python3 main.py`, submit a query, and confirm the code returns a response from the local model (SC-001, US1 acceptance scenario 1)

### Implementation for User Story 1

- [X] T004 [US1] Ensure the Python session connects to the Local API and returns its responses: run `python3 main.py`; the session connects to the Local API (local model) and the user receives the model response (FR-001; contracts/interactive-session.md; US1 scenario 1)
- [X] T005 [US1] Add the unreachable-API error path in `main.py`: when the Local API is not running, the user gets a clear error message (US1 scenario 2; contracts/interactive-session.md)

**Checkpoint**: User Story 1 is fully functional and independently testable: run `python3 main.py` and confirm a local-model response with the Local API up, and the error message with it down

---

## Phase 4: User Story 2 - No skills remain in the project (Priority: P2)

**Goal**: Users find no skills-related components or documentation; the project focuses on the Python code

**Independent Test**: Search the project for skills-related components and documentation; none exist (US2 acceptance scenario 1)

### Implementation for User Story 2

- [X] T006 [P] [US2] Remove the report-generation skills component: delete `.github/skills/report-generation/` so no skills components remain (FR-002, SC-002)
- [X] T007 [P] [US2] Update the README: remove the "Report-generation skill" sections; the documentation focuses on the Python code and the Local API connection (FR-003, SC-002; README.md)
- [X] T008 [US2] Verify no skills-related mentions remain in the project: search project files for skills-related components/documentation; none should exist (US2 scenario 1)

**Checkpoint**: No skills-related components or documentation remain in the project

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T009 Run quickstart.md validation: with the Local API running, run `python3 main.py` and confirm the response from the local model (quickstart scenario 1); then stop the Local API and confirm the clear unreachable-API error (quickstart scenario 2)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Independent of User Story 1 (T008 verifies after T006/T007)

### Within Each User Story

- Story complete before moving to next priority
- Commit after each task or logical group

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T001, T002)
- All Foundational tasks marked [P] can run in parallel (within Phase 2) (T003)
- [P] tasks: T001, T002, T003, T006, T007 - different files, no dependencies

### Parallel Example: User Story 1

```bash
# Sequential within the same file (main.py):
Task: "Ensure the Python session connects to the Local API (T004)"
Task: "Add the unreachable-API error path in main.py (T005)"
```

---

### Parallel Example: User Story 2

```bash
# Launch tasks for User Story 2 together (different files):
Task: "Remove the report-generation skills component: delete `.github/skills/report-generation/` (T006)"
Task: "Update the README: remove the skills sections (README.md) (T007)"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: run `python3 main.py` against the Local API and confirm a local-model response
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Validate (MVP)
3. Add User Story 2 → Test independently → Validate
4. Run quickstart.md validation (Polish - Phase 5)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify the smoke test in Foundational passes before starting user stories
- Tests are OPTIONAL - no test tasks were included since the specification did not request them
- T009 runs the quickstart validation end-to-end (quickstart.md scenarios 1 and 2)
