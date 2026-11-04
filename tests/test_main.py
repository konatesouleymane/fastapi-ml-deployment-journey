from fastapi.testclient import TestClient
from src.main import app

test = TestClient(app)


def test_main():
    response = test.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "BIENVENUE"
    assert data["status"] == "Connected"


def test_prediction():
    response = {}
    response = test.post('/predict', json=data)
    assert response.status_code == 200
    data = response.json()

