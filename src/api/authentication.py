import json
import os
from src.api.base import baseAPI
from src.config.endpoints import Endpoints


class loginAPI(baseAPI):
    def __init__(self, baseURL=None, session=None):
        super().__init__(baseURL, session)

    def login(self, payload: dict):
        self.response = self.post(Endpoints.AUTH_LOGIN, payload)
        assert self.response.status_code in [200, 201], (
            f"Login failed with status code: {self.response.status_code}"
        )
        return self.response.json()

    def saveSession(self,login):
        os.makedirs("test_data/api_data", exist_ok=True)
        with open("test_data/api_data/api_session.json", 'w') as f:
            f.write(json.dumps(login.response.json()))
    
    def loadSession(self):
        with open("test_data/api_data/api_session.json", 'r') as f:
            #assert 'TOKEN' in json.load(f), "TOKEN not found"
            self.session.cookies.update(json.load(f)['TOKEN'])
            print("Session loaded successfully")
