from src.api.base import baseAPI
from src.config.endpoints import Endpoints


class userInfo(baseAPI):
    def __init__(self, baseURL):
        super().__init__(baseURL)

    def editDetails(self, payload, employee_id=1):
        self.response = self.patch(Endpoints.employee_name(employee_id), payload)
        assert self.response.status_code in [200, 201], (
            f"Could not edit user details: {self.response.status_code}"
        )
        return self.response.json()

    def getDetails(self, employee_id=7):
        self.response = self.get(Endpoints.employee_personal_details(employee_id))
        assert self.response.status_code in [200, 201], (
            f"Could not get user details: {self.response.status_code}"
        )
        return self.response.json()['data']