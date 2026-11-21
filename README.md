# Build AI Agent

This project contains two independent capabilities:

- A GitHub Actions workflow that reviews pull requests and posts its review as a PR comment.
- A reusable report-generation skill for coding agents.

## Report-generation skill

The skill is in [.github/skills/report-generation/SKILL.md](.github/skills/report-generation/SKILL.md). An agent that supports repository skills can load it when asked to research a topic, synthesize materials, or create a reusable report.

When asked to save a report, the skill supports Markdown (`.md`) and plain text (`.txt`). If no output path is specified, it saves under `reports/`; the default format is Markdown. Reports should cite their sources, distinguish evidence from analysis, and state material limitations.

## Pull-request review workflow

The existing GitHub Actions workflow remains at [.github/workflows/ai-review.yml](.github/workflows/ai-review.yml), with its implementation at [.github/scripts/agent_review.py](.github/scripts/agent_review.py). It runs for opened, synchronized, and reopened pull requests. Configure the `AI_BASE_URL` secret with an OpenAI-compatible endpoint (GitHub Models was retired on July 30, 2026) and the repository's Actions permissions and workflow token access as required by that endpoint.

## Existing research prototype

The original interactive research prototype remains available in [main.py](main.py) and [tools.py](tools.py). Its dependencies are listed in [requirement.txt](requirement.txt).

Do not commit `.env` or local virtual environments; these are excluded by [.gitignore](.gitignore).
