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
    payload = {
        "country": "Côte d'Ivoire",
        "crop": "Maize",
        "year": 2020,
        "rainfall_mm": 1500,
        "avg_temp_c": 25,
        "pesticides_tonnes": 100
    }
    response = test.post('/predict',json= payload)
    assert response.status_code == 200
    response_data = response.json()
    assert "prediction" in response_data
    assert isinstance(response_data["prediction"], (int, float))




def test_prediction_invalid_paylaod():
    payload = {
        "country":"Côte d'Ivoire",
        "crop": "Maize",
        "year": 2020,
        "rainfall_mm": -1500,
        "avg_temp_c": 25,
        "pesticides_tonnes": 100
    }
    response = test.post('/predict',json=payload)
    assert response.status_code==422




def test_prediction_invalid_paylaod_year():
    payload = {
        "country":"Côte d'Ivoire",
        "crop": "Maize",
        "year": 1980,
        "rainfall_mm": 1500,
        "avg_temp_c": 25,
        "pesticides_tonnes": 100
    }
    response = test.post('/predict',json=payload)
    assert response.status_code==422




def test_prediction_invalid_paylaod_country():
    payload = {
        "country":"",
        "crop": "Maize",
        "year": 2020,
        "rainfall_mm": 1500,
        "avg_temp_c": 25,
        "pesticides_tonnes": 100
    }
    response = test.post('/predict',json=payload)
    assert response.status_code==422




def test_prediction_invalid_paylaod_missing():
    payload = {
        "crop": "Maize",
        "year": 2020,
        "rainfall_mm": 1500,
        "avg_temp_c": 25,
        "pesticides_tonnes": 100
    }
    response = test.post('/predict',json=payload)
    assert response.status_code==422





def test_prediction_invalid_paylaod_added():
    payload = {
        "country":"Côte d'Ivoire",
        "crop": "Maize",
        "year": 2020,
        "rainfall_mm": 1500,
        "avg_temp_c": 25,
        "pesticides_tonnes": 100,
        "altitude": '45°'
    }
    response = test.post('/predict',json=payload)
    assert response.status_code==422