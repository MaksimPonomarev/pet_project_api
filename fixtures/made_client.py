import httpx
import pytest

from clients.pet.pet_client import PetClient


@pytest.fixture
def pet_client():
    client = httpx.Client()
    pet_client = PetClient(client)
    return pet_client