# Copilot Instructions for This Repository

## Build, Test, and Lint Commands

### Root (Course Materials)
- **Build:**
  - `npm install && npm run release` (generates all course demos and assets)
- **No root-level test or lint scripts.**

### Python Sample App (`samples/book-app-project/`)
- **Install dependencies:**
  - `pip install -r requirements.txt` (if present) or see `pyproject.toml` for dependencies
- **Run all tests:**
  - `pytest` (from within `samples/book-app-project/`)
- **Run a single test:**
  - `pytest tests/test_books.py::test_add_book`

### JavaScript Sample App (`samples/book-app-project-js/`)
- **Install dependencies:**
  - `npm install` (from within `samples/book-app-project-js/`)
- **Run all tests:**
  - `npm test`
- **Run a single test:**
  - `node --test tests/test_books.js -t "should add a book"`
- **Start app:**
  - `npm start`

## High-Level Architecture
- **This repository is an educational course, not a traditional software project.**
- **Chapters** are organized in directories `00-quick-start/` through `07-putting-it-together/`, each with its own README and hands-on exercises.
- **Primary sample app:** Python CLI book collection app in `samples/book-app-project/` (with JS and C# versions for comparison).
- **Intentional buggy code** for debugging practice is in `samples/book-app-buggy/` and `samples/buggy-code/` (do not fix these bugs).
- **Agent and skill templates** are in `samples/agents/` and `samples/skills/` for extending Copilot CLI.
- **MCP server configuration examples** are in `samples/mcp-configs/`.

## Key Conventions
- **All code examples use Python/pytest context unless otherwise noted.**
- **Do not fix bugs** in intentionally buggy sample directories.
- **When adding new chapters, update the course table in the root README.**
- **Use `samples/book-app-project/` for primary examples and exercises.**
- **Keep explanations beginner-friendly and copy-paste ready.**

## References
- See `README.md` for course overview and structure.
- See `AGENTS.md` for agent/skill conventions and build instructions.
- See `CONTRIBUTING.md` for contribution guidelines.

