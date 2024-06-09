from transformers import AutoTokenizer, AutoModel
import torch
from datasets import Dataset, load_from_disk
import pandas as pd
from pathlib import Path
from funcs import clean


class SbertPretrained:
    def __init__(self, model_name="ai-forever/sbert_large_nlu_ru"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def cls_pooling(self, model_output):
        return model_output.last_hidden_state[:, 0, :]

    def get_embeddings(self, text_list):
        
        encoded_input = self.tokenizer(
            text_list, padding=True, truncation=True, max_length=128, return_tensors="pt"
        )
        encoded_input = {k: v.to(self.device) for k, v in encoded_input.items()}
        model_output = self.model(**encoded_input)
        return self.cls_pooling(model_output)
    
    def load_df(self):
        df = pd.read_csv(Path.cwd() / 'data' / 'anekdots.csv', index_col=0)
        dataset = Dataset.from_pandas(df)

        self.embeddings_dataset = dataset.map(
            lambda x: {"embeddings": self.get_embeddings(x["text_clean"]).detach().cpu().numpy()[0]}
        )

    def load_embeddings(self):
        self.embeddings_dataset = load_from_disk(str(Path.cwd() / 'data' / 'embeddings_dataset'))

    def add_faiss_index(self):
        self.embeddings_dataset.add_faiss_index(column="embeddings")

    def find_similar(self, question, k_top=5):
        question_embedding = self.get_embeddings([clean(question)]).cpu().detach().numpy()

        scores, samples = self.embeddings_dataset.get_nearest_examples(
            "embeddings", question_embedding, k=k_top
        )

        samples_df = pd.DataFrame.from_dict(samples)
        samples_df["scores"] = scores
        samples_df.sort_values("scores", ascending=True, inplace=True)

        for i, row in samples_df.iterrows():
            print(f'{i+1}) Similarity score: {row.scores}')
            print(row.text)
            print('')