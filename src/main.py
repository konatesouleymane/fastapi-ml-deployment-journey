from fastapi import FastAPI
from src.schemas import YieldInput
import json


app = FastAPI()

@app.get("/")
def accueil():
    return  {
        'message': 'BIENVENUE',
        'stauts': 'Connected'
    }

@app.post('/predict')
def predict(payload: YieldInput):
    return payload.model_dump()