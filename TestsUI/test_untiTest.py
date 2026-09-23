from playwright.sync_api import Playwright
import pytest
from POM.authentication import authentication
import time


@pytest.mark.generic
def test_login(playwright:Playwright):
    auth=authentication("Admin","admin123",'firefox',playwright,"https://opensource-demo.orangehrmlive.com/")
    auth.login()
    time.sleep(5)
    auth.logout()
    