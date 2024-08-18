from dataclasses import dataclass
from pathlib import Path
import yaml
import torch
from numpy import array
from transformers import AutoTokenizer, AutoModel
# from .utils import load_dataset

# load config file
config_path = Path(__file__).parent / "config.yaml"
with open(config_path, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

def load_model():
    """Load a pre-trained embedding model.

    Returns:
        model (function): A function that takes a text input and returns a ClosestAnekdotPrediction object.
    """
    tokenizer = AutoTokenizer.from_pretrained(config["model"])
    model_hf = AutoModel.from_pretrained(config["model"])
    # embeddings_dataset = load_dataset(config['datapath'])

    def create_embedding(text: str):
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            embeddings = model_hf(**inputs).last_hidden_state[:, 0, :].numpy()
        return embeddings

    def model(text: str) -> array:
        return create_embedding(text)

    return model