from dataclasses import dataclass
from pathlib import Path
import yaml
from transformers import AutoTokenizer, AutoModel
from .utils import clean, get_embeddings, load_dataset

# load config file
config_path = Path(__file__).parent / "config.yaml"
with open(config_path, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


@dataclass
class ClosestAnekdotPrediction:
    """Class representing a closest anekdot prediction."""

    text: str
    score: float


def load_model():
    """Load a pre-trained embedding model.

    Returns:
        model (function): A function that takes a text input and returns a ClosestAnekdotPrediction object.
    """
    tokenizer = AutoTokenizer.from_pretrained(config["model"])
    model_hf = AutoModel.from_pretrained(config["model"])
    embeddings_dataset = load_dataset(config['datapath'])

    def model(text: str) -> ClosestAnekdotPrediction:

        question_embedding = get_embeddings(model_hf, tokenizer, [clean(text)]).detach().numpy()
        scores, samples = embeddings_dataset.get_nearest_examples("embeddings", question_embedding, k=1)

        return ClosestAnekdotPrediction(
            text=samples["text"][0],
            score=scores[0],
        )

    return model