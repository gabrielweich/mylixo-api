from starlette.testclient import TestClient
from mylixo.main import app


client = TestClient(app)


def test_addresses():
    response = client.get("/api/addresses?street=jua")
    assert response.status_code == 200


def test_garbage_collection():
    response = client.get("/api/garbage-collection?address_code=8374035&number=60")
    assert response.status_code == 200


def test_garbage_by_coordinates():
    response = client.get("/api/garbage-collection/coordinates?latitude=-30.0651485&longitude=-51.1740592")
    assert response.status_code == 200