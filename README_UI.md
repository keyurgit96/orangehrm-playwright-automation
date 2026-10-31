# Test Automation Framework Specification

A modular test automation architecture designed for web applications, implemented for OrangeHRM using **Python**, **Playwright**, and **Pytest**. Built with strict separation of concerns, persistent session state management, and trace-based observability.

---

## 1. System Overview & Tech Stack

| Component | Specification |
| :--- | :--- |
| **Language & Runtime** | Python 3.10+ |
| **Automation Engine** | Playwright for Python (`sync_api`) |
| **Test Runner & Harness** | Pytest (`pytest-playwright`, `pytest-order`, `pytest-html`) |
| **Design Pattern** | Page Object Model (POM) + Fixture Dependency Injection |
| **State Management** | Playwright Browser Context `storage_state` (JSON-serialized sessions) |
| **Observability** | Playwright Tracing API (DOM snapshots, network traffic, action logs) |
| **CI / Containerization**| Docker (`mcr.microsoft.com/playwright/python:v1.40.0-focal`), Jenkins Pipeline |

---

## 2. Directory Structure

```text
orangehrm-playwright-automation/
├── src/
│   ├── pages/                       # Page Object Model layer
│   │   ├── basePage.py              # Base page encapsulation & common actions
│   │   ├── authentication.py        # Login page object & credential actions
│   │   ├── recruitment.py           # Recruitment candidate & vacancy workflows
│   │   ├── timesheet.py             # Attendance marking & records
│   │   └── userInfo.py              # User profile & top navigation menu
│   └── utils/
│       └── helpers.py               # Runtime utilities: selectEnv, Playwright trace logger
├── tests/
│   ├── conftest.py                  # Pytest fixtures (browser setup, session storage contexts)
│   └── ui/                          # End-to-End functional test suites
│       ├── test_loginTest.py        # Parametrized authentication & session generator
│       └── test_editUserInfo.py     # Authenticated dashboard tests with tracing
├── test_data/
│   ├── auth.json                    # Serialized session state (bypasses UI login)
│   ├── authCustom.json              # Secondary environment session state
│   ├── data.json                    # Test data vectors (credentials, URLs)
│   └── data_custom.json             # Alternative environment test datasets
├── reports/                         # Test execution artifacts (HTML test reports)
├── logs/                            # Binary trace archives (*.zip) for post-mortem triage
├── Dockerfile                       # Jenkins agent container specification
├── jenkinsFile                      # Declarative CI pipeline (Docker agent + parallel runs)
├── pytest.ini                       # Test discovery rules, custom markers, and path resolution
└── requirements.txt                 # Pinned project dependencies
```

---

## 3. Core Architectural Patterns

### 3.1 Page Object Model (POM)
- UI locators and DOM interactions are isolated within `src/pages/`.
- Test scripts consume business-level page methods rather than interacting with raw Playwright locator selectors directly.
- Common interaction logic inherits from `basePage`.

### 3.2 Session State Caching (`storage_state`)
- Eliminates redundant UI authentication across test cases.
- The `test_loginCorrect` test generates and serializes authenticated cookies and local storage tokens into `test_data/auth.json`.
- The `authenticated_page` fixture spins up a new browser context initialized with this `storage_state`, allowing tests to start directly from internal authenticated dashboards.

### 3.3 Tracing & Observability
- Integrated via `logger` in `src/utils/helpers.py`.
- Captures screencasts, DOM snapshots, network activity, and console logs.
- Stores execution zip files in `logs/` for offline inspection via the Playwright Trace Viewer without re-running failed tests.

### 3.4 Multi-Environment Configuration
- Environment-specific properties and credentials handled by `selectEnv` using `python-dotenv`.
- Dynamic loading supports standard `.env` and `.custom.env` profiles.

---

## 4. Test Execution Runbook

### Environment Setup

```bash
# Initialize virtual environment
python -m venv venv
source venv/bin/activate       # Windows: .\venv\Scripts\activate

# Install dependencies and browser binaries
pip install -r requirements.txt
playwright install chromium
```

### Running Test Suites

```bash
# Execute entire test suite
pytest

# Run data-driven login validation tests
pytest -m genericTest

# Generate / update authenticated session state (auth.json)
pytest -m correctCredentials

# Run authenticated dashboard tests (bypasses login page)
pytest -m editUserInfo

# Generate self-contained HTML execution report
pytest --html=reports/runReport.html --self-contained-html
```

### Diagnostic Triage (Trace Viewer)

```bash
# Inspect recorded DOM snapshots, network requests, and execution timeline
playwright show-trace logs/<trace_filename>.zip
```

---

## 5. CI/CD Integration

The framework includes a declarative Jenkins pipeline (`jenkinsFile`):
- **Agent Container:** Runs within Microsoft's official Playwright Docker image (`mcr.microsoft.com/playwright/python:v1.40.0-focal`).
- **Headless Display:** Uses `xvfb-run` for headless browser execution in Linux container environments.
- **Parallel Stages:** Supports parallel test runs segmented by test markers.
- **Post-Build Automation:** Dispatches status notifications upon pipeline completion.
