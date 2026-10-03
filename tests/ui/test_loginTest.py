from src.pages import loginDetails
from src.pages import *
import pytest
from playwright.sync_api import Playwright
import json
with open("./test_data/data.json") as f:
    credentials_data = json.load(f)
    credentials=credentials_data["credentials"]

@pytest.mark.generic
@pytest.mark.parametrize("credentials", credentials)
def test_login(playwright: Playwright,page,credentials):
    page.goto(credentials_data["url"]["baseUrl"])
    #loginDetails(page,username='Admin',password='admin123').login()
    loginDetails(page,username=credentials["username"],password=credentials["password"]).login()
    
    