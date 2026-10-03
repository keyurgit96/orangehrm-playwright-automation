import pytest
from playwright.sync_api import Playwright
import os
from src.utils.helpers import selectEnv

selectEnv().load()

@pytest.fixture(scope="session")
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

@pytest.fixture(scope="session")
def authenticated_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=os.getenv("AUTH"))
    authenticated_page = context.new_page()
    yield authenticated_page
    authenticated_page.close()
    context.close()
    browser.close()