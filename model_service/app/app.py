import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import requests
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from ml.model import load_model

model = None
app = FastAPI()

FAISS_SERVICE_URL = "http://faiss_service:8001/search/"  # URL of the FAISS service

# create a route
@app.get("/")
def index():
    return {"text": "Closest Anekdot"}


# Register the function to run during startup
@app.on_event("startup")
def startup_event():
    global model
    model = load_model()

class TextInput(BaseModel):
    text: str

# Your FastAPI route handlers go here
@app.get("/find")
def find_anekdot(text: str):

    embedding = model(text)

    print(embedding)
    response = requests.post(FAISS_SERVICE_URL, json={"embedding": embedding.tolist()})

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error from FAISS service")

    return response.json()

@app.get("/hello")
def print_hello(name: str):
    return Response(content=f"Hello, {name}!")