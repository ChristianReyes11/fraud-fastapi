from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]


app = FastAPI(title = 'Fraudes Prediction')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)
model = load(pathlib.Path('model/fraud-v1.joblib'))

class InputData(BaseModel):
    step: int= 1
    type: int =2
    amount: float=181
    oldbalanceOrg: float= 181
    newbalanceOrig: float= 0
    oldbalanceDest: float= 0
    newbalanceDest: float= 0
    isFlaggedFraud: int=0

class OutputData(BaseModel):
    isFraud:float=1

@app.post('/score', response_model = OutputData)
def score(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict_proba(model_input)[:,-1]

    return {'isFraud':result}