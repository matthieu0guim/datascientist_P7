import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from bank import BankRisk

app = FastAPI()
pickle_in = open("loan_risk_model.pkl", 'rb')
model = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': "Hello stranger"}

@app.get('/{name}')
def get_name(name:str):
    return {"Welcome to fastapi debute": f"{name}"}

@app.post('/predict')
def loan_risk(data:BankRisk):
    data = data.dict()




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000) 