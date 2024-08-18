import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from fastapi import FastAPI, Response
from pydantic import BaseModel

from ml.model import load_model

model = None
app = FastAPI()


class ClosestAnekdotResponse(BaseModel):
    text: str
    anekdot: str
    score: float


# create a route
@app.get("/")
def index():
    return {"text": "Closest Anekdot"}


# Register the function to run during startup
@app.on_event("startup")
def startup_event():
    global model
    model = load_model()


# Your FastAPI route handlers go here
@app.get("/find")
def find_anekdot(text: str):
    anekdot = model(text)

    response = ClosestAnekdotResponse(
        text=text,
        anekdot=anekdot.text,
        score=anekdot.score,
    )

    return response

@app.get("/hello")
def print_hello(name: str):
    return Response(content=f"Hello, {name}!")