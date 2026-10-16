from src.pages import *
from src.utils import *
import pytest
from playwright.sync_api import Playwright, expect
import json
import os
data_path = os.getenv("DATA_BASE", "./test_data/data.json")

with open(data_path) as f:
    credentials_data = json.load(f)
    credentials = credentials_data["credentials"]

DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
INVALID_CREDENTIALS_MSG = "Invalid credentials"
REQUIRED_FIELD_MSG = "Required"


@pytest.mark.genericTest
@pytest.mark.parametrize("credentials", credentials)
def test_login(playwright: Playwright, page, credentials):
    page.goto(credentials_data["url"]["baseUrl"])
    Waits.for_load_state(page, "domcontentloaded")
    loginDetails(
        page, username=credentials["username"], password=credentials["password"]
    ).login()

    if credentials["expected"] == "valid":
        Waits.for_url(page, DASHBOARD_URL)
        expect(page).to_have_url(DASHBOARD_URL)
    else:
        error_locator = page.locator(".oxd-alert-content-text, .oxd-input-field-error-message")
        Waits.for_visible(error_locator.first)
        error_text = error_locator.first.inner_text()
        assert INVALID_CREDENTIALS_MSG in error_text or REQUIRED_FIELD_MSG in error_text, (
            f"Expected error message but got: '{error_text}'"
        )


@pytest.mark.correctCredentials
def test_loginCorrect(playwright: Playwright, page):
    page.goto(credentials_data["url"]["baseUrl"])
    loginDetails(page, username="Admin", password="admin123").login()

    # Wait for and verify successful login before saving session
    Waits.for_url(page, DASHBOARD_URL)
    expect(page).to_have_url(DASHBOARD_URL)

    auth_path = os.getenv("AUTH", "./test_data/auth.json")
    page.context.storage_state(path=auth_path)
