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
pip install playwright pytest pytest-order python-dotenv
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


orangehrm-playwright-automation/
├── src/
│   ├── __init__.py
│   ├── pages/                  
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── authentication.py
│   │   ├── recruitment.py
│   │   ├── timesheet.py
│   │   └── user_info.py
│   ├── config/
│   │   └── settings.py          # Base URLs, timeouts, env vars
│   └── utils/
│       ├── __init__.py
│       └── helpers.py           # Logging, custom helpers
├── tests/                       # Renamed from TestsUI/
│   ├── conftest.py              # Pytest fixtures & setup
│   └── ui/
│       ├── test_auth.py
│       ├── test_recruitment.py
│       └── test_timesheet.py
├── test_data/                   # Upload sample files, test payloads
├── pytest.ini                   # Updated with pythonpath = src
├── requirements.txt
└── README.md
```

---
