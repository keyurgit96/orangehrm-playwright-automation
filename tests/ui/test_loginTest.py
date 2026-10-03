from src.pages import *
from src.utils import *
import pytest
from playwright.sync_api import Playwright
import json
import os

selectEnv().load()
path = os.getenv("DATA_BASE")

with open(path) as f:
    credentials_data = json.load(f)
    credentials = credentials_data["credentials"]


@pytest.mark.genericTest
@pytest.mark.parametrize("credentials", credentials)
def test_login(playwright: Playwright, page, credentials):
    page.wait_for_timeout(3000)
    page.goto(credentials_data["url"]["baseUrl"])
    loginDetails(
        page, username=credentials["username"], password=credentials["password"]
    ).login()


@pytest.mark.correctCredentials
def test_loginCorrect(playwright: Playwright, page):
    page.goto(credentials_data["url"]["baseUrl"])
    loginDetails(page, username="Admin", password="admin123").login()
    page.context.storage_state(path=os.getenv("AUTH"))
