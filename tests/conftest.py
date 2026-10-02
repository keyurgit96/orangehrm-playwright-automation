import pytest


@pytest.fixture(scope="session")
def browser_context_args(playwright, browser="chrome"):
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
