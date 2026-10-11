from src.api.base import baseAPI
from src.config.endpoints import Endpoints


class timesheetAPI(baseAPI):
    def __init__(self, baseURL, session=None):
        super().__init__(baseURL, session)

    def punchIn(self, payload):
        response = self.post(Endpoints.ATTENDANCE_RECORDS, payload)
        assert response.status_code in [200, 201], (
            f"Punch in failed with status code: {response.status_code}"
        )
        return response.json()

    def punchOut(self, payload):
        response = self.put(Endpoints.ATTENDANCE_RECORDS, payload)
        assert response.status_code in [200, 201], (
            f"Punch out failed with status code: {response.status_code}"
        )
        return response.json()

    def latestUpdate(self):
        response = self.get(Endpoints.ATTENDANCE_RECORDS_LATEST)
        assert response.status_code in [200, 201], (
            f"Failed to get latest attendance state: {response.status_code}"
        )
        return response.json()['data']['state']['id']

