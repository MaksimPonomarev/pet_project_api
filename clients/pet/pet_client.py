


from clients.api_client import APIClient


class PetClient(APIClient):
    ENDPOINT = "/pet"

    def add_new_pet_api(self, json):
        return self.post(endpoint=self.ENDPOINT, json=json)

