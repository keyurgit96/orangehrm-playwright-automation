import pytest
import json
from playwright.sync_api import Playwright


@pytest.fixture(scope='session')
def credentials(request):
    return request.param


@pytest.fixture(scope="session")
def page(playwright: Playwright, browser="chrome"):
    if browser == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser == "webkit":
        browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()
