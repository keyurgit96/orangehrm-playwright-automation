import pytest
from playwright.sync_api import Playwright, expect
from src.utils.helpers import logger, Waits

DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"


@pytest.mark.order(2)
@pytest.mark.editUserInfo
def test_edituserInfo(playwright: Playwright, authenticated_page):
    l = logger(authenticated_page)
    l.startLogging()

    authenticated_page.goto(DASHBOARD_URL)

    # Wait for and verify the authenticated dashboard loaded correctly
    Waits.for_url(authenticated_page, DASHBOARD_URL)
    Waits.for_visible(authenticated_page.locator(".oxd-topbar-header-breadcrumb"))
    expect(authenticated_page).to_have_url(DASHBOARD_URL)
    expect(authenticated_page.locator(".oxd-topbar-header-breadcrumb")).to_be_visible()

    l.stopLogging("newLogfile")
