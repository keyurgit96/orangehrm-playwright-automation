import pytest
from playwright.sync_api import Playwright
from src.utils.helpers import *

selectEnv().load()


@pytest.mark.order(2)
@pytest.mark.editUserInfo
def test_edituserInfo(playwright: Playwright, authenticated_page):
    l=logger(authenticated_page)
    l.startLogging()
    authenticated_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    l.stopLogging("newLogfile")
    authenticated_page.wait_for_timeout(5000)
