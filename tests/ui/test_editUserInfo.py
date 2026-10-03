import pytest
from playwright.sync_api import Playwright
from src.utils.helpers import selectEnv

selectEnv().load()


@pytest.mark.order(2)
@pytest.mark.editUserInfo
def test_edituserInfo(playwright: Playwright, authenticated_page,env):
    authenticated_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    authenticated_page.wait_for_timeout(5000)
