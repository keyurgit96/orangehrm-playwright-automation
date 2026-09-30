import time

import pytest
from playwright.sync_api import Playwright

from src.pages import *


@pytest.mark.generic
def test_login(playwright: Playwright):
    auth = authentication(
        "Admin", "admin123", playwright, "https://opensource-demo.orangehrmlive.com/"
    )
    page = auth.login()
    # updateTimesheet(page).punchIn()
    # updateTimesheet(page).updateInDate(year='2026',month='september',day='27',comment='testComment')
    editUserDetails(page).myInfo()
    editUserDetails(page).uploadAttachment()
    # recruitment(page).recruitmentPage()
    # recruitment(page).addCandidate(jobtitle="Account Assistant",vacancy="Software Engineer")
    time.sleep(5)
    auth.logout()
