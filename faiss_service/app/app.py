from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import faiss
import numpy as np
import pickle
import datasets
from typing import Any

app = FastAPI()

# Load your FAISS index (assuming you've saved it as a .faiss file)
# index = faiss.read_index("your_faiss_index.faiss")
index = datasets.load_from_disk('data/')
index.add_faiss_index(column="embeddings")

class EmbeddingInput(BaseModel):
    embedding: list

class Response(BaseModel):
    scores: float
    examples: str


@app.post("/search", response_model=Response)
async def search_similar(input: EmbeddingInput) -> Response:
    # print(input)
    embedding = np.array(input.embedding).astype('float32')
    scores, examples = index.get_nearest_examples(
        "embeddings", embedding, k=1
    )

    return {"scores": scores[0], "examples": examples['text'][0]}