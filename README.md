# Build AI Agent

This project contains two independent capabilities:

- A GitHub Actions workflow that reviews pull requests and posts its review as a PR comment.
- The interactive Python session that connects to the Local API and returns the local model's responses.

## Local API connection

The Python session (see [main.py](main.py) and [tools.py](tools.py)) connects to the Local API endpoint — the local model installed by the user — and returns the model's responses. When the Local API is not running, the session prints a clear error message that the API is unreachable.

## Pull-request review workflow

The existing GitHub Actions workflow remains at [.github/workflows/ai-review.yml](.github/workflows/ai-review.yml), with its implementation at [.github/scripts/agent_review.py](.github/scripts/agent_review.py). It runs for opened, synchronized, and reopened pull requests. Configure the `AI_BASE_URL` secret with an OpenAI-compatible endpoint (GitHub Models was retired on July 30, 2026) and the repository's Actions permissions and workflow token access as required by that endpoint.

## Dependencies

The Python session's dependencies are listed in [requirement.txt](requirement.txt).

Do not commit `.env` or local virtual environments; these are excluded by [.gitignore](.gitignore).
