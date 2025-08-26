from fastapi import FastAPI

from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/")
def start_get():
    return {"ds":"21921"}