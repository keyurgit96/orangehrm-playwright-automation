from src.api.base import baseAPI
from src.config.endpoints import Endpoints


class recruitment(baseAPI):
    def __init__(self, baseURL):
        super().__init__(baseURL)

    def get_candidates(self, params=None):
        default_params = {
            "limit": 50,
            "offset": 0,
            "model": "list",
            "sortField": "candidate.dateOfApplication",
            "sortOrder": "DESC",
        }
        query_params = params if params is not None else default_params
        self.response = self.get(Endpoints.RECRUITMENT_CANDIDATES, params=query_params)
        assert self.response.status_code in [200, 201], (
            f"Could not get candidate details {self.response.status_code}"
        )
        return self.response.json()

    def delByFirstName(self, candidate_name, id=None):
        if id is None:
            candidate = self.get_candidates()
            for i in candidate["data"]:
                if i["firstName"] == candidate_name:
                    id = i["id"]
                    break
        self.response = self.delete(Endpoints.candidate_by_id(id))
        assert self.response.status_code in [200, 201], (
            f"Could not delete candidate details: {self.response.status_code}"
        )
        return self.response.json()

    def addCandidate(self, payload):
        self.response = self.post(Endpoints.RECRUITMENT_CANDIDATES, payload)
        assert self.response.status_code in [200, 201], (
            f"Could not add candidate details: {self.response.status_code}"
        )
        return self.response.json()
