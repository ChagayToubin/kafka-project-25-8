
from data import Data
from Publishe import Producer
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

P = Producer()
data=Data()

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>לחץ על הכםתור לשליחת המידע</h1>
    <button onclick="location.href='/send_data'">send data</button>
   
    """

@app.get("/send_data")
def send_data():
    P.publish()
    return {"message":"the data send seccsesfuly"}
