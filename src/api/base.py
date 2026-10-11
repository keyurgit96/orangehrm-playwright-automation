import requests


class baseAPI:
    def __init__(self, baseURL, session=None):
        self.baseURL = baseURL
        self.session = session
        if self.session == None:
            self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def _build_url(self, endpoint):
        if self.baseURL.endswith("/"):
            self.baseURL=self.baseURL.rstrip("/")
        clean_endpoint = endpoint.lstrip("/")
        if self.baseURL.startswith("https://") or self.baseURL.startswith("http://"):
            return f"{self.baseURL}/{clean_endpoint}"
        else:
            return f"https://{self.baseURL}/{clean_endpoint}"
    
    def post(self, endpoint, payload=None, **kwargs):
        url = self._build_url(endpoint)
        return self.session.post(url, json=payload, **kwargs)

    def get(self, endpoint, params=None, **kwargs):
        url = self._build_url(endpoint)
        return self.session.get(url, params=params, **kwargs)

    def delete(self, endpoint, payload=None, **kwargs):
        url = self._build_url(endpoint)
        return self.session.delete(url, json=payload, **kwargs)

    def put(self, endpoint, payload=None, **kwargs):
        url = self._build_url(endpoint)
        return self.session.put(url, json=payload, **kwargs)

    def patch(self, endpoint, payload=None, **kwargs):
        url = self._build_url(endpoint)
        return self.session.patch(url, json=payload, **kwargs)
