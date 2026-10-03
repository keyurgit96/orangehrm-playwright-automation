import pytest
from playwright.sync_api import Playwright
from dotenv import load_dotenv


load_dotenv()

@pytest.mark.editUserInfo
@pytest.mark.parametrize("page", [True], indirect=True)
def test_edituserInfo(playwright: Playwright, page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.wait_for_timeout(50000)
