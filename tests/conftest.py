import pytest
from playwright.sync_api import Playwright
import os
from src.utils.helpers import selectEnv

selectEnv().load()


def pytest_addoption(parser):
    """Register custom CLI options for browser and headless mode."""
    parser.addoption(
        "--browser-name",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "webkit"],
        help="Browser to run tests on: chrome | firefox | webkit  (default: chrome)",
    )
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        choices=["true", "false"],
        help="Run browser in headless mode: true | false  (default: false)",
    )


@pytest.fixture(scope="session")
def credentials(request):
    return request.param


@pytest.fixture(scope="session")
def page(playwright: Playwright, request):
    browser_name = request.config.getoption("--browser-name")
    headless = request.config.getoption("--headless").lower() == "true"

    if browser_name == "chrome":
        browser_instance = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser_instance = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser_instance = playwright.webkit.launch(headless=headless)
    else:
        browser_instance = playwright.chromium.launch(headless=headless)

    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser_instance.close()


@pytest.fixture(scope="session")
def authenticated_page(playwright: Playwright, request):
    browser_name = request.config.getoption("--browser-name")
    headless = request.config.getoption("--headless").lower() == "true"

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        browser = playwright.chromium.launch(headless=headless)

    auth_file = os.getenv("AUTH", "./test_data/auth.json")
    storage_state = auth_file if auth_file and os.path.exists(auth_file) else None
    context = browser.new_context(storage_state=storage_state)
    authenticated_page = context.new_page()
    yield authenticated_page
    authenticated_page.close()
    context.close()
    browser.close()