from playwright.sync_api import Playwright
import pytest
from POM import *
import time


@pytest.mark.generic
def test_login(playwright:Playwright):
    auth=authentication("Admin","admin123",playwright,"https://opensource-demo.orangehrmlive.com/")
    page=auth.login()
    #time.sleep(5)
    #auth.logout()
    updateTimesheet(page).punchIn()
    time.sleep(5)
    