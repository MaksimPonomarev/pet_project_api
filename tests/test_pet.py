from pydantic import BaseModel

class Credentials(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    category: Credentials
    name: str
    photoUrls: list[str]
    tags: list[Credentials]
    status: str



json={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

def test_123(pet_client):
    response = pet_client.add_new_pet_api(json=json)

    assert response.status_code == 200
    assert response.headers["content-type"]  == "application/json"
    assert response.elapsed.total_seconds() < 10

    pet = Pet(**response.json())
    print(json)
    print(response.json())
    assert json == response.json()


    print(response)

