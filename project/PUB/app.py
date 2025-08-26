from project.PUB.data import Data
from project.PUB.Publishe import Producer
#
# from data import Data
# from Publishe import Producer

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    data=Data()
    P=Producer()
    return """
    <h1>בחר פעולה</h1>
    <button onclick="location.href='/interesting'">interesting</button>
    <button onclick="location.href='/not_interesting'">not interesting</button>
    """

@app.get("/interesting")
def do_interesting():
    return {"message": "הופעלה פעולה: מעניין"}

@app.get("/not_interesting")
def do_not_interesting():
    return {"message": "הופעלה פעולה: לא מעניין"}