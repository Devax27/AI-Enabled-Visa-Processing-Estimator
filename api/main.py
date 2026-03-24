from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_processing_time

app = FastAPI()

class InputData(BaseModel):
    year: int
    month: int
    quarter: int
    visa_type: str
    visa_status: str
    wage: float
    unit: str
@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: InputData):
    result = predict_processing_time(data.dict())
    return result