from fastapi import FastAPI
from src.schemas import YieldInput
from src.model import make_prediction
import pandas as pd


app = FastAPI()

@app.get("/")
def accueil():
    return  {
        'message': 'BIENVENUE',
        'status': 'Connected'
    }

@app.post('/predict')
def predict(payload: YieldInput):
    data = payload.model_dump() 
    df = pd.DataFrame([data])
    prediction = make_prediction(df)
    return {"prediction":prediction, "unit": "hg/ha"}