DISCLAIMER: I know .env file should not be pushed to git and should be added to .gitingnore, but I have pushed it just to make people understand how it works

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
