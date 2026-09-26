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
    updateTimesheet(page).updateInDate(year='2020',month='December',day='25',comment='testComment')
    time.sleep(5)
    