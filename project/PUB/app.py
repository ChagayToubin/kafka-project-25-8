from fastapi import FastAPI
from project.PUB.data import Data
app = FastAPI()

data=Data()

@app.get("/")
def root():
    return  {"data1":dict(data.data_loader_interesting())}

@app.get("/not_interesting")
def not_interesting():
    return {"ds":"ds"}

@app.get("/interesting")
def interesting():
    return {"ds":"ds"}