import requests
from .exceptions import APIError

class Client:
    BASE_URL = "https://api.openmetrolinx.com/OpenDataAPI"

    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "GTPY/1.0",
            "Accept": "application/json",
        })

    def _request(self, endpoint: str, params: dict = None):
        if params is None:
            params = {}
        params["key"] = self.api_key
        url = f"{self.BASE_URL}/{endpoint}"
        
        response = self.session.get(url, params=params)
        
        if response.ok:
            return response.json()

        raise APIError(response)
