from httpx import Client


class APIClient:
    BASE_URL="https://petstore.swagger.io/v2"

    def __init__(self, client: Client):
        self.client = client

    def get(self, params):
        return self.client.get(url=self.BASE_URL, params=params)

    def post(self,endpoint, json):
        return self.client.post(url=f"{self.BASE_URL}{endpoint}", json=json)

    def put(self, body):
        return self.client.put(url=self.BASE_URL, json=body)

    def delete(self, params):
        return self.client.delete(url=self.BASE_URL, params=params)