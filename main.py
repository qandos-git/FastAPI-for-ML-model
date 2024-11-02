from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd


with open('artifacts\model.pkl', 'rb') as m:
    model = pickle.load(m)

with open('artifacts\preprocessor.pkl', 'rb') as p:
    processor = pickle.load(p)
    
app = FastAPI()

class Example(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    writing_score: int
    reading_score: int


@app.post("/")
def predict_example(x: Example):
    df = pd.DataFrame([x.dict()])
    df = processor.transform(df)
    yhat = model.predict(df)
    return {"result": yhat[0]}
