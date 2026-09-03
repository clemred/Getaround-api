import pandas as pd
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load('./model/model.pkl')
preprocessor = joblib.load("./model/preprocessor.joblib")

@app.post("/predict", tags=['Serving a prediction from the model'])
async def predict(data: list[dict]):
    """
    Prediction of the renting price from a JSON. Returns a JSON of the prediction.
    """
    
    # Reading data 
    df = pd.DataFrame(data[0], index=[0])

    # Pre-processing data
    quantitative_columns = ['mileage', 'engine_power']
    qualitative_columns = ['model_key',
                        'fuel',
                        'paint_color',
                        'car_type',
                        'private_parking_available',
                        'has_gps',
                        'has_air_conditioning',
                        'automatic_car',
                        'has_getaround_connect',
                        'has_speed_regulator',
                        'winter_tires']

    df = preprocessor.transform(df)

    # Making the prediction
    prediction = model.predict(df)

    return {"prediction": prediction.tolist()[0]}