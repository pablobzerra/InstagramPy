import requests
from ..objects.constants import url


class Instagram:
    def __init__(self, cookies, headers):
        self.cookies = cookies
        self.headers = headers
        pass

    def get(self, endpoint: str, body = None):
        if body != None:
            return requests.get(f"{url}{endpoint}", cookies=self.cookies, headers=self.headers, data=body).json()
        else:
            return requests.get(f"{url}{endpoint}", cookies=self.cookies, headers=self.headers).json()
    

    def post(self, endpoint: str, body = None):
        if body != None:
            return requests.post(f"{url}{endpoint}", cookies=self.cookies, headers=self.headers, data=body).json()
        else:
            return requests.post(f"{url}{endpoint}", cookies=self.cookies, headers=self.headers).json()
            