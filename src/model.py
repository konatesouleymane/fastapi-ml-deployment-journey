import joblib
from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent.parent
MODEL_PATH = PROJECT_DIR / "crop_yield_prediction" / "models" / "crop_yield_model.pkl"

model = joblib.load(MODEL_PATH)

def engineer_features(data: pd.DataFrame) -> pd.DataFrame:
    """Engineer features to match model expectations"""
    data = data.copy()

    column_mapping = {
        'country': 'Area',
        'crop': 'Item',
        'year': 'Year',
        'rainfall_mm': 'average_rain_fall_mm_per_year',
        'avg_temp_c': 'avg_temp',
    }
    data = data.rename(columns=column_mapping)

    data['temp_rain_interaction'] = (
        data['average_rain_fall_mm_per_year'] * data['avg_temp'] / 1000
    )
    data['log_pesticides'] = np.log1p(data['pesticides_tonnes'])
    data['years_since_1990'] = data['Year'] - 1990

    return data


def make_prediction(data: pd.DataFrame):
    features = engineer_features(data)
    prediction = model.predict(features)
    return float(prediction[0])