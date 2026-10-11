# 🚀 OrangeHRM Playwright Test Automation Framework

An enterprise-ready UI automation framework demonstrating clean architecture, session reuse, and observability using **Python + Playwright + Pytest**.

---

### 🌟 Key Engineering Highlights

- **Page Object Model (POM):** Strict separation of locators and actions under [`src/pages/`](src/pages/) (`basePage`, `loginDetails`, `recruitmentDetails`, `attendanceDetails`, `userInfo`).
- **Session Authentication Reuse (`auth.json`):** Saves storage state on login; subsequent tests run via `authenticated_page` fixture without UI login overhead — significantly boosting test speed and stability.
- **Data-Driven Testing (DDT):** Test cases consume external JSON payloads ([`test_data/data.json`](test_data/data.json)) with `@pytest.mark.parametrize` for positive/negative validation.
- **Playwright Tracing & Observability:** Custom `logger` (`src/utils/helpers.py`) records actions, DOM snapshots, network calls, and screenshots into `logs/*.zip` for instant failure triage.
- **Multi-Environment Support:** Dynamic loader (`selectEnv`) toggling between default `.env` and `.custom.env`.

---

### ⚡ Quick Start (Setup in 1 Minute)

```bash
# 1. Clone & activate virtual environment
git clone https://github.com/keyurgit96/orangehrm-playwright-automation.git
cd orangehrm-playwright-automation
python -m venv venv
.\venv\Scripts\activate       # On Linux/macOS: source venv/bin/activate

# 2. Install dependencies & browsers
pip install -r requirements.txt
playwright install
```

---

### 🧪 Running Tests

```bash
# Run all tests
pytest

# Run data-driven login tests
pytest -m genericTest

# Generate / update session auth state (auth.json)
pytest -m correctCredentials

# Run authenticated dashboard tests (bypasses login form)
pytest -m editUserInfo
```

---

### 🔍 Debugging with Playwright Trace Viewer

Open interactive execution timelines, screenshots, and console logs from any test run:

```bash
playwright show-trace logs/<trace_file>.zip
```

---

### 💼 Technical Competencies

`Python 3.10+` • `Playwright` • `Pytest` • `Page Object Model` • `Session State Caching` • `Data-Driven Testing` • `Trace Viewer Debugging` • `Cross-Browser Testing`

---

### 📁 Project Structure

```text
orangehrm-playwright-automation/
├── src/
│   ├── api/                     # 🌐 [API] Service Object Model (Endpoint clients)
│   │   ├── __init__.py
│   │   ├── base_api.py          # Base Playwright APIRequestContext wrapper
│   │   ├── recruitment_api.py   # Recruitment API service
│   │   ├── timesheet_api.py     # Timesheet API service
│   │   └── user_api.py          # User management API service
│   ├── pages/                   # 🖥️ [UI] Page Object Model (Locators & user actions)
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── authentication.py
│   │   ├── recruitment.py
│   │   ├── timesheet.py
│   │   └── user_info.py
│   ├── config/                  # ⚙️ [Shared] Settings & Route Constants
│   │   ├── settings.py          # Base URLs, timeouts, environment variables
│   │   └── endpoints.py         # API route endpoints
│   └── utils/                   # 🛠️ [Shared] Helpers & Utilities
│       ├── __init__.py
│       ├── helpers.py           # Logger, env loader (selectEnv)
│       └── schema_validator.py  # JSON schema validator for API responses
├── tests/
│   ├── conftest.py              # Global Pytest fixtures & session setup
│   ├── ui/                      # 🖥️ [UI] Functional UI Test Suites
│   │   ├── test_auth.py
│   │   ├── test_recruitment.py
│   │   └── test_timesheet.py
│   └── api/                     # 🌐 [API] API Test Suites & Contract Tests
│       ├── __init__.py
│       ├── conftest.py          # API fixtures (api_context, auth_api_context)
│       ├── test_auth_api.py
│       ├── test_recruitment_api.py
│       └── test_users_api.py
├── test_data/
│   ├── auth.json                # Shared browser storage state (session reuse across UI & API)
│   ├── data.json                # UI test datasets
│   └── api/                     # 🌐 [API] API Data & Contracts
│       ├── payloads/            # POST / PUT request JSON payloads
│       └── schemas/             # Response JSON schemas for schema validation
├── pytest.ini                   # Pytest test discovery & markers
├── requirements.txt
└── README.md
```

| Layer | Type | Location | Purpose |
| :--- | :--- | :--- | :--- |
| 🖥️ **UI Automation** | `[UI]` | `src/pages/`, `tests/ui/` | Page Object Model, end-to-end browser workflows |
| 🌐 **API Automation** | `[API]` | `src/api/`, `tests/api/`, `test_data/api/` | Playwright `APIRequestContext`, endpoint testing, JSON schema validation |
| ⚙️ **Shared Core** | `[Shared]` | `src/config/`, `src/utils/`, `auth.json` | Environment loader, custom logging, and shared session tokens |

---
